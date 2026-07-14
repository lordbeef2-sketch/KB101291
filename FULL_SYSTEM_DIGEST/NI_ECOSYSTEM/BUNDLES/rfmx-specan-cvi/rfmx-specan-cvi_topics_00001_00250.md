# NI DOCUMENT BUNDLE: rfmx-specan-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-specan-cvi start=1 end=250 -->
<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_ampmfetchamtopmtrace.html language=enus -->
## TOPIC 00001: RFmxSpecAn_AMPMFetchAMToPMTrace

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_ampmfetchamtopmtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_ampmfetchamtopmtrace.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_AMPMFetchAMToPMTrace

int32 __stdcall RFmxSpecAn_AMPMFetchAMToPMTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 referencePowers[],
 float32 measuredAMToPM[],
 float32 curveFitAMToPM[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the AM-to-PM trace where the **inputPowers** array forms the x-axis of the trace and the **measuredAMToPM** and **curveFitAMToPM** arrays form the y-axis of the trace.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| Reference Powers | float32[] | Returns the array of reference powers. This value is expressed in dBm. |
| measuredAMToPM | float32[] | Returns the polynomial fit phase distortion values corresponding to the reference powers. This value is expressed in degrees. |
| curveFitAMToPM | float32[] | Returns the phase distortion values corresponding to the reference powers. This value is expressed in degrees. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_ampmfetchcurvefitcoefficients.html language=enus -->
## TOPIC 00002: RFmxSpecAn_AMPMFetchCurveFitCoefficients

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_ampmfetchcurvefitcoefficients.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_ampmfetchcurvefitcoefficients.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_AMPMFetchCurveFitCoefficients

int32 __stdcall RFmxSpecAn_AMPMFetchCurveFitCoefficients (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 AMToAMCoefficients[],
 float32 AMToPMCoefficients[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the coefficients of the polynomials that approximate the AM-to-AM and AM-to-PM responses of the device under test (DUT).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| AMToAMCoefficients | float32[] | Returns the coefficients of the polynomial that approximates the AM-to-AM characteristic of the device under test. |
| AMToPMCoefficients | float32[] | Returns the coefficients of the polynomial that approximates the AM-to-PM characteristic of the device under test. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_ampmfetchcurvefitresidual.html language=enus -->
## TOPIC 00003: RFmxSpecAn_AMPMFetchCurveFitResidual

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_ampmfetchcurvefitresidual.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_ampmfetchcurvefitresidual.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_AMPMFetchCurveFitResidual

int32 __stdcall RFmxSpecAn_AMPMFetchCurveFitResidual (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* AMToAMResidual,
 float64* AMToPMResidual);

#### Purpose

Fetches the polynomial approximation residuals for the AM-to-AM and AM-to-PM responses of the device under test (DUT).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| AMToAMResidual | float64* | Returns the approximation error, in dB, in the polynomial approximation of the AM-to-AM characteristic of the DUT. |
| AMToPMResidual | float64* | Returns the approximation error, in degrees, in the polynomial approximation of the AM-to-PM characteristic of the DUT. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_ampmfetchprocessedreferencewaveform.html language=enus -->
## TOPIC 00004: RFmxSpecAn_AMPMFetchProcessedReferenceWaveform

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_ampmfetchprocessedreferencewaveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_ampmfetchprocessedreferencewaveform.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_AMPMFetchProcessedReferenceWaveform

int32 __stdcall RFmxSpecAn_AMPMFetchProcessedReferenceWaveform (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 NIComplexSingle processedReferenceWaveform[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the segment of the reference waveform used to perform the AMPM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time, in seconds |
| dx | float64* | Returns the sample duration, in seconds. |
| processedReferenceWaveform | NIComplexSingle[] | Returns the complex baseband samples, in volts. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_ampmfetchprocessedreferencewaveformsplit.html language=enus -->
## TOPIC 00005: RFmxSpecAn_AMPMFetchProcessedReferenceWaveformSplit

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_ampmfetchprocessedreferencewaveformsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_ampmfetchprocessedreferencewaveformsplit.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_AMPMFetchProcessedReferenceWaveformSplit

int32 __stdcall RFmxSpecAn_AMPMFetchProcessedReferenceWaveformSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the segment of the reference waveform used to perform the AMPM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of I and Q array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time, in seconds. |
| dx | float64* | Returns the sample duration, in seconds. |
| I | float32[] | Returns the real part of complex baseband samples, in volts. |
| Q | float32[] | Returns the imaginary part of complex baseband samples, in volts. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_analyzeiq1waveformsplit.html language=enus -->
## TOPIC 00006: RFmxSpecAn_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_analyzeiq1waveformsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_analyzeiq1waveformsplit.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_AnalyzeIQ1WaveformSplit

int32 __stdcall RFmxSpecAn_AnalyzeIQ1WaveformSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[],
 float64 x0,
 float64 dx,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32 reset,
 int64 reserved);

#### Purpose

Performs the enabled measurements on the I/Q complex waveform that you specify in the **I** and **Q** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes.
Use this function only if the Recommended Acquisition Type attribute value is either **IQ** or **IQorSpectral**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "" "result::r1" "r1" |
| x0 | float64 | Specifies the start time of the input y array. This value is expressed in seconds. |
| dx | float64 | Specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| I | float32[] | Specifies the real part of the array of complex-valued time domain data. The real part of this complex data array correspond to the in-phase (I) data. |
| Q | float32[] | Specifies the imaginary part of the array of complex-valued time domain data. The imaginary part of this complex data array correspond to the quadrature-phase (Q) data. |
| arraySize | int32 | Specifies the size of I and Q array. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
| reserved | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_autolevel.html language=enus -->
## TOPIC 00007: RFmxSpecAn_AutoLevel

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_autolevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_autolevel.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_AutoLevel

int32 __stdcall RFmxSpecAn_AutoLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 bandwidth,
 float64 measurementInterval, float64 *referenceLevel);

#### Purpose

Examines the incoming signal to calculate the peak power level and sets it as the value of the [RFMXSPECAN_ATTR_REFERENCE_LEVEL](/csh?topicname=rfmxspecancvi/rfmxspecan_attr_reference_level.html) attribute. Use this function to help calculate an approximate setting for the reference level.

The RFmxSpecAn_AutoLevel function does the following:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

RFMXSPECAN_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| bandwidth | float64 | Specifies the bandwidth, in Hz, of the signal to be analyzed. |
| measurementInterval | float64 | Specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| Output |  |  |
| Name | Type | Description |
| referenceLevel | float64* | Returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and as Vpk-pk for baseband devices. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_buildcarrierstring2.html language=enus -->
## TOPIC 00008: RFmxSpecAn_BuildCarrierString2

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_buildcarrierstring2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_buildcarrierstring2.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_BuildCarrierString2

int32 __stdcall RFmxSpecAn_BuildCarrierString2 (char selectorString[],
 int32 carrierNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the selector string to use with the SEM, ACP, and CHP carrier configuration or fetch attributes and functions. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **selectorStringOutLength** parameter.

If you want to call this function just to get the required buffer size, you must pass 0 for **selectorStringOutLength** and NULL for the **selectorStringOut** buffer.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| carrierNumber | int32 | Specifies the carrier number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_buildmarkerstring2.html language=enus -->
## TOPIC 00009: RFmxSpecAn_BuildMarkerString2

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_buildmarkerstring2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_buildmarkerstring2.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_BuildMarkerString2

int32 __stdcall RFmxSpecAn_BuildMarkerString2 (char selectorString[],
 int32 markerNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the selector string to use with marker configuration or fetch attributes and functions. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **selectorStringOutLength** parameter.

If you want to call this function just to get the required buffer size, you must pass 0 for **selectorStringOutLength** and NULL for the **selectorStringOut** buffer.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| markerNumber | int32 | Specifies the marker number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_buildsignalstring.html language=enus -->
## TOPIC 00010: RFmxSpecAn_BuildSignalString

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_buildsignalstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_buildsignalstring.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_BuildSignalString

int32 __stdcall RFmxSpecAn_BuildSignalString (char signalName[], char resultName[], int32 selectorStringLength, char selectorString[]);

#### Purpose

Creates the selector string for use with Configuration or Fetch attributes and functions. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **selectorStringLength** parameter. 
 

If you want to call this function just to get the required buffer size, you must pass 0 for **selectorStringLength** and NULL for the **selectorString** buffer.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| signalName | char[] | Specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. Example: "" "signal::sig1" "sig1" |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "" "result::r1" "r1" |
| selectorStringLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| selectorString | char[] | Returns the selector string created by this function. You can pass NULL for this parameter if selectorStringLength is set to 0, which will return the minimum buffer size required to create the signal string. If the selectorString buffer is not large enough to build the signal string, the function returns an error. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_ccdfcfgthreshold.html language=enus -->
## TOPIC 00011: RFmxSpecAn_CCDFCfgThreshold

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_ccdfcfgthreshold.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_ccdfcfgthreshold.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_CCDFCfgThreshold

int32 __stdcall RFmxSpecAn_CCDFCfgThreshold (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 thresholdEnabled, float64 thresholdLevel, int32 thresholdType);

#### Purpose

Configures the threshold level for the samples that need to be considered for the complementary cumulative distribution function (CCDF) measurement. Enable the threshold when analyzing burst signals or signals with dead time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| thresholdEnabled | int32 | Specifies whether to enable thresholding of the acquired samples to be used for the measurement. RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_FALSE (0) All samples are considered for the measurement. RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_TRUE (1) The samples above the threshold level specified in the thresholdLevel parameter are considered for the measurement. |
| RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_FALSE (0) | All samples are considered for the measurement. |  |
| RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_TRUE (1) | The samples above the threshold level specified in the thresholdLevel parameter are considered for the measurement. |  |
| thresholdLevel | float64 | Specifies either the relative or absolute threshold power level based on the value of the thresholdType parameter. |
| thresholdType | int32 | Specifies the reference for the power level used for thresholding. RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_RELATIVE (0) The threshold is relative to the peak power, in dB, of the acquired samples. RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_ABSOLUTE (1) The threshold is the absolute power, in dBm. |
| RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_RELATIVE (0) | The threshold is relative to the peak power, in dB, of the acquired samples. |  |
| RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_ABSOLUTE (1) | The threshold is the absolute power, in dBm. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_ccdffetchpower.html language=enus -->
## TOPIC 00012: RFmxSpecAn_CCDFFetchPower

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_ccdffetchpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_ccdffetchpower.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_CCDFFetchPower

int32 __stdcall RFmxSpecAn_CCDFFetchPower (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanPower, float64* meanPowerPercentile, float64* peakPower, int32* measuredSamplesCount);

#### Purpose

Returns the mean power and peak power for the complementary cumulative distribution function (CCDF) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanPower | float64* | Returns the average power, in dBm, of all the samples. If you set the RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED attribute to RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_TRUE, samples above the threshold are measured. |
| meanPowerPercentile | float64* | Returns the percentage of samples that have more power than the mean power. |
| peakPower | float64* | Returns the peak power of the acquired signal, relative to the mean power. |
| measuredSamplesCount | int32* | Returns the total number of samples measured. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_ccdffetchprobabilitiestrace.html language=enus -->
## TOPIC 00013: RFmxSpecAn_CCDFFetchProbabilitiesTrace

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_ccdffetchprobabilitiestrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_ccdffetchprobabilitiestrace.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_CCDFFetchProbabilitiesTrace

int32 __stdcall RFmxSpecAn_CCDFFetchProbabilitiesTrace (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 probabilities[], int32 arraySize, int32* actualArraySize);

#### Purpose

Returns the probabilities trace for the complementary cumulative distribution function (CCDF) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the y array. Set the arraySize parameter to 0 to get the size of the y array in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the mean power. |
| dx | float64* | Returns the bin size used by the CCDF measurement. |
| probabilities | float32[] | Returns the probability, as a percentage, indicating the occurrence of samples in the signal with power greater than the mean power by x dB. Set the arraySize parameter to 0 to get the size of the y array. You can pass NULL for this parameter if you set the arraySize parameter to 0. If the y array is not large enough to hold all the samples, the function returns an error. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_cfgrfattenuation.html language=enus -->
## TOPIC 00014: RFmxSpecAn_CfgRFAttenuation

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_cfgrfattenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_cfgrfattenuation.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_CfgRFAttenuation

int32 __stdcall RFmxSpecAn_CfgRFAttenuation (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| channelName | char[] | Set this parameter to "" (empty string) or NULL. |
| RFAttenuationAuto | int32 | Specifies whether the RFmx driver computes the RF attenuation. RFMXSPECAN_VAL_RF_ATTENUATION_AUTO_FALSE (0) Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter. RFMXSPECAN_VAL_RF_ATTENUATION_AUTO_TRUE (1) Specifies that the RFmx driver computes the RF attenuation automatically. |
| RFMXSPECAN_VAL_RF_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter. |  |
| RFMXSPECAN_VAL_RF_ATTENUATION_AUTO_TRUE (1) | Specifies that the RFmx driver computes the RF attenuation automatically. |  |
| RFAttenuationValue | float64 | Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain when the rfAttenuationAuto parameter is set to RFMXSPECAN_VAL_RF_ATTENUATION_AUTO_FALSE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_chpcfgfft.html language=enus -->
## TOPIC 00015: RFmxSpecAn_CHPCfgFFT

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_chpcfgfft.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_chpcfgfft.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_CHPCfgFFT

int32 __stdcall RFmxSpecAn_CHPCfgFFT (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 FFTWindow, float64 FFTPadding);

#### Purpose

Configures window and FFT to obtain a spectrum for the channel power (CHP) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| FFTWindow | int32 | Specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectrum topic for more information about FFT window types. RFMXSPECAN_VAL_CHP_FFT_WINDOW_NONE (0) Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. RFMXSPECAN_VAL_CHP_FFT_WINDOW_FLAT_TOP (1) Measures single-tone amplitudes accurately. RFMXSPECAN_VAL_CHP_FFT_WINDOW_HANNING (2) Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. RFMXSPECAN_VAL_CHP_FFT_WINDOW_HAMMING (3) Analyzes closely-spaced sine waves. RFMXSPECAN_VAL_CHP_FFT_WINDOW_GAUSSIAN (4) Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. RFMXSPECAN_VAL_CHP_FFT_WINDOW_BLACKMAN (5) Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. RFMXSPECAN_VAL_CHP_FFT_WINDOW_BLACKMAN_HARRIS (6) Useful as a good general purpose window, having side lobe rejection >90dB and having a moderately wide main lobe. RFMXSPECAN_VAL_CHP_FFT_WINDOW_KAISER_BESSEL (7) Separates two tones with frequencies close to each other but with widely-differing amplitudes. |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_NONE (0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |  |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_FLAT_TOP (1) | Measures single-tone amplitudes accurately. |  |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_HANNING (2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |  |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_HAMMING (3) | Analyzes closely-spaced sine waves. |  |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_GAUSSIAN (4) | Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. |  |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_BLACKMAN (5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |  |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_BLACKMAN_HARRIS (6) | Useful as a good general purpose window, having side lobe rejection >90dB and having a moderately wide main lobe. |  |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_KAISER_BESSEL (7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |  |
| FFTPadding | float64 | Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This parameter is used only when the acquisition span is less than the device instantaneous bandwidth of the device. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_chpfetchcarriermeasurement.html language=enus -->
## TOPIC 00016: RFmxSpecAn_CHPFetchCarrierMeasurement

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_chpfetchcarriermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_chpfetchcarriermeasurement.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_CHPFetchCarrierMeasurement

int32 __stdcall RFmxSpecAn_CHPFetchCarrierMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* absolutePower,
 float64* PSD,
 float64* relativePower);

#### Purpose

Returns the averaged channel power measurements. 
 

Use "carrier<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxSpecAn_BuildCarrierString2 function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| absolutePower | float64* | Returns the absolute power, in dBm, measured in the specified integration bandwidth. |
| PSD | float64* | Returns the power spectral density of the channel, in dBm/Hz. |
| relativePower | float64* | Returns the carrier power, in dB, measured relative to the total carrier power. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_chpfetchtotalcarrierpower.html language=enus -->
## TOPIC 00017: RFmxSpecAn_CHPFetchTotalCarrierPower

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_chpfetchtotalcarrierpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_chpfetchtotalcarrierpower.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_CHPFetchTotalCarrierPower

int32 __stdcall RFmxSpecAn_CHPFetchTotalCarrierPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* totalCarrierPower);

#### Purpose

Returns the total integrated carrier power.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| totalCarrierPower | float64 | Returns the total integrated power of all carriers, in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_chpread.html language=enus -->
## TOPIC 00018: RFmxSpecAn_CHPRead

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_chpread.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_chpread.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_CHPRead

int32 __stdcall RFmxSpecAn_CHPRead (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* absolutePower,
 float64* PSD);

#### Purpose

Configures hardware for acquisition, performs measurement on acquired data, and returns the channel power (CHP) measurement results.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| absolutePower | float64* | Returns the averaged CHP, in dBm, measured in the specified integration bandwidth. |
| PSD | float64* | Returns the power spectral density of the channel, in dBm/Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_chpvalidatenoisecalibrationdata.html language=enus -->
## TOPIC 00019: RFmxSpecAn_CHPValidateNoiseCalibrationData

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_chpvalidatenoisecalibrationdata.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_chpvalidatenoisecalibrationdata.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_CHPValidateNoiseCalibrationData

int32 __stdcall RFmxSpecAn_CHPValidateNoiseCalibrationData (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32* noiseCalibrationDataValid);

#### Purpose

Indicates whether calibration data is valid for the configuration specified by the signal name in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| noiseCalibrationDataValid | int32* | Returns whether the calibration data is valid. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_deletelist.html language=enus -->
## TOPIC 00020: RFmxSpecAn_DeleteList

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_deletelist.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_deletelist.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DeleteList

int32 __stdcall RFmxSpecAn_DeleteList (niRFmxInstrHandle instrumentHandle,
 char listName[]);

#### Purpose

Deletes the list instance and all the list steps that you specify in the **listName** parameter. When a list step is deleted, all the instances of attributes associated with the list step are also removed. 
**supported devices :**PXIe-5840/5841/5842

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| listName | char[] | Specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix.Example:"list::samplelist1""samplelist1"You can use the RFmxSpecAn_BuildListString function to build the list name. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_disabletrigger.html language=enus -->
## TOPIC 00021: RFmxSpecAn_DisableTrigger

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_disabletrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_disabletrigger.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DisableTrigger

int32 __stdcall RFmxSpecAn_DisableTrigger (niRFmxInstrHandle instrumentHandle, char selectorString[]);

#### Purpose

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdcfgapplydpduserdpdpolynomial.html language=enus -->
## TOPIC 00022: RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomial

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdcfgapplydpduserdpdpolynomial.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdcfgapplydpduserdpdpolynomial.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomial

int32 __stdcall RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomial (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 NIComplexSingle DPDPolynomial[],
int32 arraySize);

#### Purpose

Configures the array of memory polynomial or generalized memory polynomial coefficients when you set the [RFMXSPECAN_ATTR_DPD_MODEL](/csh?topicname=rfmxspecancvi/rfmxspecan_attr_dpd_model.html) attribute to RFMXSPECAN_VAL_DPD_MODEL_MEMORY_POLYNOMIAL or RFMXSPECAN_VAL_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| DPDPolynomial | NIComplexSingle[] | Specifies the array of memory polynomial or generalized memory polynomial coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_MEMORY_POLYNOMIAL or RFMXSPECAN_VAL_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL. |
| arraySize | int32 | Specifies the size of the DPDPolynomial array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdcfgapplydpduserlookuptablesplit.html language=enus -->
## TOPIC 00023: RFmxSpecAn_DPDCfgApplyDPDUserLookupTableSplit

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdcfgapplydpduserlookuptablesplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdcfgapplydpduserlookuptablesplit.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDCfgApplyDPDUserLookupTableSplit

int32 __stdcall RFmxSpecAn_DPDCfgApplyDPDUserLookupTableSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float32 LUTInputPowers[],
 float32 I[],
 float32 Q[],
 int32 arraySize);

#### Purpose

Configures the predistortion lookup table when you set the [RFMXSPECAN_ATTR_DPD_MODEL](/csh?topicname=rfmxspecancvi/rfmxspecan_attr_dpd_model.html) attribute to RFMXSPECAN_VAL_DPD_MODEL_LOOKUP_TABLE.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| LUTInputPowers | float32[] | Specifies the array of lookup table power levels, in dBm. |
| I | float32[] | Specifies the real part of the array of lookup table complex gain values for magnitude and phase predistortion. |
| Q | float32[] | Specifies the imaginary part of the array of lookup table complex gain values for magnitude and phase predistortion. |
| arraySize | int32 | Specifies the size of I and Q array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdcfgdpdmodel.html language=enus -->
## TOPIC 00024: RFmxSpecAn_DPDCfgDPDModel

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdcfgdpdmodel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdcfgdpdmodel.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDCfgDPDModel

int32 __stdcall RFmxSpecAn_DPDCfgDPDModel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 DPDModel);

#### Purpose

Configures the DPD model used by the DPD measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| DPDModel | int32 | Specifies the DPD model used by the DPD measurement. RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_LOOKUP_TABLE (0) This model computes the complex gain coefficients applied to linearize systems with negligible memory effects. RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_MEMORY_POLYNOMIAL (1) This model computes the memory polynomial predistortion coefficients used to linearize systems with moderate memory effects. RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL (2) This model computes the generalized memory polynomial predistortion coefficients used to linearize systems with significant memory effects. RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_DECOMPOSED_VECTOR_ROTATION (3) This model computes the decomposed vector rotation predistortion coefficients used to linearize wideband systems with significant memory effects. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_LOOKUP_TABLE (0) | This model computes the complex gain coefficients applied to linearize systems with negligible memory effects. |  |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_MEMORY_POLYNOMIAL (1) | This model computes the memory polynomial predistortion coefficients used to linearize systems with moderate memory effects. |  |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL (2) | This model computes the generalized memory polynomial predistortion coefficients used to linearize systems with significant memory effects. |  |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_DECOMPOSED_VECTOR_ROTATION (3) | This model computes the decomposed vector rotation predistortion coefficients used to linearize wideband systems with significant memory effects. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdcfgextractmodeltargetwaveformsplit.html language=enus -->
## TOPIC 00025: RFmxSpecAn_DPDCfgExtractModelTargetWaveformSplit

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdcfgextractmodeltargetwaveformsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdcfgextractmodeltargetwaveformsplit.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDCfgExtractModelTargetWaveformSplit

int32 __stdcall RFmxSpecAn_DPDCfgExtractModelTargetWaveformSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 x0,
 float64 dx,
 float32 targetWaveformI[],
 float32 targetWaveformQ[],
 int32 arraySize);

#### Purpose

Configures the complex baseband equivalent of the Target waveform desired at the output of the Predistorter Model to be extracted when performing the DPD measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| x0 | float64 | Specifies the start time, in seconds. |
| dx | float64 | Specifies the sample duration, in seconds. |
| I | NIComplexSingle[] | Specifies the real part of complex baseband samples, in volts. |
| Q | NIComplexSingle[] | Specifies the imaginary part of complex baseband samples, in volts. |
| arraySize | int32 | Specifies the size of the referenceWaveform array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdcfgmeasurementinterval.html language=enus -->
## TOPIC 00026: RFmxSpecAn_DPDCfgMeasurementInterval

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdcfgmeasurementinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdcfgmeasurementinterval.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDCfgMeasurementInterval

int32 __stdcall RFmxSpecAn_DPDCfgMeasurementInterval (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 measurementInterval);

#### Purpose

Specifies the duration, in seconds, of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading up to the start of the first active portion of the reference waveform.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementInterval | float64 | Specifies the acquisition time, in seconds, for the DPD measurement. This parameter also specifies the duration of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading up to the start of the first active portion of the reference waveform. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdfetchapplydpdprecfrpapr.html language=enus -->
## TOPIC 00027: RFmxSpecAn_DPDFetchApplyDPDPreCFRPAPR

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdfetchapplydpdprecfrpapr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdfetchapplydpdprecfrpapr.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDFetchApplyDPDPreCFRPAPR

int32 __stdcall RFmxSpecAn_DPDFetchApplyDPDPreCFRPAPR(niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* preCFRPAPR);

#### Purpose

Fetches the PAPR of the pre-distorted waveform before CFR is applied to it.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| averageGain | float64* | Returns the PAPR of the pre-distorted waveform before CFR is applied when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_ENABLED_TRUE. This value is expressed in dB. When you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_ENABLED_FALSE and the the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_LOOKUP_TABLE, the PAPR of the pre-distorted waveform is returned. When you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_ENABLED_FALSE and the the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_MEMORY_POLYNOMIAL or RFMXSPECAN_VAL_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL, the PAPR of the clipped pre-distorted waveform is returned. The pre-distorted waveform is clipped such that its peak amplitude does not exceed the peak of the input waveform, scaled to DUT average input power, by 6 dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdfetchaveragegain.html language=enus -->
## TOPIC 00028: RFmxSpecAn_DPDFetchAverageGain

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdfetchaveragegain.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdfetchaveragegain.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDFetchAverageGain

int32 __stdcall RFmxSpecAn_DPDFetchAverageGain (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* averageGain);

#### Purpose

Fetches the average gain, in dB, of the device under test (DUT) for the DPD measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| averageGain | float64* | Returns the average gain, in dB, of the device under test. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdfetchdpdpolynomial.html language=enus -->
## TOPIC 00029: RFmxSpecAn_DPDFetchDPDPolynomial

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdfetchdpdpolynomial.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdfetchdpdpolynomial.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDFetchDPDPolynomial

int32 __stdcall RFmxSpecAn_DPDFetchDPDPolynomial (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle DPDPolynomial[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the memory polynomial or generalized memory polynomial coefficients when you set the [RFMXSPECAN_ATTR_DPD_MODEL](/csh?topicname=rfmxspecancvi/rfmxspecan_attr_dpd_model.html) attribute to RFMXSPECAN_VAL_DPD_MODEL_MEMORY_POLYNOMIAL or RFMXSPECAN_VAL_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| DPDPolynomial | NIComplexSingle[] | Returns the memory polynomial or generalized memory polynomial coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_MEMORY_POLYNOMIAL or RFMXSPECAN_VAL_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdfetchdvrmodel.html language=enus -->
## TOPIC 00030: RFmxSpecAn_DPDFetchDVRModel

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdfetchdvrmodel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdfetchdvrmodel.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDFetchDVRModel

int32 __stdcall RFmxSpecAn_DPDFetchDVRModel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle DVRModel[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the decomposed vector rotation model coefficients when you set the [RFMXSPECAN_ATTR_DPD_MODEL](/csh?topicname=rfmxspecancvi/rfmxspecan_attr_dpd_model.html) attribute to RFMXSPECAN_VAL_DPD_MODEL_DECOMPOSED_VECTOR_ROTATION.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the referenceWaveform array. |
| Output |  |  |
| Name | Type | Description |
| DVRModel | NIComplexSingle[] | Returns the decomposed vector rotation model coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_DECOMPOSED_VECTOR_ROTATION. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdfetchdvrmodelsplit.html language=enus -->
## TOPIC 00031: RFmxSpecAn_DPDFetchDVRModelSplit

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdfetchdvrmodelsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdfetchdvrmodelsplit.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDFetchDVRModelSplit

int32 __stdcall RFmxSpecAn_DPDFetchDVRModelSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 DVRModelI[],
 float32 DVRModelQ[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the decomposed vector rotation model coefficients when you set the [RFMXSPECAN_ATTR_DPD_MODEL](/csh?topicname=rfmxspecancvi/rfmxspecan_attr_dpd_model.html) attribute to RFMXSPECAN_VAL_DPD_MODEL_DECOMPOSED_VECTOR_ROTATION.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the referenceWaveform array. |
| Output |  |  |
| Name | Type | Description |
| DVRModel | NIComplexSingle[] | Specifies an array of the real part of complex-valued time domain data. This array corresponds to the in-phase (I) data. |
| DVRModel | NIComplexSingle[] | Specifies an array of the imaginary part of complex-valued time domain data. This array corresponds to the quadrature-phase (Q) data. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_dpdfetchlookuptable.html language=enus -->
## TOPIC 00032: RFmxSpecAn_DPDFetchLookupTable

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_dpdfetchlookuptable.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_dpdfetchlookuptable.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_DPDFetchLookupTable

int32 __stdcall RFmxSpecAn_DPDFetchLookupTable (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 inputPowers[],
 NIComplexSingle complexGains[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the predistortion lookup table when you set the [RFMXSPECAN_ATTR_DPD_MODEL](/csh?topicname=rfmxspecancvi/rfmxspecan_attr_dpd_model.html) attribute to RFMXSPECAN_VAL_DPD_MODEL_LOOKUP_TABLE.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| inputPowers | float32[] | Returns the lookup table power levels, in dBm. |
| complexGains | NIComplexSingle[] | Returns the lookup table complex gain values, in dB, for magnitude and phase predistortion. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_getattributef64.html language=enus -->
## TOPIC 00033: RFmxSpecAn_GetAttributeF64

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_getattributef64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_getattributef64.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_GetAttributeF64

int32 __stdcall RFmxSpecAn_GetAttributeF64 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 *attrVal);

#### Purpose

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float64* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_getattributei16.html language=enus -->
## TOPIC 00034: RFmxSpecAn_GetAttributeI16

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_getattributei16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_getattributei16.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_GetAttributeI16

int32 __stdcall RFmxSpecAn_GetAttributeI16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int16 *attrVal);

#### Purpose

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int16* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_getattributei32array.html language=enus -->
## TOPIC 00035: RFmxSpecAn_GetAttributeI32Array

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_getattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_getattributei32array.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_GetAttributeI32Array

int32 __stdcall RFmxSpecAn_GetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int32[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_getattributeu8.html language=enus -->
## TOPIC 00036: RFmxSpecAn_GetAttributeU8

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_getattributeu8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_getattributeu8.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_GetAttributeU8

int32 __stdcall RFmxSpecAn_GetAttributeU8 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_harmcfgautoharmonics.html language=enus -->
## TOPIC 00037: RFmxSpecAn_HarmCfgAutoHarmonics

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_harmcfgautoharmonics.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_harmcfgautoharmonics.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_HarmCfgAutoHarmonics

int32 __stdcall RFmxSpecAn_HarmCfgAutoHarmonics (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 autoHarmonicsSetupEnabled);

#### Purpose

Configures auto configuration of successive harmonics. 
 


**Supported devices**: PXIe-5665, PXIe-5668

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| autoHarmonicsSetupEnabled | int32 | Specifies whether to enable auto configuration of successive harmonics. RFMXSPECAN_VAL_HARM_AUTO_HARMONICS_SETUP_ENABLED_FALSE (0) The measurement uses manual configuration for the harmonic order, harmonic bandwidth, and harmonic measurement interval. RFMXSPECAN_VAL_HARM_AUTO_HARMONICS_SETUP_ENABLED_TRUE (1) The measurement uses the RFMXSPECAN_ATTR_HARM_NUMBER_OF_HARMONICS attribute and configuration of the fundamental to configure successive harmonics. Bandwidth of Nth order harmonic = N * (Bandwidth of fundamental). Measurement interval of Nth order harmonics = (Measurement interval of fundamental)/N |
| RFMXSPECAN_VAL_HARM_AUTO_HARMONICS_SETUP_ENABLED_FALSE (0) | The measurement uses manual configuration for the harmonic order, harmonic bandwidth, and harmonic measurement interval. |  |
| RFMXSPECAN_VAL_HARM_AUTO_HARMONICS_SETUP_ENABLED_TRUE (1) | The measurement uses the RFMXSPECAN_ATTR_HARM_NUMBER_OF_HARMONICS attribute and configuration of the fundamental to configure successive harmonics. Bandwidth of Nth order harmonic = N * (Bandwidth of fundamental). Measurement interval of Nth order harmonics = (Measurement interval of fundamental)/N |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_harmcfgaveraging.html language=enus -->
## TOPIC 00038: RFmxSpecAn_HarmCfgAveraging

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_harmcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_harmcfgaveraging.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_HarmCfgAveraging

int32 __stdcall RFmxSpecAn_HarmCfgAveraging (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType);

#### Purpose

Configures averaging for the harmonics measurement. 
 


**Supported devices**: PXIe-5665, PXIe-5668

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXSPECAN_VAL_HARM_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition. RFMXSPECAN_VAL_HARM_AVERAGING_ENABLED_TRUE (1) The measurement uses the averagingCount parameter to calculate the number of acquisitions over which the measurement is averaged. |
| RFMXSPECAN_VAL_HARM_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXSPECAN_VAL_HARM_AVERAGING_ENABLED_TRUE (1) | The measurement uses the averagingCount parameter to calculate the number of acquisitions over which the measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXSPECAN_VAL_HARM_AVERAGING_ENABLED_TRUE. |
| averagingType | int32 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_LOG (1) The power spectrum is averaged in a logarithm scale. RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_SCALAR (2) The square root of the power spectrum is averaged. RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_MAXIMUM (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_MINIMUM (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithm scale. |  |
| RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |  |
| RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_idpdfetchequalizercoefficients.html language=enus -->
## TOPIC 00039: RFmxSpecAn_IDPDFetchEqualizerCoefficients

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_idpdfetchequalizercoefficients.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_idpdfetchequalizercoefficients.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_IDPDFetchEqualizerCoefficients

int32 __stdcall RFmxSpecAn_IDPDFetchEqualizerCoefficients (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 NIComplexSingle equalizerCoefficients[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the trained equalizer coefficients.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the referenceWaveform array. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | This parameter always returns 0. |
| dx | float64* | Returns the frequency bin spacing, in Hz. |
| equalizerCoefficients | NIComplexSingle[] | Returns the updated equalizer coefficients. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_idpdfetchprocessedreferencewaveform.html language=enus -->
## TOPIC 00040: RFmxSpecAn_IDPDFetchProcessedReferenceWaveform

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_idpdfetchprocessedreferencewaveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_idpdfetchprocessedreferencewaveform.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_IDPDFetchProcessedReferenceWaveform

int32 __stdcall RFmxSpecAn_IDPDFetchProcessedReferenceWaveform (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 NIComplexSingle processedReferenceWaveform[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the reference waveform used to perform the IDPD measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the referenceWaveform array. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time, in seconds. |
| dx | float64* | Returns the frequency bin spacing, in Hz. |
| processedReferenceWaveform | NIComplexSingle[] | Returns the complex baseband samples, in volts. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_imcfgfrequencydefinition.html language=enus -->
## TOPIC 00041: RFmxSpecAn_IMCfgFrequencyDefinition

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_imcfgfrequencydefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_imcfgfrequencydefinition.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_IMCfgFrequencyDefinition

int32 __stdcall RFmxSpecAn_IMCfgFrequencyDefinition (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 frequencyDefinition);

#### Purpose

Configures whether you can specify the tones and intermod frequencies as either relative to the RF center frequency or as absolute frequencies.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| frequencyDefinition | int32 | Specifies whether you can specify the tones and intermod frequencies as either relative to the RF center frequency or as absolute frequencies. RFMXSPECAN_VAL_IM_FREQUENCY_DEFINITION_RELATIVE (0) The tone and intermod frequencies are relative to the RF center frequency.RFMXSPECAN_VAL_IM_FREQUENCY_DEFINITION_ABSOLUTE (1) The tone and intermod frequencies are absolute frequencies. The measurement ignores the RF center frequency. |
| RFMXSPECAN_VAL_IM_FREQUENCY_DEFINITION_RELATIVE (0) | The tone and intermod frequencies are relative to the RF center frequency. |  |
| RFMXSPECAN_VAL_IM_FREQUENCY_DEFINITION_ABSOLUTE (1) | The tone and intermod frequencies are absolute frequencies. The measurement ignores the RF center frequency. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_imcfgfundamentaltones.html language=enus -->
## TOPIC 00042: RFmxSpecAn_IMCfgFundamentalTones

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_imcfgfundamentaltones.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_imcfgfundamentaltones.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_IMCfgFundamentalTones

int32 __stdcall RFmxSpecAn_IMCfgFundamentalTones (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 lowerToneFrequency,
 float64 upperToneFrequency);

#### Purpose

Configures the frequencies of the upper and lower frequencies in a two-tone input signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| lowerToneFrequency | float64 | Specifies the frequency of the tone that has a lower frequency among the two tones in the input signal. This value is expressed in Hz. |
| upperToneFrequency | float64 | Specifies the frequency of the tone that has a higher frequency among the two tones in the input signal. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_imcfgintermodarray.html language=enus -->
## TOPIC 00043: RFmxSpecAn_IMCfgIntermodArray

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_imcfgintermodarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_imcfgintermodarray.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_IMCfgIntermodArray

int32 __stdcall RFmxSpecAn_IMCfgIntermodArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 intermodOrder[],
 float64 lowerIntermodFrequency[],
 float64 upperIntermodFrequency[],
 int32 intermodSide[],
 int32 intermodEnabled[],
 int32 numberOfElements);

#### Purpose

Configures the intermod order, intermod side, lower intermod frequency, and upper intermod frequency when you set the [RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED](/csh?topicname=rfmxspecancvi/rfmxspecan_attr_im_auto_intermods_setup_enabled.html) attribute to RFMXSPECAN_VAL_IM_AUTO_INTERMODS_SETUP_ENABLED_FALSE.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| intermodOrder | int32[] | Specifies array of orders of the intermod. |
| lowerIntermodFrequency | float64[] | Specifies an array of the frequencies of the lower intermodulation products. This value is expressed in Hz. |
| upperIntermodFrequency | float64[] | Specifies an array of frequencies of the upper intermodulation products. This value is expressed in Hz. |
| intermodSide | int32[] | Specifies whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. RFMXSPECAN_VAL_IM_INTERMOD_SIDE_LOWER (0) Measures the intermodulation product corresponding to the lowerIntermodFrequency parameter.RFMXSPECAN_VAL_IM_INTERMOD_SIDE_UPPER (1) Measures the intermodulation product corresponding to the upperIntermodFrequency parameter.RFMXSPECAN_VAL_IM_INTERMOD_SIDE_BOTH (2) Measures the intermodulation product corresponding to the lowerIntermodFrequency and upperIntermodFrequency parameters. |
| RFMXSPECAN_VAL_IM_INTERMOD_SIDE_LOWER (0) | Measures the intermodulation product corresponding to the lowerIntermodFrequency parameter. |  |
| RFMXSPECAN_VAL_IM_INTERMOD_SIDE_UPPER (1) | Measures the intermodulation product corresponding to the upperIntermodFrequency parameter. |  |
| RFMXSPECAN_VAL_IM_INTERMOD_SIDE_BOTH (2) | Measures the intermodulation product corresponding to the lowerIntermodFrequency and upperIntermodFrequency parameters. |  |
| intermodEnabled | int32[] | Specifies whether to enable an intermod for the IM measurement. RFMXSPECAN_VAL_IM_INTERMOD_ENABLED_FALSE (0) Disables the intermod for the IM measurement. The results for the disabled intermods are displayed as NaN.RFMXSPECAN_VAL_IM_INTERMOD_ENABLED_TRUE (1) Enables the intermod for the IM measurement. |
| RFMXSPECAN_VAL_IM_INTERMOD_ENABLED_FALSE (0) | Disables the intermod for the IM measurement. The results for the disabled intermods are displayed as NaN. |  |
| RFMXSPECAN_VAL_IM_INTERMOD_ENABLED_TRUE (1) | Enables the intermod for the IM measurement. |  |
| numberOfElements | int32 | Specifies the number of elements in each array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_imcfgmeasurementmethod.html language=enus -->
## TOPIC 00044: RFmxSpecAn_IMCfgMeasurementMethod

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_imcfgmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_imcfgmeasurementmethod.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_IMCfgMeasurementMethod

int32 __stdcall RFmxSpecAn_IMCfgMeasurementMethod (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 measurementMethod);

#### Purpose

Configures the method for performing the IM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementMethod | int32 | Specifies the method for performing the IM measurement. RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_NORMAL (0) The IM measurement acquires the spectrum using the same signal analyzer settings across frequency bands. Use this method when the fundamental tone separation is not large. Supported devices:PXIe-5644/5645/5646/5840/5841/5830/5831/5832, PXIe-5663/5665/5668.RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_DYNAMIC_RANGE (1) The IM measurement acquires a segmented spectrum using the signal analyzer specific optimizations for different frequency bands. The spectrum is acquired in segments, one per tone or intermod frequency to be measured. The span of each acquired spectral segment is equal to the frequency separation between the two input tones, or 1 MHz, whichever is smaller.Use this method to configure the IM measurement and the signal analyzer for maximum dynamic range instead of measurement speed.Supported devices:PXIe-5665/5668RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_SEGMENTED (2) Similar to the dynamicRange method, this method also acquires a segmented spectrum, except that signal analyzer is not explicitly configured to provide maximum dynamic range. Use this method when the frequency separation of the two input tones is large and the measurement accuracy can be traded off for measurement speed.Supported devices:PXIe-5644/5645/5646/5840/5841/5842/5860/5830/5831/5832, PXIe-5663/5665/5668 |
| RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_NORMAL (0) | The IM measurement acquires the spectrum using the same signal analyzer settings across frequency bands. Use this method when the fundamental tone separation is not large. Supported devices:PXIe-5644/5645/5646/5840/5841/5830/5831/5832, PXIe-5663/5665/5668. |  |
| RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_DYNAMIC_RANGE (1) | The IM measurement acquires a segmented spectrum using the signal analyzer specific optimizations for different frequency bands. The spectrum is acquired in segments, one per tone or intermod frequency to be measured. The span of each acquired spectral segment is equal to the frequency separation between the two input tones, or 1 MHz, whichever is smaller.Use this method to configure the IM measurement and the signal analyzer for maximum dynamic range instead of measurement speed.Supported devices:PXIe-5665/5668 |  |
| RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_SEGMENTED (2) | Similar to the dynamicRange method, this method also acquires a segmented spectrum, except that signal analyzer is not explicitly configured to provide maximum dynamic range. Use this method when the frequency separation of the two input tones is large and the measurement accuracy can be traded off for measurement speed.Supported devices:PXIe-5644/5645/5646/5840/5841/5842/5860/5830/5831/5832, PXIe-5663/5665/5668 |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_imcfgnumberofintermods.html language=enus -->
## TOPIC 00045: RFmxSpecAn_IMCfgNumberOfIntermods

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_imcfgnumberofintermods.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_imcfgnumberofintermods.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_IMCfgNumberOfIntermods

int32 __stdcall RFmxSpecAn_IMCfgNumberOfIntermods (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfIntermods);

#### Purpose

Configures the number of intermods to measure when you set the [RFMXSpecAn_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED](/csh?topicname=rfmxspecancvi/rfmxspecan_attr_im_auto_intermods_setup_enabled.html) attribute to RFMXSPECAN_VAL_IM_AUTO_INTERMODS_SETUP_ENABLED_FALSE.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| numberOfIntermods | int32 | Specifies the number of intermods to measure when you set the RFMXSpecAn_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to RFMXSPECAN_VAL_IM_AUTO_INTERMODS_SETUP_ENABLED_FALSE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_initialize.html language=enus -->
## TOPIC 00046: RFmxSpecAn_Initialize

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_initialize.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_Initialize

int32 __stdcall RFmxSpecAn_Initialize (char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession);

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
| optionString | char[] | Sets the initial value of certain attributes for the session. The following attributes are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about attributes used in this parameter, refer to the NI RF Vector Signal Analyzers Help. The format of this string is "AttributeName=Value", where AttributeName is the name of the attribute and Value is the value to which the attribute is set. For example, you can simulate an PXIe-5663E using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple attributes, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx uses yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. To use external NI Source Measure Units (SMU) as the noise source power supply for the noise figure (NF) measurement, use the "NoiseSourcePowerSupply" specifier within the RFmxSetup string. For example, "RFmxSetup= NoiseSourcePowerSupply:myDCPower[0]" configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You should allocate a dedicated SMU channel for RFmx. Note RFmx supports PXIe-4138, PXIe-4139, and PXIe-4139 (40 W) SMUs. |
|  | Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |  |
|  | Note RFmx supports PXIe-4138, PXIe-4139, and PXIe-4139 (40 W) SMUs. |  |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Identifies your instrument session. |
| isNewSession | int32* | Returns RFMXSPECAN_VAL_TRUE if the function created a new session, or RFMXSPECAN_VAL_FALSE if the function returned a reference to an existing session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_markercfgbandspan.html language=enus -->
## TOPIC 00047: RFmxSpecAn_MarkerCfgBandSpan

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_markercfgbandspan.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_markercfgbandspan.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_MarkerCfgBandSpan

int32 __stdcall RFmxSpecAn_MarkerCfgBandSpan (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 span);

#### Purpose

Configures the band span of the selected marker. 
Use "marker<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| span | float64 | Specifies the width of the span for the selected marker. This attribute selects the trace data within the specified span to perform specified marker function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_markercfgthreshold.html language=enus -->
## TOPIC 00048: RFmxSpecAn_MarkerCfgThreshold

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_markercfgthreshold.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_markercfgthreshold.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_MarkerCfgThreshold

int32 __stdcall RFmxSpecAn_MarkerCfgThreshold (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 thresholdEnabled, float64 threshold);

#### Purpose

Configures the threshold to use for peak search.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| thresholdEnabled | int32 | Specifies whether to enable the threshold for the trace while finding the peaks. RFMXSPECAN_VAL_MARKER_THRESHOLD_ENABLED_FALSE (0) Disables the threshold for the trace while finding the peaks. RFMXSPECAN_VAL_MARKER_THRESHOLD_ENABLED_TRUE (1) Enables the threshold for the trace while finding the peaks. |
| RFMXSPECAN_VAL_MARKER_THRESHOLD_ENABLED_FALSE (0) | Disables the threshold for the trace while finding the peaks. |  |
| RFMXSPECAN_VAL_MARKER_THRESHOLD_ENABLED_TRUE (1) | Enables the threshold for the trace while finding the peaks. |  |
| threshold | float64 | Specifies the threshold for finding the peaks on the trace. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_markercfgtrace.html language=enus -->
## TOPIC 00049: RFmxSpecAn_MarkerCfgTrace

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_markercfgtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_markercfgtrace.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_MarkerCfgTrace

int32 __stdcall RFmxSpecAn_MarkerCfgTrace (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 trace);

#### Purpose

Configures the measurement trace to be used by the marker. 
 


Use "marker<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" You can use the RFmxSpecAn_BuildMarkerString2 function to build the selector string. |
| trace | int32 | Specifies the trace. RFMXSPECAN_VAL_MARKER_TRACE_ACP_SPECTRUM (0) The marker uses the ACP spectrum trace. RFMXSPECAN_VAL_MARKER_TRACE_CCDF_GAUSSIAN_PROBABILITIES_TRACE (1) The marker uses the CCDF Gaussian probabilities trace. RFMXSPECAN_VAL_MARKER_TRACE_CCDF_PROBABILITIES_TRACE (2) The marker uses the CCDF probabilities trace. RFMXSPECAN_VAL_MARKER_TRACE_CHP_SPECTRUM (3) The marker uses the CHP spectrum trace. RFMXSPECAN_VAL_MARKER_TRACE_FCNT_POWER_TRACE (4) The marker uses the FCnt power trace. RFMXSPECAN_VAL_MARKER_TRACE_OBW_SPECTRUM (5) The marker uses the OBW spectrum trace. RFMXSPECAN_VAL_MARKER_TRACE_SEM_SPECTRUM (6) The marker uses the SEM spectrum trace. RFMXSPECAN_VAL_MARKER_TRACE_SPECTRUM (7) The marker uses the Spectrum trace. RFMXSPECAN_VAL_MARKER_TRACE_TXP_POWER_TRACE (8) The marker uses the TXP power trace. |
| RFMXSPECAN_VAL_MARKER_TRACE_ACP_SPECTRUM (0) | The marker uses the ACP spectrum trace. |  |
| RFMXSPECAN_VAL_MARKER_TRACE_CCDF_GAUSSIAN_PROBABILITIES_TRACE (1) | The marker uses the CCDF Gaussian probabilities trace. |  |
| RFMXSPECAN_VAL_MARKER_TRACE_CCDF_PROBABILITIES_TRACE (2) | The marker uses the CCDF probabilities trace. |  |
| RFMXSPECAN_VAL_MARKER_TRACE_CHP_SPECTRUM (3) | The marker uses the CHP spectrum trace. |  |
| RFMXSPECAN_VAL_MARKER_TRACE_FCNT_POWER_TRACE (4) | The marker uses the FCnt power trace. |  |
| RFMXSPECAN_VAL_MARKER_TRACE_OBW_SPECTRUM (5) | The marker uses the OBW spectrum trace. |  |
| RFMXSPECAN_VAL_MARKER_TRACE_SEM_SPECTRUM (6) | The marker uses the SEM spectrum trace. |  |
| RFMXSPECAN_VAL_MARKER_TRACE_SPECTRUM (7) | The marker uses the Spectrum trace. |  |
| RFMXSPECAN_VAL_MARKER_TRACE_TXP_POWER_TRACE (8) | The marker uses the TXP power trace. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_markercfgtype.html language=enus -->
## TOPIC 00050: RFmxSpecAn_MarkerCfgType

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_markercfgtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_markercfgtype.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_MarkerCfgType

int32 __stdcall RFmxSpecAn_MarkerCfgType (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 markerType);

#### Purpose

Configures the marker type. 
 


Use "marker<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" You can use the RFmxSpecAn_BuildMarkerString2 function to build the selector string. |
| markerType | int32 | Specifies whether the marker is disabled (Off) or is enabled (On) as a normal marker, delta marker or a fixed marker. RFMXSPECAN_VAL_MARKER_MARKER_TYPE_OFF (0) The marker is disabled. RFMXSPECAN_VAL_MARKER_MARKER_TYPE_NORMAL (1) The marker is enabled as a normal marker. RFMXSPECAN_VAL_MARKER_MARKER_TYPE_DELTA (3) The marker is enabled as a delta marker. RFMXSPECAN_VAL_MARKER_MARKER_TYPE_FIXED (4) The marker is enabled as a fixed marker. |
| RFMXSPECAN_VAL_MARKER_MARKER_TYPE_OFF (0) | The marker is disabled. |  |
| RFMXSPECAN_VAL_MARKER_MARKER_TYPE_NORMAL (1) | The marker is enabled as a normal marker. |  |
| RFMXSPECAN_VAL_MARKER_MARKER_TYPE_DELTA (3) | The marker is enabled as a delta marker. |  |
| RFMXSPECAN_VAL_MARKER_MARKER_TYPE_FIXED (4) | The marker is enabled as a fixed marker. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_markerfetchxy.html language=enus -->
## TOPIC 00051: RFmxSpecAn_MarkerFetchXY

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_markerfetchxy.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_markerfetchxy.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_MarkerFetchXY

int32 __stdcall RFmxSpecAn_MarkerFetchXY (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64* markerXLocation,
 float64* markerYLocation);

#### Purpose

Returns the X and Y locations of the marker.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name, result name, and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" "result::r1/marker0" "signal::sig1/result::r1/marker0" You can use the RFmxSpecAn_BuildMarkerString2 function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| markerXLocation | float64* | Returns the marker X location. |
| markerYLocation | float64* | Returns the marker Y location. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_markernextpeak.html language=enus -->
## TOPIC 00052: RFmxSpecAn_MarkerNextPeak

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_markernextpeak.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_markernextpeak.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_MarkerNextPeak

int32 __stdcall RFmxSpecAn_MarkerNextPeak (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 nextPeak, int32 *nextPeakFound);

#### Purpose

Moves the marker to the next highest or next left or next right peak above the threshold on the configured trace. 
 


Use "marker<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name, result name, and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" "result::r1/marker0" "signal::sig1/result::r1/marker0" You can use the RFmxSpecAn_BuildMarkerString2 function to build the selector string. |
| nextPeak | int32 | Specifies the next peak on the trace. RFMXSPECAN_VAL_MARKER_NEXT_PEAK_NEXT_HIGHEST (0) Moves the marker to the next highest peak above the threshold on the configured trace. RFMXSPECAN_VAL_MARKER_NEXT_PEAK_NEXT_LEFT (1) Moves the marker to the next peak to the left of the configured trace. RFMXSPECAN_VAL_MARKER_NEXT_PEAK_NEXT_RIGHT (2) Moves the marker to the next peak to the right of the configured trace. |
| RFMXSPECAN_VAL_MARKER_NEXT_PEAK_NEXT_HIGHEST (0) | Moves the marker to the next highest peak above the threshold on the configured trace. |  |
| RFMXSPECAN_VAL_MARKER_NEXT_PEAK_NEXT_LEFT (1) | Moves the marker to the next peak to the left of the configured trace. |  |
| RFMXSPECAN_VAL_MARKER_NEXT_PEAK_NEXT_RIGHT (2) | Moves the marker to the next peak to the right of the configured trace. |  |
| Output |  |  |
| Name | Type | Description |
| nextPeakFound | int32* | Indicates whether the function has found the next peak on the trace. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_markerpeaksearch.html language=enus -->
## TOPIC 00053: RFmxSpecAn_MarkerPeakSearch

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_markerpeaksearch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_markerpeaksearch.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_MarkerPeakSearch

int32 __stdcall RFmxSpecAn_MarkerPeakSearch (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *numberOfPeaks);

#### Purpose

Moves the marker to the highest peak above the threshold on the configured trace. 
 


Use "marker<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name, result name, and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" "result::r1/marker0" "signal::sig1/result::r1/marker0" You can use the RFmxSpecAn_BuildMarkerString2 function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| numberOfPeaks | int32* | Returns the total number of peaks above the threshold, when you enable the marker threshold. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_nfcfgaveraging.html language=enus -->
## TOPIC 00054: RFmxSpecAn_NFCfgAveraging

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_nfcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_nfcfgaveraging.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_NFCfgAveraging

int32 __stdcall RFmxSpecAn_NFCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount);

#### Purpose

Configures averaging for the noise figure (NF) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXSPECAN_VAL_NF_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXSPECAN_VAL_NF_AVERAGING_ENABLED_TRUE (1) The measurement uses the value of the averagingCount parameter to calculate the number of acquisitions over which the measurement is averaged. |
| RFMXSPECAN_VAL_NF_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXSPECAN_VAL_NF_AVERAGING_ENABLED_TRUE (1) | The measurement uses the value of the averagingCount parameter to calculate the number of acquisitions over which the measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXSPECAN_VAL_NF_AVERAGING_ENABLED_TRUE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_nffetchyfactorpowers.html language=enus -->
## TOPIC 00055: RFmxSpecAn_NFFetchYFactorPowers

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_nffetchyfactorpowers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_nffetchyfactorpowers.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_NFFetchYFactorPowers

int32 __stdcall RFmxSpecAn_NFFetchYFactorPowers (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 hotPower[],
 float64 coldPower[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Fetches the hot and cold powers measured when the Y-Factor based noise figure (NF) measurement is performed.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| hotPower | float64[] | Returns an array of powers measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute, when the noise source is enabled. This value is expressed in dBm. A valid result is returned only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to RFMXSPECAN_VAL_NF_MEASUREMENT_METHOD_Y_FACTOR. |
| coldPower | float64[] | Returns an array of powers measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute, when the noise source is disabled. This value is expressed in dBm. A valid result is returned only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to RFMXSPECAN_VAL_NF_MEASUREMENT_METHOD_Y_FACTOR. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_nffetchyfactors.html language=enus -->
## TOPIC 00056: RFmxSpecAn_NFFetchYFactors

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_nffetchyfactors.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_nffetchyfactors.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_NFFetchYFactors

int32 __stdcall RFmxSpecAn_NFFetchYFactors (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 measurementYFactor[],
 float64 calibrationYFactor[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Returns the measurement Y-factor and calibration Y-factor values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| measurementYFactor | float64[] | Returns the array of measurement Y-Factor values measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dB. This function returns a valid result only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to RFMXSPECAN_VAL_NF_MEASUREMENT_METHOD_Y_FACTOR. |
| calibrationYFactor | float64[] | Returns the array of calibration Y-Factor values measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dB. This function returns a valid result only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to RFMXSPECAN_VAL_NF_MEASUREMENT_METHOD_Y_FACTOR. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_nfrecommendreferencelevel.html language=enus -->
## TOPIC 00057: RFmxSpecAn_NFRecommendReferenceLevel

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_nfrecommendreferencelevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_nfrecommendreferencelevel.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_NFRecommendReferenceLevel

int32 __stdcall RFmxSpecAn_NFRecommendReferenceLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 DUTMaxGain,
 float64 DUTMaxNoiseFigure,
 float64* referenceLevel);

#### Purpose

Computes and sets an appropriate reference level based on the expected maximum DUT gain, maximum DUT noise figure, and other measurement and analyzer attributes. You must not set the [RFMXINSTR_ATTR_MIXER_LEVEL](/csh?topicname=rfmxinstrcvi/rfmxinstr_attr_mixer_level.html), [RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET](/csh?topicname=rfmxinstrcvi/rfmxinstr_attr_mixer_level_offset.html), [RFMXINSTR_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET](/csh?topicname=rfmxinstrcvi/rfmxinstr_attr_if_output_power_level_offset.html), and [RFMXINSTR_ATTR_IF_FILTER_BANDWIDTH](/csh?topicname=rfmxinstrcvi/rfmxinstr_attr_if_filter_bandwidth.html) attributes in order to obtain an appropriate recommended reference level.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| DUTMaxGain | float64 | Returns the expected maximum gain from the DUT. This value is expressed in dB. |
| DUTMaxNoiseFigure | float64 | Returns the expected maximum noise figure of the DUT. This value is expressed in dB. |
| Output |  |  |
| Name | Type | Description |
| referenceLevel | float64* | Returns the recommended reference level for the NF measurement. This value is expressed in dBm for RF devices and as Vpk-pk for baseband devices. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_nfvalidatecalibrationdata.html language=enus -->
## TOPIC 00058: RFmxSpecAn_NFValidateCalibrationData

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_nfvalidatecalibrationdata.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_nfvalidatecalibrationdata.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_NFValidateCalibrationData

int32 __stdcall RFmxSpecAn_NFValidateCalibrationData(
 niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32* calibrationDataValid
);

#### Purpose

Indicates whether calibration data is valid for configuration specified by the signal name in the **Selector string** attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| calibrationDataValid | int32* | Returns whether the calibration data is valid. |

| RFMXSPECAN_VAL_CALIBRATION_DATA_VALID_FALSE (0) | Returns false if the calibration data is not present for one or more frequency points in the list. |
| --- | --- |
| RFMXSPECAN_VAL_CALIBRATION_DATA_VALID_TRUE (1) | Returns true if the calibration data is present for all frequencies in the list. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_obwcfgaveraging.html language=enus -->
## TOPIC 00059: RFmxSpecAn_OBWCfgAveraging

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_obwcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_obwcfgaveraging.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_OBWCfgAveraging

int32 __stdcall RFmxSpecAn_OBWCfgAveraging (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType);

#### Purpose

Configures averaging for the occupied bandwidth (OBW) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition. RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_TRUE (1) The measurement uses the averagingCount parameter to calculate the number of acquisitions over which the measurement is averaged. |
| RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_TRUE (1) | The measurement uses the averagingCount parameter to calculate the number of acquisitions over which the measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_TRUE. |
| averagingType | int32 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_LOG (1) The power spectrum is averaged in a logarithm scale. RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_SCALAR (2) The square root of the power spectrum is averaged. RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MINIMUM (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithm scale. |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_obwcfgbandwidthpercentage.html language=enus -->
## TOPIC 00060: RFmxSpecAn_OBWCfgBandwidthPercentage

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_obwcfgbandwidthpercentage.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_obwcfgbandwidthpercentage.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_OBWCfgBandwidthPercentage

int32 __stdcall RFmxSpecAn_OBWCfgBandwidthPercentage (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 bandwidthPercentage);

#### Purpose

Configures the percentage of the total power that is contained in the occupied bandwidth (OBW).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| bandwidthPercentage | float64 | Specifies the percentage of the total power that is contained in the OBW. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_obwcfgfft.html language=enus -->
## TOPIC 00061: RFmxSpecAn_OBWCfgFFT

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_obwcfgfft.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_obwcfgfft.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_OBWCfgFFT

int32 __stdcall RFmxSpecAn_OBWCfgFFT (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 FFTWindow, float64 FFTPadding);

#### Purpose

Configures window and FFT to obtain a spectrum for the occupied bandwidth (OBW) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| FFTWindow | int32 | Specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectrum topic for more information about FFT window types. RFMXSPECAN_VAL_OBW_FFT_WINDOW_NONE (0) Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. RFMXSPECAN_VAL_OBW_FFT_WINDOW_FLAT_TOP (1) Measures single-tone amplitudes accurately. RFMXSPECAN_VAL_OBW_FFT_WINDOW_HANNING (2) Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. RFMXSPECAN_VAL_OBW_FFT_WINDOW_HAMMING (3) Analyzes closely-spaced sine waves. RFMXSPECAN_VAL_OBW_FFT_WINDOW_GAUSSIAN (4) Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. RFMXSPECAN_VAL_OBW_FFT_WINDOW_BLACKMAN (5) Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. RFMXSPECAN_VAL_OBW_FFT_WINDOW_BLACKMAN_HARRIS (6) Useful as a good general purpose window, having side lobe rejection >90dB and having a moderately wide main lobe. RFMXSPECAN_VAL_OBW_FFT_WINDOW_KAISER_BESSEL (7) Separates two tones with frequencies close to each other but with widely-differing amplitudes. |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_NONE (0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |  |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_FLAT_TOP (1) | Measures single-tone amplitudes accurately. |  |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_HANNING (2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |  |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_HAMMING (3) | Analyzes closely-spaced sine waves. |  |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_GAUSSIAN (4) | Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. |  |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_BLACKMAN (5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |  |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_BLACKMAN_HARRIS (6) | Useful as a good general purpose window, having side lobe rejection >90dB and having a moderately wide main lobe. |  |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_KAISER_BESSEL (7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |  |
| FFTPadding | float64 | Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: waveform size * padding. This parameter is used only when the acquisition span is less than the device instantaneous bandwidth of the device. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_obwcfgpowerunits.html language=enus -->
## TOPIC 00062: RFmxSpecAn_OBWCfgPowerUnits

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_obwcfgpowerunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_obwcfgpowerunits.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_OBWCfgPowerUnits

int32 __stdcall RFmxSpecAn_OBWCfgPowerUnits (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnits);

#### Purpose

Configures the units for the absolute power.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| powerUnits | int32 | Specifies the units for the absolute power. RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM (0) The absolute powers are reported in dBm. RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM_PER_HZ (1) The absolute powers are reported in dBm/Hz. |
| RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM (0) | The absolute powers are reported in dBm. |  |
| RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM_PER_HZ (1) | The absolute powers are reported in dBm/Hz. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_obwcfgrbwfilter.html language=enus -->
## TOPIC 00063: RFmxSpecAn_OBWCfgRBWFilter

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_obwcfgrbwfilter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_obwcfgrbwfilter.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_OBWCfgRBWFilter

int32 __stdcall RFmxSpecAn_OBWCfgRBWFilter (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 RBWAuto, float64 RBW, int32 RBWFilterType);

#### Purpose

Configures the resolution bandwidth (RBW) filter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| RBWAuto | int32 | Specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the Spectrum topic for more information about RBW and sweep time. RFMXSPECAN_VAL_OBW_RBW_AUTO_FALSE (0) The measurement uses the RBW that you specify in the RBW parameter. RFMXSPECAN_VAL_OBW_RBW_AUTO_TRUE (1) The measurement computes the RBW. |
| RFMXSPECAN_VAL_OBW_RBW_AUTO_FALSE (0) | The measurement uses the RBW that you specify in the RBW parameter. |  |
| RFMXSPECAN_VAL_OBW_RBW_AUTO_TRUE (1) | The measurement computes the RBW. |  |
| RBW | float64 | Specifies the bandwidth, in Hz, of the RBW filter used to sweep the acquired carrier signal, when you set the RBWAuto parameter to RFMXSPECAN_VAL_OBW_RBW_AUTO_FALSE. |
| RBWFilterType | int32 | Specifies the shape of the digital RBW filter. RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED (0) No RBW filtering is performed. RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN (1) An RBW filter with a Gaussian response is applied. RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_FLAT (2) An RBW filter with a flat response is applied. RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_SYNCH_TUNED_4 (3) An RBW filter with a 4-pole synchronously-tuned response is applied. RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_SYNCH_TUNED_5 (4) An RBW filter with a 5-pole synchronously-tuned response is applied. |
| RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |  |
| RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |  |
| RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_SYNCH_TUNED_4 (3) | An RBW filter with a 4-pole synchronously-tuned response is applied. |  |
| RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_SYNCH_TUNED_5 (4) | An RBW filter with a 5-pole synchronously-tuned response is applied. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_obwcfgspan.html language=enus -->
## TOPIC 00064: RFmxSpecAn_OBWCfgSpan

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_obwcfgspan.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_obwcfgspan.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_OBWCfgSpan

int32 __stdcall RFmxSpecAn_OBWCfgSpan (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 span);

#### Purpose

Configures the frequency range, in Hz, around the center frequency, to acquire for the measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| span | float64 | Specifies the frequency range, in Hz, around the center frequency, to acquire for the measurement. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_obwcfgsweeptime.html language=enus -->
## TOPIC 00065: RFmxSpecAn_OBWCfgSweepTime

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_obwcfgsweeptime.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_obwcfgsweeptime.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_OBWCfgSweepTime

int32 __stdcall RFmxSpecAn_OBWCfgSweepTime (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval);

#### Purpose

Configures the sweep time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| sweepTimeAuto | int32 | Specifies whether the measurement computes the sweep time. RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) The measurement uses the sweep time that you specify in the sweepTimeInterval parameter. RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the sweepTimeInterval parameter. |  |
| RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) | The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |  |
| sweepTimeInterval | float64 | Specifies the sweep time, in seconds, when you set the sweepTimeAuto parameter to RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_FALSE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_pavtcfgmeasurementlocationtype.html language=enus -->
## TOPIC 00066: RFmxSpecAn_PAVTCfgMeasurementLocationType

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_pavtcfgmeasurementlocationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_pavtcfgmeasurementlocationtype.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_PAVTCfgMeasurementLocationType

int32 __stdcall RFmxSpecAn_PAVTCfgMeasurementLocationType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 measurementLocationType);

#### Purpose

Configures the measurement location type for the segments.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementLocationType | int32 | Specifies whether the location at which the segment is measured is indicated by time or trigger. RFMXSPECAN_VAL_PAVT_MEASUREMENT_LOCATION_TYPE_TIME (0) The measurement is performed over a single record across multiple segments separated in time. The measurement locations of the segments are specified by the RFMXSPECAN_ATTR_PAVT_SEGMENT_START_TIME attribute. The number of segments is equal to the number of segment start times.RFMXSPECAN_VAL_PAVT_MEASUREMENT_LOCATION_TYPE_TRIGGER (1) The measurement is performed across segments obtained in multiple records, where each record is obtained when a trigger is received. The number of segments is equal to the number of triggers (records). |
| RFMXSPECAN_VAL_PAVT_MEASUREMENT_LOCATION_TYPE_TIME (0) | The measurement is performed over a single record across multiple segments separated in time. The measurement locations of the segments are specified by the RFMXSPECAN_ATTR_PAVT_SEGMENT_START_TIME attribute. The number of segments is equal to the number of segment start times. |  |
| RFMXSPECAN_VAL_PAVT_MEASUREMENT_LOCATION_TYPE_TRIGGER (1) | The measurement is performed across segments obtained in multiple records, where each record is obtained when a trigger is received. The number of segments is equal to the number of triggers (records). |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_pavtcfgnumberofsegments.html language=enus -->
## TOPIC 00067: RFmxSpecAn_PAVTCfgNumberOfSegments

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_pavtcfgnumberofsegments.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_pavtcfgnumberofsegments.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_PAVTCfgNumberOfSegments

int32 __stdcall RFmxSpecAn_PAVTCfgNumberOfSegments (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfSegments);

#### Purpose

Configures the number of segments.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| numberOfSegments | int32 | Specifies the number of segments to be measured. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_pavtcfgsegmenttype.html language=enus -->
## TOPIC 00068: RFmxSpecAn_PAVTCfgSegmentType

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_pavtcfgsegmenttype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_pavtcfgsegmenttype.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_PAVTCfgSegmentType

int32 __stdcall RFmxSpecAn_PAVTCfgSegmentType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 segmentType);

#### Purpose

Configures the segment type.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| segmentType | int32 | Specifies the type of segment. RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_PHASE_AND_AMPLITUDE (0) Phase and amplitude is measured in this segment.RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_AMPLITUDE (1) Amplitude is measured in this segment.RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_FREQUENCY_ERROR_MEASUREMENT (2) Frequency error is measured in this segment. |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_PHASE_AND_AMPLITUDE (0) | Phase and amplitude is measured in this segment. |  |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_AMPLITUDE (1) | Amplitude is measured in this segment. |  |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_FREQUENCY_ERROR_MEASUREMENT (2) | Frequency error is measured in this segment. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_pavtcfgsegmenttypearray.html language=enus -->
## TOPIC 00069: RFmxSpecAn_PAVTCfgSegmentTypeArray

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_pavtcfgsegmenttypearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_pavtcfgsegmenttypearray.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_PAVTCfgSegmentTypeArray

int32 __stdcall RFmxSpecAn_PAVTCfgSegmentTypeArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 segmentType[],
 int32 numberOfElements);

#### Purpose

Configures an array of segment types.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| segmentType | int32[] | Specifies the type of segment. RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_PHASE_AND_AMPLITUDE (0) Phase and amplitude is measured in this segment.RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_AMPLITUDE (1) Amplitude is measured in this segment.RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_FREQUENCY_ERROR_MEASUREMENT (2) Frequency error is measured in this segment. |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_PHASE_AND_AMPLITUDE (0) | Phase and amplitude is measured in this segment. |  |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_AMPLITUDE (1) | Amplitude is measured in this segment. |  |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_FREQUENCY_ERROR_MEASUREMENT (2) | Frequency error is measured in this segment. |  |
| numberOfElements | int32 | Specifies the number of elements in each array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_pavtfetchamplitudetrace.html language=enus -->
## TOPIC 00070: RFmxSpecAn_PAVTFetchAmplitudeTrace

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_pavtfetchamplitudetrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_pavtfetchamplitudetrace.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_PAVTFetchAmplitudeTrace

int32 __stdcall RFmxSpecAn_PAVTFetchAmplitudeTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 traceIndex,
 float64* x0,
 float64* dx,
 float32 amplitude[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the amplitude trace for the measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| traceIndex | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency, in Hz. |
| dx | float64* | Returns the frequency bin spacing, in Hz. |
| amplitude | float32[] | Returns the amplitude values of the complex baseband samples, in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_pavtfetchphaseandamplitude.html language=enus -->
## TOPIC 00071: RFmxSpecAn_PAVTFetchPhaseAndAmplitude

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_pavtfetchphaseandamplitude.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_pavtfetchphaseandamplitude.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_PAVTFetchPhaseAndAmplitude

int32 __stdcall RFmxSpecAn_PAVTFetchPhaseAndAmplitude (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* meanRelativePhase,
 float64* meanRelativeAmplitude,
 float64* meanAbsolutePhase,
 float64* meanAbsoluteAmplitude);

#### Purpose

Fetches the mean values of phase and amplitude of the segment. 
Use "segment<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0". Example:"segment0""signal::sig1/segment0""result::r1/segment0""signal::sig1/result::r1/segment0"You can use the RFmxSpecAn_BuildSegmentString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanRelativePhase | float64* | Returns the mean phase of the segment relative to the first segment of the measurement. This value is expressed in degrees. |
| meanRelativeAmplitude | float64* | Returns the mean amplitude of the segment relative to the first segment of the measurement. This value is expressed in dB. |
| meanAbsolutePhase | float64* | Returns the mean absolute phase of the segment. This value is expressed in degrees. |
| meanAbsoluteAmplitude | float64* | Returns the mean absolute amplitude of the segment. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_phasenoisecfgsmoothing.html language=enus -->
## TOPIC 00072: RFmxSpecAn_PhaseNoiseCfgSmoothing

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_phasenoisecfgsmoothing.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_phasenoisecfgsmoothing.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_PhaseNoiseCfgSmoothing

int32 __stdcall RFmxSpecAn_PhaseNoiseCfgSmoothing (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 smoothingType,
 float64 smoothingPercentage);

#### Purpose

Configures the smoothing type and smoothing percentage used to smoothen the measured log plot trace.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| smoothingType | int32 | Specifies the smoothing type used to smoothen a log plot trace. RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_NONE (0) Smoothing is disabled. RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_LINEAR (1) Performs linear moving average filtering on the measured phase noise log plot trace. RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_LOGARITHMIC (2) Performs logarithmic moving average filtering on the measured phase noise log plot trace. RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_MEDIAN (3) Performs moving median filtering on the measured phase noise log plot trace. |
| RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_NONE (0) | Smoothing is disabled. |  |
| RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_LINEAR (1) | Performs linear moving average filtering on the measured phase noise log plot trace. |  |
| RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_LOGARITHMIC (2) | Performs logarithmic moving average filtering on the measured phase noise log plot trace. |  |
| RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_MEDIAN (3) | Performs moving median filtering on the measured phase noise log plot trace. |  |
| smoothingPercentage | float64 | Specifies the number of points to use in the moving average filter as a percentage of total number of points in the log plot trace. This value is expressed as a percentage. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgaveraging.html language=enus -->
## TOPIC 00073: RFmxSpecAn_SEMCfgAveraging

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgaveraging.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgAveraging

int32 __stdcall RFmxSpecAn_SEMCfgAveraging (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType);

#### Purpose

Configures averaging for the spectral emission mask (SEM) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition. RFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_TRUE (1) The measurement uses the averagingCount parameter to calculate the number of acquisitions over which the measurement is averaged. |
| RFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_TRUE (1) | The measurement uses the averagingCount parameter to calculate the number of acquisitions over which the measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_TRUE. |
| averagingType | int32 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_LOG (1) The power spectrum is averaged in a logarithm scale. RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_SCALAR (2) The square root of the power spectrum is averaged. RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_MINIMUM (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithm scale. |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgcarrierchannelbandwidth.html language=enus -->
## TOPIC 00074: RFmxSpecAn_SEMCfgCarrierChannelBandwidth

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgcarrierchannelbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgcarrierchannelbandwidth.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgCarrierChannelBandwidth

int32 __stdcall RFmxSpecAn_SEMCfgCarrierFrequency (niRFmxInstrHandle instrumentHandle, char selectorString[],float64 carrierChannelBandwidth);

#### Purpose

Configures the channel bandwidth of the carrier. 
 


Use "carrier<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxSpecAn_BuildCarrierString2 function to build the selector string. |
| carrierChannelBandwidth | float64 | Specifies the channel bandwidth of the carrier. It is used to calculate the values of the RFMXSPECAN_ATTR_SEM_OFFSET_START_FREQUENCY and RFMXSPECAN_ATTR_SEM_OFFSET_STOP_FREQUENCY attributes when you set the RFMXSPECAN_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION attribute to RFMXSPECAN_VAL_SEM_CARRIER_EDGE_TO_MEASUREMENT_BANDWIDTH_CENTER or RFMXSPECAN_VAL_SEM_CARRIER_EDGE_TO_MEASUREMENT_BANDWIDTH_EDGE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgcarrierenabled.html language=enus -->
## TOPIC 00075: RFmxSpecAn_SEMCfgCarrierEnabled

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgcarrierenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgcarrierenabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgCarrierEnabled

int32 __stdcall RFmxSpecAn_SEMCfgCarrierEnabled (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 carrierEnabled);

#### Purpose

Configures whether to consider the carrier power as part of total carrier power measurement. 
 


Use "carrier<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxSpecAn_BuildCarrierString2 function to build the selector string. |
| carrierEnabled | int32 | Specifies whether to consider the carrier power as part of total carrier power measurement. RFMXSPECAN_VAL_SEM_ENABLED_FALSE (0) The carrier power is not considered as part of the total carrier power. RFMXSPECAN_VAL_SEM_ENABLED_TRUE (1) The carrier power is considered as part of the total carrier power. |
| RFMXSPECAN_VAL_SEM_ENABLED_FALSE (0) | The carrier power is not considered as part of the total carrier power. |  |
| RFMXSPECAN_VAL_SEM_ENABLED_TRUE (1) | The carrier power is considered as part of the total carrier power. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgcarrierfrequency.html language=enus -->
## TOPIC 00076: RFmxSpecAn_SEMCfgCarrierFrequency

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgcarrierfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgcarrierfrequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgCarrierFrequency

int32 __stdcall RFmxSpecAn_SEMCfgCarrierFrequency (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 carrierFrequency);

#### Purpose

Configures the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. 
 


Use "carrier<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxSpecAn_BuildCarrierString2 function to build the selector string. |
| carrierFrequency | float64 | Specifies the center frequency, in hertz (Hz), of the carrier, relative to the RF center frequency. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgoffsetbandwidthintegral.html language=enus -->
## TOPIC 00077: RFmxSpecAn_SEMCfgOffsetBandwidthIntegral

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgoffsetbandwidthintegral.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgoffsetbandwidthintegral.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgOffsetBandwidthIntegral

int32 __stdcall RFmxSpecAn_SEMCfgOffsetBandwidthIntegral (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral);

#### Purpose

Configures the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). 
 


Use "offset<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and offset number. If you do not specify the signal name, the default signal instance is used. Example: "offset0" "signal::sig1/offset0" You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| bandwidthIntegral | int32 | Specifies the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW. If you set this parameter to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of the bandwidth integral and the RBW. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgoffsetfrequencyarray.html language=enus -->
## TOPIC 00078: RFmxSpecAn_SEMCfgOffsetFrequencyArray

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgoffsetfrequencyarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgoffsetfrequencyarray.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgOffsetFrequencyArray

int32 __stdcall RFmxSpecAn_SEMCfgOffsetFrequencyArray (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency[], float64 offsetStopFrequency[], int32 offsetEnabled[], int32 offsetSideband[], int32 numberOfElements);

#### Purpose

Configures the offset frequency start and stop values and specifies whether the offset segment is present on one side, or on both sides of the carriers.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| offsetStartFrequency | float64[] | Specifies the array of start frequencies, in hertz (Hz), of each offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the RFMXSPECAN_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION attribute. Specify NULL if you do not want to set a value for this array. |
| offsetStopFrequency | float64[] | Specifies the array of stop frequencies, in hertz (Hz), of each offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the RFMXSPECAN_RANGE_TABLE_SEM_OFFSET_FREQUENCY_DEFINITION attribute. Specify NULL if you do not want to set a value for this array. |
| offsetEnabled | int32[] | Specifies whether to enable the offset segment for the SEM measurement. Specify NULL if you do not want to set a value for this array. RFMXSPECAN_VAL_SEM_OFFSET_ENABLED_FALSE (0) Disables the offset segment for the SEM measurement. RFMXSPECAN_VAL_SEM_OFFSET_ENABLED_TRUE (1) Enables the offset segment for the SEM measurement. |
| RFMXSPECAN_VAL_SEM_OFFSET_ENABLED_FALSE (0) | Disables the offset segment for the SEM measurement. |  |
| RFMXSPECAN_VAL_SEM_OFFSET_ENABLED_TRUE (1) | Enables the offset segment for the SEM measurement. |  |
| offsetSideband | int32[] | Specifies whether the offset segment is present on one side, or on both sides of the carriers. Specify NULL if you do not want to set a value for this array. RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE (0) Configures a lower offset segment to the left of the leftmost carrier. RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_POSITIVE (1) Configures an upper offset segment to the right of the rightmost carrier. RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_BOTH (2) Configures both negative and positive offset segments. |
| RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE (0) | Configures a lower offset segment to the left of the leftmost carrier. |  |
| RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_POSITIVE (1) | Configures an upper offset segment to the right of the rightmost carrier. |  |
| RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_BOTH (2) | Configures both negative and positive offset segments. |  |
| numberOfElements | int32 | Specifies the number of elements in each array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgoffsetrbwfilter.html language=enus -->
## TOPIC 00079: RFmxSpecAn_SEMCfgOffsetRBWFilter

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgoffsetrbwfilter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgoffsetrbwfilter.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgOffsetRBWFilter

int32 __stdcall RFmxSpecAn_SEMCfgOffsetRBWFilter (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 RBWAuto, float64 RBW, int32 RBWFilterType);

#### Purpose

Configures the resolution bandwidth (RBW) filter of the offset segment. 
 


Use "offset<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and offset number. If you do not specify the signal name, the default signal instance is used. Example: "offset0" "signal::sig1/offset0" You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| RBWAuto | int32 | Specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the SEM topic for more information about RBW and sweep time. RFMXSPECAN_VAL_SEM_RBW_AUTO_FALSE (0) The measurement uses the RBW that you specify in the RBW parameter. RFMXSPECAN_VAL_SEM_RBW_AUTO_TRUE (1) The measurement computes the RBW. |
| RFMXSPECAN_VAL_SEM_RBW_AUTO_FALSE (0) | The measurement uses the RBW that you specify in the RBW parameter. |  |
| RFMXSPECAN_VAL_SEM_RBW_AUTO_TRUE (1) | The measurement computes the RBW. |  |
| RBW | float64 | Specifies the bandwidth, in hertz (Hz), of the RBW filter used to sweep the acquired offset segment, when you set the RBWAuto parameter to RFMXSPECAN_VAL_SEM_RBW_AUTO_FALSE. |
| RBWFilterType | int32 | Specifies the shape of the digital RBW filter. RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_FFT_BASED (0) No RBW filtering is performed. RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_GAUSSIAN (1) An RBW filter with a Gaussian response is applied. RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_FLAT (2) An RBW filter with a flat response is applied. RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_SYNCH_TUNED_4 (3) An RBW filter with a 4-pole synchronously-tuned response is applied. RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_SYNCH_TUNED_5 (4) An RBW filter with a 5-pole synchronously-tuned response is applied. |
| RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |  |
| RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |  |
| RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_SYNCH_TUNED_4 (3) | An RBW filter with a 4-pole synchronously-tuned response is applied. |  |
| RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_SYNCH_TUNED_5 (4) | An RBW filter with a 5-pole synchronously-tuned response is applied. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgoffsetrelativeattenuation.html language=enus -->
## TOPIC 00080: RFmxSpecAn_SEMCfgOffsetRelativeAttenuation

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgoffsetrelativeattenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgoffsetrelativeattenuation.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgOffsetRelativeAttenuation

int32 __stdcall RFmxSpecAn_SEMCfgOffsetRelativeAttenuation (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeAttenuation);

#### Purpose

Configures the attenuation, in dB, relative to the external attenuation. 
 


Use "offset<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and offset number. If you do not specify the signal name, the default signal instance is used. Example: "offset0" "signal::sig1/offset0" You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| relativeAttenuation | float64 | Specifies the attenuation, in dB, relative to the external attenuation. Use this parameter to compensate for variations in external attenuation when the offset channels are spread wide in frequency. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgoffsetrelativeattenuationarray.html language=enus -->
## TOPIC 00081: RFmxSpecAn_SEMCfgOffsetRelativeAttenuationArray

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgoffsetrelativeattenuationarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgoffsetrelativeattenuationarray.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgOffsetRelativeAttenuationArray

int32 __stdcall RFmxSpecAn_SEMCfgOffsetRelativeAttenuationArray (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeAttenuation[], int32 numberOfElements);

#### Purpose

Configures the attenuation, in dB, relative to the external attenuation.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| relativeAttenuation | float64[] | Specifies an array of attenuation values, in dB, relative to the external attenuation. Use this parameter to compensate for the variations in external attenuation when offset channels are spread wide in frequency. Specify NULL if you do not want to set a value for this array. |
| numberOfElements | int32 | Specifies the number of elements in each array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgoffsetrelativelimit.html language=enus -->
## TOPIC 00082: RFmxSpecAn_SEMCfgOffsetRelativeLimit

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgoffsetrelativelimit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgoffsetrelativelimit.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgOffsetRelativeLimit

int32 __stdcall RFmxSpecAn_SEMCfgOffsetRelativeLimit (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 relativeLimitMode, float64 relativeLimitStart, float64 relativeLimitStop);

#### Purpose

Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment. 
 


Use "offset<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and offset number. If you do not specify the signal name, the default signal instance is used. Example: "offset0" "signal::sig1/offset0" You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| relativeLimitMode | int32 | Specifies whether the relative limit mask is a flat line or a line with a slope. RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_MANUAL (0) The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP attribute values as the two ends is considered as the mask. RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_COUPLE (1) The two ends of the line are coupled to the value of the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START attribute. |
| RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_MANUAL (0) | The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP attribute values as the two ends is considered as the mask. |  |
| RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_COUPLE (1) | The two ends of the line are coupled to the value of the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START attribute. |  |
| relativeLimitStart | float64 | Specifies the relative power limit, in dB, corresponding to the beginning of the offset segment. The value of this parameter is also set as the stop limit for the offset segment when you set the relativeLimitMode parameter to RFMXSPECAN_VAL_SEM_RELATIVE_LIMIT_MODE_COUPLE. |
| relativeLimitStop | float64 | Specifies the relative power limit, in dB, corresponding to the end of the offset segment. This parameter is ignored if you set the relativeLimitMode parameter to RFMXSPECAN_VAL_SEM_RELATIVE_LIMIT_MODE_COUPLE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semcfgoffsetrelativelimitarray.html language=enus -->
## TOPIC 00083: RFmxSpecAn_SEMCfgOffsetRelativeLimitArray

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semcfgoffsetrelativelimitarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semcfgoffsetrelativelimitarray.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMCfgOffsetRelativeLimitArray

int32 __stdcall RFmxSpecAn_SEMCfgOffsetRelativeLimitArray (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 relativeLimitMode[], float64 relativeLimitStart[], float64 relativeLimitStop[], int32 numberOfElements);

#### Purpose

Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| relativeLimitMode | int32[] | Specifies whether the relative limit mask is a flat line or a line with a slope. Specify NULL if you do not want to set a value for this array. RFMXSPECAN_VAL_SEM_RELATIVE_LIMIT_MODE_MANUAL (0) The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP attribute values as the two ends is considered as the mask. RFMXSPECAN_VAL_SEM_RELATIVE_LIMIT_MODE_COUPLE (1) The two ends of the line are coupled to the value of the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START attribute. |
| RFMXSPECAN_VAL_SEM_RELATIVE_LIMIT_MODE_MANUAL (0) | The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP attribute values as the two ends is considered as the mask. |  |
| RFMXSPECAN_VAL_SEM_RELATIVE_LIMIT_MODE_COUPLE (1) | The two ends of the line are coupled to the value of the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START attribute. |  |
| relativeLimitStart | float64[] | Specifies the array of relative power limits, in dB, corresponding to the beginning of the offset segment. The value of this parameter is also set as the stop limit for the offset segment when you set the relativeLimitMode parameter to RFMXSPECAN_VAL_SEM_RELATIVE_LIMIT_MODE_COUPLE. Specify NULL if you do not want to set a value for this array. |
| relativeLimitStop | float64[] | Specifies the array of relative power limits, in dB, corresponding to the end of the offset segment. This parameter is ignored if you set the relativeLimitMode parameter to RFMXSPECAN_VAL_SEM_RELATIVE_LIMIT_MODE_COUPLE. Specify NULL if you do not want to set a value for this array. |
| numberOfElements | int32 | Specifies the number of elements in each array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semfetchabsolutemasktrace.html language=enus -->
## TOPIC 00084: RFmxSpecAn_SEMFetchAbsoluteMaskTrace

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semfetchabsolutemasktrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semfetchabsolutemasktrace.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMFetchAbsoluteMaskTrace

int32 __stdcall RFmxSpecAn_SEMFetchAbsoluteMaskTrace (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 absoluteMask[], int32 arraySize, int32* actualArraySize);

#### Purpose

Fetches the absolute mask trace used for SEM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the y array. Set the arraySize parameter to 0 to get the size of the y array in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency, in hertz (Hz), of the channel. |
| dx | float64* | Returns the frequency bin spacing, in Hz. |
| absoluteMask | float32[] | Returns absolute mask used for the channel. Set the arraySize parameter to 0 to get the size of the y array. You can pass NULL for this parameter if you set the arraySize parameter to 0. If the y array is not large enough to hold all the samples, the function returns an error. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semfetchcarriermeasurement.html language=enus -->
## TOPIC 00085: RFmxSpecAn_SEMFetchCarrierMeasurement

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semfetchcarriermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semfetchcarriermeasurement.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMFetchCarrierMeasurement

int32 __stdcall RFmxSpecAn_SEMFetchCarrierMeasurement (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absolutePower, float64* peakAbsolutePower, float64* peakFrequency, float64* totalRelativePower);

#### Purpose

Returns the carrier power measurement. 
 


Use "carrier<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxSpecAn_BuildCarrierString2 function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| absolutePower | float64* | Returns the carrier power. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ. |
| peakAbsolutePower | float64* | Returns the peak power in the carrier channel. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ. |
| peakFrequency | float64* | Returns the frequency, in hertz (Hz), at which the peak power occurs in the carrier channel. |
| totalRelativePower | float64* | Returns the carrier power, in dB, relative to the total carrier power of all enabled carriers. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semfetchcompositemeasurementstatus.html language=enus -->
## TOPIC 00086: RFmxSpecAn_SEMFetchCompositeMeasurementStatus

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semfetchcompositemeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semfetchcompositemeasurementstatus.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMFetchCompositeMeasurementStatus

int32 __stdcall RFmxSpecAn_SEMFetchCompositeMeasurementStatus (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* compositeMeasurementStatus);

#### Purpose

Indicates the overall SEM measurement status based on the measurement limits and the fail criteria that you set in the [RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK](/csh?topicname=rfmxspecancvi/rfmxspecan_attr_sem_offset_limit_fail_mask.html) attribute for each offset segment.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| compositeMeasurementStatus | int32* | Indicates the overall measurement status based on the measurement limits and the fail criteria that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute for each offset segment. RFMXSPECAN_VAL_SEM_COMPOSITE_MEASUREMENT_STATUS_FAIL (0) Indicates that the measurement has failed. RFMXSPECAN_VAL_SEM_COMPOSITE_MEASUREMENT_STATUS_PASS (1) Indicates that the measurement has passed. |
| RFMXSPECAN_VAL_SEM_COMPOSITE_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |  |
| RFMXSPECAN_VAL_SEM_COMPOSITE_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semfetchfrequencyresolution.html language=enus -->
## TOPIC 00087: RFmxSpecAn_SEMFetchFrequencyResolution

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semfetchfrequencyresolution.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semfetchfrequencyresolution.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMFetchFrequencyResolution

int32 __stdcall RFmxSpecAn_SEMFetchFrequencyResolution (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* frequencyResolution);

#### Purpose

Returns the frequency bin spacing, in hertz (Hz), of the spectrum acquired by the measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| frequencyResolution | float64* | Returns the frequency bin spacing, in Hz, of the spectrum acquired by the measurement. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semfetchloweroffsetmargin.html language=enus -->
## TOPIC 00088: RFmxSpecAn_SEMFetchLowerOffsetMargin

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semfetchloweroffsetmargin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semfetchloweroffsetmargin.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMFetchLowerOffsetMargin

int32 __stdcall RFmxSpecAn_SEMFetchLowerOffsetMargin (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* measurementStatus,
 float64* margin,
 float64* marginFrequency,
 float64* marginAbsolutePower,
 float64* marginRelativePower);

#### Purpose

Returns the measurement status and margin from the limit line measured in the lower offset segment. 
 


Use "offset<*n*>" as the selector string to read parameters from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| measurementStatus | int32* | Indicates the lower offset measurement status based on measurement limits and the fail criteria that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. RFMXSPECAN_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) Indicates that the measurement has failed. RFMXSPECAN_VAL_SEM_MEASUREMENT_STATUS_PASS (1) Indicates that the measurement has passed. |
| RFMXSPECAN_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |  |
| RFMXSPECAN_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |  |
| margin | float64* | Returns the margin, in dB, from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. Margin is defined as the maximum difference between the spectrum and the limit mask. When you set the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute to RFMXSPECAN_VAL_SEM_LIMIT_FAIL_MASK_ABSOLUTE, the margin is with reference to the absolute limit mask. When you set the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute to RFMXSPECAN_VAL_SEM_LIMIT_FAIL_MASK_RELATIVE, the margin is with reference to the relative limit mask. When you set the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute to RFMXSPECAN_VAL_SEM_LIMIT_FAIL_MASK_ABSANDREL, the margin is the maximum of the margins referenced to the absolute and relative limit masks. When you set the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute to RFMXSPECAN_VAL_SEM_LIMIT_FAIL_MASK_ABSORREL, the margin is the minimum of the margins referenced to the absolute and relative limit masks. |
| marginFrequency | float64* | Returns the frequency, in hertz (Hz), at which the margin occurred in the lower (negative) offset. |
| marginAbsolutePower | float64* | Returns the power, in dBm or dBm/Hz, at which the margin occurred in the lower (negative) offset segment. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ. |
| marginRelativePower | float64* | Returns the power, in dB, at which the margin occurred in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semfetchloweroffsetmarginarray.html language=enus -->
## TOPIC 00089: RFmxSpecAn_SEMFetchLowerOffsetMarginArray

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semfetchloweroffsetmarginarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semfetchloweroffsetmarginarray.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMFetchLowerOffsetMarginArray

int32 __stdcall RFmxSpecAn_SEMFetchLowerOffsetMarginArray (niRFmxInstrHandle instrumentHandle, 
 char selectorString[],
 float64 timeout,
 int32 measurementStatus[],
 float64 margin[],
 float64 marginFrequency[],
 float64 marginAbsolutePower[],
 float64 marginRelativePower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| measurementStatus | int32[] | Returns the array of lower offset measurement statuses based on measurement limits and the fail criteria that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. You can pass NULL for this parameter if you set the arraySize parameter to 0. RFMXSPECAN_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) Indicates that the measurement has failed. RFMXSPECAN_VAL_SEM_MEASUREMENT_STATUS_PASS (1) Indicates that the measurement has passed. |
| RFMXSPECAN_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |  |
| RFMXSPECAN_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |  |
| margin | float64[] | Returns the margin, in dB, from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. Margin is defined as the maximum difference between the spectrum and the limit mask. You can pass NULL for this parameter if you set the arraySize parameter to 0. When you set the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute to RFMXSPECAN_VAL_SEM_LIMIT_FAIL_MASK_ABSOLUTE, the margin is with reference to the absolute limit mask. When you set the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute to RFMXSPECAN_VAL_SEM_LIMIT_FAIL_MASK_RELATIVE, the margin is with reference to the relative limit mask. When you set the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute to RFMXSPECAN_VAL_SEM_LIMIT_FAIL_MASK_ABSANDREL, the margin is the maximum of the margins referenced to the absolute and relative limit masks. When you set the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute to RFMXSPECAN_VAL_SEM_LIMIT_FAIL_MASK_ABSORREL, the margin is the minimum of the margins referenced to the absolute and relative limit masks. |
| marginFrequency | float64[] | Returns the array of frequencies, in hertz (Hz), at which the margin occurred in each lower (negative) offset segment. You can pass NULL for this parameter if you set the arraySize parameter to 0. |
| marginAbsolutePower | float64[] | Returns the array of powers, in dBm or dBm/Hz, at which the margin occurred in the lower (negative) offset segment. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ. You can pass NULL for this parameter if you set the arraySize parameter to 0. |
| marginRelativePower | float64[] | Returns the array of powers, in dB, at which the margin occurred in each lower (negative) offset segment relative to the integrated or peak power of the reference carrier. You can pass NULL for this parameter if you set the arraySize parameter to 0. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semfetchloweroffsetpower.html language=enus -->
## TOPIC 00090: RFmxSpecAn_SEMFetchLowerOffsetPower

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semfetchloweroffsetpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semfetchloweroffsetpower.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMFetchLowerOffsetPower

int32 __stdcall RFmxSpecAn_SEMFetchLowerOffsetPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* totalAbsolutePower,
 float64* totalRelativePower,
 float64* peakAbsolutePower,
 float64* peakFrequency,
 float64* peakRelativePower);

#### Purpose

Returns the lower offset segment power measurements. 
 


Use "offset<*n*>" as the selector string to read parameters from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| totalAbsolutePower | float64* | Returns the lower (negative) offset segment power measured. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ. |
| totalRelativePower | float64* | Returns the power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_INTEGRATION, the reference carrier power is the total power in the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_PEAK, the reference carrier power is the peak power in the reference carrier. |
| peakAbsolutePower | float64* | Returns the peak power measured in the lower (negative) offset segment. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ. |
| peakFrequency | float64* | Returns the frequency, in hertz (Hz), at which the peak power occurred in the offset segment. |
| peakRelativePower | float64* | Returns the peak power in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_INTEGRATION, the reference carrier power is the total power in the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_PEAK, the reference carrier power is the peak power in the reference carrier. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semfetchloweroffsetpowerarray.html language=enus -->
## TOPIC 00091: RFmxSpecAn_SEMFetchLowerOffsetPowerArray

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semfetchloweroffsetpowerarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semfetchloweroffsetpowerarray.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMFetchLowerOffsetPowerArray

int32 __stdcall RFmxSpecAn_SEMFetchLowerOffsetPowerArray (niRFmxInstrHandle instrumentHandle, 
 char selectorString[],
 float64 timeout,
 float64 totalAbsolutePower[],
 float64 totalRelativePower[],
 float64 peakAbsolutePower[],
 float64 peakFrequency[],
 float64 peakRelativePower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the arrays of lower offset segment power measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| totalAbsolutePower | float64[] | Returns the array of lower (negative) offset segment powers measured. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ. You can pass NULL for this parameter if you set the arraySize parameter to 0. |
| totalRelativePower | float64[] | Returns the array of powers in each lower (negative) offset segment relative to the integrated or peak power of the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_INTEGRATION, the reference carrier power is the total power in the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_PEAK, the reference carrier power is the peak power in the reference carrier. You can pass NULL for this parameter if you set the arraySize parameter to 0. |
| peakAbsolutePower | float64[] | Returns the array of peak powers measured in each lower (negative) offset segment. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ. You can pass NULL for this parameter if you set the arraySize parameter to 0. |
| peakFrequency | float64[] | Returns the array of frequencies, in hertz (Hz), at which the peak power occurred in each offset segment. You can pass NULL for this parameter if you set the arraySize parameter to 0. |
| peakRelativePower | float64[] | Returns the array of peak powers in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_INTEGRATION, the reference carrier power is the total power in the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_PEAK, the reference carrier power is the peak power in the reference carrier. You can pass NULL for this parameter if you set the arraySize parameter to 0. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_semfetchrelativemasktrace.html language=enus -->
## TOPIC 00092: RFmxSpecAn_SEMFetchRelativeMaskTrace

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_semfetchrelativemasktrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_semfetchrelativemasktrace.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SEMFetchRelativeMaskTrace

int32 __stdcall RFmxSpecAn_SEMFetchRelativeMaskTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 relativeMask[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the relative mask trace used for SEM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the y array. Set the arraySize parameter to 0 to get the size of the y array in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency, in hertz (Hz), of the channel. |
| dx | float64* | Returns the frequency bin spacing, in Hz. |
| relativeMask | float32[] | Returns relative mask used for the channel. Set the arraySize parameter to 0 to get the size of the y array. You can pass NULL for this parameter if you set the arraySize parameter to 0. If the y array is not large enough to hold all the samples, the function returns an error. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spectrumcfgnoisecompensationenabled.html language=enus -->
## TOPIC 00093: RFmxSpecAn_SpectrumCfgNoiseCompensationEnabled

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spectrumcfgnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spectrumcfgnoisecompensationenabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpectrumCfgNoiseCompensationEnabled

int32 __stdcall RFmxSpecAn_SpectrumCfgNoiseCompensationEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 noiseCompensationEnabled);

#### Purpose

Configures compensation of the spectrum for the inherent noise floor of the signal analyzer.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| noiseCompensationEnabled | int32 | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Supported Devices: PXIe-5663/5665/5668, PXIe-5830/5831/5832 RFMXSPECAN_VAL_SPECTRUM_NOISE_COMPENSATION_ENABLED_FALSE (0) Disables compensation of the spectrum for the noise floor of the signal analyzer. RFMXSPECAN_VAL_SPECTRUM_NOISE_COMPENSATION_ENABLED_TRUE (1) Enables compensation of the spectrum for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the Spectrum measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. |
| RFMXSPECAN_VAL_SPECTRUM_NOISE_COMPENSATION_ENABLED_FALSE (0) | Disables compensation of the spectrum for the noise floor of the signal analyzer. |  |
| RFMXSPECAN_VAL_SPECTRUM_NOISE_COMPENSATION_ENABLED_TRUE (1) | Enables compensation of the spectrum for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the Spectrum measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spectrumcfgpowerunits.html language=enus -->
## TOPIC 00094: RFmxSpecAn_SpectrumCfgPowerUnits

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spectrumcfgpowerunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spectrumcfgpowerunits.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpectrumCfgPowerUnits

int32 __stdcall RFmxSpecAn_SpectrumCfgPowerUnits (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spectrumPowerUnits);

#### Purpose

Configures the units for the absolute power.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| spectrumPowerUnits | int32 | Specifies the units for the absolute power. RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBM (0) The absolute powers are reported in dBm. RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBM_PER_HZ (1) The absolute powers are reported in dBm/Hz. RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBW (2) The absolute powers are reported in dBW. RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBV (3) The absolute powers are reported in dBV. RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBMV (4) The absolute powers are reported in dBmV. RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBUV (5) The absolute powers are reported in dBuV. RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_WATTS (6) The absolute powers are reported in W. RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_VOLTS (7) The absolute powers are reported in volts. RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_VOLTS_SQUARED (8) The absolute powers are reported in volts2. |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBM (0) | The absolute powers are reported in dBm. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBM_PER_HZ (1) | The absolute powers are reported in dBm/Hz. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBW (2) | The absolute powers are reported in dBW. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBV (3) | The absolute powers are reported in dBV. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBMV (4) | The absolute powers are reported in dBmV. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBUV (5) | The absolute powers are reported in dBuV. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_WATTS (6) | The absolute powers are reported in W. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_VOLTS (7) | The absolute powers are reported in volts. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_VOLTS_SQUARED (8) | The absolute powers are reported in volts2. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spectrumcfgrbwfilter.html language=enus -->
## TOPIC 00095: RFmxSpecAn_SpectrumCfgRBWFilter

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spectrumcfgrbwfilter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spectrumcfgrbwfilter.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpectrumCfgRBWFilter

int32 __stdcall RFmxSpecAn_SpectrumCfgRBWFilter (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 RBWAuto, float64 RBW, int32 RBWFilterType);

#### Purpose

Configures the resolution bandwidth (RBW) filter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| RBWAuto | int32 | Specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the Spectrum topic for more information about RBW and sweep time. RFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_FALSE (0) The measurement uses the RBW that you specify in the RBW parameter. RFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_TRUE (1) The measurement computes the RBW. |
| RFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_FALSE (0) | The measurement uses the RBW that you specify in the RBW parameter. |  |
| RFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_TRUE (1) | The measurement computes the RBW. |  |
| RBW | float64 | Specifies the bandwidth, in hertz (Hz), of the RBW filter used to sweep the acquired carrier signal, when you set the RBWAuto parameter to RFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_FALSE. |
| RBWFilterType | int32 | Specifies the shape of the digital RBW filter. RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_FFT_BASED (0) No RBW filtering is performed. RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_GAUSSIAN (1) An RBW filter with a Gaussian response is applied. RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_FLAT (2) An RBW filter with a flat response is applied. RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_SYNCH_TUNED_4 (3) An RBW filter with a 4-pole synchronously-tuned response is applied. RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_SYNCH_TUNED_5 (4) An RBW filter with a 5-pole synchronously-tuned response is applied. |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |  |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |  |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_SYNCH_TUNED_4 (3) | An RBW filter with a 4-pole synchronously-tuned response is applied. |  |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_SYNCH_TUNED_5 (4) | An RBW filter with a 5-pole synchronously-tuned response is applied. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spectrumcfgspan.html language=enus -->
## TOPIC 00096: RFmxSpecAn_SpectrumCfgSpan

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spectrumcfgspan.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spectrumcfgspan.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpectrumCfgSpan

int32 __stdcall RFmxSpecAn_SpectrumCfgSpan (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 span);

#### Purpose

Configures the frequency range, in hertz (Hz), around the center frequency, to acquire for the spectrum measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| span | float64 | Specifies the frequency range, in hertz (Hz), around the center frequency, to acquire for the measurement. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spectrumcfgsweeptime.html language=enus -->
## TOPIC 00097: RFmxSpecAn_SpectrumCfgSweepTime

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spectrumcfgsweeptime.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spectrumcfgsweeptime.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpectrumCfgSweepTime

int32 __stdcall RFmxSpecAn_SpectrumCfgSweepTime (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval);

#### Purpose

Configures the sweep time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| sweepTimeAuto | int32 | Specifies whether the measurement computes the sweep time. RFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_FALSE (0) The measurement uses the sweep time that you specify in the sweepTimeInterval parameter. RFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_TRUE (1) The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the sweepTimeInterval parameter. |  |
| RFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_TRUE (1) | The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute. |  |
| sweepTimeInterval | float64 | Specifies the sweep time, in seconds, when you set the sweepTimeAuto parameter to RFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_FALSE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spectrumfetchmeasurement.html language=enus -->
## TOPIC 00098: RFmxSpecAn_SpectrumFetchMeasurement

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spectrumfetchmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spectrumfetchmeasurement.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpectrumFetchMeasurement

int32 __stdcall RFmxSpecAn_SpectrumFetchMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* peakAmplitude,
 float64* peakFrequency,
 float64* frequencyResolution);

#### Purpose

Fetches the peak amplitude and frequency at which the peak occurred in the spectrum.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| peakAmplitude | float64* | Returns the peak amplitude, of the averaged spectrum. When you set the RFMXSPECAN_ATTR_SPECTRUM_SPAN attribute to 0, this function returns the peak amplitude in the time domain power trace. |
| peakFrequency | float64* | Returns the frequency, in hertz (Hz), at the peak amplitude of the averaged spectrum. This parameter is not valid if you set the RFMXSPECAN_ATTR_SPECTRUM_SPAN attribute to 0. |
| frequencyResolution | float64* | Returns the frequency bin spacing, in hertz (Hz), of the spectrum acquired by the measurement. This parameter is not valid if you set the RFMXSPECAN_ATTR_SPECTRUM_SPAN attribute to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spectrumvalidatenoisecalibrationdata.html language=enus -->
## TOPIC 00099: RFmxSpecAn_SpectrumValidateNoiseCalibrationData

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spectrumvalidatenoisecalibrationdata.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spectrumvalidatenoisecalibrationdata.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpectrumValidateNoiseCalibrationData

int32 __stdcall RFmxSpecAn_SpectrumValidateNoiseCalibrationData (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32* noiseCalibrationDataValid);

#### Purpose

Indicates whether calibration data is valid for the configuration specified by the signal name in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| noiseCalibrationDataValid | int32* | Returns whether the calibration data is valid. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spurcfgaveraging.html language=enus -->
## TOPIC 00100: RFmxSpecAn_SpurCfgAveraging

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spurcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spurcfgaveraging.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpurCfgAveraging

int32 __stdcall RFmxSpecAn_SpurCfgAveraging (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType);

#### Purpose

Configures averaging for the spurious emission (Spur) measurement. 
 


**Supported devices**: PXIe-5665, PXIe-5668

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXSPECAN_VAL_SPUR_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition. RFMXSPECAN_VAL_SPUR_AVERAGING_ENABLED_TRUE (1) The measurement uses the averagingCount parameter to calculate the number of acquisitions over which the measurement is averaged. |
| RFMXSPECAN_VAL_SPUR_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_ENABLED_TRUE (1) | The measurement uses the averagingCount parameter to calculate the number of acquisitions over which the measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXSPECAN_VAL_SPUR_AVERAGING_ENABLED_TRUE. |
| averagingType | int32 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_LOG (1) The power spectrum is averaged in a logarithm scale. RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_SCALAR (2) The square root of the power spectrum is averaged. RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_MAXIMUM (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_MINIMUM (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithm scale. |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spurcfgfftwindowtype.html language=enus -->
## TOPIC 00101: RFmxSpecAn_SpurCfgFFTWindowType

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spurcfgfftwindowtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spurcfgfftwindowtype.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpurCfgFFTWindowType

int32 __stdcall RFmxSpecAn_SpurCfgFFTWindowType (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 FFTWindow);

#### Purpose

Configures the FFT window to obtain a spectrum for the spurious emission (Spur) measurement. 
 


**Supported devices**: PXIe-5665, PXIe-5668

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| FFTWindow | int32 | Specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectrum topic for more information about FFT window types. RFMXSPECAN_VAL_SPUR_FFT_WINDOW_NONE (0) Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. RFMXSPECAN_VAL_SPUR_FFT_WINDOW_FLAT_TOP (1) Measures single-tone amplitudes accurately. RFMXSPECAN_VAL_SPUR_FFT_WINDOW_HANNING (2) Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. RFMXSPECAN_VAL_SPUR_FFT_WINDOW_HAMMING (3) Analyzes closely-spaced sine waves. RFMXSPECAN_VAL_SPUR_FFT_WINDOW_GAUSSIAN (4) Provides a balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis. RFMXSPECAN_VAL_SPUR_FFT_WINDOW_BLACKMAN (5) Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. RFMXSPECAN_VAL_SPUR_FFT_WINDOW_BLACKMAN_HARRIS (6) Useful as a good general purpose window, having side lobe rejection >90dB and having a moderately wide main lobe. RFMXSPECAN_VAL_SPUR_FFT_WINDOW_KAISER_BESSEL (7) Separates two tones with frequencies close to each other but with widely-differing amplitudes. |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_NONE (0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_FLAT_TOP (1) | Measures single-tone amplitudes accurately. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_HANNING (2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_HAMMING (3) | Analyzes closely-spaced sine waves. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_GAUSSIAN (4) | Provides a balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_BLACKMAN (5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_BLACKMAN_HARRIS (6) | Useful as a good general purpose window, having side lobe rejection >90dB and having a moderately wide main lobe. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_KAISER_BESSEL (7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spurcfgnumberofranges.html language=enus -->
## TOPIC 00102: RFmxSpecAn_SpurCfgNumberOfRanges

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spurcfgnumberofranges.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spurcfgnumberofranges.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpurCfgNumberOfRanges

int32 __stdcall RFmxSpecAn_SpurCfgNumberOfRanges (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfRanges);

#### Purpose

Configures the number of ranges. 
 


**Supported devices**: PXIe-5665, PXIe-5668

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| numberOfRanges | int32 | Specifies the number of ranges. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spurcfgrangeabsolutelimitarray.html language=enus -->
## TOPIC 00103: RFmxSpecAn_SpurCfgRangeAbsoluteLimitArray

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spurcfgrangeabsolutelimitarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spurcfgrangeabsolutelimitarray.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpurCfgRangeAbsoluteLimitArray

int32 __stdcall RFmxSpecAn_SpurCfgRangeAbsoluteLimitArray (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 absoluteLimitMode[], float64 absoluteLimitStart[], float64 absoluteLimitStop[], int32 numberOfElements);

#### Purpose

Configures the absolute power limits corresponding to the beginning and end of the frequency range and specifies whether the absolute limit threshold is a flat line or a line with a slope. 
 


**Supported devices**: PXIe-5665, PXIe-5668

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| absoluteLimitMode | int32[] | Specifies whether the absolute limit threshold is a flat line or a line with a slope. Specify NULL if you do not want to set a value for this array. RFMXSPECAN_VAL_SPUR_ABSOLUTE_LIMIT_MODE_MANUAL (0) The line specified by the RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_START and RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_STOP attribute values as the two ends is considered as the mask. RFMXSPECAN_VAL_SPUR_ABSOLUTE_LIMIT_MODE_COUPLE (1) The two ends of the line are coupled to the value of the RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_START attribute. |
| RFMXSPECAN_VAL_SPUR_ABSOLUTE_LIMIT_MODE_MANUAL (0) | The line specified by the RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_START and RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_STOP attribute values as the two ends is considered as the mask. |  |
| RFMXSPECAN_VAL_SPUR_ABSOLUTE_LIMIT_MODE_COUPLE (1) | The two ends of the line are coupled to the value of the RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_START attribute. |  |
| absoluteLimitStart | float64[] | Specifies the array of absolute power limits, in dBm, corresponding to the beginning of the frequency range. The value of this parameter is also set as the absolute power limit for the range when you set the absoluteLimitMode parameter to RFMXSPECAN_VAL_SPUR_ABSOLUTE_LIMIT_MODE_COUPLE. Specify NULL if you do not want to set a value for this array. |
| absoluteLimitStop | float64[] | Specifies the array of absolute power limits, in dBm, corresponding to the end of the frequency range. This parameter is ignored when you set the absoluteLimitMode parameter to RFMXSPECAN_VAL_SPUR_ABSOLUTE_LIMIT_MODE_COUPLE. Specify NULL if you do not want to set a value for this array. |
| numberOfElements | int32 | Specifies the number of elements in each array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=cvirfmxspecan_spurcfgtracerangeindex.html language=enus -->
## TOPIC 00104: RFmxSpecAn_SpurCfgTraceRangeIndex

- bundle_id: `rfmx-specan-cvi`
- source_path: `cvirfmxspecan_spurcfgtracerangeindex.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/cvirfmxspecan_spurcfgtracerangeindex.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn_SpurCfgTraceRangeIndex

int32 __stdcall RFmxSpecAn_SpurCfgTraceRangeIndex (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 traceRangeIndex);

#### Purpose

Specifies the index of the range used to store and retrieve the spurious emission (Spur) trace. 
 


**Supported devices**: PXIe-5665, PXIe-5668

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| traceRangeIndex | int32 | Specifies the index of the range used to store and retrieve spurious emission (Spur) traces. This parameter is not used if you set the RFMXSPECAN_ATTR_SPUR_ALL_TRACES_ENABLED attribute to RFMXSPECAN_VAL_FALSE. When you set this parameter to -1, the measurement stores and retrieves traces for all enabled ranges. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxSpecAn_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_acp_amplitude_correction_type.html language=enus -->
## TOPIC 00105: RFMXSPECAN_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_acp_amplitude_correction_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_acp_amplitude_correction_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY. Get Function: RFmxSpecAn_ACPGetAmplitudeCorrectionType Set Function: RFmxSpecAn_ACPSetAmplitudeCorrectionType |
| Values: | RFMXSPECAN_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY (0)All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. RFMXSPECAN_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN (1)An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |
| RFMXSPECAN_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY (0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXSPECAN_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN (1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_acp_carrier_rrc_filter_alpha.html language=enus -->
## TOPIC 00106: RFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ALPHA

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_acp_carrier_rrc_filter_alpha.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_acp_carrier_rrc_filter_alpha.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ALPHA

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. Use 'carrier(n)' as the selector string to configure or read this attribute. The default value is 0.1. Get Function: RFmxSpecAn_ACPGetCarrierRRCFilterAlpha Set Function: RFmxSpecAn_ACPSetCarrierRRCFilterAlpha |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_acp_carrier_rrc_filter_enabled.html language=enus -->
## TOPIC 00107: RFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_acp_carrier_rrc_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_acp_carrier_rrc_filter_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel before measuring the carrier channel power. Use 'carrier(n)' as the selector string to configure or read this attribute. The default value is RFMXSPECAN_VAL_ACP_CARRIER_RRC_FILTER_ENABLED_FALSE. Get Function: RFmxSpecAn_ACPGetCarrierRRCFilterEnabled Set Function: RFmxSpecAn_ACPSetCarrierRRCFilterEnabled |
| Values: | RFMXSPECAN_VAL_ACP_CARRIER_RRC_FILTER_ENABLED_FALSE (0)The channel power of the acquired carrier channel is measured directly. RFMXSPECAN_VAL_ACP_CARRIER_RRC_FILTER_ENABLED_TRUE (1)The measurement applies the RRC filter on the acquired carrier channel before measuring the carrier channel power. |
| RFMXSPECAN_VAL_ACP_CARRIER_RRC_FILTER_ENABLED_FALSE (0) | The channel power of the acquired carrier channel is measured directly. |
| RFMXSPECAN_VAL_ACP_CARRIER_RRC_FILTER_ENABLED_TRUE (1) | The measurement applies the RRC filter on the acquired carrier channel before measuring the carrier channel power. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_acp_offset_enabled.html language=enus -->
## TOPIC 00108: RFMXSPECAN_ATTR_ACP_OFFSET_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_acp_offset_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_acp_offset_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_ACP_OFFSET_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the offset channel for ACP measurement. Use 'offset(n)' as the selector string to configure or read this attribute. The default value is RFMXSPECAN_VAL_ACP_OFFSET_FREQUENCY_ENABLED_TRUE. Get Function: RFmxSpecAn_ACPGetOffsetEnabled Set Function: RFmxSpecAn_ACPSetOffsetEnabled |
| Values: | RFMXSPECAN_VAL_ACP_OFFSET_FREQUENCY_ENABLED_FALSE (0)Disables the offset channel for ACP measurement. RFMXSPECAN_VAL_ACP_OFFSET_FREQUENCY_ENABLED_TRUE (1)Enables the offset channel for ACP measurement. |
| RFMXSPECAN_VAL_ACP_OFFSET_FREQUENCY_ENABLED_FALSE (0) | Disables the offset channel for ACP measurement. |
| RFMXSPECAN_VAL_ACP_OFFSET_FREQUENCY_ENABLED_TRUE (1) | Enables the offset channel for ACP measurement. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_acp_offset_sideband.html language=enus -->
## TOPIC 00109: RFMXSPECAN_ATTR_ACP_OFFSET_SIDEBAND

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_acp_offset_sideband.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_acp_offset_sideband.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_ACP_OFFSET_SIDEBAND

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the offset channel is present on one side, or on both sides of the carrier. Use 'offset(n)' as the selector string to configure or read this attribute. The default value is RFMXSPECAN_VAL_ACP_OFFSET_SIDEBAND_BOTH. Get Function: RFmxSpecAn_ACPGetOffsetSideband Set Function: RFmxSpecAn_ACPSetOffsetSideband |
| Values: | RFMXSPECAN_VAL_ACP_OFFSET_SIDEBAND_NEGATIVE (0)Configures a lower offset segment to the left of the leftmost carrier. RFMXSPECAN_VAL_ACP_OFFSET_SIDEBAND_POSITIVE (1)Configures an upper offset segment to the right of the rightmost carrier. RFMXSPECAN_VAL_ACP_OFFSET_SIDEBAND_BOTH (2)Configures both negative and positive offset segments. |
| RFMXSPECAN_VAL_ACP_OFFSET_SIDEBAND_NEGATIVE (0) | Configures a lower offset segment to the left of the leftmost carrier. |
| RFMXSPECAN_VAL_ACP_OFFSET_SIDEBAND_POSITIVE (1) | Configures an upper offset segment to the right of the rightmost carrier. |
| RFMXSPECAN_VAL_ACP_OFFSET_SIDEBAND_BOTH (2) | Configures both negative and positive offset segments. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_acp_power_units.html language=enus -->
## TOPIC 00110: RFMXSPECAN_ATTR_ACP_POWER_UNITS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_acp_power_units.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_acp_power_units.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_ACP_POWER_UNITS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the units for the absolute power. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_ACP_POWER_UNITS_DBM_PER_HZ. Get Function: RFmxSpecAn_ACPGetPowerUnits Set Function: RFmxSpecAn_ACPSetPowerUnits |
| Values: | RFMXSPECAN_VAL_ACP_POWER_UNITS_DBM (0)The absolute powers are reported in dBm. RFMXSPECAN_VAL_ACP_POWER_UNITS_DBM_PER_HZ (1)The absolute powers are reported in dBm/Hz. |
| RFMXSPECAN_VAL_ACP_POWER_UNITS_DBM (0) | The absolute powers are reported in dBm. |
| RFMXSPECAN_VAL_ACP_POWER_UNITS_DBM_PER_HZ (1) | The absolute powers are reported in dBm/Hz. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_acp_results_carrier_total_relative_power.html language=enus -->
## TOPIC 00111: RFMXSPECAN_ATTR_ACP_RESULTS_CARRIER_TOTAL_RELATIVE_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_acp_results_carrier_total_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_acp_results_carrier_total_relative_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_ACP_RESULTS_CARRIER_TOTAL_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the carrier power measured relative to the total carrier power of all active carriers. This value is expressed in dB. Use 'carrier(n)' as the selector string to read this result. Get Function: RFmxSpecAn_ACPGetResultsCarrierTotalRelativePower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ampm_results_peak_reference_power.html language=enus -->
## TOPIC 00112: RFMXSPECAN_ATTR_AMPM_RESULTS_PEAK_REFERENCE_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ampm_results_peak_reference_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ampm_results_peak_reference_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_AMPM_RESULTS_PEAK_REFERENCE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the peak reference power. This value is expressed in dBm. You do not need to use a selector string to read this attribute for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxSpecAn_AMPMGetResultsPeakReferencePower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ampm_signal_type.html language=enus -->
## TOPIC 00113: RFMXSPECAN_ATTR_AMPM_SIGNAL_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ampm_signal_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ampm_signal_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_AMPM_SIGNAL_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals. To time-align the sinusoidal reference waveform to the acquired signal, set the RFMXSPECAN_ATTR_AMPM_SIGNAL_TYPE attribute to Tones, which switches the AMPM measurement alignment algorithm. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_AMPM_SIGNAL_TYPE_MODULATED. Get Function: RFmxSpecAn_AMPMGetSignalType Set Function: RFmxSpecAn_AMPMSetSignalType |
| Values: | RFMXSPECAN_VAL_AMPM_SIGNAL_TYPE_MODULATED (0)The reference waveform is a cellular or connectivity standard signal. RFMXSPECAN_VAL_AMPM_SIGNAL_TYPE_TONES (1)The reference waveform is a continuous signal comprising of one or more tones. |
| RFMXSPECAN_VAL_AMPM_SIGNAL_TYPE_MODULATED (0) | The reference waveform is a cellular or connectivity standard signal. |
| RFMXSPECAN_VAL_AMPM_SIGNAL_TYPE_TONES (1) | The reference waveform is a continuous signal comprising of one or more tones. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ampm_threshold_enabled.html language=enus -->
## TOPIC 00114: RFMXSPECAN_ATTR_AMPM_THRESHOLD_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ampm_threshold_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ampm_threshold_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_AMPM_THRESHOLD_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable thresholding of the acquired samples used for the AMPM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_AMPM_THRESHOLD_ENABLED_TRUE. Get Function: RFmxSpecAn_AMPMGetThresholdEnabled Set Function: RFmxSpecAn_AMPMSetThresholdEnabled |
| Values: | RFMXSPECAN_VAL_AMPM_THRESHOLD_ENABLED_FALSE (0)All samples are considered for the AMPM measurement. RFMXSPECAN_VAL_AMPM_THRESHOLD_ENABLED_TRUE (1)Samples above the threshold level specified in the RFMXSPECAN_ATTR_AMPM_THRESHOLD_LEVEL attribute are considered for the AMPM measurement. |
| RFMXSPECAN_VAL_AMPM_THRESHOLD_ENABLED_FALSE (0) | All samples are considered for the AMPM measurement. |
| RFMXSPECAN_VAL_AMPM_THRESHOLD_ENABLED_TRUE (1) | Samples above the threshold level specified in the RFMXSPECAN_ATTR_AMPM_THRESHOLD_LEVEL attribute are considered for the AMPM measurement. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ampm_threshold_level.html language=enus -->
## TOPIC 00115: RFMXSPECAN_ATTR_AMPM_THRESHOLD_LEVEL

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ampm_threshold_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ampm_threshold_level.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_AMPM_THRESHOLD_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies either the relative or absolute threshold power level, based on the value of the RFMXSPECAN_ATTR_AMPM_THRESHOLD_TYPE attribute. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is -20 dB. Get Function: RFmxSpecAn_AMPMGetThresholdLevel Set Function: RFmxSpecAn_AMPMSetThresholdLevel |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_measurement_enabled.html language=enus -->
## TOPIC 00116: RFMXSPECAN_ATTR_CCDF_MEASUREMENT_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_measurement_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the CCDF measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_FALSE. Get Function: RFmxSpecAn_CCDFGetMeasurementEnabled Set Function: RFmxSpecAn_CCDFSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_number_of_analysis_threads.html language=enus -->
## TOPIC 00117: RFMXSPECAN_ATTR_CCDF_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_number_of_analysis_threads.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for CCDF measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxSpecAn_CCDFGetNumberOfAnalysisThreads Set Function: RFmxSpecAn_CCDFSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_number_of_records.html language=enus -->
## TOPIC 00118: RFMXSPECAN_ATTR_CCDF_NUMBER_OF_RECORDS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_number_of_records.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_number_of_records.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_NUMBER_OF_RECORDS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for the CCDF measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxSpecAn_CCDFGetNumberOfRecords Set Function: RFmxSpecAn_CCDFSetNumberOfRecords |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_rbw_filter_bandwidth.html language=enus -->
## TOPIC 00119: RFMXSPECAN_ATTR_CCDF_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_rbw_filter_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_rbw_filter_bandwidth.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_RBW_FILTER_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the signal. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 100 kHz. Get Function: RFmxSpecAn_CCDFGetRBWFilterBandwidth Set Function: RFmxSpecAn_CCDFSetRBWFilterBandwidth |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_rbw_filter_type.html language=enus -->
## TOPIC 00120: RFMXSPECAN_ATTR_CCDF_RBW_FILTER_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_rbw_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_rbw_filter_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_RBW_FILTER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the shape of the digital resolution bandwidth (RBW) filter. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CCDF_RBW_FILTER_TYPE_NONE. Get Function: RFmxSpecAn_CCDFGetRBWFilterType Set Function: RFmxSpecAn_CCDFSetRBWFilterType |
| Values: | RFMXSPECAN_VAL_CCDF_RBW_FILTER_TYPE_NONE (5)The measurement does not use any RBW filtering. RFMXSPECAN_VAL_CCDF_RBW_FILTER_TYPE_GAUSSIAN (1)The RBW filter has a Gaussian response. RFMXSPECAN_VAL_CCDF_RBW_FILTER_TYPE_FLAT (2)The RBW filter has a flat response. RFMXSPECAN_VAL_CCDF_RBW_FILTER_TYPE_RRC (6)The RRC filter with the roll-off specified by the RFMXSPECAN_ATTR_CCDF_RBW_FILTER_RRC_ALPHA attribute is used as the RBW filter. |
| RFMXSPECAN_VAL_CCDF_RBW_FILTER_TYPE_NONE (5) | The measurement does not use any RBW filtering. |
| RFMXSPECAN_VAL_CCDF_RBW_FILTER_TYPE_GAUSSIAN (1) | The RBW filter has a Gaussian response. |
| RFMXSPECAN_VAL_CCDF_RBW_FILTER_TYPE_FLAT (2) | The RBW filter has a flat response. |
| RFMXSPECAN_VAL_CCDF_RBW_FILTER_TYPE_RRC (6) | The RRC filter with the roll-off specified by the RFMXSPECAN_ATTR_CCDF_RBW_FILTER_RRC_ALPHA attribute is used as the RBW filter. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_results_mean_power.html language=enus -->
## TOPIC 00121: RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_results_mean_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_results_mean_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the average power of all the samples. This value is expressed in dBm. If you set the RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED attribute to RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_TRUE, samples above the threshold are measured. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_CCDFGetResultsMeanPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_results_mean_power_percentile.html language=enus -->
## TOPIC 00122: RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER_PERCENTILE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_results_mean_power_percentile.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_results_mean_power_percentile.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER_PERCENTILE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the percentage of samples that have more power than the mean power. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_CCDFGetResultsMeanPowerPercentile |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_results_measured_samples_count.html language=enus -->
## TOPIC 00123: RFMXSPECAN_ATTR_CCDF_RESULTS_MEASURED_SAMPLES_COUNT

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_results_measured_samples_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_results_measured_samples_count.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_RESULTS_MEASURED_SAMPLES_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeI32 |
| Description: | Returns the total number of samples measured. The total number of samples includes only the samples above the threshold, when you set the RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED attribute to RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_TRUE. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_CCDFGetResultsMeasuredSampleCount |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_results_one_hundredth_percent_power.html language=enus -->
## TOPIC 00124: RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_HUNDREDTH_PERCENT_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_results_one_hundredth_percent_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_results_one_hundredth_percent_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_HUNDREDTH_PERCENT_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the power above the mean power, over which 0.01% of the total samples in the signal are present. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_CCDFGetResultsOneHundredthPercentPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_results_one_percent_power.html language=enus -->
## TOPIC 00125: RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_PERCENT_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_results_one_percent_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_results_one_percent_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_PERCENT_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the power above the mean power, over which 1% of the total samples in the signal are present. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_CCDFGetResultsOnePercentPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_results_one_ten_thousandth_percent_power.html language=enus -->
## TOPIC 00126: RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_TEN_THOUSANDTH_PERCENT_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_results_one_ten_thousandth_percent_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_results_one_ten_thousandth_percent_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_TEN_THOUSANDTH_PERCENT_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the power above the mean power, over which 0.0001% of the total samples in the signal are present. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_CCDFGetResultsOneTenThousandthPercentPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_results_peak_power.html language=enus -->
## TOPIC 00127: RFMXSPECAN_ATTR_CCDF_RESULTS_PEAK_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_results_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_results_peak_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_RESULTS_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the peak power of the acquired signal, relative to the mean power. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxSpecAn_CCDFGetResultsPeakPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_results_ten_percent_power.html language=enus -->
## TOPIC 00128: RFMXSPECAN_ATTR_CCDF_RESULTS_TEN_PERCENT_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_results_ten_percent_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_results_ten_percent_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_RESULTS_TEN_PERCENT_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the power above the mean power, over which 10% of the total samples in the signal are present. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_CCDFGetResultsTenPercentPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_threshold_enabled.html language=enus -->
## TOPIC 00129: RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_threshold_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_threshold_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable thresholding of the acquired samples to be used for the CCDF measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_FALSE. Get Function: RFmxSpecAn_CCDFGetThresholdEnabled Set Function: RFmxSpecAn_CCDFSetThresholdEnabled |
| Values: | RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_FALSE (0)All samples are considered for the CCDF measurement. RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_TRUE (1)The samples above the threshold level specified in the RFMXSPECAN_ATTR_CCDF_THRESHOLD_LEVEL attribute are considered for the CCDF measurement. |
| RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_FALSE (0) | All samples are considered for the CCDF measurement. |
| RFMXSPECAN_VAL_CCDF_THRESHOLD_ENABLED_TRUE (1) | The samples above the threshold level specified in the RFMXSPECAN_ATTR_CCDF_THRESHOLD_LEVEL attribute are considered for the CCDF measurement. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_threshold_level.html language=enus -->
## TOPIC 00130: RFMXSPECAN_ATTR_CCDF_THRESHOLD_LEVEL

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_threshold_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_threshold_level.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_THRESHOLD_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies either the relative or absolute threshold power level based on the value of the RFMXSPECAN_ATTR_CCDF_THRESHOLD_TYPE attribute. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is -20. Get Function: RFmxSpecAn_CCDFGetThresholdLevel Set Function: RFmxSpecAn_CCDFSetThresholdLevel |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_ccdf_threshold_type.html language=enus -->
## TOPIC 00131: RFMXSPECAN_ATTR_CCDF_THRESHOLD_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_ccdf_threshold_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_ccdf_threshold_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CCDF_THRESHOLD_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the reference for the power level used for thresholding. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_RELATIVE. Get Function: RFmxSpecAn_CCDFGetThresholdType Set Function: RFmxSpecAn_CCDFSetThresholdType |
| Values: | RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_RELATIVE (0)The threshold is relative to the peak power of the acquired samples. RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_ABSOLUTE (1)The threshold is the absolute power, in dBm. |
| RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_RELATIVE (0) | The threshold is relative to the peak power of the acquired samples. |
| RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_ABSOLUTE (1) | The threshold is the absolute power, in dBm. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_center_frequency.html language=enus -->
## TOPIC 00132: RFMXSPECAN_ATTR_CENTER_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_center_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_center_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CENTER_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default of this attribute is hardware dependent. Get Function: RFmxSpecAn_GetCenterFrequency Set Function: RFmxSpecAn_SetCenterFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_all_traces_enabled.html language=enus -->
## TOPIC 00133: RFMXSPECAN_ATTR_CHP_ALL_TRACES_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_all_traces_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_FALSE. Get Function: RFmxSpecAn_CHPGetAllTracesEnabled Set Function: RFmxSpecAn_CHPSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_amplitude_correction_type.html language=enus -->
## TOPIC 00134: RFMXSPECAN_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_amplitude_correction_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_amplitude_correction_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY. Get Function: RFmxSpecAn_CHPGetAmplitudeCorrectionType Set Function: RFmxSpecAn_CHPSetAmplitudeCorrectionType |
| Values: | RFMXSPECAN_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY (0)All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. RFMXSPECAN_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN (1)An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |
| RFMXSPECAN_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY (0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXSPECAN_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN (1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_averaging_count.html language=enus -->
## TOPIC 00135: RFMXSPECAN_ATTR_CHP_AVERAGING_COUNT

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_averaging_count.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_CHP_AVERAGING_ENABLED attribute to RFMXSPECAN_VAL_CHP_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxSpecAn_CHPGetAveragingCount Set Function: RFmxSpecAn_CHPSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_averaging_enabled.html language=enus -->
## TOPIC 00136: RFMXSPECAN_ATTR_CHP_AVERAGING_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_averaging_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the CHP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CHP_AVERAGING_ENABLED_FALSE. Get Function: RFmxSpecAn_CHPGetAveragingEnabled Set Function: RFmxSpecAn_CHPSetAveragingEnabled |
| Values: | RFMXSPECAN_VAL_CHP_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXSPECAN_VAL_CHP_AVERAGING_ENABLED_TRUE (1)The CHP measurement uses the RFMXSPECAN_ATTR_CHP_AVERAGING_COUNT attribute as the number of acquisitions over which the CHP measurement is averaged. |
| RFMXSPECAN_VAL_CHP_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXSPECAN_VAL_CHP_AVERAGING_ENABLED_TRUE (1) | The CHP measurement uses the RFMXSPECAN_ATTR_CHP_AVERAGING_COUNT attribute as the number of acquisitions over which the CHP measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_averaging_type.html language=enus -->
## TOPIC 00137: RFMXSPECAN_ATTR_CHP_AVERAGING_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_averaging_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_RMS. Get Function: RFmxSpecAn_CHPGetAveragingType Set Function: RFmxSpecAn_CHPSetAveragingType |
| Values: | RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_SCALAR (2)The square root of the power spectrum is averaged. RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_MAXIMUM (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_MINIMUM (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |
| RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_CHP_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_carrier_integration_bandwidth.html language=enus -->
## TOPIC 00138: RFMXSPECAN_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_carrier_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_carrier_integration_bandwidth.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the frequency range, over which the measurement integrates the power. This value is expressed in Hz. Use 'carrier(n)' as the selector string to configure or read this attribute. The default value is 1 MHz. Get Function: RFmxSpecAn_CHPGetCarrierIntegrationBandwidth Set Function: RFmxSpecAn_CHPSetCarrierIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_carrier_rrc_filter_alpha.html language=enus -->
## TOPIC 00139: RFMXSPECAN_ATTR_CHP_CARRIER_RRC_FILTER_ALPHA

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_carrier_rrc_filter_alpha.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_carrier_rrc_filter_alpha.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_CARRIER_RRC_FILTER_ALPHA

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the roll-off factor of the root-raised-cosine (RRC) filter. Use 'carrier(n)' as the selector string to configure or read this attribute. The default value is 0.1. Get Function: RFmxSpecAn_CHPGetCarrierRRCFilterAlpha Set Function: RFmxSpecAn_CHPSetCarrierRRCFilterAlpha |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_carrier_rrc_filter_enabled.html language=enus -->
## TOPIC 00140: RFMXSPECAN_ATTR_CHP_CARRIER_RRC_FILTER_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_carrier_rrc_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_carrier_rrc_filter_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_CARRIER_RRC_FILTER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired channel before measuring the channel power. Use 'carrier(n)' as the selector string to configure or read this attribute. The default value is RFMXSPECAN_VAL_CHP_CARRIER_RRC_FILTER_ENABLED_FALSE. Get Function: RFmxSpecAn_CHPGetCarrierRRCFilterEnabled Set Function: RFmxSpecAn_CHPSetCarrierRRCFilterEnabled |
| Values: | RFMXSPECAN_VAL_CHP_CARRIER_RRC_FILTER_ENABLED_FALSE (0)The channel power of the acquired channel is measured directly. RFMXSPECAN_VAL_CHP_CARRIER_RRC_FILTER_ENABLED_TRUE (1)The measurement applies the RRC filter on the acquired channel before measuring the channel power. |
| RFMXSPECAN_VAL_CHP_CARRIER_RRC_FILTER_ENABLED_FALSE (0) | The channel power of the acquired channel is measured directly. |
| RFMXSPECAN_VAL_CHP_CARRIER_RRC_FILTER_ENABLED_TRUE (1) | The measurement applies the RRC filter on the acquired channel before measuring the channel power. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_fft_padding.html language=enus -->
## TOPIC 00141: RFMXSPECAN_ATTR_CHP_FFT_PADDING

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_fft_padding.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_fft_padding.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_FFT_PADDING

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the factor by which the time-domain waveform is zero-padded before fast Fourier transform (FFT). The FFT size is given by the following formula: waveform size * padding This attribute is used only when the acquisition span is less than the device instantaneous bandwidth of the device. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is -1. Get Function: RFmxSpecAn_CHPGetFFTPadding Set Function: RFmxSpecAn_CHPSetFFTPadding |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_fft_window.html language=enus -->
## TOPIC 00142: RFMXSPECAN_ATTR_CHP_FFT_WINDOW

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_fft_window.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_fft_window.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_FFT_WINDOW

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the FFT window type to use to reduce spectral leakage. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CHP_FFT_WINDOW_FLAT_TOP. Get Function: RFmxSpecAn_CHPGetFFTWindow Set Function: RFmxSpecAn_CHPSetFFTWindow |
| Values: | RFMXSPECAN_VAL_CHP_FFT_WINDOW_NONE (0)Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. RFMXSPECAN_VAL_CHP_FFT_WINDOW_FLAT_TOP (1)Measures single-tone amplitudes accurately. RFMXSPECAN_VAL_CHP_FFT_WINDOW_HANNING (2)Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. RFMXSPECAN_VAL_CHP_FFT_WINDOW_HAMMING (3)Analyzes closely-spaced sine waves. RFMXSPECAN_VAL_CHP_FFT_WINDOW_GAUSSIAN (4)Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. RFMXSPECAN_VAL_CHP_FFT_WINDOW_BLACKMAN (5)Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. RFMXSPECAN_VAL_CHP_FFT_WINDOW_BLACKMAN_HARRIS (6)Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. RFMXSPECAN_VAL_CHP_FFT_WINDOW_KAISER_BESSEL (7)Separates two tones with frequencies close to each other but with widely-differing amplitudes. |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_NONE (0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_FLAT_TOP (1) | Measures single-tone amplitudes accurately. |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_HANNING (2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_HAMMING (3) | Analyzes closely-spaced sine waves. |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_GAUSSIAN (4) | Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_BLACKMAN (5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_BLACKMAN_HARRIS (6) | Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |
| RFMXSPECAN_VAL_CHP_FFT_WINDOW_KAISER_BESSEL (7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_measurement_enabled.html language=enus -->
## TOPIC 00143: RFMXSPECAN_ATTR_CHP_MEASUREMENT_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_measurement_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the CHP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_FALSE. Get Function: RFmxSpecAn_CHPGetMeasurementEnabled Set Function: RFmxSpecAn_CHPSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_noise_calibration_averaging_auto.html language=enus -->
## TOPIC 00144: RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_AUTO

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_noise_calibration_averaging_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_noise_calibration_averaging_auto.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE. Get Function: RFmxSpecAn_CHPGetNoiseCalibrationAveragingAuto Set Function: RFmxSpecAn_CHPSetNoiseCalibrationAveragingAuto |
| Values: | RFMXSPECAN_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE (0)RFmx uses the averages that you set for the RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_COUNT attribute. RFMXSPECAN_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE (1)RFmx uses a noise calibration averaging count of 32. |
| RFMXSPECAN_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE (0) | RFmx uses the averages that you set for the RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_COUNT attribute. |
| RFMXSPECAN_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE (1) | RFmx uses a noise calibration averaging count of 32. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_noise_calibration_averaging_count.html language=enus -->
## TOPIC 00145: RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_COUNT

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_noise_calibration_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_noise_calibration_averaging_count.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the averaging count used for noise calibration when you set the RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_AUTO attribute to RFMXSPECAN_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 32. Get Function: RFmxSpecAn_CHPGetNoiseCalibrationAveragingCount Set Function: RFmxSpecAn_CHPSetNoiseCalibrationAveragingCount |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_noise_compensation_enabled.html language=enus -->
## TOPIC 00146: RFMXSPECAN_ATTR_CHP_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_noise_compensation_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_NOISE_COMPENSATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_MODE attribute to RFMXSPECAN_VAL_CHP_NOISE_CALIBRATION_MODE_AUTO, or set the RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_MODE attribute to RFMXSPECAN_VAL_CHP_NOISE_CALIBRATION_MODE_MANUAL and RFMXSPECAN_ATTR_CHP_MEASUREMENT_MODE attribute to RFMXSPECAN_VAL_CHP_MEASUREMENT_MODE_MEASURE. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE. Get Function: RFmxSpecAn_CHPGetNoiseCompensationEnabled Set Function: RFmxSpecAn_CHPSetNoiseCompensationEnabled |
| Values: | RFMXSPECAN_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE (0)Disables noise compensation. RFMXSPECAN_VAL_CHP_NOISE_COMPENSATION_ENABLED_TRUE (1)Enables noise compensation. |
| RFMXSPECAN_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE (0) | Disables noise compensation. |
| RFMXSPECAN_VAL_CHP_NOISE_COMPENSATION_ENABLED_TRUE (1) | Enables noise compensation. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_number_of_carriers.html language=enus -->
## TOPIC 00147: RFMXSPECAN_ATTR_CHP_NUMBER_OF_CARRIERS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_number_of_carriers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_number_of_carriers.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_NUMBER_OF_CARRIERS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the number of carriers. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxSpecAn_CHPGetNumberOfCarriers Set Function: RFmxSpecAn_CHPSetNumberOfCarriers |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_rbw_filter_auto_bandwidth.html language=enus -->
## TOPIC 00148: RFMXSPECAN_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_rbw_filter_auto_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_rbw_filter_auto_bandwidth.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the resolution bandwidth (RBW). You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CHP_RBW_AUTO_TRUE. Get Function: RFmxSpecAn_CHPGetRBWFilterAutoBandwidth Set Function: RFmxSpecAn_CHPSetRBWFilterAutoBandwidth |
| Values: | RFMXSPECAN_VAL_CHP_RBW_AUTO_FALSE (0)The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. RFMXSPECAN_VAL_CHP_RBW_AUTO_TRUE (1)The measurement computes the RBW. |
| RFMXSPECAN_VAL_CHP_RBW_AUTO_FALSE (0) | The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_VAL_CHP_RBW_AUTO_TRUE (1) | The measurement computes the RBW. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_rbw_filter_bandwidth_definition.html language=enus -->
## TOPIC 00149: RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH_DEFINITION

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_rbw_filter_bandwidth_definition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_rbw_filter_bandwidth_definition.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH_DEFINITION

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the bandwidth definition that you use to specify the value of the RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. The default value is RFMXSPECAN_VAL_CHP_RBW_FILTER_BANDWIDTH_DEFINITION_3DB. Get Function: RFmxSpecAn_CHPGetRBWFilterBandwidthDefinition Set Function: RFmxSpecAn_CHPSetRBWFilterBandwidthDefinition |
| Values: | RFMXSPECAN_VAL_CHP_RBW_FILTER_BANDWIDTH_DEFINITION_3DB (0)Defines the RBW in terms of the 3 dB bandwidth of the RBW filter. When you set the RFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPE attribute to RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED, RBW is the 3 dB bandwidth of the window specified by the RFMXSPECAN_ATTR_CHP_FFT_WINDOW attribute. RFMXSPECAN_VAL_CHP_RBW_FILTER_BANDWIDTH_DEFINITION_BIN_WIDTH (2)Defines the RBW in terms of the spectrum bin width computed using an FFT when you set the RFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPE attribute to FFT Based. |
| RFMXSPECAN_VAL_CHP_RBW_FILTER_BANDWIDTH_DEFINITION_3DB (0) | Defines the RBW in terms of the 3 dB bandwidth of the RBW filter. When you set the RFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPE attribute to RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED, RBW is the 3 dB bandwidth of the window specified by the RFMXSPECAN_ATTR_CHP_FFT_WINDOW attribute. |
| RFMXSPECAN_VAL_CHP_RBW_FILTER_BANDWIDTH_DEFINITION_BIN_WIDTH (2) | Defines the RBW in terms of the spectrum bin width computed using an FFT when you set the RFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPE attribute to FFT Based. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_rbw_filter_type.html language=enus -->
## TOPIC 00150: RFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_rbw_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_rbw_filter_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the shape of the digital resolution bandwidth (RBW) filter. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN. Get Function: RFmxSpecAn_CHPGetRBWFilterType Set Function: RFmxSpecAn_CHPSetRBWFilterType |
| Values: | RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED (0)No RBW filtering is performed. RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN (1)An RBW filter with a Gaussian response is applied. RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_FLAT (2)An RBW filter with a flat response is applied. |
| RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |
| RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |
| RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_chp_results_carrier_relative_power.html language=enus -->
## TOPIC 00151: RFMXSPECAN_ATTR_CHP_RESULTS_CARRIER_RELATIVE_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_chp_results_carrier_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_chp_results_carrier_relative_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_CHP_RESULTS_CARRIER_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the carrier power measured relative to the total carrier power of all carriers. This value is expressed in dB. Use 'carrier(n)' as the selector string to read this result. Get Function: RFmxSpecAn_CHPGetResultsCarrierRelativePower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_all_traces_enabled.html language=enus -->
## TOPIC 00152: RFMXSPECAN_ATTR_DPD_ALL_TRACES_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_all_traces_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the DPD measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_FALSE. Get Function: RFmxSpecAn_DPDGetAllTracesEnabled Set Function: RFmxSpecAn_DPDSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_apply_dpd_cfr_enabled.html language=enus -->
## TOPIC 00153: RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_apply_dpd_cfr_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_apply_dpd_cfr_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the crest factor reduction (CFR) on the pre-distorted waveform. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_ENABLED_FALSE. Get Function: RFmxSpecAn_DPDGetApplyDPDCFREnabled Set Function: RFmxSpecAn_DPDSetApplyDPDCFREnabled |
| Values: | RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_ENABLED_FALSE (0)Disables CFR. The maximum increase in PAPR, after pre-distortion, is limited to 6 dB. RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_ENABLED_TRUE (1)Enables CFR. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_ENABLED_FALSE (0) | Disables CFR. The maximum increase in PAPR, after pre-distortion, is limited to 6 dB. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_ENABLED_TRUE (1) | Enables CFR. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_apply_dpd_lookup_table_correction_type.html language=enus -->
## TOPIC 00154: RFMXSPECAN_ATTR_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_apply_dpd_lookup_table_correction_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_apply_dpd_lookup_table_correction_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the predistortion type when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_LOOKUP_TABLE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_MAGNITUDE_AND_PHASE. Get Function: RFmxSpecAn_DPDGetApplyDPDLookupTableCorrectionType Set Function: RFmxSpecAn_DPDSetApplyDPDLookupTableCorrectionType |
| Values: | RFMXSPECAN_VAL_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_MAGNITUDE_AND_PHASE (0)The measurement predistorts the magnitude and phase of the input waveform. RFMXSPECAN_VAL_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_MAGNITUDE_ONLY (1)The measurement predistorts only the magnitude of the input waveform. RFMXSPECAN_VAL_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_PHASE_ONLY (2)The measurement predistorts only the phase of the input waveform. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_MAGNITUDE_AND_PHASE (0) | The measurement predistorts the magnitude and phase of the input waveform. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_MAGNITUDE_ONLY (1) | The measurement predistorts only the magnitude of the input waveform. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_PHASE_ONLY (2) | The measurement predistorts only the phase of the input waveform. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_frequency_offset_correction_enabled.html language=enus -->
## TOPIC 00155: RFMXSPECAN_ATTR_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_frequency_offset_correction_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_frequency_offset_correction_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable frequency offset correction for the DPD measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED_TRUE. Get Function: RFmxSpecAn_DPDGetFrequencyOffsetCorrectionEnabled Set Function: RFmxSpecAn_DPDSetFrequencyOffsetCorrectionEnabled |
| Values: | RFMXSPECAN_VAL_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED_FALSE (0)The measurement computes and corrects any frequency offset between the reference and the acquired waveforms. RFMXSPECAN_VAL_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED_TRUE (1)The measurement does not perform frequency offset correction. |
| RFMXSPECAN_VAL_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED_FALSE (0) | The measurement computes and corrects any frequency offset between the reference and the acquired waveforms. |
| RFMXSPECAN_VAL_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED_TRUE (1) | The measurement does not perform frequency offset correction. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_iq_origin_offset_correction_enabled.html language=enus -->
## TOPIC 00156: RFMXSPECAN_ATTR_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_iq_origin_offset_correction_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_iq_origin_offset_correction_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Enables the IQ origin offset correction for the measurement. When you set this attribute to True, the measurement computes and corrects any origin offset between the reference and the acquired waveforms. When you set this attribute to False, origin offset correction is not performed. The default value is RFMXSPECAN_VAL_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_TRUE. Get Function: RFmxSpecAn_DPDGetIQOriginOffsetCorrectionEnabled Set Function: RFmxSpecAn_DPDSetIQOriginOffsetCorrectionEnabled |
| Values: | RFMXSPECAN_VAL_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_FALSE (0)Disables IQ origin offset correction. RFMXSPECAN_VAL_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_TRUE (1)Enables IQ origin offset correction. |
| RFMXSPECAN_VAL_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_FALSE (0) | Disables IQ origin offset correction. |
| RFMXSPECAN_VAL_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_TRUE (1) | Enables IQ origin offset correction. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_iterative_dpd_enabled.html language=enus -->
## TOPIC 00157: RFMXSPECAN_ATTR_DPD_ITERATIVE_DPD_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_iterative_dpd_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_iterative_dpd_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_ITERATIVE_DPD_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable iterative computation of the DPD Results DPD Polynomial using indirect-learning architecture. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_ITERATIVE_DPD_ENABLED_FALSE. Get Function: RFmxSpecAn_DPDGetIterativeDPDEnabled Set Function: RFmxSpecAn_DPDSetIterativeDPDEnabled |
| Values: | RFMXSPECAN_VAL_DPD_ITERATIVE_DPD_ENABLED_FALSE (0)RFmx computes the DPD Results DPD Polynomial without considering the value of the DPD Previous DPD Polynomial. RFMXSPECAN_VAL_DPD_ITERATIVE_DPD_ENABLED_TRUE (1)RFmx computes the DPD Results DPD Polynomial based on the value of the DPD Previous DPD Polynomial. |
| RFMXSPECAN_VAL_DPD_ITERATIVE_DPD_ENABLED_FALSE (0) | RFmx computes the DPD Results DPD Polynomial without considering the value of the DPD Previous DPD Polynomial. |
| RFMXSPECAN_VAL_DPD_ITERATIVE_DPD_ENABLED_TRUE (1) | RFmx computes the DPD Results DPD Polynomial based on the value of the DPD Previous DPD Polynomial. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_lookup_table_am_to_am_curve_fit_order.html language=enus -->
## TOPIC 00158: RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_ORDER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_lookup_table_am_to_am_curve_fit_order.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_lookup_table_am_to_am_curve_fit_order.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_ORDER

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the degree of the polynomial used to approximate the device under test AM-to-AM characteristic when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_LOOKUP_TABLE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 7. Get Function: RFmxSpecAn_DPDGetLookupTableAMToAMCurveFitOrder Set Function: RFmxSpecAn_DPDSetLookupTableAMToAMCurveFitOrder |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_lookup_table_am_to_am_curve_fit_type.html language=enus -->
## TOPIC 00159: RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_lookup_table_am_to_am_curve_fit_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_lookup_table_am_to_am_curve_fit_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the polynomial approximation cost-function of the device under test AM-to-AM characteristic when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_LOOKUP_TABLE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_TYPE_LEAST_ABSOLUTE_RESIDUAL. Get Function: RFmxSpecAn_DPDGetLookupTableAMToAMCurveFitType Set Function: RFmxSpecAn_DPDSetLookupTableAMToAMCurveFitType |
| Values: | RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_TYPE_LEAST_SQUARE (0)Minimizes the energy of the polynomial approximation error. RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_TYPE_LEAST_ABSOLUTE_RESIDUAL (1)Minimizes the magnitude of the polynomial approximation error. RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_TYPE_BISQUARE (2)Excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_TYPE_LEAST_SQUARE (0) | Minimizes the energy of the polynomial approximation error. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_TYPE_LEAST_ABSOLUTE_RESIDUAL (1) | Minimizes the magnitude of the polynomial approximation error. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_TYPE_BISQUARE (2) | Excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_lookup_table_am_to_pm_curve_fit_type.html language=enus -->
## TOPIC 00160: RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_lookup_table_am_to_pm_curve_fit_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_lookup_table_am_to_pm_curve_fit_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_LOOKUP_TABLE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE_LEAST_ABSOLUTE_RESIDUAL. Get Function: RFmxSpecAn_DPDGetLookupTableAMToPMCurveFitType Set Function: RFmxSpecAn_DPDSetLookupTableAMToPMCurveFitType |
| Values: | RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE_LEAST_SQUARE (0)Minimizes the energy of the polynomial approximation error. RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE_LEAST_ABSOLUTE_RESIDUAL (1)Minimizes the magnitude of the polynomial approximation error. RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE_BISQUARE (2)Excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE_LEAST_SQUARE (0) | Minimizes the energy of the polynomial approximation error. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE_LEAST_ABSOLUTE_RESIDUAL (1) | Minimizes the magnitude of the polynomial approximation error. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE_BISQUARE (2) | Excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_lookup_table_threshold_level.html language=enus -->
## TOPIC 00161: RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_LEVEL

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_lookup_table_threshold_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_lookup_table_threshold_level.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies either the relative or absolute threshold power level based on the value of the RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_TYPE attribute. This value is expressed in dB or dBm. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is -20. Get Function: RFmxSpecAn_DPDGetLookupTableThresholdLevel Set Function: RFmxSpecAn_DPDSetLookupTableThresholdLevel |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_lookup_table_threshold_type.html language=enus -->
## TOPIC 00162: RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_lookup_table_threshold_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_lookup_table_threshold_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the reference for the power level used for thresholding. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_THRESHOLD_TYPE_RELATIVE. Get Function: RFmxSpecAn_DPDGetLookupTableThresholdType Set Function: RFmxSpecAn_DPDSetLookupTableThresholdType |
| Values: | RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_THRESHOLD_TYPE_RELATIVE (0)The threshold is relative to the peak power of the acquired samples. RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_THRESHOLD_TYPE_ABSOLUTE (1)The threshold is the absolute power, in dBm. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_THRESHOLD_TYPE_RELATIVE (0) | The threshold is relative to the peak power of the acquired samples. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_THRESHOLD_TYPE_ABSOLUTE (1) | The threshold is the absolute power, in dBm. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_measurement_enabled.html language=enus -->
## TOPIC 00163: RFMXSPECAN_ATTR_DPD_MEASUREMENT_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_measurement_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable DPD measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_FALSE. Get Function: RFmxSpecAn_DPDGetMeasurementEnabled Set Function: RFmxSpecAn_DPDSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_memory_polynomial_lag_order_type.html language=enus -->
## TOPIC 00164: RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_memory_polynomial_lag_order_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_memory_polynomial_lag_order_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Configures the type of terms of the lag order DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE_ALL_ORDERS. Get Function: RFmxSpecAn_DPDGetMemoryPolynomialLagOrderType Set Function: RFmxSpecAn_DPDSetMemoryPolynomialLagOrderType |
| Values: | RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE_ALL_ORDERS (0)The memory polynomial will compute all the terms for the given order. RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE_ODD_ORDERS_ONLY (1)The memory polynomial will compute the non-zero coefficients only for the odd terms. RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE_EVEN_ORDERS_ONLY (2)The memory polynomial will compute the non-zero coefficents only for the even terms. |
| RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE_ALL_ORDERS (0) | The memory polynomial will compute all the terms for the given order. |
| RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE_ODD_ORDERS_ONLY (1) | The memory polynomial will compute the non-zero coefficients only for the odd terms. |
| RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE_EVEN_ORDERS_ONLY (2) | The memory polynomial will compute the non-zero coefficents only for the even terms. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_memory_polynomial_maximum_lag.html language=enus -->
## TOPIC 00165: RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_MAXIMUM_LAG

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_memory_polynomial_maximum_lag.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_memory_polynomial_maximum_lag.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_MAXIMUM_LAG

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the maximum lag stagger cross term of the DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL. This term value corresponds to Mb in the equation for the generalized memory polynomial. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxSpecAn_DPDGetMemoryPolynomialMaximumLag Set Function: RFmxSpecAn_DPDSetMemoryPolynomialMaximumLag |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_memory_polynomial_order.html language=enus -->
## TOPIC 00166: RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_ORDER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_memory_polynomial_order.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_memory_polynomial_order.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_ORDER

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the order of the DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_MEMORY_POLYNOMIAL or RFMXSPECAN_VAL_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL. This order value corresponds to Ka in the equation for the generalized memory polynomial. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 3. Get Function: RFmxSpecAn_DPDGetMemoryPolynomialOrder Set Function: RFmxSpecAn_DPDSetMemoryPolynomialOrder |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_memory_polynomial_order_type.html language=enus -->
## TOPIC 00167: RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_ORDER_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_memory_polynomial_order_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_memory_polynomial_order_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_ORDER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Configures the type of terms of the DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to RFMXSPECAN_VAL_DPD_MODEL_MEMORY_POLYNOMIAL or RFMXSPECAN_VAL_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_ORDER_TYPE_ALL_ORDERS. Get Function: RFmxSpecAn_DPDGetMemoryPolynomialOrderType Set Function: RFmxSpecAn_DPDSetMemoryPolynomialOrderType |
| Values: | RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_ORDER_TYPE_ALL_ORDERS (0)The memory polynomial will compute all the terms for the given order. RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_ORDER_TYPE_ODD_ORDERS_ONLY (1)The memory polynomial will compute the non-zero coefficients only for the odd terms. RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_ORDER_TYPE_EVEN_ORDERS_ONLY (2)The memory polynomial will compute the non-zero coefficents only for the first linear term and all even terms. |
| RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_ORDER_TYPE_ALL_ORDERS (0) | The memory polynomial will compute all the terms for the given order. |
| RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_ORDER_TYPE_ODD_ORDERS_ONLY (1) | The memory polynomial will compute the non-zero coefficients only for the odd terms. |
| RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_ORDER_TYPE_EVEN_ORDERS_ONLY (2) | The memory polynomial will compute the non-zero coefficents only for the first linear term and all even terms. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_number_of_analysis_threads.html language=enus -->
## TOPIC 00168: RFMXSPECAN_ATTR_DPD_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_number_of_analysis_threads.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism of the DPD measurement. The number of threads can range from 1 to the number of physical cores. However, the number of threads you set may not all be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxSpecAn_DPDGetNumberofAnalysisThreads Set Function: RFmxSpecAn_DPDSetNumberofAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_pre_dpd_cfr_enabled.html language=enus -->
## TOPIC 00169: RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_pre_dpd_cfr_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_pre_dpd_cfr_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the crest factor reduction (CFR) when applying pre-DPD signal conditioning. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_ENABLED_FALSE. Get Function: RFmxSpecAn_DPDGetPreDPDCFREnabled Set Function: RFmxSpecAn_DPDSetPreDPDCFREnabled |
| Values: | RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_ENABLED_FALSE (0)Disables the CFR. The RFmxSpecAn_DPDApplyPreDPDSignalConditioning function returns an error when the CFR is disabled. RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_ENABLED_TRUE (1)Enables the CFR. |
| RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_ENABLED_FALSE (0) | Disables the CFR. The RFmxSpecAn_DPDApplyPreDPDSignalConditioning function returns an error when the CFR is disabled. |
| RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_ENABLED_TRUE (1) | Enables the CFR. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_signal_type.html language=enus -->
## TOPIC 00170: RFMXSPECAN_ATTR_DPD_SIGNAL_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_signal_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_signal_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_SIGNAL_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals. To time-align the sinusoidal reference waveform to the acquired signal, set the RFMXSPECAN_ATTR_DPD_SIGNAL_TYPE attribute to Tones, which switches the DPD measurement alignment algorithm. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_SIGNAL_TYPE_MODULATED. Get Function: RFmxSpecAn_DPDGetSignalType Set Function: RFmxSpecAn_DPDSetSignalType |
| Values: | RFMXSPECAN_VAL_DPD_SIGNAL_TYPE_MODULATED (0)The reference waveform is a cellular or connectivity standard signal. RFMXSPECAN_VAL_DPD_SIGNAL_TYPE_TONES (1)The reference waveform is a continuous signal comprising one or more tones. |
| RFMXSPECAN_VAL_DPD_SIGNAL_TYPE_MODULATED (0) | The reference waveform is a cellular or connectivity standard signal. |
| RFMXSPECAN_VAL_DPD_SIGNAL_TYPE_TONES (1) | The reference waveform is a continuous signal comprising one or more tones. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_dpd_target_gain_type.html language=enus -->
## TOPIC 00171: RFMXSPECAN_ATTR_DPD_TARGET_GAIN_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_dpd_target_gain_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_dpd_target_gain_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_DPD_TARGET_GAIN_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the gain expected from the DUT after applying DPD on the input waveform. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_DPD_TARGET_GAIN_TYPE_AVERAGE_GAIN. Get Function: RFmxSpecAn_DPDGetTargetGainType Set Function: RFmxSpecAn_DPDSetTargetGainType |
| Values: | RFMXSPECAN_VAL_DPD_TARGET_GAIN_TYPE_AVERAGE_GAIN (0)The DPD polynomial or lookup table is computed by assuming that the linearized gain expected from the DUT after applying DPD on the input waveform is equal to the average power gain provided by the DUT without DPD. RFMXSPECAN_VAL_DPD_TARGET_GAIN_TYPE_LINEAR_REGION_GAIN (1)The DPD polynomial or lookup table is computed by assuming that the linearized gain expected from the DUT after applying DPD on the input waveform is equal to the gain provided by the DUT, without DPD, to the parts of the reference waveform that do not drive the DUT into non-linear gain-expansion or compression regions of its input-output characteristics. The measurement computes the linear region gain as the average gain experienced by the parts of the reference waveform that are below a threshold which is computed as shown in the following equation: Linear region threshold (dBm) = Max {-25, Min {reference waveform power} + 6, DUT Average Input Power -15} RFMXSPECAN_VAL_DPD_TARGET_GAIN_TYPE_PEAK_INPUT_POWER_GAIN (2)The DPD polynomial or lookup table is computed by assuming that the linearized gain expected from the DUT after applying DPD on the input waveform is equal to the average power gain provided by the DUT, without DPD, to all the samples of the reference waveform for which the magnitude is greater than the peak power in the reference waveform (dBm) - 0.5dB. |
| RFMXSPECAN_VAL_DPD_TARGET_GAIN_TYPE_AVERAGE_GAIN (0) | The DPD polynomial or lookup table is computed by assuming that the linearized gain expected from the DUT after applying DPD on the input waveform is equal to the average power gain provided by the DUT without DPD. |
| RFMXSPECAN_VAL_DPD_TARGET_GAIN_TYPE_LINEAR_REGION_GAIN (1) | The DPD polynomial or lookup table is computed by assuming that the linearized gain expected from the DUT after applying DPD on the input waveform is equal to the gain provided by the DUT, without DPD, to the parts of the reference waveform that do not drive the DUT into non-linear gain-expansion or compression regions of its input-output characteristics. The measurement computes the linear region gain as the average gain experienced by the parts of the reference waveform that are below a threshold which is computed as shown in the following equation: Linear region threshold (dBm) = Max {-25, Min {reference waveform power} + 6, DUT Average Input Power -15} |
| RFMXSPECAN_VAL_DPD_TARGET_GAIN_TYPE_PEAK_INPUT_POWER_GAIN (2) | The DPD polynomial or lookup table is computed by assuming that the linearized gain expected from the DUT after applying DPD on the input waveform is equal to the average power gain provided by the DUT, without DPD, to all the samples of the reference waveform for which the magnitude is greater than the peak power in the reference waveform (dBm) - 0.5dB. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_fcnt_number_of_analysis_threads.html language=enus -->
## TOPIC 00172: RFMXSPECAN_ATTR_FCNT_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_fcnt_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_fcnt_number_of_analysis_threads.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_FCNT_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for FCnt measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxSpecAn_FCntGetNumberOfAnalysisThreads Set Function: RFmxSpecAn_FCntSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_fcnt_rbw_filter_type.html language=enus -->
## TOPIC 00173: RFMXSPECAN_ATTR_FCNT_RBW_FILTER_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_fcnt_rbw_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_fcnt_rbw_filter_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_FCNT_RBW_FILTER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the shape of the digital resolution bandwidth (RBW) filter. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_NONE. Get Function: RFmxSpecAn_FCntGetRBWFilterType Set Function: RFmxSpecAn_FCntSetRBWFilterType |
| Values: | RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_NONE (5)The measurement does not use any RBW filtering. RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_GAUSSIAN (1)The RBW filter has a Gaussian response. RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_FLAT (2)The RBW filter has a flat response. RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_RRC (6)The RRC filter with the roll-off specified by RFMXSPECAN_ATTR_FCNT_RBW_FILTER_RRC_ALPHA attribute is used as the RBW filter. |
| RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_NONE (5) | The measurement does not use any RBW filtering. |
| RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_GAUSSIAN (1) | The RBW filter has a Gaussian response. |
| RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_FLAT (2) | The RBW filter has a flat response. |
| RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_RRC (6) | The RRC filter with the roll-off specified by RFMXSPECAN_ATTR_FCNT_RBW_FILTER_RRC_ALPHA attribute is used as the RBW filter. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_averaging_type.html language=enus -->
## TOPIC 00174: RFMXSPECAN_ATTR_HARM_AVERAGING_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_averaging_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the averaging type for the Harmonics measurement. The averaged power trace is used for the measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_RMS. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668 Get Function: RFmxSpecAn_HarmGetAveragingType Set Function: RFmxSpecAn_HarmSetAveragingType |
| Values: | RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_RMS (0)The power trace is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_LOG (1)The power trace is averaged in a logarithmic scale. RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_SCALAR (2)The square root of the power trace is averaged. RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_MAXIMUM (3)The maximum instantaneous power in the power trace is retained from one acquisition to the next. RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_MINIMUM (4)The minimum instantaneous power in the power trace is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_RMS (0) | The power trace is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_LOG (1) | The power trace is averaged in a logarithmic scale. |
| RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_SCALAR (2) | The square root of the power trace is averaged. |
| RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_MAXIMUM (3) | The maximum instantaneous power in the power trace is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_HARM_AVERAGING_TYPE_MINIMUM (4) | The minimum instantaneous power in the power trace is retained from one acquisition to the next. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_fundamental_measurement_interval.html language=enus -->
## TOPIC 00175: RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_MEASUREMENT_INTERVAL

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_fundamental_measurement_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_fundamental_measurement_interval.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_MEASUREMENT_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the acquisition time for the Harmonics measurement of the fundamental signal. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.001. Supported devices: PXIe-5665/5668 Get Function: RFmxSpecAn_HarmGetFundamentalMeasurementInterval Set Function: RFmxSpecAn_HarmSetFundamentalMeasurementInterval |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_fundamental_rbw_filter_alpha.html language=enus -->
## TOPIC 00176: RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_ALPHA

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_fundamental_rbw_filter_alpha.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_fundamental_rbw_filter_alpha.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_ALPHA

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.1. Supported devices: PXIe-5665/5668 Get Function: RFmxSpecAn_HarmGetFundamentalRBWFilterAlpha Set Function: RFmxSpecAn_HarmSetFundamentalRBWFilterAlpha |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_fundamental_rbw_filter_type.html language=enus -->
## TOPIC 00177: RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_fundamental_rbw_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_fundamental_rbw_filter_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the shape of the digital resolution bandwidth (RBW) filter. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_HARM_RBW_FILTER_TYPE_GAUSSIAN. Supported devices: PXIe-5665/5668 Get Function: RFmxSpecAn_HarmGetFundamentalRBWFilterType Set Function: RFmxSpecAn_HarmSetFundamentalRBWFilterType |
| Values: | RFMXSPECAN_VAL_HARM_RBW_FILTER_TYPE_NONE (5)The measurement does not use any RBW filtering. RFMXSPECAN_VAL_HARM_RBW_FILTER_TYPE_GAUSSIAN (1)The RBW filter has a Gaussian response. RFMXSPECAN_VAL_HARM_RBW_FILTER_TYPE_FLAT (2)The RBW filter has a flat response. RFMXSPECAN_VAL_HARM_RBW_FILTER_TYPE_RRC (6)The RRC filter with the roll-off specified by the RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_ALPHA attribute is used as the RBW filter. |
| RFMXSPECAN_VAL_HARM_RBW_FILTER_TYPE_NONE (5) | The measurement does not use any RBW filtering. |
| RFMXSPECAN_VAL_HARM_RBW_FILTER_TYPE_GAUSSIAN (1) | The RBW filter has a Gaussian response. |
| RFMXSPECAN_VAL_HARM_RBW_FILTER_TYPE_FLAT (2) | The RBW filter has a flat response. |
| RFMXSPECAN_VAL_HARM_RBW_FILTER_TYPE_RRC (6) | The RRC filter with the roll-off specified by the RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_ALPHA attribute is used as the RBW filter. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_harmonic_enabled.html language=enus -->
## TOPIC 00178: RFMXSPECAN_ATTR_HARM_HARMONIC_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_harmonic_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_harmonic_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_HARMONIC_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable a particular harmonic for measurement. Only the enabled harmonics are used to measure the total harmonic distortion (THD). This attribute is not used if you set the RFMXSPECAN_ATTR_HARM_AUTO_SETUP_ENABLED to RFMXSPECAN_VAL_HARM_AUTO_HARMONICS_SETUP_ENABLED_TRUE. Use 'harmonic(n)' as the selector string to configure or read this attribute. The default value is RFMXSPECAN_VAL_HARM_HARMONIC_ENABLED_TRUE. Supported devices: PXIe-5665/5668 Get Function: RFmxSpecAn_HarmGetHarmonicEnabled Set Function: RFmxSpecAn_HarmSetHarmonicEnabled |
| Values: | RFMXSPECAN_VAL_HARM_HARMONIC_ENABLED_FALSE (0)Disables the harmonic for measurement. RFMXSPECAN_VAL_HARM_HARMONIC_ENABLED_TRUE (1)Enables the harmonic for measurement. |
| RFMXSPECAN_VAL_HARM_HARMONIC_ENABLED_FALSE (0) | Disables the harmonic for measurement. |
| RFMXSPECAN_VAL_HARM_HARMONIC_ENABLED_TRUE (1) | Enables the harmonic for measurement. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_harmonic_measurement_interval.html language=enus -->
## TOPIC 00179: RFMXSPECAN_ATTR_HARM_HARMONIC_MEASUREMENT_INTERVAL

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_harmonic_measurement_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_harmonic_measurement_interval.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_HARMONIC_MEASUREMENT_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the acquisition time for the harmonic. This value is expressed in seconds. This attribute is not used if you set the RFMXSPECAN_ATTR_HARM_AUTO_SETUP_ENABLED to RFMXSPECAN_VAL_HARM_AUTO_HARMONICS_SETUP_ENABLED_TRUE. Use 'harmonic(n)' as the selector string to configure or read this attribute. The default value is 1 ms. Supported devices: PXIe-5665/5668 Get Function: RFmxSpecAn_HarmGetHarmonicMeasurementInterval Set Function: RFmxSpecAn_HarmSetHarmonicMeasurementInterval |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_noise_compensation_enabled.html language=enus -->
## TOPIC 00180: RFMXSPECAN_ATTR_HARM_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_noise_compensation_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_NOISE_COMPENSATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_HARM_NOISE_COMPENSATION_ENABLED_FALSE. Get Function: RFmxSpecAn_HarmGetNoiseCompensationEnabled Set Function: RFmxSpecAn_HarmSetNoiseCompensationEnabled |
| Values: | RFMXSPECAN_VAL_HARM_NOISE_COMPENSATION_ENABLED_FALSE (0)Disables compensation of the average harmonic powers for the noise floor of the signal analyzer. RFMXSPECAN_VAL_HARM_NOISE_COMPENSATION_ENABLED_TRUE (1)Enables compensation of the average harmonic powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the harmonics measurement and cached for future use. If the signal analyzer or measurement parameters change, noise floors are measured again. Supported devices: PXIe-5663/5665/5668 |
| RFMXSPECAN_VAL_HARM_NOISE_COMPENSATION_ENABLED_FALSE (0) | Disables compensation of the average harmonic powers for the noise floor of the signal analyzer. |
| RFMXSPECAN_VAL_HARM_NOISE_COMPENSATION_ENABLED_TRUE (1) | Enables compensation of the average harmonic powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the harmonics measurement and cached for future use. If the signal analyzer or measurement parameters change, noise floors are measured again. Supported devices: PXIe-5663/5665/5668 |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_number_of_analysis_threads.html language=enus -->
## TOPIC 00181: RFMXSPECAN_ATTR_HARM_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_number_of_analysis_threads.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for Harmonics measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Supported devices: PXIe-5665/5668 Get Function: RFmxSpecAn_HarmGetNumberOfAnalysisThreads Set Function: RFmxSpecAn_HarmSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_number_of_harmonics.html language=enus -->
## TOPIC 00182: RFMXSPECAN_ATTR_HARM_NUMBER_OF_HARMONICS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_number_of_harmonics.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_number_of_harmonics.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_NUMBER_OF_HARMONICS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the number of harmonics, including fundamental, to measure. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 3. Supported devices: PXIe-5665/5668 Get Function: RFmxSpecAn_HarmGetNumberOfHarmonics Set Function: RFmxSpecAn_HarmSetNumberOfHarmonics |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_results_average_fundamental_power.html language=enus -->
## TOPIC 00183: RFMXSPECAN_ATTR_HARM_RESULTS_AVERAGE_FUNDAMENTAL_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_results_average_fundamental_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_results_average_fundamental_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_RESULTS_AVERAGE_FUNDAMENTAL_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the average power measured at the fundamental frequency. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_HarmGetResultsAverageFundamentalPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_results_harmonic_average_absolute_power.html language=enus -->
## TOPIC 00184: RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_ABSOLUTE_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_results_harmonic_average_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_results_harmonic_average_absolute_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the average absolute power measured at the harmonic specified by the selector string. This value is expressed in dBm. Use 'harmonic(n)' as the selector string to read this result. Get Function: RFmxSpecAn_HarmGetResultsHarmonicAverageAbsolutePower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_results_harmonic_average_relative_power.html language=enus -->
## TOPIC 00185: RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_RELATIVE_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_results_harmonic_average_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_results_harmonic_average_relative_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the average power relative to the fundamental power measured at the harmonic specified by the selector string. This value is expressed in dB. Use 'harmonic(n)' as the selector string to read this result. Get Function: RFmxSpecAn_HarmGetResultsHarmonicAverageRelativePower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_results_harmonic_frequency.html language=enus -->
## TOPIC 00186: RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_results_harmonic_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_results_harmonic_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the RF frequency of the harmonic. This value is expressed in Hz. Use 'harmonic(n)' as the selector string to read this result. Get Function: RFmxSpecAn_HarmGetResultsHarmonicFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_harm_results_harmonic_rbw.html language=enus -->
## TOPIC 00187: RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_RBW

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_harm_results_harmonic_rbw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_harm_results_harmonic_rbw.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_RBW

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the resolution bandwidth (RBW) which is used by the harmonic measurement, for the harmonic specified by the selector string. This value is expressed in Hz. Use 'harmonic(n)' as the selector string to read this result. Get Function: RFmxSpecAn_HarmGetResultsHarmonicRBW |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_idpd_dut_average_input_power.html language=enus -->
## TOPIC 00188: RFMXSPECAN_ATTR_IDPD_DUT_AVERAGE_INPUT_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_idpd_dut_average_input_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_idpd_dut_average_input_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IDPD_DUT_AVERAGE_INPUT_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the initial (first itertion) average power of the signal at the input port of the device under test. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is -20. Get Function: RFmxSpecAn_IDPDGetDUTAverageInputPower Set Function: RFmxSpecAn_IDPDSetDUTAverageInputPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_idpd_equalizer_filter_length.html language=enus -->
## TOPIC 00189: RFMXSPECAN_ATTR_IDPD_EQUALIZER_FILTER_LENGTH

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_idpd_equalizer_filter_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_idpd_equalizer_filter_length.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IDPD_EQUALIZER_FILTER_LENGTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the length of the equalizer filter to be trained. This attribute is applicable when you set RFMXSPECAN_ATTR_IDPD_EQUALIZER_MODE to RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_TRAIN. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 101.Valid values are 1 to 4096, inclusive. Get Function: RFmxSpecAn_IDPDGetEqualizerFilterLength Set Function: RFmxSpecAn_IDPDSetEqualizerFilterLength |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_idpd_equalizer_mode.html language=enus -->
## TOPIC 00190: RFMXSPECAN_ATTR_IDPD_EQUALIZER_MODE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_idpd_equalizer_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_idpd_equalizer_mode.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IDPD_EQUALIZER_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable equalization. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_OFF. Get Function: RFmxSpecAn_IDPDGetEqualizerMode Set Function: RFmxSpecAn_IDPDSetEqualizerMode |
| Values: | RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_OFF (0)Equalization filter is not applied. RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_TRAIN (1)Train Equalization filter. The filter length is obtained from the IDPD Equalizer Filter Length attribute. RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_HOLD (2)The RFmxSpecAn_IDPDCfgEqualizerCoefficients function specifies the filter that acts as the equalization filter. This filter is applied prior to calculating the predistorted waveform. |
| RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_OFF (0) | Equalization filter is not applied. |
| RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_TRAIN (1) | Train Equalization filter. The filter length is obtained from the IDPD Equalizer Filter Length attribute. |
| RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_HOLD (2) | The RFmxSpecAn_IDPDCfgEqualizerCoefficients function specifies the filter that acts as the equalization filter. This filter is applied prior to calculating the predistorted waveform. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_idpd_evm_enabled.html language=enus -->
## TOPIC 00191: RFMXSPECAN_ATTR_IDPD_EVM_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_idpd_evm_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_idpd_evm_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IDPD_EVM_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable EVM computation. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_IDPD_EVM_ENABLED_FALSE. Get Function: RFmxSpecAn_IDPDGetEVMEnabled Set Function: RFmxSpecAn_IDPDSetEVMEnabled |
| Values: | RFMXSPECAN_VAL_IDPD_EVM_ENABLED_FALSE (0)Disables EVM computation. NaN is returned for Mean RMS EVM. RFMXSPECAN_VAL_IDPD_EVM_ENABLED_TRUE (1)Enables EVM computation. |
| RFMXSPECAN_VAL_IDPD_EVM_ENABLED_FALSE (0) | Disables EVM computation. NaN is returned for Mean RMS EVM. |
| RFMXSPECAN_VAL_IDPD_EVM_ENABLED_TRUE (1) | Enables EVM computation. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_idpd_gain_expansion.html language=enus -->
## TOPIC 00192: RFMXSPECAN_ATTR_IDPD_GAIN_EXPANSION

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_idpd_gain_expansion.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_idpd_gain_expansion.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IDPD_GAIN_EXPANSION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the increase of input power relative to the peak power value of the reference signal. This value is expressed in dB. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 6. Get Function: RFmxSpecAn_IDPDGetGainExpansion Set Function: RFmxSpecAn_IDPDSetGainExpansion |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_idpd_measurement_sample_rate_mode.html language=enus -->
## TOPIC 00193: RFMXSPECAN_ATTR_IDPD_MEASUREMENT_SAMPLE_RATE_MODE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_idpd_measurement_sample_rate_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_idpd_measurement_sample_rate_mode.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IDPD_MEASUREMENT_SAMPLE_RATE_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies acquisition sample rate configuration mode. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_IDPD_MEASUREMENT_SAMPLE_RATE_MODE_REFERENCE_WAVEFORM. Get Function: RFmxSpecAn_IDPDGetMeasurementSampleRateMode Set Function: RFmxSpecAn_IDPDSetMeasurementSampleRateMode |
| Values: | RFMXSPECAN_VAL_IDPD_MEASUREMENT_SAMPLE_RATE_MODE_USER (0)Acquisition sample rate is defined by the RFMXSPECAN_ATTR_IDPD_MEASUREMENT_SAMPLE_RATE. RFMXSPECAN_VAL_IDPD_MEASUREMENT_SAMPLE_RATE_MODE_REFERENCE_WAVEFORM (1) Acquisition sample rate is set to match the sample rate of the reference waveform. |
| RFMXSPECAN_VAL_IDPD_MEASUREMENT_SAMPLE_RATE_MODE_USER (0) | Acquisition sample rate is defined by the RFMXSPECAN_ATTR_IDPD_MEASUREMENT_SAMPLE_RATE. |
| RFMXSPECAN_VAL_IDPD_MEASUREMENT_SAMPLE_RATE_MODE_REFERENCE_WAVEFORM (1) | Acquisition sample rate is set to match the sample rate of the reference waveform. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_idpd_reference_waveform_idle_duration_present.html language=enus -->
## TOPIC 00194: RFMXSPECAN_ATTR_IDPD_REFERENCE_WAVEFORM_IDLE_DURATION_PRESENT

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_idpd_reference_waveform_idle_duration_present.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_idpd_reference_waveform_idle_duration_present.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IDPD_REFERENCE_WAVEFORM_IDLE_DURATION_PRESENT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the reference waveform contains idle duration or dead time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_IDPD_REFERENCE_WAVEFORM_IDLE_DURATION_PRESENT_FALSE. Get Function: RFmxSpecAn_IDPDGetReferenceWaveformIdleDurationPresent Set Function: RFmxSpecAn_IDPDSetReferenceWaveformIdleDurationPresent |
| Values: | RFMXSPECAN_VAL_IDPD_REFERENCE_WAVEFORM_IDLE_DURATION_PRESENT_FALSE (0)Reference waveform has no idle duration. RFMXSPECAN_VAL_IDPD_REFERENCE_WAVEFORM_IDLE_DURATION_PRESENT_TRUE (1)Reference waveform contains idle duration. |
| RFMXSPECAN_VAL_IDPD_REFERENCE_WAVEFORM_IDLE_DURATION_PRESENT_FALSE (0) | Reference waveform has no idle duration. |
| RFMXSPECAN_VAL_IDPD_REFERENCE_WAVEFORM_IDLE_DURATION_PRESENT_TRUE (1) | Reference waveform contains idle duration. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_idpd_synchronization_estimation_stop.html language=enus -->
## TOPIC 00195: RFMXSPECAN_ATTR_IDPD_SYNCHRONIZATION_ESTIMATION_STOP

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_idpd_synchronization_estimation_stop.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_idpd_synchronization_estimation_stop.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IDPD_SYNCHRONIZATION_ESTIMATION_STOP

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the stop time of the synchronization estimation interval relative to the start of the reference waveform. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.001. Get Function: RFmxSpecAn_IDPDGetSynchronizationEstimationStop Set Function: RFmxSpecAn_IDPDSetSynchronizationEstimationStop |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_im_all_traces_enabled.html language=enus -->
## TOPIC 00196: RFMXSPECAN_ATTR_IM_ALL_TRACES_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_im_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_im_all_traces_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IM_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the IM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_FALSE. Get Function: RFmxSpecAn_IMGetAllTracesEnabled Set Function: RFmxSpecAn_IMSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_im_rbw_filter_type.html language=enus -->
## TOPIC 00197: RFMXSPECAN_ATTR_IM_RBW_FILTER_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_im_rbw_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_im_rbw_filter_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IM_RBW_FILTER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the response of the digital RBW filter. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_IM_RBW_FILTER_TYPE_GAUSSIAN. Get Function: RFmxSpecAn_IMGetRBWFilterType Set Function: RFmxSpecAn_IMSetRBWFilterType |
| Values: | RFMXSPECAN_VAL_IM_RBW_FILTER_TYPE_FFT_BASED (0)No RBW filtering is performed. RFMXSPECAN_VAL_IM_RBW_FILTER_TYPE_GAUSSIAN (1)An RBW filter with a Gaussian response is applied. RFMXSPECAN_VAL_IM_RBW_FILTER_TYPE_FLAT (2)An RBW filter with a flat response is applied. |
| RFMXSPECAN_VAL_IM_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |
| RFMXSPECAN_VAL_IM_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |
| RFMXSPECAN_VAL_IM_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_im_results_lower_intermod_power.html language=enus -->
## TOPIC 00198: RFMXSPECAN_ATTR_IM_RESULTS_LOWER_INTERMOD_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_im_results_lower_intermod_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_im_results_lower_intermod_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IM_RESULTS_LOWER_INTERMOD_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the peak power measured around the lower intermod frequency when you set the RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED attribute to RFMXSPECAN_VAL_IM_LOCAL_PEAK_SEARCH_ENABLED_TRUE. This value is expressed in dBm. When you set the RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED attribute to RFMXSPECAN_VAL_IM_LOCAL_PEAK_SEARCH_ENABLED_FALSE, the measurement returns the power at the lower intermod frequency. Use 'intermod(n)' as the selector string to read this result. Get Function: RFmxSpecAn_IMGetResultsLowerIntermodPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_im_results_upper_intermod_power.html language=enus -->
## TOPIC 00199: RFMXSPECAN_ATTR_IM_RESULTS_UPPER_INTERMOD_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_im_results_upper_intermod_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_im_results_upper_intermod_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IM_RESULTS_UPPER_INTERMOD_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the peak power measured around the upper intermod frequency when you set the RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED attribute to RFMXSPECAN_VAL_IM_LOCAL_PEAK_SEARCH_ENABLED_TRUE. This value is expressed in dBm. When you set the RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED attribute to RFMXSPECAN_VAL_IM_LOCAL_PEAK_SEARCH_ENABLED_FALSE, the measurement returns the power at the upper intermod frequency. Use 'intermod(n)' as the selector string to read this result. Get Function: RFmxSpecAn_IMGetResultsUpperIntermodPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_im_results_upper_tone_power.html language=enus -->
## TOPIC 00200: RFMXSPECAN_ATTR_IM_RESULTS_UPPER_TONE_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_im_results_upper_tone_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_im_results_upper_tone_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IM_RESULTS_UPPER_TONE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the peak power measured around the upper tone frequency when you set the RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED attribute to RFMXSPECAN_VAL_IM_LOCAL_PEAK_SEARCH_ENABLED_TRUE. This value is expressed in dBm. When you set the RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED attribute to RFMXSPECAN_VAL_IM_LOCAL_PEAK_SEARCH_ENABLED_FALSE, the measurement returns the power at the upper tone frequency. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_IMGetResultsFundamentalUpperTonePower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_im_sweep_time_auto.html language=enus -->
## TOPIC 00201: RFMXSPECAN_ATTR_IM_SWEEP_TIME_AUTO

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_im_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_im_sweep_time_auto.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IM_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_IM_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxSpecAn_IMGetSweepTimeAuto Set Function: RFmxSpecAn_IMSetSweepTimeAuto |
| Values: | RFMXSPECAN_VAL_IM_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_IM_SWEEP_TIME_INTERVAL attribute. RFMXSPECAN_VAL_IM_SWEEP_TIME_AUTO_TRUE (1)The measurement computes the sweep time based on the value of the RFMXSPECAN_ATTR_IM_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_VAL_IM_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_IM_SWEEP_TIME_INTERVAL attribute. |
| RFMXSPECAN_VAL_IM_SWEEP_TIME_AUTO_TRUE (1) | The measurement computes the sweep time based on the value of the RFMXSPECAN_ATTR_IM_RBW_FILTER_BANDWIDTH attribute. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_im_upper_intermod_frequency.html language=enus -->
## TOPIC 00202: RFMXSPECAN_ATTR_IM_UPPER_INTERMOD_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_im_upper_intermod_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_im_upper_intermod_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IM_UPPER_INTERMOD_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the frequency of the upper intermodulation product. This value is expressed in Hz. This attribute is not used when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to RFMXSPECAN_VAL_IM_AUTO_INTERMODS_SETUP_ENABLED_TRUE. Use 'intermod(n)' as the selector string to configure or read this attribute. The default value is 3 MHz. Get Function: RFmxSpecAn_IMGetUpperIntermodFrequency Set Function: RFmxSpecAn_IMSetUpperIntermodFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_iq_acquisition_time.html language=enus -->
## TOPIC 00203: RFMXSPECAN_ATTR_IQ_ACQUISITION_TIME

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_iq_acquisition_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_iq_acquisition_time.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IQ_ACQUISITION_TIME

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the acquisition time for the I/Q measurement. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.001. Get Function: RFmxSpecAn_IQGetAcquisitionTime Set Function: RFmxSpecAn_IQSetAcquisitionTime |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_iq_bandwidth.html language=enus -->
## TOPIC 00204: RFMXSPECAN_ATTR_IQ_BANDWIDTH

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_iq_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_iq_bandwidth.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IQ_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the minimum acquisition bandwidth when you set the RFMXSPECAN_ATTR_IQ_BANDWIDTH_AUTO attribute to RFMXSPECAN_VAL_IQ_AUTO_BANDWIDTH_FALSE. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1 MHz. Get Function: RFmxSpecAn_IQGetBandwidth Set Function: RFmxSpecAn_IQSetBandwidth |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_iq_delete_record_on_fetch.html language=enus -->
## TOPIC 00205: RFMXSPECAN_ATTR_IQ_DELETE_RECORD_ON_FETCH

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_iq_delete_record_on_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_iq_delete_record_on_fetch.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IQ_DELETE_RECORD_ON_FETCH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the measurement deletes the fetched record. The default value is RFMXSPECAN_VAL_IQ_DELETE_RECORD_ON_FETCH_TRUE. Get Function: RFmxSpecAn_IQGetDeleteRecordOnFetch Set Function: RFmxSpecAn_IQSetDeleteRecordOnFetch |
| Values: | RFMXSPECAN_VAL_IQ_DELETE_RECORD_ON_FETCH_FALSE (0)The measurement does not delete the fetched record. RFMXSPECAN_VAL_IQ_DELETE_RECORD_ON_FETCH_TRUE (1)The measurement deletes the fetched record. |
| RFMXSPECAN_VAL_IQ_DELETE_RECORD_ON_FETCH_FALSE (0) | The measurement does not delete the fetched record. |
| RFMXSPECAN_VAL_IQ_DELETE_RECORD_ON_FETCH_TRUE (1) | The measurement deletes the fetched record. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_iq_power_edge_trigger_slope.html language=enus -->
## TOPIC 00206: RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_iq_power_edge_trigger_slope.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_iq_power_edge_trigger_slope.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This attribute is used only when you set the RFMXSPECAN_ATTR_TRIGGER_TYPE attribute to RFMXSPECAN_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Rising Slope. Get Function: RFmxSpecAn_GetIQPowerEdgeTriggerSlope Set Function: RFmxSpecAn_SetIQPowerEdgeTriggerSlope |
| Values: | RFMXSPECAN_VAL_IQ_POWER_EDGE_RISING_SLOPE (0)The trigger asserts when the signal power is rising. RFMXSPECAN_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1)The trigger asserts when the signal power is falling. |
| RFMXSPECAN_VAL_IQ_POWER_EDGE_RISING_SLOPE (0) | The trigger asserts when the signal power is rising. |
| RFMXSPECAN_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1) | The trigger asserts when the signal power is falling. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_iq_sample_rate.html language=enus -->
## TOPIC 00207: RFMXSPECAN_ATTR_IQ_SAMPLE_RATE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_iq_sample_rate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_iq_sample_rate.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_IQ_SAMPLE_RATE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the acquisition sample rate. This value is expressed in samples per second (S/s). You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 50 MS/s. Get Function: RFmxSpecAn_IQGetSampleRate Set Function: RFmxSpecAn_IQSetSampleRate |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_calibration_loss_temperature.html language=enus -->
## TOPIC 00208: RFMXSPECAN_ATTR_NF_CALIBRATION_LOSS_TEMPERATURE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_calibration_loss_temperature.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_calibration_loss_temperature.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_CALIBRATION_LOSS_TEMPERATURE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the physical temperature of the ohmic loss elements specified by the RFMXSPECAN_ATTR_NF_CALIBRATION_LOSS attribute. This value is expressed in kelvin. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 297. Get Function: RFmxSpecAn_NFGetCalibrationLossTemperature Set Function: RFmxSpecAn_NFSetCalibrationLossTemperature |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_calibration_setup_id.html language=enus -->
## TOPIC 00209: RFMXSPECAN_ATTR_NF_CALIBRATION_SETUP_ID

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_calibration_setup_id.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_calibration_setup_id.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_CALIBRATION_SETUP_ID

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeStringRFmxSpecAn_GetAttributeString |
| Description: | Associates a unique string identifier with the hardware setup used to perform calibration for the NF measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is an empty string. Get Function: RFmxSpecAn_NFGetCalibrationSetupId Set Function: RFmxSpecAn_NFSetCalibrationSetupId |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_cold_source_dut_s_parameters_frequency.html language=enus -->
## TOPIC 00210: RFMXSPECAN_ATTR_NF_COLD_SOURCE_DUT_S_PARAMETERS_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_cold_source_dut_s_parameters_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_cold_source_dut_s_parameters_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_COLD_SOURCE_DUT_S_PARAMETERS_FREQUENCY

| Data Type: | float64 [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64ArrayRFmxSpecAn_GetAttributeF64Array |
| Description: | Specifies an array of frequencies corresponding to the s-parameters of the DUT specified by the RFMXSPECAN_ATTR_NF_COLD_SOURCE_DUT_S21, RFMXSPECAN_ATTR_NF_COLD_SOURCE_DUT_S12, RFMXSPECAN_ATTR_NF_COLD_SOURCE_DUT_S11, and RFMXSPECAN_ATTR_NF_COLD_SOURCE_DUT_S22 attributes. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is an empty array. Get Function: RFmxSpecAn_NFGetColdSourceDUTSParametersFrequency Set Function: RFmxSpecAn_NFSetColdSourceDUTSParametersFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_cold_source_mode.html language=enus -->
## TOPIC 00211: RFMXSPECAN_ATTR_NF_COLD_SOURCE_MODE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_cold_source_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_cold_source_mode.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_COLD_SOURCE_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT for the cold source method. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_NF_COLD_SOURCE_MODE_MEASURE. Get Function: RFmxSpecAn_NFGetColdSourceMode Set Function: RFmxSpecAn_NFSetColdSourceMode |
| Values: | RFMXSPECAN_VAL_NF_COLD_SOURCE_MODE_MEASURE (0)The noise figure (NF) measurement computes the noise characteristics of the DUT and compensates for the noise figure of the analyzer. RFMXSPECAN_VAL_NF_COLD_SOURCE_MODE_CALIBRATE (1)The NF measurement computes the noise characteristics of the analyzer. |
| RFMXSPECAN_VAL_NF_COLD_SOURCE_MODE_MEASURE (0) | The noise figure (NF) measurement computes the noise characteristics of the DUT and compensates for the noise figure of the analyzer. |
| RFMXSPECAN_VAL_NF_COLD_SOURCE_MODE_CALIBRATE (1) | The NF measurement computes the noise characteristics of the analyzer. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_dut_input_loss.html language=enus -->
## TOPIC 00212: RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_dut_input_loss.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_dut_input_loss.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS

| Data Type: | float64 [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64ArrayRFmxSpecAn_GetAttributeF64Array |
| Description: | Specifies an array of the ohmic losses between the noise source and the input port of the DUT, as a function of the frequency. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS_COMPENSATION_ENABLED attribute to RFMXSPECAN_VAL_NF_DUT_INPUT_LOSS_COMPENSATION_ENABLED_TRUE. You must exclude any loss which is inherent to the noise source and is common between the calibration and measurement steps, and configure the loss using the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS attribute. Specify the frequencies at which the losses were measured using the RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS_FREQUENCY attribute. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is an empty array. Get Function: RFmxSpecAn_NFGetDUTInputLoss Set Function: RFmxSpecAn_NFSetDUTInputLoss |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_dut_input_loss_frequency.html language=enus -->
## TOPIC 00213: RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_dut_input_loss_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_dut_input_loss_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS_FREQUENCY

| Data Type: | float64 [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64ArrayRFmxSpecAn_GetAttributeF64Array |
| Description: | Specifies an array of frequencies corresponding to the value of the RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS attribute. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is an empty array. Get Function: RFmxSpecAn_NFGetDUTInputLossFrequency Set Function: RFmxSpecAn_NFSetDUTInputLossFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_dut_output_loss.html language=enus -->
## TOPIC 00214: RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_dut_output_loss.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_dut_output_loss.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS

| Data Type: | float64 [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64ArrayRFmxSpecAn_GetAttributeF64Array |
| Description: | Specifies the array of ohmic losses between the output port of the DUT and the input port of the analyzer, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measurement when you set the RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED attribute to RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_TRUE. Specify the array of frequencies at which the losses were measured using the RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_FREQUENCY attribute. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is an empty array. Get Function: RFmxSpecAn_NFGetDUTOutputLoss Set Function: RFmxSpecAn_NFSetDUTOutputLoss |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_dut_output_loss_compensation_enabled.html language=enus -->
## TOPIC 00215: RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_dut_output_loss_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_dut_output_loss_compensation_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_FALSE. Get Function: RFmxSpecAn_NFGetDUTOutputLossCompensationEnabled Set Function: RFmxSpecAn_NFSetDUTOutputLossCompensationEnabled |
| Values: | RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_FALSE (0)The NF measurement ignores ohmic losses. RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_TRUE (1)The NF measurement accounts for the ohmic losses. |
| RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_FALSE (0) | The NF measurement ignores ohmic losses. |
| RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_TRUE (1) | The NF measurement accounts for the ohmic losses. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_dut_output_loss_frequency.html language=enus -->
## TOPIC 00216: RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_dut_output_loss_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_dut_output_loss_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_FREQUENCY

| Data Type: | float64 [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64ArrayRFmxSpecAn_GetAttributeF64Array |
| Description: | Specifies the array of frequencies corresponding to the value of the RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS attribute. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is an empty array. Get Function: RFmxSpecAn_NFGetDUTOutputLossFrequency Set Function: RFmxSpecAn_NFSetDUTOutputLossFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_external_preamp_present.html language=enus -->
## TOPIC 00217: RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_PRESENT

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_external_preamp_present.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_external_preamp_present.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_PRESENT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies if an external preamplifier is present in the signal path. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_FALSE. Get Function: RFmxSpecAn_NFGetExternalPreampPresent Set Function: RFmxSpecAn_NFSetExternalPreampPresent |
| Values: | RFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_FALSE (0)No external preamplifier present in the signal path. RFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_TRUE (1)An external preamplifier present in the signal path. |
| RFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_FALSE (0) | No external preamplifier present in the signal path. |
| RFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_TRUE (1) | An external preamplifier present in the signal path. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_frequency_converter_lo_frequency.html language=enus -->
## TOPIC 00218: RFMXSPECAN_ATTR_NF_FREQUENCY_CONVERTER_LO_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_frequency_converter_lo_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_frequency_converter_lo_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_FREQUENCY_CONVERTER_LO_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the fixed LO frequency of the DUT when you set the RFMXSPECAN_ATTR_NF_DUT_TYPE attribute to either RFMXSPECAN_VAL_NF_DUT_TYPE_DOWNCONVERTER or RFMXSPECAN_VAL_NF_DUT_TYPE_UPCONVERTER. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10 MHz. Get Function: RFmxSpecAn_NFGetFrequencyConverterLOFrequency Set Function: RFmxSpecAn_NFSetFrequencyConverterLOFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_measurement_bandwidth.html language=enus -->
## TOPIC 00219: RFMXSPECAN_ATTR_NF_MEASUREMENT_BANDWIDTH

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_measurement_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_measurement_bandwidth.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_MEASUREMENT_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the effective noise-bandwidth in which power measurements are performed for the noise figure (NF) measurement. This value is expressed in Hz. The default value is 100 kHz. Get Function: RFmxSpecAn_NFGetMeasurementBandwidth Set Function: RFmxSpecAn_NFSetMeasurementBandwidth |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_measurement_interval.html language=enus -->
## TOPIC 00220: RFMXSPECAN_ATTR_NF_MEASUREMENT_INTERVAL

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_measurement_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_measurement_interval.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_MEASUREMENT_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the duration for which the signals are acquired at each frequency which you specify in the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1 ms. Get Function: RFmxSpecAn_NFGetMeasurementInterval Set Function: RFmxSpecAn_NFSetMeasurementInterval |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_number_of_analysis_threads.html language=enus -->
## TOPIC 00221: RFMXSPECAN_ATTR_NF_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_number_of_analysis_threads.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the noise figure (NF) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. The default value is 1. Get Function: RFmxSpecAn_NFGetNumberOfAnalysisThreads Set Function: RFmxSpecAn_NFSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_results_dut_noise_temperature.html language=enus -->
## TOPIC 00222: RFMXSPECAN_ATTR_NF_RESULTS_DUT_NOISE_TEMPERATURE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_results_dut_noise_temperature.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_results_dut_noise_temperature.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_RESULTS_DUT_NOISE_TEMPERATURE

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64Array |
| Description: | Returns an array of the equivalent thermal noise temperatures of the DUT measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in kelvin. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_NFGetResultsDUTNoiseTemperature |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_y_factor_noise_source_loss_frequency.html language=enus -->
## TOPIC 00223: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_y_factor_noise_source_loss_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_y_factor_noise_source_loss_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_FREQUENCY

| Data Type: | float64 [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64ArrayRFmxSpecAn_GetAttributeF64Array |
| Description: | Specifies the frequencies corresponding to the ohmic loss inherent to the noise source used in the Y-Factor method specified by the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS attribute. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is an empty array. Get Function: RFmxSpecAn_NFGetYFactorNoiseSourceLossFrequency Set Function: RFmxSpecAn_NFSetYFactorNoiseSourceLossFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_nf_y_factor_noise_source_type.html language=enus -->
## TOPIC 00224: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_nf_y_factor_noise_source_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_nf_y_factor_noise_source_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the noise source type for performing the noise figure (NF) measurement when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to RFMXSPECAN_VAL_NF_MEASUREMENT_METHOD_Y_FACTOR. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_TYPE_EXTERNAL_NOISE_SOURCE. Get Function: RFmxSpecAn_NFGetYFactorNoiseSourceType Set Function: RFmxSpecAn_NFSetYFactorNoiseSourceType |
| Values: | RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_TYPE_EXTERNAL_NOISE_SOURCE (0)The NF measurement generates noise using an external noise source, that is controlled either by an internal noise source power supply or an NI Source Measure Unit (SMU). Supported Devices: PXIe-5665 (3.6 GHz), PXIe-5668, PXIe-5644/5645/5646*, PXIe-5840*/5841*/5842*/5860*, PXIe 5830/5831*/5832* *Use an external NI Source Measure Unit (SMU) as the noise source power supply for the Noise Figure measurement. During initialization, specify the SMU resource name using 'NoiseSourcePowerSupply' as the specifier within the RFmxSetup string. For example, 'RFmxSetup= NoiseSourcePowerSupply:myDCPower' configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You should allocate a dedicated SMU channel for RFmx. RFmx supports PXIe-4138, PXIe-4139, and PXIe-4139 (40 W) SMUs. RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_TYPE_RF_SIGNAL_GENERATOR (1)When you measure Y-Factor based NF using a supported NI vector signal transceiver (VST) instrument, RFmx generates noise using the vector signal generator (VSG) integrated into the same VST. RFmx automatically configures the vector signal generator (VSG) to generate noise at the specified bandwidth and ENR levels that you set using the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR_FREQUENCY and RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR attributes. Supported Devices: PXIe-5842/5860 |
| RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_TYPE_EXTERNAL_NOISE_SOURCE (0) | The NF measurement generates noise using an external noise source, that is controlled either by an internal noise source power supply or an NI Source Measure Unit (SMU). Supported Devices: PXIe-5665 (3.6 GHz), PXIe-5668, PXIe-5644/5645/5646*, PXIe-5840*/5841*/5842*/5860*, PXIe 5830/5831*/5832* *Use an external NI Source Measure Unit (SMU) as the noise source power supply for the Noise Figure measurement. During initialization, specify the SMU resource name using 'NoiseSourcePowerSupply' as the specifier within the RFmxSetup string. For example, 'RFmxSetup= NoiseSourcePowerSupply:myDCPower' configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You should allocate a dedicated SMU channel for RFmx. RFmx supports PXIe-4138, PXIe-4139, and PXIe-4139 (40 W) SMUs. |
| RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_TYPE_RF_SIGNAL_GENERATOR (1) | When you measure Y-Factor based NF using a supported NI vector signal transceiver (VST) instrument, RFmx generates noise using the vector signal generator (VSG) integrated into the same VST. RFmx automatically configures the vector signal generator (VSG) to generate noise at the specified bandwidth and ENR levels that you set using the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR_FREQUENCY and RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR attributes. Supported Devices: PXIe-5842/5860 |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_number_of_steps.html language=enus -->
## TOPIC 00225: RFMXSPECAN_ATTR_NUMBER_OF_STEPS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_number_of_steps.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_number_of_steps.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_NUMBER_OF_STEPS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the number of active steps in a list. You need to use a selector string to configure or read this attribute for the list instance. The default value is 0. Get Function: RFmxSpecAn_GetNumberOfSteps Set Function: RFmxSpecAn_SetNumberOfSteps |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_obw_all_traces_enabled.html language=enus -->
## TOPIC 00226: RFMXSPECAN_ATTR_OBW_ALL_TRACES_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_obw_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_obw_all_traces_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_OBW_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the OBW. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_FALSE. Get Function: RFmxSpecAn_OBWGetAllTracesEnabled Set Function: RFmxSpecAn_OBWSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_obw_averaging_count.html language=enus -->
## TOPIC 00227: RFMXSPECAN_ATTR_OBW_AVERAGING_COUNT

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_obw_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_obw_averaging_count.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_OBW_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_OBW_AVERAGING_ENABLED attribute to RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxSpecAn_OBWGetAveragingCount Set Function: RFmxSpecAn_OBWSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_obw_averaging_enabled.html language=enus -->
## TOPIC 00228: RFMXSPECAN_ATTR_OBW_AVERAGING_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_obw_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_obw_averaging_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_OBW_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the OBW measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_FALSE. Get Function: RFmxSpecAn_OBWGetAveragingEnabled Set Function: RFmxSpecAn_OBWSetAveragingEnabled |
| Values: | RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_TRUE (1)The OBW measurement uses the RFMXSPECAN_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |
| RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_TRUE (1) | The OBW measurement uses the RFMXSPECAN_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_obw_averaging_type.html language=enus -->
## TOPIC 00229: RFMXSPECAN_ATTR_OBW_AVERAGING_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_obw_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_obw_averaging_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_OBW_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for OBW measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_RMS. Get Function: RFmxSpecAn_OBWGetAveragingType Set Function: RFmxSpecAn_OBWSetAveragingType |
| Values: | RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_SCALAR (2)The square root of the power spectrum is averaged. RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MINIMUM (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_obw_bandwidth_percentage.html language=enus -->
## TOPIC 00230: RFMXSPECAN_ATTR_OBW_BANDWIDTH_PERCENTAGE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_obw_bandwidth_percentage.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_obw_bandwidth_percentage.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_OBW_BANDWIDTH_PERCENTAGE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the percentage of the total power that is contained in the OBW. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 99%. Get Function: RFmxSpecAn_OBWGetBandwidthPercentage Set Function: RFmxSpecAn_OBWSetBandwidthPercentage |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_obw_fft_padding.html language=enus -->
## TOPIC 00231: RFMXSPECAN_ATTR_OBW_FFT_PADDING

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_obw_fft_padding.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_obw_fft_padding.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_OBW_FFT_PADDING

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the factor by which the time-domain waveform is zero-padded before fast Fourier transform (FFT). The FFT size is given by the following formula: waveform size * padding This attribute is used only when the acquisition span is less than the device instantaneous bandwidth of the device. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is -1. Get Function: RFmxSpecAn_OBWGetFFTPadding Set Function: RFmxSpecAn_OBWSetFFTPadding |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_obw_fft_window.html language=enus -->
## TOPIC 00232: RFMXSPECAN_ATTR_OBW_FFT_WINDOW

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_obw_fft_window.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_obw_fft_window.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_OBW_FFT_WINDOW

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the FFT window type to use to reduce spectral leakage. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_OBW_FFT_WINDOW_FLAT_TOP. Get Function: RFmxSpecAn_OBWGetFFTWindow Set Function: RFmxSpecAn_OBWSetFFTWindow |
| Values: | RFMXSPECAN_VAL_OBW_FFT_WINDOW_NONE (0)Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. RFMXSPECAN_VAL_OBW_FFT_WINDOW_FLAT_TOP (1)Measures single-tone amplitudes accurately. RFMXSPECAN_VAL_OBW_FFT_WINDOW_HANNING (2)Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. RFMXSPECAN_VAL_OBW_FFT_WINDOW_HAMMING (3)Analyzes closely-spaced sine waves. RFMXSPECAN_VAL_OBW_FFT_WINDOW_GAUSSIAN (4)Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. RFMXSPECAN_VAL_OBW_FFT_WINDOW_BLACKMAN (5)Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. RFMXSPECAN_VAL_OBW_FFT_WINDOW_BLACKMAN_HARRIS (6)Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. RFMXSPECAN_VAL_OBW_FFT_WINDOW_KAISER_BESSEL (7)Separates two tones with frequencies close to each other but with widely-differing amplitudes. |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_NONE (0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_FLAT_TOP (1) | Measures single-tone amplitudes accurately. |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_HANNING (2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_HAMMING (3) | Analyzes closely-spaced sine waves. |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_GAUSSIAN (4) | Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_BLACKMAN (5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_BLACKMAN_HARRIS (6) | Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |
| RFMXSPECAN_VAL_OBW_FFT_WINDOW_KAISER_BESSEL (7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_obw_power_units.html language=enus -->
## TOPIC 00233: RFMXSPECAN_ATTR_OBW_POWER_UNITS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_obw_power_units.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_obw_power_units.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_OBW_POWER_UNITS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the units for the absolute power. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM_PER_HZ. Get Function: RFmxSpecAn_OBWGetPowerUnits Set Function: RFmxSpecAn_OBWSetPowerUnits |
| Values: | RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM (0)The absolute powers are reported in dBm. RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM_PER_HZ (1)The absolute powers are reported in dBm/Hz. |
| RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM (0) | The absolute powers are reported in dBm. |
| RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM_PER_HZ (1) | The absolute powers are reported in dBm/Hz. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_obw_results_start_frequency.html language=enus -->
## TOPIC 00234: RFMXSPECAN_ATTR_OBW_RESULTS_START_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_obw_results_start_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_obw_results_start_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_OBW_RESULTS_START_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the start frequency of the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = stop frequency - start frequency You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_OBWGetResultsStartFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_obw_sweep_time_auto.html language=enus -->
## TOPIC 00235: RFMXSPECAN_ATTR_OBW_SWEEP_TIME_AUTO

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_obw_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_obw_sweep_time_auto.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_OBW_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxSpecAn_OBWGetSweepTimeAuto Set Function: RFmxSpecAn_OBWSetSweepTimeAuto |
| Values: | RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1)The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. |
| RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) | The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_pavt_results_mean_absolute_phase.html language=enus -->
## TOPIC 00236: RFMXSPECAN_ATTR_PAVT_RESULTS_MEAN_ABSOLUTE_PHASE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_pavt_results_mean_absolute_phase.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_pavt_results_mean_absolute_phase.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_PAVT_RESULTS_MEAN_ABSOLUTE_PHASE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the mean absolute phase of the segment. This value is expressed in degrees. Use 'segment(n)' as the selector string to read this result. Get Function: RFmxSpecAn_PAVTGetResultsMeanAbsolutePhase |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_phasenoise_cancellation_enabled.html language=enus -->
## TOPIC 00237: RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_phasenoise_cancellation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_phasenoise_cancellation_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable or disable the phase noise cancellation. Refer to the Phase Noise topic for more information on phase noise cancellation. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_PHASENOISE_CANCELLATION_ENABLED_FALSE. Get Function: RFmxSpecAn_PhaseNoiseGetCancellationEnabled Set Function: RFmxSpecAn_PhaseNoiseSetCancellationEnabled |
| Values: | RFMXSPECAN_VAL_PHASENOISE_CANCELLATION_ENABLED_FALSE (0)Disables phase noise cancellation. RFMXSPECAN_VAL_PHASENOISE_CANCELLATION_ENABLED_TRUE (1)Enables phase noise cancellation. |
| RFMXSPECAN_VAL_PHASENOISE_CANCELLATION_ENABLED_FALSE (0) | Disables phase noise cancellation. |
| RFMXSPECAN_VAL_PHASENOISE_CANCELLATION_ENABLED_TRUE (1) | Enables phase noise cancellation. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_phasenoise_cancellation_frequency.html language=enus -->
## TOPIC 00238: RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_phasenoise_cancellation_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_phasenoise_cancellation_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_FREQUENCY

| Data Type: | float32 [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF32ArrayRFmxSpecAn_GetAttributeF32Array |
| Description: | Specifies an array of frequencies where the reference phase noise has been measured. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxSpecAn_PhaseNoiseGetCancellationFrequency Set Function: RFmxSpecAn_PhaseNoiseSetCancellationFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_phasenoise_cancellation_reference_phase_noise.html language=enus -->
## TOPIC 00239: RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_REFERENCE_PHASE_NOISE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_phasenoise_cancellation_reference_phase_noise.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_phasenoise_cancellation_reference_phase_noise.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_REFERENCE_PHASE_NOISE

| Data Type: | float32 [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF32ArrayRFmxSpecAn_GetAttributeF32Array |
| Description: | Specifies an array of reference phase noise at the frequencies specified by the RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_FREQUENCY attribute . You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxSpecAn_PhaseNoiseGetCancellationReferencePhaseNoise Set Function: RFmxSpecAn_PhaseNoiseSetCancellationReferencePhaseNoise |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_phasenoise_measurement_enabled.html language=enus -->
## TOPIC 00240: RFMXSPECAN_ATTR_PHASENOISE_MEASUREMENT_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_phasenoise_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_phasenoise_measurement_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_PHASENOISE_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the phase noise measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_FALSE. Get Function: RFmxSpecAn_PhaseNoiseGetMeasurementEnabled Set Function: RFmxSpecAn_PhaseNoiseSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_phasenoise_range_stop_frequency.html language=enus -->
## TOPIC 00241: RFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_phasenoise_range_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_phasenoise_range_stop_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the stop frequency for the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to RFMXSPECAN_VAL_PHASENOISE_RANGE_DEFINITION_MANUAL. Use 'range(n)' as the selector string to configure or read this attribute. The default value is 1E+06. Get Function: RFmxSpecAn_PhaseNoiseGetRangeStopFrequency Set Function: RFmxSpecAn_PhaseNoiseSetRangeStopFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_phasenoise_rbw_percentage.html language=enus -->
## TOPIC 00242: RFMXSPECAN_ATTR_PHASENOISE_RBW_PERCENTAGE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_phasenoise_rbw_percentage.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_phasenoise_rbw_percentage.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_PHASENOISE_RBW_PERCENTAGE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the RBW as a percentage of the start frequency of each subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to RFMXSPECAN_VAL_PHASENOISE_RANGE_DEFINITION_AUTO. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxSpecAn_PhaseNoiseGetRBWPercentage Set Function: RFmxSpecAn_PhaseNoiseSetRBWPercentage |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_phasenoise_results_integrated_noise_residual_fm.html language=enus -->
## TOPIC 00243: RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_FM

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_phasenoise_results_integrated_noise_residual_fm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_phasenoise_results_integrated_noise_residual_fm.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_FM

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64Array |
| Description: | Returns the residual FM in Hz. You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxSpecAn_PhaseNoiseGetResultsResidualFM |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_phasenoise_start_frequency.html language=enus -->
## TOPIC 00244: RFMXSPECAN_ATTR_PHASENOISE_START_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_phasenoise_start_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_phasenoise_start_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_PHASENOISE_START_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the start frequency of the offset frequency range when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to RFMXSPECAN_VAL_PHASENOISE_RANGE_DEFINITION_AUTO. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1000. Get Function: RFmxSpecAn_PhaseNoiseGetStartFrequency Set Function: RFmxSpecAn_PhaseNoiseSetStartFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_phasenoise_stop_frequency.html language=enus -->
## TOPIC 00245: RFMXSPECAN_ATTR_PHASENOISE_STOP_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_phasenoise_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_phasenoise_stop_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_PHASENOISE_STOP_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the stop frequency of the offset frequency range when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to RFMXSPECAN_VAL_PHASENOISE_RANGE_DEFINITION_AUTO. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1E+06. Get Function: RFmxSpecAn_PhaseNoiseGetStopFrequency Set Function: RFmxSpecAn_PhaseNoiseSetStopFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_reference_level_headroom.html language=enus -->
## TOPIC 00246: RFMXSPECAN_ATTR_REFERENCE_LEVEL_HEADROOM

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_reference_level_headroom.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_reference_level_headroom.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_REFERENCE_LEVEL_HEADROOM

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the margin RFmx adds to the RFMXSPECAN_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the RFMXSPECAN_ATTR_REFERENCE_LEVEL plus the RFMXSPECAN_ATTR_REFERENCE_LEVEL_HEADROOM. If you know the input power of the signal precisely or previously included the margin in the RFMXSPECAN_ATTR_REFERENCE_LEVEL, you could improve the signal-to-noise ratio by reducing the RFMXSPECAN_ATTR_REFERENCE_LEVEL_HEADROOM. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Supported devices: PXIe-5668, PXIe-5830/5831/5832/5840/5841/5842/5860. Default valuesPXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Get Function: RFmxSpecAn_GetReferenceLevelHeadroom Set Function: RFmxSpecAn_SetReferenceLevelHeadroom |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_carrier_channel_bandwidth.html language=enus -->
## TOPIC 00247: RFMXSPECAN_ATTR_SEM_CARRIER_CHANNEL_BANDWIDTH

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_carrier_channel_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_carrier_channel_bandwidth.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_CARRIER_CHANNEL_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | specifies the channel bandwidth of the carrier. This parameter is used to calculate the values of the RFMXSPECAN_ATTR_SEM_OFFSET_START_FREQUENCY and RFMXSPECAN_ATTR_SEM_OFFSET_STOP_FREQUENCY attributes when you set the RFMXSPECAN_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION attribute to RFMXSPECAN_VAL_SEM_CARRIER_EDGE_TO_MEASUREMENT_BANDWIDTH_CENTER or RFMXSPECAN_VAL_SEM_CARRIER_EDGE_TO_MEASUREMENT_BANDWIDTH_EDGE. Use 'carrier(n)' as the selector string to configure or read this attribute. The default value is 2 MHz. Get Function: RFmxSpecAn_SEMGetCarrierChannelBandwidth Set Function: RFmxSpecAn_SEMSetCarrierChannelBandwidth |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_carrier_frequency.html language=enus -->
## TOPIC 00248: RFMXSPECAN_ATTR_SEM_CARRIER_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_carrier_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_carrier_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_CARRIER_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the center frequency of the carrier, relative to the RF center frequency. This value is expressed in Hz. Use 'carrier(n)' as the selector string to configure or read this attribute. The default value is 0. Get Function: RFmxSpecAn_SEMGetCarrierFrequency Set Function: RFmxSpecAn_SEMSetCarrierFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_carrier_integration_bandwidth.html language=enus -->
## TOPIC 00249: RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_carrier_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_carrier_integration_bandwidth.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the frequency range, over which the measurement integrates the carrier power. This value is expressed in Hz. Use 'carrier(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsCarrierIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_composite_measurement_status.html language=enus -->
## TOPIC 00250: RFMXSPECAN_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_composite_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_composite_measurement_status.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeI32 |
| Description: | Indicates the overall measurement status based on the measurement limits and the fail criteria that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute for each offset segment. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_SEMGetResultsCompositeMeasurementStatus |
| Values: | RFMXSPECAN_VAL_SEM_COMPOSITE_MEASUREMENT_STATUS_FAIL (0)Indicates that the measurement has failed. RFMXSPECAN_VAL_SEM_COMPOSITE_MEASUREMENT_STATUS_PASS (1)Indicates that the measurement has passed. |
| RFMXSPECAN_VAL_SEM_COMPOSITE_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |
| RFMXSPECAN_VAL_SEM_COMPOSITE_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |
