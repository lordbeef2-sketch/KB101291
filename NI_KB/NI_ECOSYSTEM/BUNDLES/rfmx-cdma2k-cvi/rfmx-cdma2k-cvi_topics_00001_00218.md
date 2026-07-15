# NI DOCUMENT BUNDLE: rfmx-cdma2k-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-cdma2k-cvi start=1 end=218 -->
<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_acpcfgsweeptime.html language=enus -->
## TOPIC 00001: RFmxCDMA2k_ACPCfgSweepTime

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_acpcfgsweeptime.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_acpcfgsweeptime.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ACPCfgSweepTime

int32 __stdcall RFmxCDMA2k_ACPCfgSweepTime (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 sweepTimeAuto,
 float64 sweepTimeInterval);

#### Purpose

Configures the sweep time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| sweepTimeAuto | int32 | Specifies whether the measurement computes the sweep time.RFMXCDMA2K_VAL_ACP_SWEEP_TIME_AUTO_FALSE (0) The measurement uses the sweep time that you specify using the sweepTimeInterval parameter.RFMXCDMA2K_VAL_ACP_SWEEP_TIME_AUTO_TRUE (1) The measurement uses the default sweep time of 0.001667 seconds. |
| RFMXCDMA2K_VAL_ACP_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify using the sweepTimeInterval parameter. |  |
| RFMXCDMA2K_VAL_ACP_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the default sweep time of 0.001667 seconds. |  |
| sweepTimeInterval | float64 | Specifies the sweep time if you set the sweepTimeAuto parameter to RFMXCDMA2K_VAL_ACP_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_acpfetchcarrierabsolutepower.html language=enus -->
## TOPIC 00002: RFmxCDMA2k_ACPFetchCarrierAbsolutePower

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_acpfetchcarrierabsolutepower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_acpfetchcarrierabsolutepower.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ACPFetchCarrierAbsolutePower

int32 __stdcall RFmxCDMA2k_ACPFetchCarrierAbsolutePower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* carrierAbsolutePower);

#### Purpose

Returns the absolute carrier power.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| carrierAbsolutePower | float64* | Returns the averaged channel power measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_acpfetchoffsetmeasurementarray.html language=enus -->
## TOPIC 00003: RFmxCDMA2k_ACPFetchOffsetMeasurementArray

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_acpfetchoffsetmeasurementarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_acpfetchoffsetmeasurementarray.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ACPFetchOffsetMeasurementArray

int32 __stdcall RFmxCDMA2k_ACPFetchOffsetMeasurementArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 lowerRelativePower[],
 float64 upperRelativePower[],
 float64 lowerAbsolutePower[],
 float64 upperAbsolutePower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the carrier absolute power.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| lowerRelativePower | float64[] | Returns the array of lower offset channel powers measured relative to the carrier absolute power. This value is expressed in dB. |
| upperRelativePower | float64[] | Returns the array of upper offset channel powers measured relative to the carrier absolute power. This value is expressed in dB. |
| lowerAbsolutePower | float64[] | Returns the array of lower offset channel absolute powers. |
| upperAbsolutePower | float64[] | Returns the array of upper offset channel absolute powers. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_acpfetchrelativepowerstrace.html language=enus -->
## TOPIC 00004: RFmxCDMA2k_ACPFetchRelativePowersTrace

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_acpfetchrelativepowerstrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_acpfetchrelativepowerstrace.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ACPFetchRelativePowersTrace

int32 __stdcall RFmxCDMA2k_ACPFetchRelativePowersTrace(
 niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 traceIndex,
 float64* x0,
 float64* dx,
 float32 relativePowersTrace[],
 int32 arraySize,
 int32* actualArraySize
);

#### Purpose

Fetches the relative powers trace for the ACP measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| traceIndex | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency. This value is expressed in Hz. |
| dx | float64* | Returns the frequency bin spacing. This value is expressed in Hz. |
| relativePowersTrace | float32[] | Returns the trace of relative power measured relative to the absolute carrier power in the offset channel specified by the traceIndex parameter. This value is expressed in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_acpfetchspectrum.html language=enus -->
## TOPIC 00005: RFmxCDMA2k_ACPFetchSpectrum

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_acpfetchspectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_acpfetchspectrum.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ACPFetchSpectrum

int32 __stdcall RFmxCDMA2k_ACPFetchSpectrum (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 spectrum[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the spectrum used for the ACP measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency. This value is expressed in Hz. |
| dx | float64* | Returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | float32[] | Returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_analyzespectrum1waveform.html language=enus -->
## TOPIC 00006: RFmxCDMA2k_AnalyzeSpectrum1Waveform

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_analyzespectrum1waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_analyzespectrum1waveform.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_AnalyzeSpectrum1Waveform

int32 __stdcall RFmxCDMA2k_AnalyzeSpectrum1Waveform (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[],
 float64 x0,
 float64 dx,
 float32 spectrum[],
 int32 arraySize,
 int32 reset,
 int64 reserved);

#### Purpose

Performs the enabled measurements on the spectrum waveform that you specify in **spectrum** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node.
Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either **spectral** or **IQorSpectral**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| x0 | float64 | Specifies the start frequency of the spectrum. This value is expressed in Hz. |
| dx | float64 | Specifies the frequency interval between data points in the spectrum. |
| spectrum | float32[] | Contains the real-value power spectrum. |
| arraySize | int32 | Specifies the size of the array. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_autolevel.html language=enus -->
## TOPIC 00007: RFmxCDMA2k_AutoLevel

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_autolevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_autolevel.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_AutoLevel

int32 __stdcall RFmxCDMA2k_AutoLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 measurementInterval,
 float64* referenceLevel);

#### Purpose

Examines the input signal to calculate the peak power level and sets it as the value of the [RFMXCDMA2k_ATTR_REFERENCE_LEVEL](/csh?topicname=rfmxcdma2kcvi/rfmxcdma2k_attr_reference_level.html) attribute. Use this function to calculate an approximate setting for the reference level. 
The RFmxCDMA2k Auto Level function does the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the [RFMXCDMA2k_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL](/csh?topicname=rfmxcdma2kcvi/rfmxcdma2k_attr_auto_level_initial_reference_level.html) attribute. 
When using PXIe-5663/5665/5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxCDMA2k Auto Level function. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| measurementInterval | float64 | Specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the signal analyzer. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| Output |  |  |
| Name | Type | Description |
| referenceLevel | float64* | Returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_buildsignalstring.html language=enus -->
## TOPIC 00008: RFmxCDMA2k_BuildSignalString

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_buildsignalstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_buildsignalstring.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_BuildSignalString

int32 __stdcall RFmxCDMA2k_BuildSignalString (char signalName[],
 char resultName[],
 int32 selectorStringLength,
 char selectorString[]);

#### Purpose

Creates a selector string to use with configuration or fetch attributes and functions. 
Refer to the [Selector String](/csh?topicname=rfmxspecan/selector_string_cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| signalName | char[] | Specifies the name of the signal when using named signal configurations. This input accepts the signal name with or without the "signal::" prefix. Examples:"""signal::sig1""sig1" |
| resultName | char[] | Specifies the name of the result when performing overlapped measurements. This input accepts the result name with or without the "result::" prefix. Examples:"""result::r1""r1" |
| selectorStringLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | char[] | Returns the selector string you can use in the input to Configuration functions, Fetch functions, or other functions that build selector strings. This string contains the signal and/or result names with their appropriate prefixes.Examples:"signal::sig1""result::r1""signal::sig1/result::r1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cdacfgmeasurementchannel.html language=enus -->
## TOPIC 00009: RFmxCDMA2k_CDACfgMeasurementChannel

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cdacfgmeasurementchannel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cdacfgmeasurementchannel.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CDACfgMeasurementChannel

int32 __stdcall RFmxCDMA2k_CDACfgMeasurementChannel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 walshCodeLength,
 int32 walshCodeNumber,
 int32 branch);

#### Purpose

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| walshCodeLength | int32 | Specifies the Walsh code length of a channel subject to channel specific analysis. |
| walshCodeNumber | int32 | Specifies the Walsh code number of a channel subject to channel specific analysis. |
| branch | int32 | Specifies the Walsh branch of a channel subject to channel specific analysis. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cdacfgpowerunit.html language=enus -->
## TOPIC 00010: RFmxCDMA2k_CDACfgPowerUnit

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cdacfgpowerunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cdacfgpowerunit.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CDACfgPowerUnit

int32 __stdcall RFmxCDMA2k_CDACfgPowerUnit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 powerUnit);

#### Purpose

Configures the **powerUnit** parameter for the code domain power results, except for the **totalPower** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| powerUnit | int32 | Specifies the measurement unit of the measured code domain power results. This value is expressed in dB/dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cdafetchcodedomainiandqpowertrace.html language=enus -->
## TOPIC 00011: RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cdafetchcodedomainiandqpowertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cdafetchcodedomainiandqpowertrace.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace

int32 __stdcall RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 ICodeDomainPowers[],
 float32 QCodeDomainPowers[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the I and Q code power trace measured in the code domain of the base spreading factor.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| ICodeDomainPowers | float32[] | Returns the array of I code power measured in the code domain of the base spreading factor. This value is expressed in dB or dBm. |
| QCodeDomainPowers | float32[] | Returns the array of Q code power measured in the code domain of the base spreading factor. This value is expressed in dB or dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cdafetchsymbolphaseerrortrace.html language=enus -->
## TOPIC 00012: RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cdafetchsymbolphaseerrortrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cdafetchsymbolphaseerrortrace.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 symbolPhaseError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the symbol phase error trace of the configured measurement channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| symbolPhaseError | float32[] | Returns the array of symbol phase error values of the configured measurement channel. This value is expressed in degrees. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cdafetchsymbolpowertrace.html language=enus -->
## TOPIC 00013: RFmxCDMA2k_CDAFetchSymbolPowerTrace

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cdafetchsymbolpowertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cdafetchsymbolpowertrace.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CDAFetchSymbolPowerTrace

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolPowerTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 symbolPowers[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the symbol power trace of the configured measurement channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| symbolPowers | float32[] | Returns the array of symbol power of the configured measurement channel. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cfgiqpoweredgetrigger.html language=enus -->
## TOPIC 00014: RFmxCDMA2k_CfgIQPowerEdgeTrigger

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cfgiqpoweredgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cfgiqpoweredgetrigger.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CfgIQPowerEdgeTrigger

int32 __stdcall RFmxCDMA2k_CfgIQPowerEdgeTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char IQPowerEdgeSource[],
 int32 IQPowerEdgeSlope,
 float64 IQPowerEdgeLevel,
 float64 triggerDelay,
 int32 minimumQuietTimeMode,
 float64 minimumQuietTime,
 int32 IQPowerEdgeLevelType,
 int32 enableTrigger);

#### Purpose

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. 
To trigger on burst signals, specify a minimum quiet time. The minimum quiet time ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts but large enough to ignore power changes within a burst.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| IQPowerEdgeSource | char[] | Specifies the channel from which the device monitors the trigger. |
| IQPowerEdgeSlope | int32 | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. RFMXCDMA2K_VAL_IQ_POWER_EDGE_RISING_SLOPE (0) The trigger asserts when the signal power is rising.RFMXCDMA2K_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1) The trigger asserts when the signal power is falling. |
| RFMXCDMA2K_VAL_IQ_POWER_EDGE_RISING_SLOPE (0) | The trigger asserts when the signal power is rising. |  |
| RFMXCDMA2K_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1) | The trigger asserts when the signal power is falling. |  |
| IQPowerEdgeLevel | float64 | Specifies the power level at which the device triggers, depending on the value of the IQPowerEdgeSlope parameter. The value is expressed in dB when the IQPowerEdgeLevelType parameter is set to RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE or in dBm when it is set to RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE. |
| triggerDelay | float64 | Specifies the trigger delay time. This value is expressed in seconds. |
| minimumQuietTimeMode | int32 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| minimumQuietTime | float64 | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQPowerEdgeSlope parameter to RFMXCDMA2K_VAL_IQ_POWER_EDGE_RISING_SLOPE, the signal is quiet while it is below the trigger level. If you set the IQPowerEdgeSlope parameter to RFMXCDMA2K_VAL_IQ_POWER_EDGE_FALLING_SLOPE, the signal is quiet when it is above the trigger level. |
| IQPowerEdgeLevelType | int32 | Specifies the reference for theIQPowerEdgeLevel parameter. The IQPowerEdgeLevelType parameter is used only when you set the Trigger Type attribute to RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE.RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0) The IQ Power Edge Level attribute is relative to the value of the reference level attribute.RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1) The IQ Power Edge Level attribute specifies the absolute power. |
| RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0) | The IQ Power Edge Level attribute is relative to the value of the reference level attribute. |  |
| RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1) | The IQ Power Edge Level attribute specifies the absolute power. |  |
| enableTrigger | int32 | Specifies whether the trigger is used. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cfgmechanicalattenuation.html language=enus -->
## TOPIC 00015: RFmxCDMA2k_CfgMechanicalAttenuation

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cfgmechanicalattenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cfgmechanicalattenuation.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CfgMechanicalAttenuation

int32 __stdcall RFmxCDMA2k_CfgMechanicalAttenuation (niRFmxInstrHandle instrumentHandle,
 char channelName[],
 int32 mechanicalAttenuationAuto,
 float64 mechanicalAttenuationValue);

#### Purpose

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgMechanicalAttenuation](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_cfgmechanicalattenuation.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| channelName | char[] | Set this parameter to "" (empty string) or NULL. |
| mechanicalAttenuationAuto | int32 | Specifies whether the RFmx driver chooses an attenuation setting based on the hardware settings. RFMXCDMA2k_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE(0) Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. RFMXCDMA2k_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE(1) Specifies that the measurement computes the mechanical attenuation. |
| RFMXCDMA2k_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE(0) | Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. |  |
| RFMXCDMA2k_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE(1) | Specifies that the measurement computes the mechanical attenuation. |  |
| mechanicalAttenuationValue | float64 | Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cfgnumberofchannels.html language=enus -->
## TOPIC 00016: RFmxCDMA2k_CfgNumberOfChannels

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cfgnumberofchannels.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cfgnumberofchannels.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CfgNumberOfChannels

int32 __stdcall RFmxCDMA2k_CfgNumberOfChannels (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfChannels);

#### Purpose

Configures the number of channels for the user-defined channel configuration when you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](/csh?topicname=rfmxcdma2kcvi/rfmxcdma2k_attr_channel_configuration_mode.html) attribute to RFMXCDMA2K_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| numberOfChannels | int32 | Specifies the number of user-defined channels. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cfgradioconfiguration.html language=enus -->
## TOPIC 00017: RFmxCDMA2k_CfgRadioConfiguration

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cfgradioconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cfgradioconfiguration.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CfgRadioConfiguration

int32 __stdcall RFmxCDMA2k_CfgRadioConfiguration (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 radioConfiguration);

#### Purpose

Configures the radio configuration of the CDMA2k signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| radioConfiguration | int32 | Specifies the radio configuration of the CDMA2k signal to be analyzed. RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC1 (0) Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH), and up to seven reverse supplemental code channels (R-SCCHs). Analysis of multiple channels is not supported.RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC2 (1) Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH, and up to seven R-SCCHs. Analysis of multiple channels is not supported.RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC3 (2) Radio configuration 3 includes binary phase shift keying (BPSK), R-FCH, and up to two reverse supplemental channels (R-SCHs).RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC4 (3) Radio configuration 4 includes BPSK, R-FCH, and up to two R-SCHs. |
| RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC1 (0) | Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH), and up to seven reverse supplemental code channels (R-SCCHs). Analysis of multiple channels is not supported. |  |
| RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC2 (1) | Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH, and up to seven R-SCCHs. Analysis of multiple channels is not supported. |  |
| RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC3 (2) | Radio configuration 3 includes binary phase shift keying (BPSK), R-FCH, and up to two reverse supplemental channels (R-SCHs). |  |
| RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC4 (3) | Radio configuration 4 includes BPSK, R-FCH, and up to two R-SCHs. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cfgreferencelevel.html language=enus -->
## TOPIC 00018: RFmxCDMA2k_CfgReferenceLevel

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cfgreferencelevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cfgreferencelevel.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CfgReferenceLevel

int32 __stdcall RFmxCDMA2k_CfgReferenceLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 referenceLevel);

#### Purpose

Configures the reference level. The reference level represents the maximum expected power of an input RF signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| referenceLevel | float64 | Specifies the reference level, which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cfgrfattenuation.html language=enus -->
## TOPIC 00019: RFmxCDMA2k_CfgRFAttenuation

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cfgrfattenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cfgrfattenuation.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CfgRFAttenuation

int32 __stdcall RFmxCDMA2k_CfgRFAttenuation (niRFmxInstrHandle instrumentHandle,
 char channelName[],
 int32 RFAttenuationAuto,
 float64 RFAttenuationValue);

#### Purpose

Configures the nominal attenuation and the RFmx driver setting.

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgRFAttenuation](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_cfgrfattenuation.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| channelName | char[] | Set this parameter to "" (empty string) or NULL. |
| RFAttenuationAuto | int32 | Specifies whether the RFmx driver computes the RF attenuation. RFMXCDMA2k_VAL_RF_ATTENUATION_AUTO_FALSE(0) Specifies that the RFmx driver uses the value configured using the RFAttenuationValue parameter. RFMXCDMA2k_VAL_RF_ATTENUATION_AUTO_TRUE(1) Specifies that the RFmx driver computes the RF attenuation. |
| RFMXCDMA2k_VAL_RF_ATTENUATION_AUTO_FALSE(0) | Specifies that the RFmx driver uses the value configured using the RFAttenuationValue parameter. |  |
| RFMXCDMA2k_VAL_RF_ATTENUATION_AUTO_TRUE(1) | Specifies that the RFmx driver computes the RF attenuation. |  |
| RFAttenuationValue | float64 | Specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain when you set the RFAttenuationAuto parameter to RFMXCDMA2k_VAL_RF_ATTENUATION_AUTO_FALSE. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cfgsoftwareedgetrigger.html language=enus -->
## TOPIC 00020: RFmxCDMA2k_CfgSoftwareEdgeTrigger

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cfgsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cfgsoftwareedgetrigger.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CfgSoftwareEdgeTrigger

int32 __stdcall RFmxCDMA2k_CfgSoftwareEdgeTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 triggerDelay,
 int32 enableTrigger);

#### Purpose

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| triggerDelay | float64 | Specifies the trigger delay time. This value is expressed in seconds. |
| enableTrigger | int32 | Specifies whether to enable the trigger. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cfguplinkspreading.html language=enus -->
## TOPIC 00021: RFmxCDMA2k_CfgUplinkSpreading

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cfguplinkspreading.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cfguplinkspreading.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CfgUplinkSpreading

int32 __stdcall RFmxCDMA2k_CfgUplinkSpreading (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int64 uplinkSpreadingLongCodeMask);

#### Purpose

Configures the scrambling code used for the uplink transmission.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| uplinkSpreadingLongCodeMask | int64 | Specifies the long code mask for uplink spreading. This number is a 42-bit binary number, represented as a 64-bit integer. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_cfguserdefinedchannelarray.html language=enus -->
## TOPIC 00022: RFmxCDMA2k_CfgUserDefinedChannelArray

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_cfguserdefinedchannelarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_cfguserdefinedchannelarray.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CfgUserDefinedChannelArray

int32 __stdcall RFmxCDMA2k_CfgUserDefinedChannelArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 walshCodeLength[],
 int32 walshCodeNumber[],
 int32 branch[],
 int32 numberOfElements);

#### Purpose

Configures all user-defined channels when you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](/csh?topicname=rfmxcdma2kcvi/rfmxcdma2k_attr_channel_configuration_mode.html) attribute to RFMXCDMA2K_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED. 
Use equal-sized arrays for **walshCodeLength**, **walshCodeNumber**, and **branch**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| walshCodeLength | int32[] | Specifies the Walsh code length of the CDMA2k signal. |
| walshCodeNumber | int32[] | Specifies the Walsh code number of the CDMA2k signal. |
| branch | int32[] | Specifies the branch on which a specific user-defined channel is mapped. RFMXCDMA2K_VAL_BRANCH_I (0) Specifies the in-phase branch.RFMXCDMA2K_VAL_BRANCH_Q (1) Specifies the quadrature branch.RFMXCDMA2K_VAL_BRANCH_I_AND_Q (2) Specifies the in-phase and quadrature branch. |
| RFMXCDMA2K_VAL_BRANCH_I (0) | Specifies the in-phase branch. |  |
| RFMXCDMA2K_VAL_BRANCH_Q (1) | Specifies the quadrature branch. |  |
| RFMXCDMA2K_VAL_BRANCH_I_AND_Q (2) | Specifies the in-phase and quadrature branch. |  |
| numberOfElements | int32 | Specifies the number of elements in each array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_checkmeasurementstatus.html language=enus -->
## TOPIC 00023: RFmxCDMA2k_CheckMeasurementStatus

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_checkmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_checkmeasurementstatus.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CheckMeasurementStatus

int32 __stdcall RFmxCDMA2k_CheckMeasurementStatus (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32* done);

#### Purpose

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| done | int32* | Indicates whether the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_chpcfgrbwfilter.html language=enus -->
## TOPIC 00024: RFmxCDMA2k_CHPCfgRBWFilter

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_chpcfgrbwfilter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_chpcfgrbwfilter.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CHPCfgRBWFilter

int32 __stdcall RFmxCDMA2k_CHPCfgRBWFilter (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 RBWAuto,
 float64 RBW,
 int32 RBWFilterType);

#### Purpose

Configures the RBW filter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| RBWAuto | int32 | Specifies whether the measurement computes the RBW.RFMXCDMA2K_VAL_CHP_RBW_AUTO_FALSE (0) The measurement uses the RBW that you specify in the RBW parameter.RFMXCDMA2K_VAL_CHP_RBW_AUTO_TRUE (1) The measurement computes the RBW. |
| RFMXCDMA2K_VAL_CHP_RBW_AUTO_FALSE (0) | The measurement uses the RBW that you specify in the RBW parameter. |  |
| RFMXCDMA2K_VAL_CHP_RBW_AUTO_TRUE (1) | The measurement computes the RBW. |  |
| RBW | float64 | Specifies the bandwidth of the RBW filter used to sweep the acquired signal if you set the RBWAuto parameter to RFMXCDMA2K_VAL_CHP_RBW_AUTO_FALSE. This value is expressed in Hz. |
| RBWFilterType | int32 | Specifies the shape of the digital RBW filter. RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED (0) No RBW filtering is performed.RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN (1) An RBW filter with a Gaussian response is applied.RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_FLAT (2) An RBW filter with a flat response is applied. |
| RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |  |
| RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXCDMA2K_VAL_CHP_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_chpcfgsweeptime.html language=enus -->
## TOPIC 00025: RFmxCDMA2k_CHPCfgSweepTime

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_chpcfgsweeptime.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_chpcfgsweeptime.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CHPCfgSweepTime

int32 __stdcall RFmxCDMA2k_CHPCfgSweepTime (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 sweepTimeAuto,
 float64 sweepTimeInterval);

#### Purpose

Configures the sweep time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| sweepTimeAuto | int32 | Specifies whether the measurement computes the sweep time.RFMXCDMA2K_VAL_CHP_SWEEP_TIME_AUTO_FALSE (0) The measurement uses the sweep time that you specify using the sweepTimeInterval parameter.RFMXCDMA2K_VAL_CHP_SWEEP_TIME_AUTO_TRUE (1) The measurement uses the default sweep time of 0.001667 seconds. |
| RFMXCDMA2K_VAL_CHP_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify using the sweepTimeInterval parameter. |  |
| RFMXCDMA2K_VAL_CHP_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the default sweep time of 0.001667 seconds. |  |
| sweepTimeInterval | float64 | Specifies the sweep time if you set the sweepTimeAuto parameter to RFMXCDMA2K_VAL_CHP_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_chpfetchcarrierabsolutepower.html language=enus -->
## TOPIC 00026: RFmxCDMA2k_CHPFetchCarrierAbsolutePower

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_chpfetchcarrierabsolutepower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_chpfetchcarrierabsolutepower.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CHPFetchCarrierAbsolutePower

int32 __stdcall RFmxCDMA2k_CHPFetchCarrierAbsolutePower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* carrierAbsolutePower);

#### Purpose

Returns the absolute carrier power of the CHP measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| carrierAbsolutePower | float64* | Returns the averaged channel power measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_commit.html language=enus -->
## TOPIC 00027: RFmxCDMA2k_Commit

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_commit.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_Commit

int32 __stdcall RFmxCDMA2k_Commit (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Commits settings to the hardware. Calling this function is optional. RFmxCDMA2k commits settings to the hardware when you call the [RFmxCDMA2k_Initiate](/csh?topicname=rfmxcdma2kcvi/cvirfmxcdma2k_initiate.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_createsignalconfiguration.html language=enus -->
## TOPIC 00028: RFmxCDMA2k_CreateSignalConfiguration

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_createsignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_createsignalconfiguration.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_CreateSignalConfiguration

int32 __stdcall RFmxCDMA2k_CreateSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char signalName[]);

#### Purpose

Creates a new instance of a signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| signalName | char[] | Specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix.Examples:"signal::sig1""sig1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_disabletrigger.html language=enus -->
## TOPIC 00029: RFmxCDMA2k_DisableTrigger

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_disabletrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_disabletrigger.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_DisableTrigger

int32 __stdcall RFmxCDMA2k_DisableTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getallnamedresultnames.html language=enus -->
## TOPIC 00030: RFmxCDMA2k_GetAllNamedResultNames

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getallnamedresultnames.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getallnamedresultnames.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAllNamedResultNames

int32 __stdcall RFmxCDMA2k_GetAllNamedResultNames(
 niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultNames[],
 int32 resultNamesBufferSize,
 int32* actualResultNamesSize,
 int32* defaultResultExists
);

#### Purpose

Returns the named result names of the signal that you specify in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| resultNamesBufferSize | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| Output |  |  |
| Name | Type | Description |
| ResultNames | char[] | Returns the comma delimited result names. |
| actualResultNamesSize | int32* | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | int32* | Indicates whether the default result exists. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributef64array.html language=enus -->
## TOPIC 00031: RFmxCDMA2k_GetAttributeF64Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributef64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributef64array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeF64Array

int32 __stdcall RFmxCDMA2k_GetAttributeF64Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float64 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float64[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributei32array.html language=enus -->
## TOPIC 00032: RFmxCDMA2k_GetAttributeI32Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributei32array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeI32Array

int32 __stdcall RFmxCDMA2k_GetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int32 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int32[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributei64array.html language=enus -->
## TOPIC 00033: RFmxCDMA2k_GetAttributeI64Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributei64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributei64array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeI64Array

int32 __stdcall RFmxCDMA2k_GetAttributeI64Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int64[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributei8.html language=enus -->
## TOPIC 00034: RFmxCDMA2k_GetAttributeI8

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributei8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributei8.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeI8

int32 __stdcall RFmxCDMA2k_GetAttributeI8 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributei8array.html language=enus -->
## TOPIC 00035: RFmxCDMA2k_GetAttributeI8Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributei8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributei8array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeI8Array

int32 __stdcall RFmxCDMA2k_GetAttributeI8Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int8 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int8[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array. If you set the arraySize parameter to 0, it returns the required array size. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributenicomplexdoublearray.html language=enus -->
## TOPIC 00036: RFmxCDMA2k_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributenicomplexdoublearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributenicomplexdoublearray.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeNIComplexDoubleArray

int32 __stdcall RFmxCDMA2k_GetAttributeNIComplexDoubleArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 NIComplexDouble attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | NIComplexDouble[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributenicomplexsinglearray.html language=enus -->
## TOPIC 00037: RFmxCDMA2k_GetAttributeNIComplexSingleArray

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributenicomplexsinglearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributenicomplexsinglearray.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeNIComplexSingleArray

int32 __stdcall RFmxCDMA2k_GetAttributeNIComplexSingleArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 NIComplexSingle attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | NIComplexSingle[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributestring.html language=enus -->
## TOPIC 00038: RFmxCDMA2k_GetAttributeString

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributestring.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeString

int32 __stdcall RFmxCDMA2k_GetAttributeString (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[]);

#### Purpose

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributeu16.html language=enus -->
## TOPIC 00039: RFmxCDMA2k_GetAttributeU16

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributeu16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributeu16.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeU16

int32 __stdcall RFmxCDMA2k_GetAttributeU16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt16 *attrVal);

#### Purpose

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt16* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributeu32.html language=enus -->
## TOPIC 00040: RFmxCDMA2k_GetAttributeU32

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributeu32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributeu32.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeU32

int32 __stdcall RFmxCDMA2k_GetAttributeU32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributeu32array.html language=enus -->
## TOPIC 00041: RFmxCDMA2k_GetAttributeU32Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributeu32array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeU32Array

int32 __stdcall RFmxCDMA2k_GetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt32 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt32[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributeu64array.html language=enus -->
## TOPIC 00042: RFmxCDMA2k_GetAttributeU64Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributeu64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributeu64array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeU64Array

int32 __stdcall RFmxCDMA2k_GetAttributeU64Array (niRFmxInstrHandle instrumentHandle, 
 char selectorString[], 
 int32 attributeID, 
 uInt64 attrVal[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt64[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributeu8.html language=enus -->
## TOPIC 00043: RFmxCDMA2k_GetAttributeU8

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributeu8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributeu8.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeU8

int32 __stdcall RFmxCDMA2k_GetAttributeU8 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_getattributeu8array.html language=enus -->
## TOPIC 00044: RFmxCDMA2k_GetAttributeU8Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_getattributeu8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_getattributeu8array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetAttributeU8Array

int32 __stdcall RFmxCDMA2k_GetAttributeU8Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt8 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt8[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_geterror.html language=enus -->
## TOPIC 00045: RFmxCDMA2k_GetError

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_geterror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_geterror.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetError

int32 __stdcall RFmxCDMA2k_GetError (niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[]);

#### Purpose

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter. 
 
If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For **Example**, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. 
 

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

|  | Note Use the RFmxCDMA2k_GetErrorString function if the RFmxCDMA2k_GetError function does not return an error message. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. If a valid session handle is passed, the last error stored in that session is retrieved. You can pass NULL to retrieve the last error stored in the current execution thread. |
| errorCode | int32* | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescriptionBufferSize | int32 | Passes the number of bytes in the char array you specify in the errorDescription parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize ? 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string. The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_geterrorstring.html language=enus -->
## TOPIC 00046: RFmxCDMA2k_GetErrorString

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_geterrorstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_geterrorstring.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_GetErrorString

int32 __stdcall RFmxCDMA2k_GetErrorString (niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[]);

#### Purpose

Converts a status code returned by an RFmxCDMA2k function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter. 
 

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For **Example**, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. 
 

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| errorCode | int32* | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescriptionBufferSize | int32 | Passes the number of bytes in the char array you specify in the errorDescription parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize – 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string. The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_initialize.html language=enus -->
## TOPIC 00047: rfmxcdma2k_Initialize

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_initialize.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_Initialize

int32 __stdcall RFmxCDMA2k_Initialize (char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession);

#### Purpose

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Initialize](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_initialize.html) function.

[IMAGE alt='image' src='note.gif'] Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| resourceName | char[] | Specifies the resource name of the device to initialize. The following table shows examples of how to specify the resource name. Example # Device Type Syntax 1 myRFmxDevice RFmx device, device name is "myRFmxDevice" 2 myLogicalName IVI logical name or virtual instrument, name is "myLogicalName" For NI-DAQmx devices, the syntax is the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot2. You can rename an NI-DAQmx device by right-clicking the name in MAX, selecting Rename from the pull-down menu, and entering a new name. You can also pass the name of an IVI logical name configured with the IVI Configuration utility. For additional information about IVI, refer to the IVI section of the Measurement & Automation Explorer Help. |
| Example # | Device Type | Syntax |
| 1 | myRFmxDevice | RFmx device, device name is "myRFmxDevice" |
| 2 | myLogicalName | IVI logical name or virtual instrument, name is "myLogicalName" |
| optionString | char[] | Sets the initial value of certain attributes for the session. The following attributes are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about attributes used in this parameter, refer to the NI RF Vector Signal Analyzers Help. The format of this string is "AttributeName=Value", where AttributeName is the name of the attribute and Value is the value to which the attribute is set. For example, you can simulate an PXIe-5663E using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple attributes, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx uses yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |
|  | Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |  |
| isNewSession | int32* | Returns RFMXCDMA2k_VAL_TRUE if the function created a new session, or RFMXCDMA2k_VAL_FALSE if the function returned a reference to an existing session. |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Identifies your instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_initializefromnirfsasession.html language=enus -->
## TOPIC 00048: RFmxCDMA2k_InitializeFromNIRFSASession

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_initializefromnirfsasession.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_initializefromnirfsasession.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_InitializeFromNIRFSASession

int32 __stdcall RFmxCDMA2k_InitializeFromNIRFSASession (uInt32 NIRFSASession, niRFmxInstrHandle *handleOut);

#### Purpose

Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. 

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_InitializeFromNIRFSASession](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_initializefromnirfsasession.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| NIRFSASession | uInt32 | Specifies the NIRFSA session handle of the device to initialize. |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Returns an RFmx instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_initiate.html language=enus -->
## TOPIC 00049: RFmxCDMA2k_Initiate

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_initiate.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_Initiate

int32 __stdcall RFmxCDMA2k_Initiate (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[]);

#### Purpose

Initiates all enabled measurements. Call this function after configuring the signal and measurement. 
This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the [RFmxCDMA2k_WaitforMeasurementComplete](/csh?topicname=rfmxcdma2kcvi/cvirfmxcdma2k_waitformeasurementcomplete.html) function or [RFmxCDMA2k_CheckMeasurementStatus](/csh?topicname=rfmxcdma2kcvi/cvirfmxcdma2k_checkmeasurementstatus.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising the signal name and the result name. The result name can either by specified through this input or the resultName input. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by the resultName input or the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result:" prefix. Examples:"""result::r1""r1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modacccfgsynchronizationmodeandinterval.html language=enus -->
## TOPIC 00050: RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modacccfgsynchronizationmodeandinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modacccfgsynchronizationmodeandinterval.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval

int32 __stdcall RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 synchronizationMode,
 int32 measurementOffset,
 int32 measurementLength);

#### Purpose

Configures the synchronization mode, offset, and length for modulation accuracy (ModAcc) analysis.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| synchronizationMode | int32 | Specifies whether the measurement is performed from the frame, slot, or symbol boundary.RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME (0) The frame boundary is detected, and the measurement is performed over the number of slots specified by the modAccMeasLength parameter starting at the modacc measurement offset slots from the frame boundary.RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT (1) The slot boundary is detected, and the measurement is performed over the number of slots specified by the modAccMeasLength parameter starting at the modacc measurement offset slots from the slot boundary.RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY (2) The symbol boundary is detected, and the measurement is performed over the number of slots specified by the modAccMeasLength parameter starting at the modacc measurement offset slots from the symbol boundary. |
| RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the modAccMeasLength parameter starting at the modacc measurement offset slots from the frame boundary. |  |
| RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary is detected, and the measurement is performed over the number of slots specified by the modAccMeasLength parameter starting at the modacc measurement offset slots from the slot boundary. |  |
| RFMXCDMA2K_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY (2) | The symbol boundary is detected, and the measurement is performed over the number of slots specified by the modAccMeasLength parameter starting at the modacc measurement offset slots from the symbol boundary. |  |
| measurementOffset | int32 | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. |
| measurementLength | int32 | Specifies the duration of the modulation accuracy measurement. This value is expressed in slots. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modaccfetchconstellationtrace.html language=enus -->
## TOPIC 00051: RFmxCDMA2k_ModAccFetchConstellationTrace

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modaccfetchconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modaccfetchconstellationtrace.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccFetchConstellationTrace

int32 __stdcall RFmxCDMA2k_ModAccFetchConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle constellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the complex chips of the corrected composite signal for the modulation accuracy (ModAcc) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| constellation | NIComplexSingle[] | Returns the array of complex chips of the corrected signal on which the ModAcc measurements are performed. You can use these chips to obtain the constellation diagram. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modaccfetchconstellationtracesplit.html language=enus -->
## TOPIC 00052: RFmxCDMA2k_ModAccFetchConstellationTraceSplit

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modaccfetchconstellationtracesplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modaccfetchconstellationtracesplit.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccFetchConstellationTraceSplit

int32 __stdcall RFmxCDMA2k_ModAccFetchConstellationTraceSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the complex chips of the corrected composite signal for the modulation accuracy (ModAcc) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| constellation | NIComplexSingle[] | Returns the real part of the array of complex chips of the corrected signal on which the ModAcc measurements are performed. You can use these chips to obtain the constellation diagram. |
| constellation | NIComplexSingle[] | Returns the imaginary part of the array of complex chips of the corrected signal on which the ModAcc measurements are performed. You can use these chips to obtain the constellation diagram. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modaccfetchdetectedchannel.html language=enus -->
## TOPIC 00053: RFmxCDMA2k_ModAccFetchDetectedChannel

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modaccfetchdetectedchannel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modaccfetchdetectedchannel.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccFetchDetectedChannel

int32 __stdcall RFmxCDMA2k_ModAccFetchDetectedChannel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* detectedWalshCodeLength,
 int32* detectedWalshCodeNumber,
 int32* detectedBranch);

#### Purpose

Returns a detected channel by its channel name. 
Use "channel<n>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and channel number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"channel0""signal::sig1/channel0""result::r1/channel0""signal::sig1/result::r1/channel0"You can use the RFmxCDMA2k_BuildChannelString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| detectedWalshCodeLength | int32* | Returns the detected Walsh code length. |
| detectedWalshCodeNumber | int32* | Returns the detected Walsh code number. |
| detectedBranch | int32* | Returns the detected branch.RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I (0) The signal modulated on the in-phase branch.RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_Q (1) The signal modulated on the quadrature branch.RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I_AND_Q (2) The signal modulated on the in-phase branch and quadrature branch. |
| RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I (0) | The signal modulated on the in-phase branch. |  |
| RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_Q (1) | The signal modulated on the quadrature branch. |  |
| RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I_AND_Q (2) | The signal modulated on the in-phase branch and quadrature branch. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modaccfetchdetectedchannelarray.html language=enus -->
## TOPIC 00054: RFmxCDMA2k_ModAccFetchDetectedChannelArray

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modaccfetchdetectedchannelarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modaccfetchdetectedchannelarray.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccFetchDetectedChannelArray

int32 __stdcall RFmxCDMA2k_ModAccFetchDetectedChannelArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 detectedWalshCodeLength[],
 int32 detectedWalshCodeNumber[],
 int32 detectedBranch[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the detected channels. If you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](/csh?topicname=rfmxcdma2kcvi/rfmxcdma2k_attr_channel_configuration_mode.html) attribute to RFMXCDMA2K_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED, the measurement returns the configured channels.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| detectedWalshCodeLength | int32[] | Returns the array of the detected Walsh code length. |
| detectedWalshCodeNumber | int32[] | Returns the array of the detected Walsh code number. |
| detectedBranch | int32[] | Returns the array of the detected branch.RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I (0) The signal modulated on the in-phase branch.RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_Q (1) The signal modulated on the quadrature branch.RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I_AND_Q (2) The signal modulated on the in-phase branch and quadrature branch. |
| RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I (0) | The signal modulated on the in-phase branch. |  |
| RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_Q (1) | The signal modulated on the quadrature branch. |  |
| RFMXCDMA2K_VAL_MODACC_DETECTED_BRANCH_I_AND_Q (2) | The signal modulated on the in-phase branch and quadrature branch. |  |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modaccfetchevm.html language=enus -->
## TOPIC 00055: RFmxCDMA2k_ModAccFetchEVM

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modaccfetchevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modaccfetchevm.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccFetchEVM

int32 __stdcall RFmxCDMA2k_ModAccFetchEVM (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* RMSEVM,
 float64* peakEVM,
 float64* rho,
 float64* frequencyError,
 float64* chipRateError,
 float64* RMSMagnitudeError,
 float64* RMSPhaseError);

#### Purpose

Returns the EVM value and related measurement values of the modulation accuracy (ModAcc) of the CDMA2k signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| RMSEVM | float64* | Returns the RMS EVM of the composite signal. This value is expressed as a percentage. |
| peakEVM | float64* | Returns the peak value of the uplink EVM. This value is expressed as a percentage. |
| rho | float64* | Returns the correlation of the received signal with the reference signal normalized by the signal power. |
| frequencyError | float64* | Returns the frequency error. This value is expressed in Hz. |
| chipRateError | float64* | Returns the chip rate error. This value is expressed in parts per million (ppm). |
| RMSMagnitudeError | float64* | Returns the RMS magnitude error of the composite signal. This value is expressed as a percentage. |
| RMSPhaseError | float64* | Returns the RMS phase error of the composite signal. This value is expressed in degrees (deg). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modaccfetchevmtrace.html language=enus -->
## TOPIC 00056: RFmxCDMA2k_ModAccFetchEVMTrace

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modaccfetchevmtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modaccfetchevmtrace.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccFetchEVMTrace

int32 __stdcall RFmxCDMA2k_ModAccFetchEVMTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 EVM[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the EVM trace of the ModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time. This value is expressed in seconds. |
| dx | float64* | Returns the delta parameter. |
| EVM | float32[] | Returns the real signal values stored in an array. This value is expressed as a percentage. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modaccfetchmagnitudeerrortrace.html language=enus -->
## TOPIC 00057: RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modaccfetchmagnitudeerrortrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modaccfetchmagnitudeerrortrace.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace

int32 __stdcall RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 magnitudeError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time. This value is expressed in seconds. |
| dx | float64* | Returns the chip duration. This value is expressed in seconds. |
| magnitudeError | float32[] | Returns the array of the magnitude error values. This value is expressed as a percentage. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modaccfetchpeakactivecde.html language=enus -->
## TOPIC 00058: RFmxCDMA2k_ModAccFetchPeakActiveCDE

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modaccfetchpeakactivecde.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modaccfetchpeakactivecde.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccFetchPeakActiveCDE

int32 __stdcall RFmxCDMA2k_ModAccFetchPeakActiveCDE (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* peakActiveCDE,
 int32* peakActiveCDEWalshCodeLength,
 int32* peakActiveCDEWalshCodeNumber,
 int32* peakActiveCDEBranch);

#### Purpose

Returns the peak value among the code domain errors of the active channels, along with the code number and the code length.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| peakActiveCDE | float64* | Returns the peak value of all CDEs of the active channels. This value is expressed in dB. |
| peakActiveCDEWalshCodeLength | int32* | Returns the Walsh code length of the channel corresponding to the peakActiveCDE value. |
| peakActiveCDEWalshCodeNumber | int32* | Returns the Walsh code number of the channel corresponding to the peakActiveCDE value. |
| peakActiveCDEBranch | int32* | Returns the branch of the channel corresponding to the peakActiveCDE value.RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I (0) The signal is modulated on the in-phase branch.RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q (1) The signal is modulated on the quadrature branch. |
| RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I (0) | The signal is modulated on the in-phase branch. |  |
| RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q (1) | The signal is modulated on the quadrature branch. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modaccfetchpeakcde.html language=enus -->
## TOPIC 00059: RFmxCDMA2k_ModAccFetchPeakCDE

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modaccfetchpeakcde.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modaccfetchpeakcde.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccFetchPeakCDE

int32 __stdcall RFmxCDMA2k_ModAccFetchPeakCDE (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* peakCDE,
 int32* peakCDEWalshCodeNumber,
 int32* peakCDEBranch);

#### Purpose

Returns the maximum value among the code domain errors (CDEs), in dB. 
This function calculates the CDEs by projecting the descrambled error vector onto the code domain at a specific spreading factor. 
The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform. A fixed spreading factor of 32 is used. 
This function computes the CDEs separately for I and Q branches.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| peakCDE | float64* | Returns the maximum value among the code domain errors. This value is expressed in dB. |
| peakCDEWalshCodeNumber | int32* | Returns the code number of the channel corresponding to the peakCDE value. |
| peakCDEBranch | int32* | Returns the branch of the channel corresponding to the peakCDE value.RFMXCDMA2K_VAL_MODACC_PEAK_CDE_BRANCH_I (0) The signal is modulated on the in-phase branch.RFMXCDMA2K_VAL_MODACC_PEAK_CDE_BRANCH_Q (1) The signal is modulated on the quadrature branch. |
| RFMXCDMA2K_VAL_MODACC_PEAK_CDE_BRANCH_I (0) | The signal is modulated on the in-phase branch. |  |
| RFMXCDMA2K_VAL_MODACC_PEAK_CDE_BRANCH_Q (1) | The signal is modulated on the quadrature branch. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_modaccfetchphaseerrortrace.html language=enus -->
## TOPIC 00060: RFmxCDMA2k_ModAccFetchPhaseErrorTrace

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_modaccfetchphaseerrortrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_modaccfetchphaseerrortrace.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ModAccFetchPhaseErrorTrace

int32 __stdcall RFmxCDMA2k_ModAccFetchPhaseErrorTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 phaseError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the phase error trace of the ModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time. This value is expressed in seconds. |
| dx | float64* | Returns the chip duration. This value is expressed in seconds. |
| phaseError | float32[] | Returns the array of phase error values. This value is expressed in degrees. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_obwcfgaveraging.html language=enus -->
## TOPIC 00061: RFmxCDMA2k_OBWCfgAveraging

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_obwcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_obwcfgaveraging.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_OBWCfgAveraging

int32 __stdcall RFmxCDMA2k_OBWCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount,
 int32 averagingType);

#### Purpose

Configures averaging for the OBW measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_TRUE (1) The OBW measurement uses the averagingCount parameter to calculate the number of acquisitions over which the OBW measurement is averaged. |
| RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_TRUE (1) | The OBW measurement uses the averagingCount parameter to calculate the number of acquisitions over which the OBW measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_TRUE. |
| averagingType | int32 | Specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement.RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_LOG (1) The power spectrum is averaged in a logarithmic scale.RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_SCALAR (2) The square root of the power spectrum is averaged.RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_MINIMUM (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |  |
| RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXCDMA2K_VAL_OBW_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_obwcfgsweeptime.html language=enus -->
## TOPIC 00062: RFmxCDMA2k_OBWCfgSweepTime

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_obwcfgsweeptime.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_obwcfgsweeptime.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_OBWCfgSweepTime

int32 __stdcall RFmxCDMA2k_OBWCfgSweepTime (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 sweepTimeAuto,
 float64 sweepTimeInterval);

#### Purpose

Configures the sweep time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| sweepTimeAuto | int32 | Specifies whether the measurement computes the sweep time. RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) The measurement uses the sweep time that you specify using the sweepTimeInterval parameter.RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) The measurement uses the default sweep time of 0.001667 seconds. |
| RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify using the sweepTimeInterval parameter. |  |
| RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the default sweep time of 0.001667 seconds. |  |
| sweepTimeInterval | float64 | Specifies the sweep time when you set the sweepTimeAuto parameter to RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_obwfetchmeasurement.html language=enus -->
## TOPIC 00063: RFmxCDMA2k_OBWFetchMeasurement

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_obwfetchmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_obwfetchmeasurement.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_OBWFetchMeasurement

int32 __stdcall RFmxCDMA2k_OBWFetchMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* occupiedBandwidth,
 float64* absolutePower,
 float64* startFrequency,
 float64* stopFrequency);

#### Purpose

Returns the OBW measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| occupiedBandwidth | float64* | Returns the occupied bandwidth. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency |
| absolutePower | float64* | Returns the total integrated power of the spectrum acquired by the OBW measurement. This value is expressed in dBm. |
| startFrequency | float64* | Returns the start frequency of the OBW. This value is expressed in Hz. |
| stopFrequency | float64* | Returns the stop frequency of the OBW. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_obwfetchspectrum.html language=enus -->
## TOPIC 00064: RFmxCDMA2k_OBWFetchSpectrum

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_obwfetchspectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_obwfetchspectrum.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_OBWFetchSpectrum

int32 __stdcall RFmxCDMA2k_OBWFetchSpectrum (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 spectrum[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the spectrum trace used for the OBW measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency. This value is expressed in Hz. |
| dx | float64* | Returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | float32[] | Returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_qevmcfgaveraging.html language=enus -->
## TOPIC 00065: RFmxCDMA2k_QEVMCfgAveraging

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_qevmcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_qevmcfgaveraging.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_QEVMCfgAveraging

int32 __stdcall RFmxCDMA2k_QEVMCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount);

#### Purpose

Configures averaging for QEVM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_TRUE (1) The QEVM measurement uses the averagingCount parameter to calculate the number of acquisitions over which the QEVM measurement is averaged. |
| RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_TRUE (1) | The QEVM measurement uses the averagingCount parameter to calculate the number of acquisitions over which the QEVM measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_TRUE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_qevmfetchconstellationtrace.html language=enus -->
## TOPIC 00066: RFmxCDMA2k_QEVMFetchConstellationTrace

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_qevmfetchconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_qevmfetchconstellationtrace.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_QEVMFetchConstellationTrace

int32 __stdcall RFmxCDMA2k_QEVMFetchConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle constellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the complex chips of the corrected received signal for the QEVM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| constellation | NIComplexSingle[] | Returns the array of complex chips of the corrected signal on which the QEVM measurements are performed. You can use these chips to obtain the constellation diagram. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_qevmfetchconstellationtracesplit.html language=enus -->
## TOPIC 00067: RFmxCDMA2k_QEVMFetchConstellationTraceSplit

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_qevmfetchconstellationtracesplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_qevmfetchconstellationtracesplit.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_QEVMFetchConstellationTraceSplit

int32 __stdcall RFmxCDMA2k_QEVMFetchConstellationTraceSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the complex chips of the corrected received signal for the QEVM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| constellation | NIComplexSingle[] | Returns the real part of the array of complex chips of the corrected signal on which the QEVM measurements are performed. You can use these chips to obtain the constellation diagram. |
| constellation | NIComplexSingle[] | Returns the imaginary part of the array of complex chips of the corrected signal on which the QEVM measurements are performed. You can use these chips to obtain the constellation diagram. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_qevmfetchevm.html language=enus -->
## TOPIC 00068: RFmxCDMA2k_QEVMFetchEVM

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_qevmfetchevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_qevmfetchevm.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_QEVMFetchEVM

int32 __stdcall RFmxCDMA2k_QEVMFetchEVM (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* meanRMSEVM,
 float64* maximumPeakEVM,
 float64* meanFrequencyError,
 float64* meanMagnitudeError,
 float64* meanPhaseError,
 float64* meanChipRateError);

#### Purpose

Returns the EVM value and related measurement values of the QEVM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanRMSEVM | float64* | Returns the mean averaged RMS EVM of the received signal. This value is expressed as a percentage. |
| maximumPeakEVM | float64* | Returns the maximum peak EVM of the received signal. This value is expressed as a percentage. |
| meanFrequencyError | float64* | Returns the mean averaged frequency error of the received signal. This value is expressed in Hz. |
| meanMagnitudeError | float64* | Returns the mean averaged magnitude error of the received signal. This value is expressed as a percentage. |
| meanPhaseError | float64* | Returns the mean averaged phase error of the received signal. This value is expressed in degrees. |
| meanChipRateError | float64* | Returns the measured mean chip rate error of the received signal. This value is expressed in parts per million (ppm). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_resetattribute.html language=enus -->
## TOPIC 00069: RFmxCDMA2k_ResetAttribute

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_resetattribute.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_resetattribute.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ResetAttribute

int32 __stdcall RFmxCDMA2k_ResetAttribute (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID);

#### Purpose

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being reset. Refer to the selector string topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_resettodefault.html language=enus -->
## TOPIC 00070: RFmxCDMA2k_ResetToDefault

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_resettodefault.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_resettodefault.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_ResetToDefault

int32 __stdcall RFmxCDMA2k_ResetToDefault (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Resets a signal configuration to the default values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_semfetchspectrum.html language=enus -->
## TOPIC 00071: RFmxCDMA2k_SEMFetchSpectrum

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_semfetchspectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_semfetchspectrum.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SEMFetchSpectrum

int32 __stdcall RFmxCDMA2k_SEMFetchSpectrum (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 spectrum[],
 float32 relativeMask[],
 float32 absoluteMask[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the spectrum used for the SEM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency. This value is expressed in Hz. |
| dx | float64* | Returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | float32[] | Returns the array of averaged powers measured at each frequency bin. This value is expressed in dBm. |
| relativeMask | float32[] | Returns the array of power levels for relative mask. This value is expressed in dB. |
| absoluteMask | float32[] | Returns the array of power levels for absolute mask. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_semfetchupperoffsetpowerarray.html language=enus -->
## TOPIC 00072: RFmxCDMA2k_SEMFetchUpperOffsetPowerArray

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_semfetchupperoffsetpowerarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_semfetchupperoffsetpowerarray.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SEMFetchUpperOffsetPowerArray

int32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetPowerArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 absoluteIntegratedPower[],
 float64 relativeIntegratedPower[],
 float64 absolutePeakPower[],
 float64 peakFrequency[],
 float64 relativePeakPower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the arrays of upper offset segment power measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| absoluteIntegratedPower | float64[] | Returns the array of upper (positive) offset segment powers measured. |
| relativeIntegratedPower | float64[] | Returns the array of powers measured in each upper (positive) offset segment relative to the carrier absolute integrated power. |
| absolutePeakPower | float64[] | Returns the array of peak powers measured in each upper (positive) offset segment. The power is measured in dBm. |
| peakFrequency | float64[] | Returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
| relativePeakPower | float64[] | Returns the array of peak powers measured in each upper (positive) offset segment relative to the carrier absolute integrated power. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributef32.html language=enus -->
## TOPIC 00073: RFmxCDMA2k_SetAttributeF32

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributef32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributef32.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeF32

int32 __stdcall RFmxCDMA2k_SetAttributeF32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributef32array.html language=enus -->
## TOPIC 00074: RFmxCDMA2k_SetAttributeF32Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributef32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributef32array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeF32Array

int32 __stdcall RFmxCDMA2k_SetAttributeF32Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributef64.html language=enus -->
## TOPIC 00075: RFmxCDMA2k_SetAttributeF64

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributef64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributef64.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeF64

int32 __stdcall RFmxCDMA2k_SetAttributeF64 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal);

#### Purpose

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float64 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributef64array.html language=enus -->
## TOPIC 00076: RFmxCDMA2k_SetAttributeF64Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributef64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributef64array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeF64Array

int32 __stdcall RFmxCDMA2k_SetAttributeF64Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float64 attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributei16.html language=enus -->
## TOPIC 00077: RFmxCDMA2k_SetAttributeI16

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributei16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributei16.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeI16

int32 __stdcall RFmxCDMA2k_SetAttributeI16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int16 attrVal);

#### Purpose

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int16 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributei32.html language=enus -->
## TOPIC 00078: RFmxCDMA2k_SetAttributeI32

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributei32.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeI32

int32 __stdcall RFmxCDMA2k_SetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributei32array.html language=enus -->
## TOPIC 00079: RFmxCDMA2k_SetAttributeI32Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributei32array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeI32Array

int32 __stdcall RFmxCDMA2k_SetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int32 attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributei64.html language=enus -->
## TOPIC 00080: RFmxCDMA2k_SetAttributeI64

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributei64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributei64.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeI64

int32 __stdcall RFmxCDMA2k_SetAttributeI64 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 attrVal);

#### Purpose

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int64 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributei64array.html language=enus -->
## TOPIC 00081: RFmxCDMA2k_SetAttributeI64Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributei64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributei64array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeI64Array

int32 __stdcall RFmxCDMA2k_SetAttributeI64Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributenicomplexdoublearray.html language=enus -->
## TOPIC 00082: RFmxCDMA2k_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributenicomplexdoublearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributenicomplexdoublearray.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeNIComplexDoubleArray

int32 __stdcall RFmxCDMA2k_SetAttributeNIComplexDoubleArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 NIComplexDouble attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributenicomplexsinglearray.html language=enus -->
## TOPIC 00083: RFmxCDMA2k_SetAttributeNIComplexSingleArray

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributenicomplexsinglearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributenicomplexsinglearray.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeNIComplexSingleArray

int32 __stdcall RFmxCDMA2k_SetAttributeNIComplexSingleArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 NIComplexSingle attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributestring.html language=enus -->
## TOPIC 00084: RFmxCDMA2k_SetAttributeString

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributestring.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeString

int32 __stdcall RFmxCDMA2k_SetAttributeString (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, char attrVal[]);

#### Purpose

Sets the value of an RFmx string attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | char[] | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributeu16.html language=enus -->
## TOPIC 00085: RFmxCDMA2k_SetAttributeU16

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributeu16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributeu16.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeU16

int32 __stdcall RFmxCDMA2k_SetAttributeU16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt16 attrVal);

#### Purpose

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt16 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributeu32.html language=enus -->
## TOPIC 00086: RFmxCDMA2k_SetAttributeU32

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributeu32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributeu32.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeU32

int32 __stdcall RFmxCDMA2k_SetAttributeU32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributeu32array.html language=enus -->
## TOPIC 00087: RFmxCDMA2k_SetAttributeU32Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributeu32array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeU32Array

int32 __stdcall RFmxCDMA2k_SetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt32 attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributeu64array.html language=enus -->
## TOPIC 00088: RFmxCDMA2k_SetAttributeU64Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributeu64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributeu64array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeU64Array

int32 __stdcall RFmxCDMA2k_SetAttributeU64Array (niRFmxInstrHandle instrumentHandle, 
 char selectorString[], 
 int32 attributeID, 
 uInt64 attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt64[] | Pass the value to which you want to set the attribute. Note Some of the values might not be valid depending on the current state of the instrument session. |
|  | Note Some of the values might not be valid depending on the current state of the instrument session. |  |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_setattributeu8array.html language=enus -->
## TOPIC 00089: RFmxCDMA2k_SetAttributeU8Array

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_setattributeu8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_setattributeu8array.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SetAttributeU8Array

int32 __stdcall RFmxCDMA2k_SetAttributeU8Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt8 attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_slotphasefetchphasediscontinuities.html language=enus -->
## TOPIC 00090: RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_slotphasefetchphasediscontinuities.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_slotphasefetchphasediscontinuities.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities

int32 __stdcall RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 slotPhaseDiscontinuity[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the phase discontinuity values for the slot boundaries in the measurement interval.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| slotPhaseDiscontinuity | float64[] | Returns the array of phase discontinuity values for the slot boundaries in the measurement interval. This value is expressed in degrees. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=cvirfmxcdma2k_waitforacquisitioncomplete.html language=enus -->
## TOPIC 00091: RFmxCDMA2k_WaitForAcquisitionComplete

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `cvirfmxcdma2k_waitforacquisitioncomplete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/cvirfmxcdma2k_waitforacquisitioncomplete.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFmxCDMA2k_WaitForAcquisitionComplete

int32 __stdcall RFmxCDMA2k_WaitForAcquisitionComplete (niRFmxInstrHandle instrumentHandle, float64 timeout);

#### Purpose

Waits and blocks the data flow until the acquisition is complete. This function is typically called after a specific initiate function. 
 


This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_waitforacquisitioncomplete.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxCDMA2k_Initialize function. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxCDMA2k_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_all_traces_enabled.html language=enus -->
## TOPIC 00092: RFMXCDMA2K_ATTR_ACP_ALL_TRACES_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_all_traces_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_FALSE. Get Function: RFmxCDMA2k_ACPGetAllTracesEnabled Set Function: RFmxCDMA2k_ACPSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_averaging_count.html language=enus -->
## TOPIC 00093: RFMXCDMA2K_ATTR_ACP_AVERAGING_COUNT

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_averaging_count.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_ACP_AVERAGING_ENABLED attribute to RFMXCDMA2K_VAL_ACP_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxCDMA2k_ACPGetAveragingCount Set Function: RFmxCDMA2k_ACPSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_if_output_power_offset_auto.html language=enus -->
## TOPIC 00094: RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_if_output_power_offset_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_if_output_power_offset_auto.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This attribute is used only if you set the RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE. Get Function: RFmxCDMA2k_ACPGetIFOutputPowerOffsetAuto Set Function: RFmxCDMA2k_ACPSetIFOutputPowerOffsetAuto |
| Values: | RFMXCDMA2K_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE (0)The measurement does not compute an IF output power level offset for the offset channels. RFMXCDMA2K_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE (1)The measurement computes an IF output power level offset for the offset channels. |
| RFMXCDMA2K_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE (0) | The measurement does not compute an IF output power level offset for the offset channels. |
| RFMXCDMA2K_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE (1) | The measurement computes an IF output power level offset for the offset channels. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_measurement_enabled.html language=enus -->
## TOPIC 00095: RFMXCDMA2K_ATTR_ACP_MEASUREMENT_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_measurement_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable the ACP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_FALSE. Get Function: RFmxCDMA2k_ACPGetMeasurementEnabled Set Function: RFmxCDMA2k_ACPSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_measurement_method.html language=enus -->
## TOPIC 00096: RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_measurement_method.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the method for performing the ACP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_NORMAL. Get Function: RFmxCDMA2k_ACPGetMeasurementMethod Set Function: RFmxCDMA2k_ACPSetMeasurementMethod |
| Values: | RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_NORMAL (0)The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE (1)The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT (2)The ACP measurement acquires I/Q samples for a duration specified by the RFMXCDMA2k_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. These samples are divided into smaller chunks. The size of each chunk is defined by the RFMXCDMA2k_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize the ACP measurement speed. The accuracy of the results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time averaging is allowed. The following attributes have limited support when you set the RFMXCDMA2k_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXCDMA2k_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT. The RFMXCDMA2k_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute will only support RFMXCDMA2k_VAL_ACP_RBW_AUTO_TRUE value. The RFMXCDMA2k_ATTR_ACP_RBW_FILTER_TYPE attribute will only support RFMXCDMA2k_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED value. The RFMXCDMA2k_ATTR_ACP_AVERAGING_COUNT attribute will only support a value greater than or equal to 1. The RFMXCDMA2k_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS attribute will only support a value of 1. Note: For multi-span FFT, the averaging count should be 1. |
| RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_NORMAL (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. |
| RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT (2) | The ACP measurement acquires I/Q samples for a duration specified by the RFMXCDMA2k_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. These samples are divided into smaller chunks. The size of each chunk is defined by the RFMXCDMA2k_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize the ACP measurement speed. The accuracy of the results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time averaging is allowed. The following attributes have limited support when you set the RFMXCDMA2k_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXCDMA2k_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT. The RFMXCDMA2k_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute will only support RFMXCDMA2k_VAL_ACP_RBW_AUTO_TRUE value. The RFMXCDMA2k_ATTR_ACP_RBW_FILTER_TYPE attribute will only support RFMXCDMA2k_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED value. The RFMXCDMA2k_ATTR_ACP_AVERAGING_COUNT attribute will only support a value greater than or equal to 1. The RFMXCDMA2k_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS attribute will only support a value of 1. Note: For multi-span FFT, the averaging count should be 1. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_near_if_output_power_offset.html language=enus -->
## TOPIC 00097: RFMXCDMA2K_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_near_if_output_power_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_near_if_output_power_offset.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeF64RFmxCDMA2k_GetAttributeF64 |
| Description: | Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the RFMXCDMA2K_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXCDMA2K_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE and set the RFMXCDMA2K_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to RFMXCDMA2K_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10Â dB. Get Function: RFmxCDMA2k_ACPGetNearIFOutputPowerOffset Set Function: RFmxCDMA2k_ACPSetNearIFOutputPowerOffset |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_noise_compensation_enabled.html language=enus -->
## TOPIC 00098: RFMXCDMA2K_ATTR_ACP_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_noise_compensation_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_NOISE_COMPENSATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE. Get Function: RFmxCDMA2k_ACPGetNoiseCompensationEnabled Set Function: RFmxCDMA2k_ACPSetNoiseCompensationEnabled |
| Values: | RFMXCDMA2K_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE (0)Disables compensation of the channel powers for the noise floor of the signal analyzer. RFMXCDMA2K_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE (1)Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |
| RFMXCDMA2K_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE (0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| RFMXCDMA2K_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_number_of_analysis_threads.html language=enus -->
## TOPIC 00099: RFMXCDMA2K_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_number_of_analysis_threads.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the ACP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxCDMA2k_ACPGetNumberOfAnalysisThreads Set Function: RFmxCDMA2k_ACPSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_rbw_filter_auto_bandwidth.html language=enus -->
## TOPIC 00100: RFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_rbw_filter_auto_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_rbw_filter_auto_bandwidth.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the RBW. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_ACP_RBW_AUTO_TRUE. Get Function: RFmxCDMA2k_ACPGetRBWFilterAutoBandwidth Set Function: RFmxCDMA2k_ACPSetRBWFilterAutoBandwidth |
| Values: | RFMXCDMA2K_VAL_ACP_RBW_AUTO_FALSE (0)The measurement uses the RBW that you specify in the RFMXCDMA2K_ATTR_ACP_RBW_FILTER_BANDWIDTH attribute. RFMXCDMA2K_VAL_ACP_RBW_AUTO_TRUE (1)The measurement computes the RBW. |
| RFMXCDMA2K_VAL_ACP_RBW_AUTO_FALSE (0) | The measurement uses the RBW that you specify in the RFMXCDMA2K_ATTR_ACP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXCDMA2K_VAL_ACP_RBW_AUTO_TRUE (1) | The measurement computes the RBW. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_results_lower_offset_absolute_power.html language=enus -->
## TOPIC 00101: RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_results_lower_offset_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_results_lower_offset_absolute_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the absolute measured lower offset channel power. This value is expressed in dBm. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_ACPGetResultsLowerOffsetAbsolutePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_results_lower_offset_relative_power.html language=enus -->
## TOPIC 00102: RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_results_lower_offset_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_results_lower_offset_relative_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the lower offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_ACPGetResultsLowerOffsetRelativePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_results_upper_offset_absolute_power.html language=enus -->
## TOPIC 00103: RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_results_upper_offset_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_results_upper_offset_absolute_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the absolute measured upper offset channel power. This value is expressed in dBm. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_ACPGetResultsUpperOffsetAbsolutePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_results_upper_offset_relative_power.html language=enus -->
## TOPIC 00104: RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_results_upper_offset_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_results_upper_offset_relative_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the upper offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_ACPGetResultsUpperOffsetRelativePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_acp_sweep_time_interval.html language=enus -->
## TOPIC 00105: RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_INTERVAL

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_acp_sweep_time_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_acp_sweep_time_interval.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeF64RFmxCDMA2k_GetAttributeF64 |
| Description: | Specifies the sweep time when you set the RFMXCDMA2K_ATTR_ACP_SWEEP_TIME_AUTO attribute to RFMXCDMA2K_VAL_ACP_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.0016667Â seconds. Get Function: RFmxCDMA2k_ACPGetSweepTimeInterval Set Function: RFmxCDMA2k_ACPSetSweepTimeInterval |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_auto_level_initial_reference_level.html language=enus -->
## TOPIC 00106: RFMXCDMA2K_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_auto_level_initial_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_auto_level_initial_reference_level.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeF64RFmxCDMA2k_GetAttributeF64 |
| Description: | Specifies the initial reference level that the RFmxCDMA2k_AutoLevel function uses to estimate the peak power of the input signal. This value is expressed in dBm. The default value is 30Â dBm. Get Function: RFmxCDMA2k_GetAutoLevelInitialReferenceLevel Set Function: RFmxCDMA2k_SetAutoLevelInitialReferenceLevel |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_band_class.html language=enus -->
## TOPIC 00107: RFMXCDMA2K_ATTR_BAND_CLASS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_band_class.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_band_class.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_BAND_CLASS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Valid values are 0 to 12, 14 and 15. Get Function: RFmxCDMA2k_GetBandClass Set Function: RFmxCDMA2k_SetBandClass |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_base_spreading_factor.html language=enus -->
## TOPIC 00108: RFMXCDMA2K_ATTR_CDA_BASE_SPREADING_FACTOR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_base_spreading_factor.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_base_spreading_factor.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_BASE_SPREADING_FACTOR

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the base spreading factor used to calculate the code domain power traces. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 64. The valid values are 2, 4, 8, 16, 32, and 64. Get Function: RFmxCDMA2k_CDAGetBaseSpreadingFactor Set Function: RFmxCDMA2k_CDASetBaseSpreadingFactor |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_iq_quadrature_error_removal_enabled.html language=enus -->
## TOPIC 00109: RFMXCDMA2K_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_iq_quadrature_error_removal_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_iq_quadrature_error_removal_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE. Get Function: RFmxCDMA2k_CDAGetIQQuadratureErrorRemovalEnabled Set Function: RFmxCDMA2k_CDASetIQQuadratureErrorRemovalEnabled |
| Values: | RFMXCDMA2K_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE (0)I/Q quadrature error is not removed before the CDA measurement. RFMXCDMA2K_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE (1)I/Q quadrature error is removed before the CDA measurement. |
| RFMXCDMA2K_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE (0) | I/Q quadrature error is not removed before the CDA measurement. |
| RFMXCDMA2K_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE (1) | I/Q quadrature error is removed before the CDA measurement. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_power_unit.html language=enus -->
## TOPIC 00110: RFMXCDMA2K_ATTR_CDA_POWER_UNIT

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_power_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_power_unit.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_POWER_UNIT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the measurement unit of the measured code domain power results. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM. Get Function: RFmxCDMA2k_CDAGetPowerUnit Set Function: RFmxCDMA2k_CDASetPowerUnit |
| Values: | RFMXCDMA2K_VAL_CDA_POWER_UNIT_DB (0)The CDA measurement results are reported in dB. RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM (1)The CDA measurement results are reported in dBm. |
| RFMXCDMA2K_VAL_CDA_POWER_UNIT_DB (0) | The CDA measurement results are reported in dB. |
| RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM (1) | The CDA measurement results are reported in dBm. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_i_mean_active_power.html language=enus -->
## TOPIC 00111: RFMXCDMA2K_ATTR_CDA_RESULTS_I_MEAN_ACTIVE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_i_mean_active_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_i_mean_active_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_I_MEAN_ACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the average power of all active code channels measured on the I-branch. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsIMeanActivePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_i_peak_inactive_power.html language=enus -->
## TOPIC 00112: RFMXCDMA2K_ATTR_CDA_RESULTS_I_PEAK_INACTIVE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_i_peak_inactive_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_i_peak_inactive_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_I_PEAK_INACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum measured code power among the set of inactive channels on the I-branch and in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsIPeakInactivePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_iq_gain_imbalance.html language=enus -->
## TOPIC 00113: RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_iq_gain_imbalance.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_iq_gain_imbalance.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsIQGainImbalance |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_iq_origin_offset.html language=enus -->
## TOPIC 00114: RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_ORIGIN_OFFSET

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_iq_origin_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_iq_origin_offset.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_ORIGIN_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsIQOriginOffset |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_iq_quadrature_error.html language=enus -->
## TOPIC 00115: RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_iq_quadrature_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_iq_quadrature_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the I/Q quadrature error of the composite signal averaged over all measured slots. This value is expressed in degrees. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsIQQuadratureError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_mean_active_power.html language=enus -->
## TOPIC 00116: RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_ACTIVE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_mean_active_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_mean_active_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_ACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the average power of all active code channels. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsMeanActivePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_mean_inactive_power.html language=enus -->
## TOPIC 00117: RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_mean_inactive_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_mean_inactive_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsMeanInactivePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_mean_pilot_power.html language=enus -->
## TOPIC 00118: RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_PILOT_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_mean_pilot_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_mean_pilot_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_PILOT_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean power of the R-PICH. Returns the mean power value in dB, when you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to RFMXCDMA2K_VAL_CDA_POWER_UNIT_DB. Returns the mean power value in dBm, when you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsMeanPilotPower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_mean_symbol_power.html language=enus -->
## TOPIC 00119: RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_mean_symbol_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_mean_symbol_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to RFMXCDMA2K_VAL_CDA_POWER_UNIT_DB, and in dBm, when you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsMeanSymbolPower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_peak_inactive_power.html language=enus -->
## TOPIC 00120: RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_INACTIVE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_peak_inactive_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_peak_inactive_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_PEAK_INACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum measured code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsPeakInactivePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_cda_results_q_mean_active_power.html language=enus -->
## TOPIC 00121: RFMXCDMA2K_ATTR_CDA_RESULTS_Q_MEAN_ACTIVE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_cda_results_q_mean_active_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_cda_results_q_mean_active_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CDA_RESULTS_Q_MEAN_ACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the average power of all active code channels measured on the Q-branch. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to RFMXCDMA2K_VAL_CDA_POWER_UNIT_DBM, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_CDAGetResultsQMeanActivePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_chp_number_of_analysis_threads.html language=enus -->
## TOPIC 00122: RFMXCDMA2K_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_chp_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_chp_number_of_analysis_threads.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxCDMA2k_CHPGetNumberOfAnalysisThreads Set Function: RFmxCDMA2k_CHPSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_chp_rbw_filter_auto_bandwidth.html language=enus -->
## TOPIC 00123: RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_chp_rbw_filter_auto_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_chp_rbw_filter_auto_bandwidth.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the RBW. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_CHP_RBW_AUTO_TRUE. Get Function: RFmxCDMA2k_CHPGetRBWFilterAutoBandwidth Set Function: RFmxCDMA2k_CHPSetRBWFilterAutoBandwidth |
| Values: | RFMXCDMA2K_VAL_CHP_RBW_AUTO_FALSE (0)The measurement uses the RBW that you specify in the RFMXCDMA2K_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. RFMXCDMA2K_VAL_CHP_RBW_AUTO_TRUE (1)The measurement computes the RBW. |
| RFMXCDMA2K_VAL_CHP_RBW_AUTO_FALSE (0) | The measurement uses the RBW that you specify in the RFMXCDMA2K_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXCDMA2K_VAL_CHP_RBW_AUTO_TRUE (1) | The measurement computes the RBW. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_downlink_spreading_pn_offset.html language=enus -->
## TOPIC 00124: RFMXCDMA2K_ATTR_DOWNLINK_SPREADING_PN_OFFSET

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_downlink_spreading_pn_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_downlink_spreading_pn_offset.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_DOWNLINK_SPREADING_PN_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specified the PN offset in increments of 64 chips for forward link. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxCDMA2k_GetDownlinkSpreadingPNOffset Set Function: RFmxCDMA2k_SetDownlinkSpreadingPNOffset |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_iq_power_edge_trigger_source.html language=enus -->
## TOPIC 00125: RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_iq_power_edge_trigger_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_iq_power_edge_trigger_source.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeStringRFmxCDMA2k_GetAttributeString |
| Description: | Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXCDMA2K_ATTR_TRIGGER_TYPE attribute to RFMXCDMA2K_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value of this attribute is hardware dependent. Get Function: RFmxCDMA2k_GetIQPowerEdgeTriggerSource Set Function: RFmxCDMA2k_SetIQPowerEdgeTriggerSource |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_limited_configuration_change.html language=enus -->
## TOPIC 00126: RFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGE

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_limited_configuration_change.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_limited_configuration_change.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this property can help achieve faster measurements. When you set this attribute to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this attribute, you need to be aware of the limitations of this feature, which are listed in the Limitations of the RFMXCDMA2K_ATTR_LIMITED_CONFIGURATION_CHANGE Attribute topic. You can also use this attribute to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr attributes from a locked configuration. NI recommends you use this attribute in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this attribute to a value other than Disabled for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this attribute if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality attributes while testing each device under test. RFmx automatically optimizes that use case. Specify the named signal configuration you are setting this attribute in the selector string input. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED. Get Function: RFmxCDMA2k_GetLimitedConfigurationChange Set Function: RFmxCDMA2k_SetLimitedConfigurationChange |
| Values: | RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED (0)This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE (1)Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY (2)Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and RFMXCDMA2K_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL (3)Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXCDMA2K_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL (4)Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, RFMXCDMA2K_ATTR_REFERENCE_LEVEL, and RFMXCDMA2K_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL (5)Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, RFMXCDMA2K_ATTR_CENTER_FREQUENCY, RFMXCDMA2K_ATTR_REFERENCE_LEVEL, and RFMXCDMA2K_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED (0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE (1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY (2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and RFMXCDMA2K_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL (3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXCDMA2K_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to RFMXCDMA2K_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL (4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, RFMXCDMA2K_ATTR_REFERENCE_LEVEL, and RFMXCDMA2K_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXCDMA2K_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL (5) | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, RFMXCDMA2K_ATTR_CENTER_FREQUENCY, RFMXCDMA2K_ATTR_REFERENCE_LEVEL, and RFMXCDMA2K_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_link_direction.html language=enus -->
## TOPIC 00127: RFMXCDMA2K_ATTR_LINK_DIRECTION

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_link_direction.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_link_direction.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_LINK_DIRECTION

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the link direction of the received signal. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_LINK_DIRECTION_UPLINK. Get Function: RFmxCDMA2k_GetLinkDirection Set Function: RFmxCDMA2k_SetLinkDirection |
| Values: | RFMXCDMA2K_VAL_LINK_DIRECTION_DOWNLINK (0)CDMA2k measurement uses 3GPP CDMA2k forward link direction also known as downlink direction to measure the received signal. RFMXCDMA2K_VAL_LINK_DIRECTION_UPLINK (1)CDMA2k measurement uses 3GPP CDMA2k reverse link direction also known as uplink direction to measure the received signal. |
| RFMXCDMA2K_VAL_LINK_DIRECTION_DOWNLINK (0) | CDMA2k measurement uses 3GPP CDMA2k forward link direction also known as downlink direction to measure the received signal. |
| RFMXCDMA2K_VAL_LINK_DIRECTION_UPLINK (1) | CDMA2k measurement uses 3GPP CDMA2k reverse link direction also known as uplink direction to measure the received signal. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_modacc_all_traces_enabled.html language=enus -->
## TOPIC 00128: RFMXCDMA2K_ATTR_MODACC_ALL_TRACES_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_modacc_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_modacc_all_traces_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_MODACC_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_FALSE. Get Function: RFmxCDMA2k_ModAccGetAllTracesEnabled Set Function: RFmxCDMA2k_ModAccSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_modacc_receive_filter_enabled.html language=enus -->
## TOPIC 00129: RFMXCDMA2K_ATTR_MODACC_RECEIVE_FILTER_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_modacc_receive_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_modacc_receive_filter_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_MODACC_RECEIVE_FILTER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable the received filter for the ModAcc measurement. For RC1/2, this attribute refers to the band-limiting filter specified in the Chapter 6.4.2.1 of 3GPP2 C.S0011-E. For RC3/4, this attribute refers to the complementary filter specified in the Chapter 6.4.2.2 of 3GPP2 C.S0011-E. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_MODACC_RECEIVE_FILTER_ENABLED_TRUE. Get Function: RFmxCDMA2k_ModAccGetReceiveFilterEnabled Set Function: RFmxCDMA2k_ModAccSetReceiveFilterEnabled |
| Values: | RFMXCDMA2K_VAL_MODACC_RECEIVE_FILTER_ENABLED_FALSE (0)Disables received filtering for the ModAcc measurement. RFMXCDMA2K_VAL_MODACC_RECEIVE_FILTER_ENABLED_TRUE (1)Enables received filtering for the ModAcc measurement. |
| RFMXCDMA2K_VAL_MODACC_RECEIVE_FILTER_ENABLED_FALSE (0) | Disables received filtering for the ModAcc measurement. |
| RFMXCDMA2K_VAL_MODACC_RECEIVE_FILTER_ENABLED_TRUE (1) | Enables received filtering for the ModAcc measurement. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_modacc_results_chip_rate_error.html language=enus -->
## TOPIC 00130: RFMXCDMA2K_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_modacc_results_chip_rate_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_modacc_results_chip_rate_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the chip rate error. This value is expressed in parts per million (ppm). You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_ModAccGetResultsChipRateError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_modacc_results_iq_origin_offset.html language=enus -->
## TOPIC 00131: RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_modacc_results_iq_origin_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_modacc_results_iq_origin_offset.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_ModAccGetResultsIQOriginOffset |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_modacc_results_iq_quadrature_error.html language=enus -->
## TOPIC 00132: RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_modacc_results_iq_quadrature_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_modacc_results_iq_quadrature_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_ModAccGetResultsIQQuadratureError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_modacc_results_number_of_detected_channels.html language=enus -->
## TOPIC 00133: RFMXCDMA2K_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_modacc_results_number_of_detected_channels.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_modacc_results_number_of_detected_channels.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeI32 |
| Description: | Returns the total number of detected channels. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to RFMXCDMA2K_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED, the attribute returns the number of configured channels. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_ModAccGetResultsNumberOfDetectedChannels |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_modacc_results_peak_active_cde.html language=enus -->
## TOPIC 00134: RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_modacc_results_peak_active_cde.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_modacc_results_peak_active_cde.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum value among the code domain errors (CDEs) for all active channels. This value is expressed in dB. The active CDEs are computed by projecting the descrambled error vector onto the codes of each active channel. The active CDE is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_ModAccGetResultsPeakActiveCDE |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_modacc_results_peak_active_cde_branch.html language=enus -->
## TOPIC 00135: RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_BRANCH

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_modacc_results_peak_active_cde_branch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_modacc_results_peak_active_cde_branch.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_BRANCH

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeI32 |
| Description: | Returns the branch of the channel corresponding to the value that the RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE attribute returns. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_ModAccGetResultsPeakActiveCDEBranch |
| Values: | RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I (0)The signal is modulated on the in-phase branch. RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q (1)The signal is modulated on the quadrature branch. RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I_AND_Q (2)Complex modulated signal. |
| RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I (0) | The signal is modulated on the in-phase branch. |
| RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q (1) | The signal is modulated on the quadrature branch. |
| RFMXCDMA2K_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I_AND_Q (2) | Complex modulated signal. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_modacc_results_peak_evm.html language=enus -->
## TOPIC 00136: RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_EVM

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_modacc_results_peak_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_modacc_results_peak_evm.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_MODACC_RESULTS_PEAK_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the peak EVM of the composite signal. This value is expressed as a percentage. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_ModAccGetResultsPeakEVM |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_obw_averaging_count.html language=enus -->
## TOPIC 00137: RFMXCDMA2K_ATTR_OBW_AVERAGING_COUNT

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_obw_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_obw_averaging_count.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_OBW_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED attribute to RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxCDMA2k_OBWGetAveragingCount Set Function: RFmxCDMA2k_OBWSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_obw_averaging_enabled.html language=enus -->
## TOPIC 00138: RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_obw_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_obw_averaging_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_OBW_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the OBW measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_FALSE. Get Function: RFmxCDMA2k_OBWGetAveragingEnabled Set Function: RFmxCDMA2k_OBWSetAveragingEnabled |
| Values: | RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_TRUE (1)The OBW measurement uses the value of the RFMXCDMA2K_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |
| RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXCDMA2K_VAL_OBW_AVERAGING_ENABLED_TRUE (1) | The OBW measurement uses the value of the RFMXCDMA2K_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_obw_results_occupied_bandwidth.html language=enus -->
## TOPIC 00139: RFMXCDMA2K_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_obw_results_occupied_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_obw_results_occupied_bandwidth.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_OBWGetResultsOccupiedBandwidth |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_obw_results_start_frequency.html language=enus -->
## TOPIC 00140: RFMXCDMA2K_ATTR_OBW_RESULTS_START_FREQUENCY

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_obw_results_start_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_obw_results_start_frequency.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_OBW_RESULTS_START_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the start frequency of the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_OBWGetResultsStartFrequency |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_obw_results_stop_frequency.html language=enus -->
## TOPIC 00141: RFMXCDMA2K_ATTR_OBW_RESULTS_STOP_FREQUENCY

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_obw_results_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_obw_results_stop_frequency.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_OBW_RESULTS_STOP_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the stop frequency of the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_OBWGetResultsStopFrequency |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_obw_span.html language=enus -->
## TOPIC 00142: RFMXCDMA2K_ATTR_OBW_SPAN

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_obw_span.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_obw_span.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_OBW_SPAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the frequency span of the OBW measurement. This value is expressed in Hz. You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_OBWGetSpan |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_obw_sweep_time_auto.html language=enus -->
## TOPIC 00143: RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_obw_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_obw_sweep_time_auto.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxCDMA2k_OBWGetSweepTimeAuto Set Function: RFmxCDMA2k_OBWSetSweepTimeAuto |
| Values: | RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the sweep time that you specify in the RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1)The measurement uses the default sweep time of 0.001667 seconds. |
| RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. |
| RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the default sweep time of 0.001667 seconds. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_obw_sweep_time_interval.html language=enus -->
## TOPIC 00144: RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVAL

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_obw_sweep_time_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_obw_sweep_time_interval.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeF64RFmxCDMA2k_GetAttributeF64 |
| Description: | Specifies the sweep time when you set the RFMXCDMA2K_ATTR_OBW_SWEEP_TIME_AUTO attribute to RFMXCDMA2K_VAL_OBW_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.001667Â seconds. Get Function: RFmxCDMA2k_OBWGetSweepTimeInterval Set Function: RFmxCDMA2k_OBWSetSweepTimeInterval |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_all_traces_enabled.html language=enus -->
## TOPIC 00145: RFMXCDMA2K_ATTR_QEVM_ALL_TRACES_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_all_traces_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_FALSE. Get Function: RFmxCDMA2k_QEVMGetAllTracesEnabled Set Function: RFmxCDMA2k_QEVMSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_averaging_count.html language=enus -->
## TOPIC 00146: RFMXCDMA2K_ATTR_QEVM_AVERAGING_COUNT

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_averaging_count.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the number of measurements used for averaging when you set the RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED attribute to RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default values is 10. The valid values are 1 to 10000, inclusive. Get Function: RFmxCDMA2k_QEVMGetAveragingCount Set Function: RFmxCDMA2k_QEVMSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_averaging_enabled.html language=enus -->
## TOPIC 00147: RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_averaging_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the QEVM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_FALSE. Get Function: RFmxCDMA2k_QEVMGetAveragingEnabled Set Function: RFmxCDMA2k_QEVMSetAveragingEnabled |
| Values: | RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_FALSE (0)The averaging is disabled for the measurement. RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_TRUE (1)The averaging is enabled for the measurement. |
| RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_FALSE (0) | The averaging is disabled for the measurement. |
| RFMXCDMA2K_VAL_QEVM_AVERAGING_ENABLED_TRUE (1) | The averaging is enabled for the measurement. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_iq_gain_imbalance_removal_enabled.html language=enus -->
## TOPIC 00148: RFMXCDMA2K_ATTR_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_iq_gain_imbalance_removal_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_iq_gain_imbalance_removal_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to remove I/Q gain imbalance before QEVM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE. Get Function: RFmxCDMA2k_QEVMGetIQGainImbalanceRemovalEnabled Set Function: RFmxCDMA2k_QEVMSetIQGainImbalanceRemovalEnabled |
| Values: | RFMXCDMA2K_VAL_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE (0)I/Q gain imbalance is not removed before the QEVM measurement. RFMXCDMA2K_VAL_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE (1)I/Q gain imbalance is removed before the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE (0) | I/Q gain imbalance is not removed before the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE (1) | I/Q gain imbalance is removed before the QEVM measurement. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_iq_offset_removal_enabled.html language=enus -->
## TOPIC 00149: RFMXCDMA2K_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_iq_offset_removal_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_iq_offset_removal_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to remove I/Q offset before QEVM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_FALSE. Get Function: RFmxCDMA2k_QEVMGetIQOffsetRemovalEnabled Set Function: RFmxCDMA2k_QEVMSetIQOffsetRemovalEnabled |
| Values: | RFMXCDMA2K_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_FALSE (0)I/Q offset is not removed before the QEVM measurement. RFMXCDMA2K_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_TRUE (1)I/Q offset is removed before the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_FALSE (0) | I/Q offset is not removed before the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_TRUE (1) | I/Q offset is removed before the QEVM measurement. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_iq_quadrature_error_removal_enabled.html language=enus -->
## TOPIC 00150: RFMXCDMA2K_ATTR_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_iq_quadrature_error_removal_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_iq_quadrature_error_removal_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to remove I/Q quadrature error before QEVM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE. Get Function: RFmxCDMA2k_QEVMGetIQQuadratureErrorRemovalEnabled Set Function: RFmxCDMA2k_QEVMSetIQQuadratureErrorRemovalEnabled |
| Values: | RFMXCDMA2K_VAL_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE (0)I/Q quadrature error is not removed before the QEVM measurement. RFMXCDMA2K_VAL_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE (1)I/Q quadrature error is removed before the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE (0) | I/Q quadrature error is not removed before the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE (1) | I/Q quadrature error is removed before the QEVM measurement. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_measurement_enabled.html language=enus -->
## TOPIC 00151: RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_measurement_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable the QEVM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_FALSE. Get Function: RFmxCDMA2k_QEVMGetMeasurementEnabled Set Function: RFmxCDMA2k_QEVMSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_measurement_length.html language=enus -->
## TOPIC 00152: RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_LENGTH

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_measurement_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_measurement_length.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_MEASUREMENT_LENGTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the number of chips used for a single measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1536. The valid values are 700 to 2500, inclusive. Get Function: RFmxCDMA2k_QEVMGetMeasurementLength Set Function: RFmxCDMA2k_QEVMSetMeasurementLength |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_number_of_analysis_threads.html language=enus -->
## TOPIC 00153: RFMXCDMA2K_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_number_of_analysis_threads.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the QEVM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. The default value is 1. Valid values range from 0 to 10, inclusive. Get Function: RFmxCDMA2k_QEVMGetNumberOfAnalysisThreads Set Function: RFmxCDMA2k_QEVMSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_receive_filter_enabled.html language=enus -->
## TOPIC 00154: RFMXCDMA2K_ATTR_QEVM_RECEIVE_FILTER_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_receive_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_receive_filter_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RECEIVE_FILTER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable the received filter for the QEVM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_QEVM_RECEIVE_FILTER_ENABLED_TRUE. Get Function: RFmxCDMA2k_QEVMGetReceiveFilterEnabled Set Function: RFmxCDMA2k_QEVMSetReceiveFilterEnabled |
| Values: | RFMXCDMA2K_VAL_QEVM_RECEIVE_FILTER_ENABLED_FALSE (0)Disables received filtering for the QEVM measurement. RFMXCDMA2K_VAL_QEVM_RECEIVE_FILTER_ENABLED_TRUE (1)Enables received filtering for the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_RECEIVE_FILTER_ENABLED_FALSE (0) | Disables received filtering for the QEVM measurement. |
| RFMXCDMA2K_VAL_QEVM_RECEIVE_FILTER_ENABLED_TRUE (1) | Enables received filtering for the QEVM measurement. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_maximum_chip_rate_error.html language=enus -->
## TOPIC 00155: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_maximum_chip_rate_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_maximum_chip_rate_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum chip rate error. This value is expressed in parts per million (ppm). You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMaximumChipRateError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_maximum_frequency_error.html language=enus -->
## TOPIC 00156: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_maximum_frequency_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_maximum_frequency_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum frequency error of the received signal. This value is expressed in Hz. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMaximumFrequencyError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_maximum_iq_gain_imbalance.html language=enus -->
## TOPIC 00157: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_maximum_iq_gain_imbalance.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_maximum_iq_gain_imbalance.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum I/Q gain imbalance of the received signal. This value is expressed in dB. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMaximumIQGainImbalance |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_maximum_iq_origin_offset.html language=enus -->
## TOPIC 00158: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_maximum_iq_origin_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_maximum_iq_origin_offset.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum origin offset of the received signal. This value is expressed in dB. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMaximumIQOriginOffset |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_maximum_iq_quadrature_error.html language=enus -->
## TOPIC 00159: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_QUADRATURE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_maximum_iq_quadrature_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_maximum_iq_quadrature_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_IQ_QUADRATURE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMaximumIQQuadratureError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_maximum_magnitude_error.html language=enus -->
## TOPIC 00160: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_maximum_magnitude_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_maximum_magnitude_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum magnitude error of the received signal. This value is expressed as a percentage. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMaximumMagnitudeError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_maximum_peak_evm.html language=enus -->
## TOPIC 00161: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PEAK_EVM

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_maximum_peak_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_maximum_peak_evm.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PEAK_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum peak EVM of the received signal. This value is expressed as a percentage. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMaximumPeakEVM |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_maximum_phase_error.html language=enus -->
## TOPIC 00162: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_maximum_phase_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_maximum_phase_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum phase error of the received signal. This value is expressed in degrees. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMaximumPhaseError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_maximum_rms_evm.html language=enus -->
## TOPIC 00163: RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_RMS_EVM

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_maximum_rms_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_maximum_rms_evm.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MAXIMUM_RMS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the maximum RMS EVM of the received signal. This value is expressed as a percentage. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMaximumRMSEVM |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_mean_chip_rate_error.html language=enus -->
## TOPIC 00164: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_mean_chip_rate_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_mean_chip_rate_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean chip rate error. This value is expressed in parts per million (ppm). You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMeanChipRateError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_mean_frequency_error.html language=enus -->
## TOPIC 00165: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_mean_frequency_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_mean_frequency_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean averaged frequency error of the received signal. This value is expressed in Hz. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMeanFrequencyError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_mean_iq_gain_imbalance.html language=enus -->
## TOPIC 00166: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_GAIN_IMBALANCE

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_mean_iq_gain_imbalance.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_mean_iq_gain_imbalance.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_GAIN_IMBALANCE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean I/Q gain imbalance of the received signal. This value is expressed in dB. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMeanIQGainImbalance |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_mean_iq_origin_offset.html language=enus -->
## TOPIC 00167: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_mean_iq_origin_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_mean_iq_origin_offset.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean averaged origin offset of the received signal. This value is expressed in dB. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMeanIQOriginOffset |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_mean_iq_quadrature_error.html language=enus -->
## TOPIC 00168: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_QUADRATURE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_mean_iq_quadrature_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_mean_iq_quadrature_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_IQ_QUADRATURE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMeanIQQuadratureError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_mean_magnitude_error.html language=enus -->
## TOPIC 00169: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_mean_magnitude_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_mean_magnitude_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean averaged magnitude error of the received signal. This value is expressed as a percentage. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMeanMagnitudeError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_mean_peak_evm.html language=enus -->
## TOPIC 00170: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PEAK_EVM

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_mean_peak_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_mean_peak_evm.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PEAK_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean averaged peak EVM of the received signal. This value is expressed as a percentage. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMeanPeakEVM |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_mean_phase_error.html language=enus -->
## TOPIC 00171: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PHASE_ERROR

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_mean_phase_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_mean_phase_error.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_PHASE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean averaged phase error of the received signal. This value is expressed in degrees. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMeanPhaseError |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_results_mean_rms_evm.html language=enus -->
## TOPIC 00172: RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_RMS_EVM

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_results_mean_rms_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_results_mean_rms_evm.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_RESULTS_MEAN_RMS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the mean averaged RMS EVM of the received signal. This value is expressed as a percentage. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_QEVMGetResultsMeanRMSEVM |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_qevm_spectrum_inverted.html language=enus -->
## TOPIC 00173: RFMXCDMA2K_ATTR_QEVM_SPECTRUM_INVERTED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_qevm_spectrum_inverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_qevm_spectrum_inverted.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_QEVM_SPECTRUM_INVERTED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether the spectrum of the signal is inverted. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_QEVM_SPECTRUM_INVERTED_FALSE. Get Function: RFmxCDMA2k_QEVMGetSpectrumInverted Set Function: RFmxCDMA2k_QEVMSetSpectrumInverted |
| Values: | RFMXCDMA2K_VAL_QEVM_SPECTRUM_INVERTED_FALSE (0)The measurement spectrum is normal. RFMXCDMA2K_VAL_QEVM_SPECTRUM_INVERTED_TRUE (1)The measurement spectrum is inverted. |
| RFMXCDMA2K_VAL_QEVM_SPECTRUM_INVERTED_FALSE (0) | The measurement spectrum is normal. |
| RFMXCDMA2K_VAL_QEVM_SPECTRUM_INVERTED_TRUE (1) | The measurement spectrum is inverted. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_radio_configuration.html language=enus -->
## TOPIC 00174: RFMXCDMA2K_ATTR_RADIO_CONFIGURATION

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_radio_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_radio_configuration.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_RADIO_CONFIGURATION

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the radio configuration for the channel. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC3. Get Function: RFmxCDMA2k_GetRadioConfiguration Set Function: RFmxCDMA2k_SetRadioConfiguration |
| Values: | RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC1 (0)If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to RFMXCDMA2K_VAL_LINK_DIRECTION_UPLINK, Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH), and reverse supplemental code channels (R-SCCHs). If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to RFMXCDMA2K_VAL_LINK_DIRECTION_DOWNLINK, Radio Configuration 1 includes binary phase-shift keying (BPSK), forward fundamental channels (F-FCHs) and forward supplemental channels (F-SCHs). RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC2 (1)If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Uplink, Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH, and R-SCCHs. If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Downlink, Radio Configuration 2 includes BPSKs, F-FCHs and F-SCHs. RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC3 (2)If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Uplink, Radio configuration 3 includes BPSK, R-FCH, and reverse supplemental channels (R-SCHs). If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Downlink, Radio Configuration 3 includes quadrature phase-shift keying (QPSK), F-FCHs and F-SCHs. RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC4 (3)If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Uplink, Radio configuration 4 includes BPSK, R-FCH, and R-SCHs. If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Downlink, Radio Configuration 4 includes QPSK, F-FCHs and F-SCHs. RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC5 (4)If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Uplink, Radio configuration 5 is not supported and gives invalid results. If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Downlink, Radio Configuration 5 includes QPSK, F-FCHs and F-SCHs. |
| RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC1 (0) | If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to RFMXCDMA2K_VAL_LINK_DIRECTION_UPLINK, Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH), and reverse supplemental code channels (R-SCCHs). If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to RFMXCDMA2K_VAL_LINK_DIRECTION_DOWNLINK, Radio Configuration 1 includes binary phase-shift keying (BPSK), forward fundamental channels (F-FCHs) and forward supplemental channels (F-SCHs). |
| RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC2 (1) | If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Uplink, Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH, and R-SCCHs. If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Downlink, Radio Configuration 2 includes BPSKs, F-FCHs and F-SCHs. |
| RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC3 (2) | If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Uplink, Radio configuration 3 includes BPSK, R-FCH, and reverse supplemental channels (R-SCHs). If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Downlink, Radio Configuration 3 includes quadrature phase-shift keying (QPSK), F-FCHs and F-SCHs. |
| RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC4 (3) | If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Uplink, Radio configuration 4 includes BPSK, R-FCH, and R-SCHs. If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Downlink, Radio Configuration 4 includes QPSK, F-FCHs and F-SCHs. |
| RFMXCDMA2K_VAL_RADIO_CONFIGURATION_RC5 (4) | If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Uplink, Radio configuration 5 is not supported and gives invalid results. If RFMXCDMA2K_ATTR_LINK_DIRECTION attribute is set to Downlink, Radio Configuration 5 includes QPSK, F-FCHs and F-SCHs. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_reference_level.html language=enus -->
## TOPIC 00175: RFMXCDMA2K_ATTR_REFERENCE_LEVEL

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_reference_level.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_REFERENCE_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeF64RFmxCDMA2k_GetAttributeF64 |
| Description: | Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value of this attribute is hardware dependent. Get Function: RFmxCDMA2k_GetReferenceLevel Set Function: RFmxCDMA2k_SetReferenceLevel |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_reference_level_headroom.html language=enus -->
## TOPIC 00176: RFMXCDMA2K_ATTR_REFERENCE_LEVEL_HEADROOM

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_reference_level_headroom.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_reference_level_headroom.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_REFERENCE_LEVEL_HEADROOM

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeF64RFmxCDMA2k_GetAttributeF64 |
| Description: | Specifies the margin RFmx adds to the RFMXCDMA2K_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow provided that the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise by reducing the Reference Level Headroom. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Valid values: PXIe-5668R: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxCDMA2k_GetReferenceLevelHeadroom Set Function: RFmxCDMA2k_SetReferenceLevelHeadroom |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_result_fetch_timeout.html language=enus -->
## TOPIC 00177: RFMXCDMA2K_ATTR_RESULT_FETCH_TIMEOUT

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_result_fetch_timeout.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_result_fetch_timeout.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_RESULT_FETCH_TIMEOUT

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeF64RFmxCDMA2k_GetAttributeF64 |
| Description: | Specifies the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete before fetching the measurement. The default value is 10Â seconds. Get Function: RFmxCDMA2k_GetResultFetchTimeout Set Function: RFmxCDMA2k_SetResultFetchTimeout |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_selected_ports.html language=enus -->
## TOPIC 00178: RFMXCDMA2K_ATTR_SELECTED_PORTS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_selected_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_selected_ports.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SELECTED_PORTS

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeStringRFmxCDMA2k_GetAttributeString |
| Description: | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Valid values: PXIe-5830: if0, if1 Other devices: (empty string) PXIe-5831/5832: if0, if1, rf<0-1>/port, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values: PXIe-5830: if1 Other devices: (empty string) Get Function: RFmxCDMA2k_GetSelectedPorts Set Function: RFmxCDMA2k_SetSelectedPorts |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_all_traces_enabled.html language=enus -->
## TOPIC 00179: RFMXCDMA2K_ATTR_SEM_ALL_TRACES_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_all_traces_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_FALSE. Get Function: RFmxCDMA2k_SEMGetAllTracesEnabled Set Function: RFmxCDMA2k_SEMSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_averaging_count.html language=enus -->
## TOPIC 00180: RFMXCDMA2K_ATTR_SEM_AVERAGING_COUNT

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_averaging_count.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED attribute to RFMXCDMA2K_VAL_SEM_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxCDMA2k_SEMGetAveragingCount Set Function: RFmxCDMA2k_SEMSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_averaging_enabled.html language=enus -->
## TOPIC 00181: RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_averaging_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the SEM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_SEM_AVERAGING_ENABLED_FALSE. Get Function: RFmxCDMA2k_SEMGetAveragingEnabled Set Function: RFmxCDMA2k_SEMSetAveragingEnabled |
| Values: | RFMXCDMA2K_VAL_SEM_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXCDMA2K_VAL_SEM_AVERAGING_ENABLED_TRUE (1)The SEM measurement uses the value of the RFMXCDMA2K_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_ENABLED_TRUE (1) | The SEM measurement uses the value of the RFMXCDMA2K_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_averaging_type.html language=enus -->
## TOPIC 00182: RFMXCDMA2K_ATTR_SEM_AVERAGING_TYPE

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_averaging_type.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_RMS. Get Function: RFmxCDMA2k_SEMGetAveragingType Set Function: RFmxCDMA2k_SEMSetAveragingType |
| Values: | RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_SCALAR (2)The square root of the power spectrum is averaged. RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_MAXIMUM (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_MINIMUM (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXCDMA2K_VAL_SEM_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_carrier_integration_bandwidth.html language=enus -->
## TOPIC 00183: RFMXCDMA2K_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_carrier_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_carrier_integration_bandwidth.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the SEM carrier integration bandwidth. This value is expressed in Hz. You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_SEMGetCarrierIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_measurement_enabled.html language=enus -->
## TOPIC 00184: RFMXCDMA2K_ATTR_SEM_MEASUREMENT_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_measurement_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable the SEM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_FALSE. Get Function: RFmxCDMA2k_SEMGetMeasurementEnabled Set Function: RFmxCDMA2k_SEMSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_number_of_analysis_threads.html language=enus -->
## TOPIC 00185: RFMXCDMA2K_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_number_of_analysis_threads.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the SEM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxCDMA2k_SEMGetNumberOfAnalysisThreads Set Function: RFmxCDMA2k_SEMSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_number_of_offsets.html language=enus -->
## TOPIC 00186: RFMXCDMA2K_ATTR_SEM_NUMBER_OF_OFFSETS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_number_of_offsets.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_NUMBER_OF_OFFSETS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeI32 |
| Description: | Returns the number of SEM offset segments. You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxCDMA2k_SEMGetNumberOfOffsets |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_offset_bandwidth_integral.html language=enus -->
## TOPIC 00187: RFMXCDMA2K_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_offset_bandwidth_integral.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_offset_bandwidth_integral.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeI32 |
| Description: | Returns the bandwidth integral for a specific offset segment. A bandwidth integral greater than 1 indicates a RBW filter of a narrower bandwidth is used for the offset segment measurement, and digital processing is used to achieve the RBW defined for the offset segment. Use the following equation to calculate the value of the offset segment RBW: offset segment RBW = RBW * BW integral Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetOffsetBandwidthIntegral |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_offset_rbw_filter_bandwidth.html language=enus -->
## TOPIC 00188: RFMXCDMA2K_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_offset_rbw_filter_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_offset_rbw_filter_bandwidth.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetOffsetRBWFilterBandwidth |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_offset_rbw_filter_type.html language=enus -->
## TOPIC 00189: RFMXCDMA2K_ATTR_SEM_OFFSET_RBW_FILTER_TYPE

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_offset_rbw_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_offset_rbw_filter_type.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_OFFSET_RBW_FILTER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeI32 |
| Description: | Returns the type of RBW filter used to sweep the offset segment. Use 'offset(n)' as the Selector Strings to read this result. The default value is RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN. Get Function: RFmxCDMA2k_SEMGetOffsetRBWFilterType |
| Values: | RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED (0)No RBW filtering is performed. RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN (1)The RBW filter has a Gaussian response. RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT (2)The RBW filter has a flat response. RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_4 (3)The RBW filter has a response of a 4-pole synchronously tuned filter. RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_5 (4)The RBW filter has a response of a 5-pole synchronously tuned filter. |
| RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |
| RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN (1) | The RBW filter has a Gaussian response. |
| RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT (2) | The RBW filter has a flat response. |
| RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_4 (3) | The RBW filter has a response of a 4-pole synchronously tuned filter. |
| RFMXCDMA2K_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_5 (4) | The RBW filter has a response of a 5-pole synchronously tuned filter. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_offset_start_frequency.html language=enus -->
## TOPIC 00190: RFMXCDMA2K_ATTR_SEM_OFFSET_START_FREQUENCY

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_offset_start_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_offset_start_frequency.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_OFFSET_START_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetOffsetStartFrequency |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_offset_stop_frequency.html language=enus -->
## TOPIC 00191: RFMXCDMA2K_ATTR_SEM_OFFSET_STOP_FREQUENCY

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_offset_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_offset_stop_frequency.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_OFFSET_STOP_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetOffsetStopFrequency |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_carrier_absolute_integrated_power.html language=enus -->
## TOPIC 00192: RFMXCDMA2K_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_carrier_absolute_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_carrier_absolute_integrated_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23Â MHz. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_SEMGetResultsCarrierAbsoluteIntegratedPower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_lower_offset_absolute_integrated_power.html language=enus -->
## TOPIC 00193: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_lower_offset_absolute_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_lower_offset_absolute_integrated_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsLowerOffsetAbsoluteIntegratedPower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_lower_offset_absolute_peak_power.html language=enus -->
## TOPIC 00194: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_lower_offset_absolute_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_lower_offset_absolute_peak_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsLowerOffsetAbsolutePeakPower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_lower_offset_margin.html language=enus -->
## TOPIC 00195: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_lower_offset_margin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_lower_offset_margin.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask, which can be absolute or relative. Use 'offset(n)' as the Selector Strings to read this result. Setting Specified by the Standard: Margin DescriptionAbsolute: Returns the margin with reference to the absolute limit mask.Relative: Returns the margin with reference to the relative limit mask.Abs AND Rel: Returns the margin as the maximum of the margin referenced to the absolute and relative limit masks.Abs OR Rel: Returns the margin as the minimum of the margin referenced to the absolute and relative limit masks. Get Function: RFmxCDMA2k_SEMGetResultsLowerOffsetMargin |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_lower_offset_margin_absolute_power.html language=enus -->
## TOPIC 00196: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_lower_offset_margin_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_lower_offset_margin_absolute_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsLowerOffsetMarginAbsolutePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_lower_offset_margin_frequency.html language=enus -->
## TOPIC 00197: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_lower_offset_margin_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_lower_offset_margin_frequency.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsLowerOffsetMarginFrequency |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_lower_offset_margin_relative_power.html language=enus -->
## TOPIC 00198: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_lower_offset_margin_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_lower_offset_margin_relative_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsLowerOffsetMarginRelativePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_lower_offset_measurement_status.html language=enus -->
## TOPIC 00199: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_lower_offset_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_lower_offset_measurement_status.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeI32 |
| Description: | Indicates the lower offset segment measurement status based on measurement limits specified by the standard. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsLowerOffsetMeasurementStatus |
| Values: | RFMXCDMA2K_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL (0)The lower offset segment measurement fails according to the measurement limits specified by the standard. RFMXCDMA2K_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS (1)The lower offset segment measurement passes according to the measurement limits specified by the standard. |
| RFMXCDMA2K_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL (0) | The lower offset segment measurement fails according to the measurement limits specified by the standard. |
| RFMXCDMA2K_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS (1) | The lower offset segment measurement passes according to the measurement limits specified by the standard. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_lower_offset_peak_frequency.html language=enus -->
## TOPIC 00200: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_lower_offset_peak_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_lower_offset_peak_frequency.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsLowerOffsetPeakFrequency |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_lower_offset_relative_integrated_power.html language=enus -->
## TOPIC 00201: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_lower_offset_relative_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_lower_offset_relative_integrated_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsLowerOffsetRelativeIntegratedPower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_lower_offset_relative_peak_power.html language=enus -->
## TOPIC 00202: RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_lower_offset_relative_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_lower_offset_relative_peak_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the peak power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsLowerOffsetRelativePeakPower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_measurement_status.html language=enus -->
## TOPIC 00203: RFMXCDMA2K_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_measurement_status.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeI32 |
| Description: | Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxCDMA2k_SEMGetResultsMeasurementStatus |
| Values: | RFMXCDMA2K_VAL_SEM_MEASUREMENT_STATUS_FAIL (0)The measurement fails according to the measurement limits specified by this standard. RFMXCDMA2K_VAL_SEM_MEASUREMENT_STATUS_PASS (1)The measurement passes according to the measurement limits specified by this standard. |
| RFMXCDMA2K_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | The measurement fails according to the measurement limits specified by this standard. |
| RFMXCDMA2K_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | The measurement passes according to the measurement limits specified by this standard. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_upper_offset_absolute_integrated_power.html language=enus -->
## TOPIC 00204: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_upper_offset_absolute_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_upper_offset_absolute_integrated_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the power measured in the upper (positive) offset segment. This value is expressed in dB. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsUpperOffsetAbsoluteIntegratedPower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_upper_offset_absolute_peak_power.html language=enus -->
## TOPIC 00205: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_upper_offset_absolute_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_upper_offset_absolute_peak_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the peak power measured in the upper (positive) offset segment. This value is expressed in dBm. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsUpperOffsetAbsolutePeakPower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_upper_offset_margin.html language=enus -->
## TOPIC 00206: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_upper_offset_margin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_upper_offset_margin.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative). Use 'offset(n)' as the Selector Strings to read this result. Setting Specified by the Standard: Margin DescriptionAbsolute: Returns the margin with reference to the absolute limit mask.Relative: Returns the margin with reference to the relative limit mask.Abs AND Rel: Returns the margin as the maximum of the margin referenced to the absolute and relative limit masks.Abs OR Rel: Returns the margin as the minimum of the margin referenced to the absolute and relative limit masks. Get Function: RFmxCDMA2k_SEMGetResultsUpperOffsetMargin |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_upper_offset_margin_absolute_power.html language=enus -->
## TOPIC 00207: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_upper_offset_margin_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_upper_offset_margin_absolute_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsUpperOffsetMarginAbsolutePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_upper_offset_margin_frequency.html language=enus -->
## TOPIC 00208: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_upper_offset_margin_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_upper_offset_margin_frequency.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsUpperOffsetMarginFrequency |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_upper_offset_margin_relative_power.html language=enus -->
## TOPIC 00209: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_upper_offset_margin_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_upper_offset_margin_relative_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsUpperOffsetMarginRelativePower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_upper_offset_measurement_status.html language=enus -->
## TOPIC 00210: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_upper_offset_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_upper_offset_measurement_status.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeI32 |
| Description: | Indicates the upper offset measurement status based on measurement limits set by the standard. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsUpperOffsetMeasurementStatus |
| Values: | RFMXCDMA2K_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL (0)The lower offset segment measurement fails according to the measurement limits specified by this standard. RFMXCDMA2K_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS (1)The lower offset segment measurement passes according to the measurement limits specified by this standard. |
| RFMXCDMA2K_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL (0) | The lower offset segment measurement fails according to the measurement limits specified by this standard. |
| RFMXCDMA2K_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS (1) | The lower offset segment measurement passes according to the measurement limits specified by this standard. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_upper_offset_peak_frequency.html language=enus -->
## TOPIC 00211: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_upper_offset_peak_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_upper_offset_peak_frequency.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsUpperOffsetPeakFrequency |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_results_upper_offset_relative_peak_power.html language=enus -->
## TOPIC 00212: RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_results_upper_offset_relative_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_results_upper_offset_relative_peak_power.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxCDMA2k_GetAttributeF64 |
| Description: | Returns the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. Use 'offset(n)' as the Selector Strings to read this result. Get Function: RFmxCDMA2k_SEMGetResultsUpperOffsetRelativePeakPower |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_sweep_time_auto.html language=enus -->
## TOPIC 00213: RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_AUTO

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_sweep_time_auto.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_SEM_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxCDMA2k_SEMGetSweepTimeAuto Set Function: RFmxCDMA2k_SEMSetSweepTimeAuto |
| Values: | RFMXCDMA2K_VAL_SEM_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the sweep time that you specify in the RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_INTERVAL attribute. RFMXCDMA2K_VAL_SEM_SWEEP_TIME_AUTO_TRUE (1)The measurement uses the default sweep time, 0.001667Â seconds. |
| RFMXCDMA2K_VAL_SEM_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_INTERVAL attribute. |
| RFMXCDMA2K_VAL_SEM_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the default sweep time, 0.001667Â seconds. |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_sem_sweep_time_interval.html language=enus -->
## TOPIC 00214: RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_sem_sweep_time_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_sem_sweep_time_interval.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeF64RFmxCDMA2k_GetAttributeF64 |
| Description: | Specifies the sweep time when you set the RFMXCDMA2K_ATTR_SEM_SWEEP_TIME_AUTO attribute to RFMXCDMA2K_VAL_SEM_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.001667Â seconds. Get Function: RFmxCDMA2k_SEMGetSweepTimeInterval Set Function: RFmxCDMA2k_SEMSetSweepTimeInterval |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_slotpower_measurement_enabled.html language=enus -->
## TOPIC 00215: RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_slotpower_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_slotpower_measurement_enabled.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies whether to enable the SlotPower measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXCDMA2K_VAL_FALSE. Get Function: RFmxCDMA2k_SlotPowerGetMeasurementEnabled Set Function: RFmxCDMA2k_SlotPowerSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_slotpower_measurement_offset.html language=enus -->
## TOPIC 00216: RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_slotpower_measurement_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_slotpower_measurement_offset.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeI32RFmxCDMA2k_GetAttributeI32 |
| Description: | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the RFMXCDMA2K_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE attribute. This value is expressed in slots. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxCDMA2k_SlotPowerGetMeasurementOffset Set Function: RFmxCDMA2k_SlotPowerSetMeasurementOffset |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_trigger_delay.html language=enus -->
## TOPIC 00217: RFMXCDMA2K_ATTR_TRIGGER_DELAY

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_trigger_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_trigger_delay.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_TRIGGER_DELAY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeF64RFmxCDMA2k_GetAttributeF64 |
| Description: | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0Â seconds. Get Function: RFmxCDMA2k_GetTriggerDelay Set Function: RFmxCDMA2k_SetTriggerDelay |

<!--NI_TOPIC bundle=rfmx-cdma2k-cvi path=rfmxcdma2k_attr_trigger_minimum_quiet_time_duration.html language=enus -->
## TOPIC 00218: RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmx-cdma2k-cvi`
- source_path: `rfmxcdma2k_attr_trigger_minimum_quiet_time_duration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-cvi/raw/resource/enus/rfmxcdma2k_attr_trigger_minimum_quiet_time_duration.html
- document_id: `rfmx-cdma2k-cvi`
- page_type: `leaf`
- content_type: ``

RFMXCDMA2K_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxCDMA2k_SetAttributeF64RFmxCDMA2k_GetAttributeF64 |
| Description: | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to RFMXCDMA2K_VAL_IQ_POWER_EDGE_RISING_SLOPE, the signal is quiet below the trigger level. If you set the RFMXCDMA2K_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to RFMXCDMA2K_VAL_IQ_POWER_EDGE_FALLING_SLOPE, the signal is quiet above the trigger level. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value of this attribute is hardware dependent. Get Function: RFmxCDMA2k_GetTriggerMinimumQuietTimeDuration Set Function: RFmxCDMA2k_SetTriggerMinimumQuietTimeDuration |
