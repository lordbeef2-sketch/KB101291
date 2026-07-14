# NI DOCUMENT BUNDLE: rfmxspecan-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxspecan-c-api-ref start=501 end=623 -->
<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga8e90555159f8b3db92a6f79aac0d3a22.html language=enus -->
## TOPIC 00501: RFmxSpecAn_AMPMFetchCurveFitResidual

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga8e90555159f8b3db92a6f79aac0d3a22.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga8e90555159f8b3db92a6f79aac0d3a22.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the polynomial approximation residuals for AM-to-AM and AM-to-PM response of the device under test. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchCurveFitResidual(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *amToAMResidual, float64 *amToPMResidual)Paramete

### RFmxSpecAn_AMPMFetchCurveFitResidual

Fetches the polynomial approximation residuals for AM-to-AM and AM-to-PM response of the device under test.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchCurveFitResidual(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *amToAMResidual, float64 *amToPMResidual)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| amToAMResidual | [out] | float64 * | This parameter returns the approximation error, in dB, in the polynomial approximation of the AM-to-AM characteristic of the device under test. |
| amToPMResidual | [out] | float64 * | This parameter returns the approximation error, in degrees, in the polynomial approximation of the AM-to-PM characteristic of the device under test. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaa47cf2391a23e346a922aeb8fd25b663.html language=enus -->
## TOPIC 00502: RFmxSpecAn_AMPMFetchProcessedReferenceWaveformSplit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaa47cf2391a23e346a922aeb8fd25b663.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaa47cf2391a23e346a922aeb8fd25b663.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the segment of the reference waveform used to perform the AMPM measurement. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchProcessedReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 processedReferenceWaveformI[], f

### RFmxSpecAn_AMPMFetchProcessedReferenceWaveformSplit

Fetches the segment of the reference waveform used to perform the AMPM measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchProcessedReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 processedReferenceWaveformI[], float32 processedReferenceWaveformQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| processedReferenceWaveformI | [out] | float32[] | This parameter Returns the real part of complex baseband samples, in volts. |
| processedReferenceWaveformQ | [out] | float32[] | This parameter Returns the imaginary part of complex baseband samples, in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaa90a18b8f828cfbf8ee57e117e364606.html language=enus -->
## TOPIC 00503: RFmxSpecAn_AMPMFetchProcessedReferenceWaveform

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaa90a18b8f828cfbf8ee57e117e364606.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaa90a18b8f828cfbf8ee57e117e364606.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the segment of the reference waveform used to perform the AMPM measurement. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchProcessedReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle processedReferenceWaveform[],

### RFmxSpecAn_AMPMFetchProcessedReferenceWaveform

Fetches the segment of the reference waveform used to perform the AMPM measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchProcessedReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle processedReferenceWaveform[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| processedReferenceWaveform | [out] | NIComplexSingle[] | This parameter returns the complex baseband samples, in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaaab0a3d895fd4e44864284be8376ddc7.html language=enus -->
## TOPIC 00504: RFmxSpecAn_AMPMFetchCompressionPoints

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaaab0a3d895fd4e44864284be8376ddc7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaaab0a3d895fd4e44864284be8376ddc7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the compression points. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchCompressionPoints(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 inputCompressionPoint[], float64 outputCompressionPoint[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTy

### RFmxSpecAn_AMPMFetchCompressionPoints

Fetches the compression points.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchCompressionPoints(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 inputCompressionPoint[], float64 outputCompressionPoint[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| inputCompressionPoint | [out] | float64[] | This parameter returns the theoretical input power at which the device gain drops by the compression level, specified by the RFMXSPECAN_ATTR_AMPM_COMPRESSION_POINT_LEVEL parameter, from its mean linear gain. This value is expressed in dBm. |
| outputCompressionPoint | [out] | float64[] | This parameter returns the theoretical output power at which device gain drops by the compression level, specified by the RFMXSPECAN_ATTR_AMPM_COMPRESSION_POINT_LEVEL parameter, from its mean linear gain. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gabab153b7e6ee0fc48b5c693f3ef08b13.html language=enus -->
## TOPIC 00505: RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveform

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gabab153b7e6ee0fc48b5c693f3ef08b13.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gabab153b7e6ee0fc48b5c693f3ef08b13.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the AMPM measurement. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, N

### RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveform

Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the AMPM measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle processedMeanAcquiredWaveform[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| processedMeanAcquiredWaveform | [out] | NIComplexSingle[] | This parameter returns the complex baseband samples, in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gad35786c913259b079a7c3d24c4d6431d.html language=enus -->
## TOPIC 00506: RFmxSpecAn_AMPMFetchError

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gad35786c913259b079a7c3d24c4d6431d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gad35786c913259b079a7c3d24c4d6431d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum gain error range, phase error range, and mean phase error for the DUT. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *gainErrorRange, float64 *phaseErrorRange, float64 *meanPhaseError)Parameters

### RFmxSpecAn_AMPMFetchError

Fetches the maximum gain error range, phase error range, and mean phase error for the DUT.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *gainErrorRange, float64 *phaseErrorRange, float64 *meanPhaseError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| gainErrorRange | [out] | float64 * | This parameter returns the peak-to-peak deviation, in dB, in the gain of the device under test. |
| phaseErrorRange | [out] | float64 * | This parameter returns the peak-to-peak deviation, in degrees, in the phase distortion of the acquired signal relative to the reference waveform caused by the device under test. |
| meanPhaseError | [out] | float64 * | This parameter returns the mean phase error, in degrees, of the acquired signal relative to the reference waveform caused by the device under test. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaf01f13728ef88c06631c51b5a3bda243.html language=enus -->
## TOPIC 00507: RFmxSpecAn_AMPMFetchAMToAMTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaf01f13728ef88c06631c51b5a3bda243.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1gaf01f13728ef88c06631c51b5a3bda243.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the AM to AM trace, where the Reference Powers array forms the x-axis of the trace; and the Measured AM to AM and Curve Fit AM to AM arrays form the y-axis of the trace. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchAMToAMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 t

### RFmxSpecAn_AMPMFetchAMToAMTrace

Fetches the AM to AM trace, where the **Reference Powers** array forms the x-axis of the trace; and the **Measured AM to AM** and **Curve Fit AM to AM** arrays form the y-axis of the trace.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchAMToAMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 referencePowers[], float32 measuredAMToAM[], float32 curveFitAMToAM[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| referencePowers | [out] | float32[] | This parameter returns the array of reference powers. This value is expressed in dBm.Reference Powers are the instantaneous powers at the input port of the DUT when you set the RFMXSPECAN_ATTR_AMPM_REFERENCE_POWER_TYPE attribute to Input, and Reference Powers are the instantaneous powers at the output port of the DUT when you set the AMPM Ref Pwr Type attribute to Output. |
| measuredAMToAM | [out] | float32[] | This parameter returns the gain values corresponding to the reference powers. This value is expressed in dB. |
| curveFitAMToAM | [out] | float32[] | This parameter returns the polynomial fit gain values corresponding to the reference powers. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd.html language=enus -->
## TOPIC 00508: Apply DPD

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsUser DPDGroup membersNameDescriptionRFmxSpecAn_DPDApplyDigitalPredistortionScales the input waveform to DUT average input power and then predistorts using the DPD polynomial or the lookup table. To scale the waveform correctly, specify if the idle duration is present in the waveform. RFmxSpecA

### Apply DPD

#### Groups

- User DPD

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_DPDApplyDigitalPredistortion | Scales the input waveform to DUT average input power and then predistorts using the DPD polynomial or the lookup table. To scale the waveform correctly, specify if the idle duration is present in the waveform. |
| RFmxSpecAn_DPDApplyDigitalPredistortionSplit | Scales the input waveform to DUT average input power and then predistorts using the DPD polynomial or the lookup table. To scale the waveform correctly, specify if the idle duration is present in the waveform. |
| RFmxSpecAn_DPDCfgApplyDPDConfigurationInput | Configures the source of measurement settings for applying DPD. |
| RFmxSpecAn_DPDCfgApplyDPDLookupTableCorrectionType | Configures the predistortion type when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Lookup Table. |
| RFmxSpecAn_DPDCfgApplyDPDMemoryModelCorrectionType | Configures the predistortion type when you set the RFMXSPECAN_ATTR_DPD_MODEL property to Memory Polynomial or Generalized Memory Polynomial |
| RFmxSpecAn_DPDFetchApplyDPDPreCFRPAPR | Fetches the PAPR of the pre-distorted waveform before CFR is applied to it. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd_1ga0fd289794c0c6614ae05d9cd450ec530.html language=enus -->
## TOPIC 00509: RFmxSpecAn_DPDFetchApplyDPDPreCFRPAPR

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd_1ga0fd289794c0c6614ae05d9cd450ec530.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd_1ga0fd289794c0c6614ae05d9cd450ec530.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PAPR of the pre-distorted waveform before CFR is applied to it. Syntaxint32 __stdcall RFmxSpecAn_DPDFetchApplyDPDPreCFRPAPR(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *preCFRPAPR)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInst

### RFmxSpecAn_DPDFetchApplyDPDPreCFRPAPR

Fetches the PAPR of the pre-distorted waveform before CFR is applied to it.

#### Syntax

int32 __stdcall RFmxSpecAn_DPDFetchApplyDPDPreCFRPAPR(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *preCFRPAPR)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Result name is not supported. Any specified result name is ignored and the Pre-CFR PAPR returned corresponds to the latest execution of apply DPD for the specified signal name. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| preCFRPAPR | [out] | float64 * | This parameter returns the PAPR of the pre-distorted waveform before CFR is applied when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True. This value is expressed in dB.When you set the DPD Apply DPD CFR Enabled attribute to False and the RFMXSPECAN_ATTR_DPD_MODEL attribute to Lookup Table, the PAPR of the pre-distorted waveform is returned.When you set the DPD Apply DPD CFR Enabled attribute to False and the DPD Model attribute to Memory Polynomial or Generalized Memory Polynomial, the PAPR of the clipped pre-distorted waveform is returned. The pre-distorted waveform is clipped such that its peak amplitude does not exceed the peak of the input waveform, scaled to DUT average input power, by 6 dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Apply DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd_1gae69a86c4a69a1fe689d6fe5095dd2c45.html language=enus -->
## TOPIC 00510: RFmxSpecAn_DPDCfgApplyDPDConfigurationInput

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd_1gae69a86c4a69a1fe689d6fe5095dd2c45.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd_1gae69a86c4a69a1fe689d6fe5095dd2c45.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the source of measurement settings for applying DPD. Syntaxint32 __stdcall RFmxSpecAn_DPDCfgApplyDPDConfigurationInput(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 configurationInput)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parame

### RFmxSpecAn_DPDCfgApplyDPDConfigurationInput

Configures the source of measurement settings for applying DPD.

#### Syntax

int32 __stdcall RFmxSpecAn_DPDCfgApplyDPDConfigurationInput(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 configurationInput)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| configurationInput | [in] | int32 | This parameter specifies the mode of configuring parameters for applying DPD. The default value is Measurement.NameValueDescriptionRFMXSPECAN_VAL_DPD_APPLY_DPD_CONFIGURATION_INPUT_MEASUREMENT0 (0x0)Uses the computed DPD polynomial or lookup table for applying DPD on an input waveform using the same RFmx session handle. The configuration parameters for applying DPD such as the RFMXSPECAN_ATTR_DPD_DUT_AVERAGE_INPUT_POWER, RFMXSPECAN_ATTR_DPD_MODEL, RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE, DPD polynomial, and lookup table are obtained from the DPD measurement configuration.RFMXSPECAN_VAL_DPD_APPLY_DPD_CONFIGURATION_INPUT_USER1 (0x1)Applies DPD by using a computed DPD polynomial or lookup table on an input waveform. You must set the configuration parameters for applying DPD such as the RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DUT_AVERAGE_INPUT_POWER, RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL, RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEASUREMENT_SAMPLE_RATE, DPD polynomial, and lookup table. You do not need to call the RFmxSpecAn_Initiate function when you set the DPD Apply DPD Config Input attribute User. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_CONFIGURATION_INPUT_MEASUREMENT | 0 (0x0) | Uses the computed DPD polynomial or lookup table for applying DPD on an input waveform using the same RFmx session handle. The configuration parameters for applying DPD such as the RFMXSPECAN_ATTR_DPD_DUT_AVERAGE_INPUT_POWER, RFMXSPECAN_ATTR_DPD_MODEL, RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE, DPD polynomial, and lookup table are obtained from the DPD measurement configuration. |  |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_CONFIGURATION_INPUT_USER | 1 (0x1) | Applies DPD by using a computed DPD polynomial or lookup table on an input waveform. You must set the configuration parameters for applying DPD such as the RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DUT_AVERAGE_INPUT_POWER, RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL, RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEASUREMENT_SAMPLE_RATE, DPD polynomial, and lookup table. You do not need to call the RFmxSpecAn_Initiate function when you set the DPD Apply DPD Config Input attribute User. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Apply DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd.html language=enus -->
## TOPIC 00511: User DPD

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomialConfigures the array of memory polynomial or generalized memory polynomial coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial. RFmxSpecAn_DPDCfgApplyDP

### User DPD

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomial | Configures the array of memory polynomial or generalized memory polynomial coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial. |
| RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomialSplit | Configures the array of memory polynomial or generalized memory polynomial coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial. |
| RFmxSpecAn_DPDCfgApplyDPDUserLookupTable | Configures the predistortion lookup table when you set the RFMXSPECAN_ATTR_DPD_MODEL property to Lookup Table |
| RFmxSpecAn_DPDCfgApplyDPDUserLookupTableSplit | Configures the predistortion lookup table when you set the RFMXSPECAN_ATTR_DPD_MODEL property to Lookup Table |

#### Attachments

None

Parent topic:

Apply DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd_1ga718dc139e7f7135cc29732726cfcdc77.html language=enus -->
## TOPIC 00512: RFmxSpecAn_DPDCfgApplyDPDUserLookupTableSplit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd_1ga718dc139e7f7135cc29732726cfcdc77.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd_1ga718dc139e7f7135cc29732726cfcdc77.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the predistortion lookup table when you set the RFMXSPECAN_ATTR_DPD_MODEL property to Lookup Table Syntaxint32 __stdcall RFmxSpecAn_DPDCfgApplyDPDUserLookupTableSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float32 lutInputPowers[], float32 lutComplexGainsI[], float32 l

### RFmxSpecAn_DPDCfgApplyDPDUserLookupTableSplit

Configures the predistortion lookup table when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) property to **Lookup Table**

#### Syntax

int32 __stdcall RFmxSpecAn_DPDCfgApplyDPDUserLookupTableSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float32 lutInputPowers[], float32 lutComplexGainsI[], float32 lutComplexGainsQ[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| lutInputPowers | [in] | float32[] | This parameter specifies the array of lookup table power levels, in dBm. |
| lutComplexGainsI | [in] | float32[] | This parameter Specifies the real part of array of lookup table complex gain values for magnitude and phase predistortion. |
| lutComplexGainsQ | [in] | float32[] | This parameter Specifies the imaginary part of array of lookup table complex gain values for magnitude and phase predistortion. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

User DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd_1gac23633516670ca2f2eafed757652a60d.html language=enus -->
## TOPIC 00513: RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomial

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd_1gac23633516670ca2f2eafed757652a60d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd_1gac23633516670ca2f2eafed757652a60d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the array of memory polynomial or generalized memory polynomial coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial. Syntaxint32 __stdcall RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomial(niRFmxInstrHandle instrumentHandle, cha

### RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomial

Configures the array of memory polynomial or generalized memory polynomial coefficients when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Memory Polynomial** or **Generalized Memory Polynomial**.

#### Syntax

int32 __stdcall RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomial(niRFmxInstrHandle instrumentHandle, char selectorString[], NIComplexSingle dpdPolynomial[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| dpdPolynomial | [in] | NIComplexSingle[] | This parameter specifies the array of memory polynomial or generalized memory polynomial coefficients when you set the DPD Model attribute to Memory Polynomial or Generalized Memory Polynomial. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

User DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd_1gac290139d5e90a05da74ccccb62d7b08d.html language=enus -->
## TOPIC 00514: RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomialSplit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd_1gac290139d5e90a05da74ccccb62d7b08d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__apply__dpd__user__dpd_1gac290139d5e90a05da74ccccb62d7b08d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the array of memory polynomial or generalized memory polynomial coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial. Syntaxint32 __stdcall RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomialSplit(niRFmxInstrHandle instrumentHandle

### RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomialSplit

Configures the array of memory polynomial or generalized memory polynomial coefficients when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Memory Polynomial** or **Generalized Memory Polynomial**.

#### Syntax

int32 __stdcall RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomialSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float32 dpdPolynomialI[], float32 dpdPolynomialQ[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| dpdPolynomialI | [in] | float32[] | This parameter Specifies the real part of array of memory polynomial or generalized memory polynomial coefficients when you set the DPD Model attribute to Memory Polynomial or Generalized Memory Polynomial. |
| dpdPolynomialQ | [in] | float32[] | This parameter Specifies the imaginary part of array of memory polynomial or generalized memory polynomial coefficients when you set the DPD Model attribute to Memory Polynomial or Generalized Memory Polynomial. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

User DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ccdf_1ga935031b45c5e010dd716df9df4f58b3d.html language=enus -->
## TOPIC 00515: RFmxSpecAn_CCDFFetchProbabilitiesTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ccdf_1ga935031b45c5e010dd716df9df4f58b3d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ccdf_1ga935031b45c5e010dd716df9df4f58b3d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the probabilities trace for the CCDF measurement. Syntaxint32 __stdcall RFmxSpecAn_CCDFFetchProbabilitiesTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 probabilities[], int32 arraySize, int32 *actualArraySize)ParametersName

### RFmxSpecAn_CCDFFetchProbabilitiesTrace

Returns the probabilities trace for the CCDF measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_CCDFFetchProbabilitiesTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 probabilities[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the mean power. |
| dx | [out] | float64 * | This parameter returns the bin size used by the CCDF measurement. |
| probabilities | [out] | float32[] | This parameter returns the probability, as a percentage, indicating the occurrence of samples in the signal with power greater than the mean power by x dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CCDF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1ga2491114f3633220dfb5201cf82e27c0a.html language=enus -->
## TOPIC 00516: RFmxSpecAn_DPDFetchDVRModelSplit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1ga2491114f3633220dfb5201cf82e27c0a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1ga2491114f3633220dfb5201cf82e27c0a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decomposed vector rotation model coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Decomposed Vector Rotation. Syntaxint32 __stdcall RFmxSpecAn_DPDFetchDVRModelSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 dvrModelI[], float3

### RFmxSpecAn_DPDFetchDVRModelSplit

Fetches the decomposed vector rotation model coefficients when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Decomposed Vector Rotation**.

#### Syntax

int32 __stdcall RFmxSpecAn_DPDFetchDVRModelSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 dvrModelI[], float32 dvrModelQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| dvrModelI | [out] | float32[] | This parameter Returns the real part of decomposed vector rotation model coefficients when you set the DPD Model attribute to Decomposed Vector Rotation. |
| dvrModelQ | [out] | float32[] | This parameter Returns the imaginary part of decomposed vector rotation model coefficients when you set the DPD Model attribute to Decomposed Vector Rotation. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1ga55e1ea7c144cb1887a7a52388ec3fea1.html language=enus -->
## TOPIC 00517: RFmxSpecAn_DPDFetchProcessedMeanAcquiredWaveform

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1ga55e1ea7c144cb1887a7a52388ec3fea1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1ga55e1ea7c144cb1887a7a52388ec3fea1.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the DPD measurement. Syntaxint32 __stdcall RFmxSpecAn_DPDFetchProcessedMeanAcquiredWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIC

### RFmxSpecAn_DPDFetchProcessedMeanAcquiredWaveform

Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the DPD measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_DPDFetchProcessedMeanAcquiredWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle processedMeanAcquiredWaveform[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| processedMeanAcquiredWaveform | [out] | NIComplexSingle[] | This parameter returns the complex baseband samples, in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1ga637b52b8d7efd74d7fd053b1ed5cd055.html language=enus -->
## TOPIC 00518: RFmxSpecAn_DPDFetchDPDPolynomial

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1ga637b52b8d7efd74d7fd053b1ed5cd055.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1ga637b52b8d7efd74d7fd053b1ed5cd055.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the memory polynomial or generalized memory polynomial coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial. Syntaxint32 __stdcall RFmxSpecAn_DPDFetchDPDPolynomial(niRFmxInstrHandle instrumentHandle, char selectorString[], fl

### RFmxSpecAn_DPDFetchDPDPolynomial

Fetches the memory polynomial or generalized memory polynomial coefficients when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Memory Polynomial** or **Generalized Memory Polynomial**.

#### Syntax

int32 __stdcall RFmxSpecAn_DPDFetchDPDPolynomial(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle dpdPolynomial[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| dpdPolynomial | [out] | NIComplexSingle[] | This parameter returns the memory polynomial or generalized memory polynomial coefficients when you set the DPD Model attribute to Memory Polynomial or Generalized Memory Polynomial. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1gac193d76704138e0a09239f118266cf8c.html language=enus -->
## TOPIC 00519: RFmxSpecAn_DPDFetchProcessedReferenceWaveform

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1gac193d76704138e0a09239f118266cf8c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1gac193d76704138e0a09239f118266cf8c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the segment of the reference waveform used to perform the DPD measurement. Syntaxint32 __stdcall RFmxSpecAn_DPDFetchProcessedReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle processedReferenceWaveform[], i

### RFmxSpecAn_DPDFetchProcessedReferenceWaveform

Fetches the segment of the reference waveform used to perform the DPD measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_DPDFetchProcessedReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle processedReferenceWaveform[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| processedReferenceWaveform | [out] | NIComplexSingle[] | This parameter returns the complex baseband samples, in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1gae8935ee099afa09de46663f8366c5880.html language=enus -->
## TOPIC 00520: RFmxSpecAn_DPDFetchDPDPolynomialSplit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1gae8935ee099afa09de46663f8366c5880.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__dpd_1gae8935ee099afa09de46663f8366c5880.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the memory polynomial or generalized memory polynomial coefficients when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial. Syntaxint32 __stdcall RFmxSpecAn_DPDFetchDPDPolynomialSplit(niRFmxInstrHandle instrumentHandle, char selectorString[

### RFmxSpecAn_DPDFetchDPDPolynomialSplit

Fetches the memory polynomial or generalized memory polynomial coefficients when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Memory Polynomial** or **Generalized Memory Polynomial**.

#### Syntax

int32 __stdcall RFmxSpecAn_DPDFetchDPDPolynomialSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 dpdPolynomialI[], float32 dpdPolynomialQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| dpdPolynomialI | [out] | float32[] | This parameter Returns the real part of memory polynomial or generalized memory polynomial coefficients when you set the DPD Model attribute to Memory Polynomial or Generalized Memory Polynomial. |
| dpdPolynomialQ | [out] | float32[] | This parameter Returns the imaginary part of memory polynomial or generalized memory polynomial coefficients when you set the DPD Model attribute to Memory Polynomial or Generalized Memory Polynomial. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__fcnt.html language=enus -->
## TOPIC 00521: FCnt

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__fcnt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__fcnt.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_FCntFetchAllanDeviationFetches the two-sample deviation of the measured frequency. RFmxSpecAn_FCntFetchFrequencyTraceFetches the frequency trace for FCnt measurement. RFmxSpecAn_FCntFetchMeasurementReturns the frequency and phase measured using the FC

### FCnt

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_FCntFetchAllanDeviation | Fetches the two-sample deviation of the measured frequency. |
| RFmxSpecAn_FCntFetchFrequencyTrace | Fetches the frequency trace for FCnt measurement. |
| RFmxSpecAn_FCntFetchMeasurement | Returns the frequency and phase measured using the FCnt measurement. |
| RFmxSpecAn_FCntFetchPhaseTrace | Fetches the phase trace for FCnt measurement. |
| RFmxSpecAn_FCntFetchPowerTrace | Fetches the power trace for FCnt measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__fcnt_1ga53eaf88cfd09b97ea5bdc98b398b6fef.html language=enus -->
## TOPIC 00522: RFmxSpecAn_FCntFetchMeasurement

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__fcnt_1ga53eaf88cfd09b97ea5bdc98b398b6fef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__fcnt_1ga53eaf88cfd09b97ea5bdc98b398b6fef.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency and phase measured using the FCnt measurement. Syntaxint32 __stdcall RFmxSpecAn_FCntFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averageRelativeFrequency, float64 *averageAbsoluteFrequency, float64 *meanPhase)ParametersNa

### RFmxSpecAn_FCntFetchMeasurement

Returns the frequency and phase measured using the FCnt measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_FCntFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averageRelativeFrequency, float64 *averageAbsoluteFrequency, float64 *meanPhase)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| averageRelativeFrequency | [out] | float64 * | This parameter returns the signal frequency relative to the RF center frequency. Only samples above the threshold are used when you set the FCnt Threshold Enabled attribute to True. |
| averageAbsoluteFrequency | [out] | float64 * | This parameter returns the RF signal frequency. Only samples above the threshold are used when you set the RFMXSPECAN_ATTR_FCNT_THRESHOLD_ENABLED attribute to True. |
| meanPhase | [out] | float64 * | This parameter returns the net phase of the vector sum of the I/Q samples used for frequency measurement. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

FCnt

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__fcnt_1gaeed87591086819101a7b1e6c5190d087.html language=enus -->
## TOPIC 00523: RFmxSpecAn_FCntFetchPhaseTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__fcnt_1gaeed87591086819101a7b1e6c5190d087.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__fcnt_1gaeed87591086819101a7b1e6c5190d087.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase trace for FCnt measurement. Syntaxint32 __stdcall RFmxSpecAn_FCntFetchPhaseTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseTrace[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptio

### RFmxSpecAn_FCntFetchPhaseTrace

Fetches the phase trace for FCnt measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_FCntFetchPhaseTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| phaseTrace | [out] | float32[] | This parameter returns the averaged phase, in degrees, measured at each time instance. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

FCnt

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__fcnt_1gaf376e035cf6b05d5f8ab1df100a6977c.html language=enus -->
## TOPIC 00524: RFmxSpecAn_FCntFetchFrequencyTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__fcnt_1gaf376e035cf6b05d5f8ab1df100a6977c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__fcnt_1gaf376e035cf6b05d5f8ab1df100a6977c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the frequency trace for FCnt measurement. Syntaxint32 __stdcall RFmxSpecAn_FCntFetchFrequencyTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 frequencyTrace[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTy

### RFmxSpecAn_FCntFetchFrequencyTrace

Fetches the frequency trace for FCnt measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_FCntFetchFrequencyTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 frequencyTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| frequencyTrace | [out] | float32[] | This parameter returns the frequency, in Hz, measured at each time instance. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

FCnt

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__harm_1ga0a7b77fbfebcce677381ef2c1c920c11.html language=enus -->
## TOPIC 00525: RFmxSpecAn_HarmFetchHarmonicMeasurementArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__harm_1ga0a7b77fbfebcce677381ef2c1c920c11.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__harm_1ga0a7b77fbfebcce677381ef2c1c920c11.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of powers measured at the harmonic frequency. Syntaxint32 __stdcall RFmxSpecAn_HarmFetchHarmonicMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 averageRelativePower[], float64 averageAbsolutePower[], float64 rbw[], float64 freque

### RFmxSpecAn_HarmFetchHarmonicMeasurementArray

Returns the array of powers measured at the harmonic frequency.

#### Syntax

int32 __stdcall RFmxSpecAn_HarmFetchHarmonicMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 averageRelativePower[], float64 averageAbsolutePower[], float64 rbw[], float64 frequency[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| averageRelativePower | [out] | float64[] | This parameter returns the array of average powers, in dB, relative to the fundamental power measured at each harmonic. |
| averageAbsolutePower | [out] | float64[] | This parameter returns the array of average absolute powers, in dBm, measured at each harmonic. |
| rbw | [out] | float64[] | This parameter returns the array of resolution bandwidths (RBW), in Hz, which is used by the harmonic measurement, for each harmonic. |
| frequency | [out] | float64[] | This parameter returns the array of frequencies, in Hz, of each harmonic. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Harm

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__harm_1ga5ffa7de9dd08d9bf6fba8803ba2994cf.html language=enus -->
## TOPIC 00526: RFmxSpecAn_HarmFetchHarmonicMeasurement

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__harm_1ga5ffa7de9dd08d9bf6fba8803ba2994cf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__harm_1ga5ffa7de9dd08d9bf6fba8803ba2994cf.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured at the harmonic frequency. Use "harmonic<n>" as the selector channel string to read results from this function. Syntaxint32 __stdcall RFmxSpecAn_HarmFetchHarmonicMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averageRelativ

### RFmxSpecAn_HarmFetchHarmonicMeasurement

Returns the power measured at the harmonic frequency. Use "harmonic<n>" as the selector channel string to read results from this function.

#### Syntax

int32 __stdcall RFmxSpecAn_HarmFetchHarmonicMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averageRelativePower, float64 *averageAbsolutePower, float64 *rbw, float64 *frequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and harmonic number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"harmonic0""signal::sig1/harmonic0""signal::sig1/result::r1/harmonic0""result::r1/harmonic0"You can use the RFmxSpecAn_BuildHarmonicString2 function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| averageRelativePower | [out] | float64 * | This parameter returns the average power, in dB, relative to the fundamental power measured at the harmonic. |
| averageAbsolutePower | [out] | float64 * | This parameter returns the average absolute power, in dBm, measured at the harmonic. |
| rbw | [out] | float64 * | This parameter returns the resolution bandwidth (RBW), in Hz, which is used by the harmonic measurement, for the harmonic. |
| frequency | [out] | float64 * | This parameter returns the RF frequency, in Hz, of the harmonic. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Harm

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__harm_1ga71a1252cd90400c4f5490469ad583409.html language=enus -->
## TOPIC 00527: RFmxSpecAn_HarmFetchHarmonicPowerTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__harm_1ga71a1252cd90400c4f5490469ad583409.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__harm_1ga71a1252cd90400c4f5490469ad583409.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power trace for the harmonics measurement. Use "harmonic<n>" as the selector string to read results from this function. Syntaxint32 __stdcall RFmxSpecAn_HarmFetchHarmonicPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float

### RFmxSpecAn_HarmFetchHarmonicPowerTrace

Fetches the power trace for the harmonics measurement. Use "harmonic<n>" as the selector string to read results from this function.

#### Syntax

int32 __stdcall RFmxSpecAn_HarmFetchHarmonicPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 power[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and harmonic number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"harmonic0""signal::sig1/harmonic0""signal::sig1/result::r1/harmonic0""result::r1/harmonic0"You can use the RFmxSpecAn_BuildHarmonicString2 function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| power | [out] | float32[] | This parameter returns the measured average power, in units specified by RFMXSPECAN_ATTR_SPECTRUM_POWER_UNITS attribute, at each time instance. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Harm

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__idpd.html language=enus -->
## TOPIC 00528: IDPD

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__idpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__idpd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_IDPDFetchEqualizerCoefficientsFetches the trained equalizer coefficients. RFmxSpecAn_IDPDFetchEqualizerCoefficientsSplitFetches the trained equalizer coefficients. RFmxSpecAn_IDPDFetchPredistortedWaveformFetches the predistorted waveform output after

### IDPD

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_IDPDFetchEqualizerCoefficients | Fetches the trained equalizer coefficients. |
| RFmxSpecAn_IDPDFetchEqualizerCoefficientsSplit | Fetches the trained equalizer coefficients. |
| RFmxSpecAn_IDPDFetchPredistortedWaveform | Fetches the predistorted waveform output after the IDPD measurement. |
| RFmxSpecAn_IDPDFetchPredistortedWaveformSplit | Fetches the predistorted waveform output after the IDPD measurement. |
| RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveform | Fetches the averaged acquired waveform, corrected for frequency, phase, and DC offsets, used to perform the IDPD measurement. |
| RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveformSplit | Fetches the averaged acquired waveform, corrected for frequency, phase, and DC offsets, used to perform the IDPD measurement. |
| RFmxSpecAn_IDPDFetchProcessedReferenceWaveform | Fetches the reference waveform used to perform the IDPD measurement. |
| RFmxSpecAn_IDPDFetchProcessedReferenceWaveformSplit | Fetches the reference waveform used to perform the IDPD measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga0cacb60bb7b217762798ad2293eb3f21.html language=enus -->
## TOPIC 00529: RFmxSpecAn_IDPDFetchPredistortedWaveform

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga0cacb60bb7b217762798ad2293eb3f21.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga0cacb60bb7b217762798ad2293eb3f21.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the predistorted waveform output after the IDPD measurement. Syntaxint32 __stdcall RFmxSpecAn_IDPDFetchPredistortedWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle predistortedWaveform[], float64 *papr, float64 *po

### RFmxSpecAn_IDPDFetchPredistortedWaveform

Fetches the predistorted waveform output after the IDPD measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_IDPDFetchPredistortedWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle predistortedWaveform[], float64 *papr, float64 *powerOffset, float64 *gain, int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| predistortedWaveform | [out] | NIComplexSingle[] | This parameter returns the complex baseband samples, in volts. |
| papr | [out] | float64 * | This parameter returns the peak-to-average power ratio of the waveform obtained after applying digital predistortion. This value is expressed in dB. |
| powerOffset | [out] | float64 * | This parameter returns the change in the average power in the waveform due to applying digital predistortion. This value is expressed in dB. |
| gain | [out] | float64 * | This parameter returns the gain of the device under test. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IDPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga3c36cf5165b9cefc9304ec32159ab90f.html language=enus -->
## TOPIC 00530: RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveform

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga3c36cf5165b9cefc9304ec32159ab90f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga3c36cf5165b9cefc9304ec32159ab90f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged acquired waveform, corrected for frequency, phase, and DC offsets, used to perform the IDPD measurement. Syntaxint32 __stdcall RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx,

### RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveform

Fetches the averaged acquired waveform, corrected for frequency, phase, and DC offsets, used to perform the IDPD measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle processedMeanAcquiredWaveform[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| processedMeanAcquiredWaveform | [out] | NIComplexSingle[] | This parameter returns the complex baseband samples, in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IDPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga67f626f4907cf6167910a14a894b5a7e.html language=enus -->
## TOPIC 00531: RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveformSplit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga67f626f4907cf6167910a14a894b5a7e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga67f626f4907cf6167910a14a894b5a7e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged acquired waveform, corrected for frequency, phase, and DC offsets, used to perform the IDPD measurement. Syntaxint32 __stdcall RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64

### RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveformSplit

Fetches the averaged acquired waveform, corrected for frequency, phase, and DC offsets, used to perform the IDPD measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 processedMeanAcquiredWaveformI[], float32 processedMeanAcquiredWaveformQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| processedMeanAcquiredWaveformI | [out] | float32[] | This parameter Returns the real part of complex baseband samples, in volts. |
| processedMeanAcquiredWaveformQ | [out] | float32[] | This parameter Returns the imaginary part of complex baseband samples, in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IDPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga7e166e21200539b65b0d8977fc039134.html language=enus -->
## TOPIC 00532: RFmxSpecAn_IDPDFetchProcessedReferenceWaveform

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga7e166e21200539b65b0d8977fc039134.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__idpd_1ga7e166e21200539b65b0d8977fc039134.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference waveform used to perform the IDPD measurement. Syntaxint32 __stdcall RFmxSpecAn_IDPDFetchProcessedReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle processedReferenceWaveform[], int32 arraySiz

### RFmxSpecAn_IDPDFetchProcessedReferenceWaveform

Fetches the reference waveform used to perform the IDPD measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_IDPDFetchProcessedReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle processedReferenceWaveform[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| processedReferenceWaveform | [out] | NIComplexSingle[] | This parameter returns the complex baseband samples, in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IDPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__im_1ga49634317ff3042e3e3d68d8745b75536.html language=enus -->
## TOPIC 00533: RFmxSpecAn_IMFetchFundamentalMeasurement

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__im_1ga49634317ff3042e3e3d68d8745b75536.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__im_1ga49634317ff3042e3e3d68d8745b75536.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak powers of the two fundamental tones. Syntaxint32 __stdcall RFmxSpecAn_IMFetchFundamentalMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *lowerTonePower, float64 *upperTonePower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]

### RFmxSpecAn_IMFetchFundamentalMeasurement

Fetches the peak powers of the two fundamental tones.

#### Syntax

int32 __stdcall RFmxSpecAn_IMFetchFundamentalMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *lowerTonePower, float64 *upperTonePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerTonePower | [out] | float64 * | This parameter returns the peak power measured around the lower tone frequency when you set the RFMXSPECAN_ATTR_IM_RESULTS_LOWER_TONE_POWER attribute to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled attribute to False, the measurement returns the power at the lower tone frequency. |
| upperTonePower | [out] | float64 * | This parameter returns the peak power measured around the upper tone frequency when you set the IM Local Peak Search Enabled attribute to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled attribute to False, the measurement returns the power at the upper tone frequency. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__im_1ga8e6043f4e60940940b89b55af57c74e1.html language=enus -->
## TOPIC 00534: RFmxSpecAn_IMFetchIntermodMeasurementArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__im_1ga8e6043f4e60940940b89b55af57c74e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__im_1ga8e6043f4e60940940b89b55af57c74e1.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of peak powers of the lower and upper intermods. Syntaxint32 __stdcall RFmxSpecAn_IMFetchIntermodMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 intermodOrder[], float64 lowerIntermodAbsolutePower[], float64 upperIntermodAbsolutePow

### RFmxSpecAn_IMFetchIntermodMeasurementArray

Fetches an array of peak powers of the lower and upper intermods.

#### Syntax

int32 __stdcall RFmxSpecAn_IMFetchIntermodMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 intermodOrder[], float64 lowerIntermodAbsolutePower[], float64 upperIntermodAbsolutePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| intermodOrder | [out] | int32[] | This parameter returns an array of the orders of the intermods. |
| lowerIntermodAbsolutePower | [out] | float64[] | This parameter returns an array of the peak power values measured around the lower intermod frequency when you set the RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED attribute to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled attribute to False, the measurement returns the power at the lower intermod frequency. |
| upperIntermodAbsolutePower | [out] | float64[] | This parameter returns an array of the peak power values measured around the upper intermod frequency when you set the IM Local Peak Search Enabled attribute to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled attribute to False, the measurement returns the power at the upper intermod frequency. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__im_1gab31dc1845e1ad21e8f2bed2b8bbbe981.html language=enus -->
## TOPIC 00535: RFmxSpecAn_IMFetchInterceptPower

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__im_1gab31dc1845e1ad21e8f2bed2b8bbbe981.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__im_1gab31dc1845e1ad21e8f2bed2b8bbbe981.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the output intercept powers for the intermod. Syntaxint32 __stdcall RFmxSpecAn_IMFetchInterceptPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *intermodOrder, float64 *worstCaseOutputInterceptPower, float64 *lowerOutputInterceptPower, float64 *upperOut

### RFmxSpecAn_IMFetchInterceptPower

Fetches the output intercept powers for the intermod.

#### Syntax

int32 __stdcall RFmxSpecAn_IMFetchInterceptPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *intermodOrder, float64 *worstCaseOutputInterceptPower, float64 *lowerOutputInterceptPower, float64 *upperOutputInterceptPower)

#### Remarks

Use "intermod<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and intermod number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"intermod0""signal::sig1/intermod0""result::r1/intermod0""signal::sig1/result::r1/intermod0"You can use the RFmxSpecAn_BuildIntermodString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| intermodOrder | [out] | int32 * | This parameter returns the order of the intermod. |
| worstCaseOutputInterceptPower | [out] | float64 * | This parameter returns the worst case output intercept power which is equal to the minimum of the values of the RFMXSPECAN_ATTR_IM_RESULTS_UPPER_OUTPUT_INTERCEPT_POWER and RFMXSPECAN_ATTR_IM_RESULTS_LOWER_OUTPUT_INTERCEPT_POWER results. This value is expressed in dBm. |
| lowerOutputInterceptPower | [out] | float64 * | This parameter returns the lower output intercept power. This value is expressed in dBm. |
| upperOutputInterceptPower | [out] | float64 * | This parameter returns the upper output intercept power. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__nf_1ga56de723acb4ca19e640d35fec1f9bcf5.html language=enus -->
## TOPIC 00536: RFmxSpecAn_NFFetchDUTNoiseFigureAndGain

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__nf_1ga56de723acb4ca19e640d35fec1f9bcf5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__nf_1ga56de723acb4ca19e640d35fec1f9bcf5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the DUT noise figure, noise temperature and gain results. Syntaxint32 __stdcall RFmxSpecAn_NFFetchDUTNoiseFigureAndGain(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 dutNoiseFigure[], float64 dutNoiseTemperature[], float64 dutGain[], int32 arraySize, int

### RFmxSpecAn_NFFetchDUTNoiseFigureAndGain

Fetches the DUT noise figure, noise temperature and gain results.

#### Syntax

int32 __stdcall RFmxSpecAn_NFFetchDUTNoiseFigureAndGain(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 dutNoiseFigure[], float64 dutNoiseTemperature[], float64 dutGain[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| dutNoiseFigure | [out] | float64[] | This parameter returns an array of the noise figures of the DUT measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dB. |
| dutNoiseTemperature | [out] | float64[] | This parameter returns an array of the equivalent thermal noise temperatures of the DUT measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in kelvin. |
| dutGain | [out] | float64[] | This parameter returns an array of the available gains of the DUT measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__nf_1ga6a366f95aadda7c253e23d483807ab5e.html language=enus -->
## TOPIC 00537: RFmxSpecAn_NFFetchYFactorPowers

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__nf_1ga6a366f95aadda7c253e23d483807ab5e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__nf_1ga6a366f95aadda7c253e23d483807ab5e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the hot and cold powers measured when the Y-Factor based noise figure (NF) measurement is performed. Syntaxint32 __stdcall RFmxSpecAn_NFFetchYFactorPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 hotPower[], float64 coldPower[], int32 arraySize, int

### RFmxSpecAn_NFFetchYFactorPowers

Fetches the hot and cold powers measured when the Y-Factor based noise figure (NF) measurement is performed.

#### Syntax

int32 __stdcall RFmxSpecAn_NFFetchYFactorPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 hotPower[], float64 coldPower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| hotPower | [out] | float64[] | This parameter returns an array of powers measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute, when the noise source is enabled. This value is expressed in dBm. A valid result is returned only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to Y-Factor. |
| coldPower | [out] | float64[] | This parameter returns an array of powers measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute, when the noise source is disabled. This value is expressed in dBm. A valid result is returned only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to Y-Factor. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__obw_1ga2e3e863f63c8d2a5ecc843b5ce473f3d.html language=enus -->
## TOPIC 00538: RFmxSpecAn_OBWFetchSpectrumTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__obw_1ga2e3e863f63c8d2a5ecc843b5ce473f3d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__obw_1ga2e3e863f63c8d2a5ecc843b5ce473f3d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum trace used for the OBW measurement. Syntaxint32 __stdcall RFmxSpecAn_OBWFetchSpectrumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTyp

### RFmxSpecAn_OBWFetchSpectrumTrace

Fetches the spectrum trace used for the OBW measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_OBWFetchSpectrumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the array of averaged powers measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1ga38173e61b394129212622f5ed3e7c43a.html language=enus -->
## TOPIC 00539: RFmxSpecAn_PAVTFetchAmplitudeTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1ga38173e61b394129212622f5ed3e7c43a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1ga38173e61b394129212622f5ed3e7c43a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the amplitude trace for the measurement. Syntaxint32 __stdcall RFmxSpecAn_PAVTFetchAmplitudeTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 amplitude[], int32 arraySize, int32 *actualArraySize)ParametersNam

### RFmxSpecAn_PAVTFetchAmplitudeTrace

Fetches the amplitude trace for the measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_PAVTFetchAmplitudeTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 amplitude[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| amplitude | [out] | float32[] | This parameter returns the amplitude values of the complex baseband samples, in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1gabd6417d6124e5e8d276e424afe23a613.html language=enus -->
## TOPIC 00540: RFmxSpecAn_PAVTFetchPhaseAndAmplitude

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1gabd6417d6124e5e8d276e424afe23a613.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1gabd6417d6124e5e8d276e424afe23a613.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean values of phase and amplitude of the segment. Syntaxint32 __stdcall RFmxSpecAn_PAVTFetchPhaseAndAmplitude(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRelativePhase, float64 *meanRelativeAmplitude, float64 *meanAbsolutePhase, float64 *mean

### RFmxSpecAn_PAVTFetchPhaseAndAmplitude

Fetches the mean values of phase and amplitude of the segment.

#### Syntax

int32 __stdcall RFmxSpecAn_PAVTFetchPhaseAndAmplitude(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRelativePhase, float64 *meanRelativeAmplitude, float64 *meanAbsolutePhase, float64 *meanAbsoluteAmplitude)

#### Remarks

Use "segment<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0".Example:"segment0""signal::sig1/segment0""result::r1/segment0""signal::sig1/result::r1/segment0"You can use the RFmxSpecAn_BuildSegmentString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRelativePhase | [out] | float64 * | This parameter returns the mean phase of the segment, relative to the phase of the reference segment. This value is expressed in degrees. |
| meanRelativeAmplitude | [out] | float64 * | This parameter returns the mean amplitude of the segment, relative to the amplitude of the reference segment. This value is expressed in dB. |
| meanAbsolutePhase | [out] | float64 * | This parameter returns the mean absolute phase of the segment. This value is expressed in degrees. |
| meanAbsoluteAmplitude | [out] | float64 * | This parameter returns the mean absolute amplitude of the segment. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1gac535445a7c58ae195435f973da62245d.html language=enus -->
## TOPIC 00541: RFmxSpecAn_PAVTFetchPhaseTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1gac535445a7c58ae195435f973da62245d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1gac535445a7c58ae195435f973da62245d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase trace for the measurement. Syntaxint32 __stdcall RFmxSpecAn_PAVTFetchPhaseTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 phase[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTy

### RFmxSpecAn_PAVTFetchPhaseTrace

Fetches the phase trace for the measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_PAVTFetchPhaseTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 phase[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| phase | [out] | float32[] | This parameter returns the phase values of the complex baseband samples, in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1gae30522d0ac01948b1ee8cfc0dc72aacd.html language=enus -->
## TOPIC 00542: RFmxSpecAn_PAVTFetchPhaseAndAmplitudeArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1gae30522d0ac01948b1ee8cfc0dc72aacd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__pavt_1gae30522d0ac01948b1ee8cfc0dc72aacd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of mean values of phase and amplitude of the segments. Syntaxint32 __stdcall RFmxSpecAn_PAVTFetchPhaseAndAmplitudeArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRelativePhase[], float64 meanRelativeAmplitude[], float64 meanAbsolutePhase

### RFmxSpecAn_PAVTFetchPhaseAndAmplitudeArray

Fetches an array of mean values of phase and amplitude of the segments.

#### Syntax

int32 __stdcall RFmxSpecAn_PAVTFetchPhaseAndAmplitudeArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRelativePhase[], float64 meanRelativeAmplitude[], float64 meanAbsolutePhase[], float64 meanAbsoluteAmplitude[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRelativePhase | [out] | float64[] | This parameter returns an array of the mean phase of the segment relative to the first segment of the measurement. This value is expressed in degrees. |
| meanRelativeAmplitude | [out] | float64[] | This parameter returns an array of the mean amplitude of the segment relative to the first segment of the measurement. This value is expressed in dB. |
| meanAbsolutePhase | [out] | float64[] | This parameter returns an array of the mean absolute phase of the segment. This value is expressed in degrees. |
| meanAbsoluteAmplitude | [out] | float64[] | This parameter returns an array of the mean absolute amplitude of the segment. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__phasenoise.html language=enus -->
## TOPIC 00543: PhaseNoise

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__phasenoise.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__phasenoise.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_PhaseNoiseFetchCarrierMeasurementFetches the carrier measurement. RFmxSpecAn_PhaseNoiseFetchIntegratedNoiseFetches the integrated noise measurement. RFmxSpecAn_PhaseNoiseFetchMeasuredLogPlotTraceFetches the log plot trace. RFmxSpecAn_PhaseNoiseFetchSm

### PhaseNoise

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_PhaseNoiseFetchCarrierMeasurement | Fetches the carrier measurement. |
| RFmxSpecAn_PhaseNoiseFetchIntegratedNoise | Fetches the integrated noise measurement. |
| RFmxSpecAn_PhaseNoiseFetchMeasuredLogPlotTrace | Fetches the log plot trace. |
| RFmxSpecAn_PhaseNoiseFetchSmoothedLogPlotTrace | Fetches the smoothened log plot trace. |
| RFmxSpecAn_PhaseNoiseFetchSpotNoise | Fetches the spot noise. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__phasenoise_1ga73e54a89aa28bf56418db15a29d2b54d.html language=enus -->
## TOPIC 00544: RFmxSpecAn_PhaseNoiseFetchIntegratedNoise

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__phasenoise_1ga73e54a89aa28bf56418db15a29d2b54d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__phasenoise_1ga73e54a89aa28bf56418db15a29d2b54d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the integrated noise measurement. Syntaxint32 __stdcall RFmxSpecAn_PhaseNoiseFetchIntegratedNoise(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 integratedPhasenoise[], float64 residualPMInRadian[], float64 residualPMInDegree[], float64 residualFm[], floa

### RFmxSpecAn_PhaseNoiseFetchIntegratedNoise

Fetches the integrated noise measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_PhaseNoiseFetchIntegratedNoise(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 integratedPhasenoise[], float64 residualPMInRadian[], float64 residualPMInDegree[], float64 residualFm[], float64 jitter[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| integratedPhasenoise | [out] | float64[] | This parameter returns the integrated phase noise. This value is expressed in dBc. |
| residualPMInRadian | [out] | float64[] | This parameter returns the residual PM in radians. |
| residualPMInDegree | [out] | float64[] | This parameter returns the residual PM. This value is expressed in degrees. |
| residualFm | [out] | float64[] | This parameter returns the residual FM. This value is expressed in Hz. |
| jitter | [out] | float64[] | This parameter returns the jitter. This value is expressed in seconds. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__phasenoise_1gaad09c9b48ef568d76495915099ca43dd.html language=enus -->
## TOPIC 00545: RFmxSpecAn_PhaseNoiseFetchSmoothedLogPlotTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__phasenoise_1gaad09c9b48ef568d76495915099ca43dd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__phasenoise_1gaad09c9b48ef568d76495915099ca43dd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the smoothened log plot trace. Syntaxint32 __stdcall RFmxSpecAn_PhaseNoiseFetchSmoothedLogPlotTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 frequency[], float32 smoothedPhasenoise[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTy

### RFmxSpecAn_PhaseNoiseFetchSmoothedLogPlotTrace

Fetches the smoothened log plot trace.

#### Syntax

int32 __stdcall RFmxSpecAn_PhaseNoiseFetchSmoothedLogPlotTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 frequency[], float32 smoothedPhasenoise[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| frequency | [out] | float32[] | This parameter returns an array of the frequency offsets where phase noise has been measured. |
| smoothedPhasenoise | [out] | float32[] | This parameter returns an array of smoothed phase noise at the frequency offset. This value is expressed in dBc/Hz. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga31e60bc30f4949db47a3feb02372a9f0.html language=enus -->
## TOPIC 00546: RFmxSpecAn_SEMFetchRelativeMaskTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga31e60bc30f4949db47a3feb02372a9f0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga31e60bc30f4949db47a3feb02372a9f0.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the relative mask trace used for SEM measurement. Syntaxint32 __stdcall RFmxSpecAn_SEMFetchRelativeMaskTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 relativeMask[], int32 arraySize, int32 *actualArraySize)ParametersNameDir

### RFmxSpecAn_SEMFetchRelativeMaskTrace

Fetches the relative mask trace used for SEM measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMFetchRelativeMaskTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 relativeMask[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency of the channel. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| relativeMask | [out] | float32[] | This parameter returns relative mask used for the channel. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga3c4de3be489b05e78ef8f4edfb938caf.html language=enus -->
## TOPIC 00547: RFmxSpecAn_SEMFetchLowerOffsetMargin

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga3c4de3be489b05e78ef8f4edfb938caf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga3c4de3be489b05e78ef8f4edfb938caf.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the lower offset segment. Use "offset<n>" as the selector string to read parameters from this function. Syntaxint32 __stdcall RFmxSpecAn_SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], floa

### RFmxSpecAn_SEMFetchLowerOffsetMargin

Returns the measurement status and margin from the limit line measured in the lower offset segment. Use "offset<n>" as the selector string to read parameters from this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter indicates the lower offset measurement status based on measurement limits and the fail criteria that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute.NameValueDescriptionRFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| margin | [out] | float64 * | This parameter returns the margin, in dB, from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. Margin is defined as the maximum difference between the spectrum and the limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Absolute, the margin is with reference to the absolute limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Relative, the margin is with reference to the relative limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Abs AND Rel, the margin is the maximum of the margins referenced to the absolute and relative limit masks.When you set the SEM Offset Seg Limit Fail Mask attribute to Abs OR Rel, the margin is the minimum of the margins referenced to the absolute and relative limit masks. |
| marginFrequency | [out] | float64 * | This parameter returns the frequency, in Hz, at which the margin occurred in the lower (negative) offset. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power, in dBm or dBm/Hz, at which the margin occurred in the lower (negative) offset segment. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the SEM Power Units attribute to dBm/Hz. |
| marginRelativePower | [out] | float64 * | This parameter returns the power, in dB, at which the margin occurred in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga73522252a8a436ee4c3f3c27e79a79d2.html language=enus -->
## TOPIC 00548: RFmxSpecAn_SEMFetchAbsoluteMaskTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga73522252a8a436ee4c3f3c27e79a79d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga73522252a8a436ee4c3f3c27e79a79d2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute mask trace used for SEM measurement. Syntaxint32 __stdcall RFmxSpecAn_SEMFetchAbsoluteMaskTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 absoluteMask[], int32 arraySize, int32 *actualArraySize)ParametersNameDir

### RFmxSpecAn_SEMFetchAbsoluteMaskTrace

Fetches the absolute mask trace used for SEM measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMFetchAbsoluteMaskTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 absoluteMask[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency of the channel. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| absoluteMask | [out] | float32[] | This parameter returns absolute mask used for the channel. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga9c7cebf255f1ae35de73d120c42c56ce.html language=enus -->
## TOPIC 00549: RFmxSpecAn_SEMFetchUpperOffsetMarginArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga9c7cebf255f1ae35de73d120c42c56ce.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__sem_1ga9c7cebf255f1ae35de73d120c42c56ce.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segments. Syntaxint32 __stdcall RFmxSpecAn_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 margin

### RFmxSpecAn_SEMFetchUpperOffsetMarginArray

Returns the measurement status and margin from the limit line measured in the upper offset segments.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns the array of upper offset measurement statuses based on measurement limits and the fail criteria that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute.NameValueDescriptionRFMXSPECAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXSPECAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXSPECAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| margin | [out] | float64[] | This parameter returns the array of margins, in dB, from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. Margin is defined as the maximum difference between the spectrum and the limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Absolute, the margin is with reference to the absolute limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Relative, the margin is with reference to the relative limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Abs AND Rel, the margin is the maximum of the margins referenced to the absolute and relative limit masks.When you set the SEM Offset Seg Limit Fail Mask attribute to Abs OR Rel, the margin is the minimum of the margins referenced to the absolute and relative limit masks. |
| marginFrequency | [out] | float64[] | This parameter returns the array of frequencies, in Hz, at which the margin occurred in each upper (positive) offset. |
| marginAbsolutePower | [out] | float64[] | This parameter returns the array of powers, in dBm or dBm/Hz, at which the margin occurred in each upper (positive) offset segment. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the SEM Power Units attribute to dBm/Hz. |
| marginRelativePower | [out] | float64[] | This parameter returns the array of powers, in dB, at which the margin occurred in each upper (positive) offset segment relative to the integrated or peak power of the reference carrier. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gac2a8f30daf12c2e488ae1bb73ab39965.html language=enus -->
## TOPIC 00550: RFmxSpecAn_SEMFetchLowerOffsetMarginArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gac2a8f30daf12c2e488ae1bb73ab39965.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gac2a8f30daf12c2e488ae1bb73ab39965.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments. Syntaxint32 __stdcall RFmxSpecAn_SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], fl

### RFmxSpecAn_SEMFetchLowerOffsetMarginArray

Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns the array of lower offset measurement statuses based on measurement limits and the fail criteria that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute.NameValueDescriptionRFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| margin | [out] | float64[] | This parameter returns the array of margins, in dB, from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. Margin is defined as the maximum difference between the spectrum and the limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Absolute, the margin is with reference to the absolute limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Relative, the margin is with reference to the relative limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Abs AND Rel, the margin is the maximum of the margins referenced to the absolute and relative limit masks.When you set the SEM Offset Seg Limit Fail Mask attribute to Abs OR Rel, the margin is the minimum of the margins referenced to the absolute and relative limit masks. |
| marginFrequency | [out] | float64[] | This parameter returns the array of frequencies, in Hz, at which the margin occurred in each lower (negative) offset segment. |
| marginAbsolutePower | [out] | float64[] | This parameter returns the array of powers, in dBm or dBm/Hz, at which the margin occurred in the lower (negative) offset segment. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the SEM Power Units attribute to dBm/Hz. |
| marginRelativePower | [out] | float64[] | This parameter returns the array of powers, in dB, at which the margin occurred in each lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gac3c5a5e5e7b6438b196d582cd4eb2bd0.html language=enus -->
## TOPIC 00551: RFmxSpecAn_SEMFetchUpperOffsetPower

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gac3c5a5e5e7b6438b196d582cd4eb2bd0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gac3c5a5e5e7b6438b196d582cd4eb2bd0.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper offset segment power measurements. Use "offset<n>" as the selector string to read parameters from this function. Syntaxint32 __stdcall RFmxSpecAn_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAbsolutePower, float6

### RFmxSpecAn_SEMFetchUpperOffsetPower

Returns the upper offset segment power measurements. Use "offset<n>" as the selector string to read parameters from this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAbsolutePower, float64 *totalRelativePower, float64 *peakAbsolutePower, float64 *peakFrequency, float64 *peakRelativePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalAbsolutePower | [out] | float64 * | This parameter returns the upper (positive) offset segment power measured.The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the SEM Power Units attribute to dBm/Hz. |
| totalRelativePower | [out] | float64 * | This parameter returns the power in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier.When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to Integration, the reference carrier power is the total power in the reference carrier. When you set the SEM Ref Type attribute to Peak, the reference carrier power is the peak power in the reference. |
| peakAbsolutePower | [out] | float64 * | This parameter returns the peak power measured in the upper (positive) offset segment. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the SEM Power Units attribute to dBm/Hz. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency, in Hz, at which the peak power occurred in the offset segment. |
| peakRelativePower | [out] | float64 * | This parameter returns the peak power in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier.When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to Integration, the reference carrier power is the total power in the reference carrier. When you set the SEM Ref Type attribute to Peak, the reference carrier power is the peak power in the reference carrier. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gac4c749c9fab86717cda17437aeb42839.html language=enus -->
## TOPIC 00552: RFmxSpecAn_SEMFetchUpperOffsetMargin

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gac4c749c9fab86717cda17437aeb42839.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gac4c749c9fab86717cda17437aeb42839.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segment. Use "offset<n>" as the selector string to read parameters from this function. Syntaxint32 __stdcall RFmxSpecAn_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], floa

### RFmxSpecAn_SEMFetchUpperOffsetMargin

Returns the measurement status and margin from the limit line measured in the upper offset segment. Use "offset<n>" as the selector string to read parameters from this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter indicates the upper offset measurement status based on measurement limits and the fail criteria that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute.NameValueDescriptionRFMXSPECAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXSPECAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXSPECAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| margin | [out] | float64 * | This parameter returns the margin, in dB, from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. Margin is defined as the maximum difference between the spectrum and the limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Absolute, the margin is with reference to the absolute limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Relative, the margin is with reference to the relative limit mask.When you set the SEM Offset Seg Limit Fail Mask attribute to Abs AND Rel, the margin is the maximum of the margins referenced to the absolute and relative limit masks.When you set the SEM Offset Seg Limit Fail Mask attribute to Abs OR Rel, the margin is the minimum of the margins referenced to the absolute and relative limit masks. |
| marginFrequency | [out] | float64 * | This parameter returns the frequency, in Hz, at which the margin occurred in the upper (positive) offset. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power, in dBm or dBm/Hz, at which the margin occurred in the upper (positive) offset segment. The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the SEM Power Units attribute to dBm/Hz. |
| marginRelativePower | [out] | float64 * | This parameter returns the power, in dB, at which the margin occurred in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gaddaeffad6c6f56de7fc3560c98c7a934.html language=enus -->
## TOPIC 00553: RFmxSpecAn_SEMFetchFrequencyResolution

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gaddaeffad6c6f56de7fc3560c98c7a934.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gaddaeffad6c6f56de7fc3560c98c7a934.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency bin spacing, in Hz, of the spectrum acquired by the measurement. Syntaxint32 __stdcall RFmxSpecAn_SEMFetchFrequencyResolution(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *frequencyResolution)ParametersNameDirectionTypeDescriptioninstrumen

### RFmxSpecAn_SEMFetchFrequencyResolution

Returns the frequency bin spacing, in Hz, of the spectrum acquired by the measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMFetchFrequencyResolution(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *frequencyResolution)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| frequencyResolution | [out] | float64 * | This parameter returns the frequency bin spacing, in Hz, of the spectrum acquired by the measurement. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gadf3f028e7ba710f7404775d64e5e2a35.html language=enus -->
## TOPIC 00554: RFmxSpecAn_SEMFetchLowerOffsetPowerArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gadf3f028e7ba710f7404775d64e5e2a35.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__sem_1gadf3f028e7ba710f7404775d64e5e2a35.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of lower offset segment power measurements. Syntaxint32 __stdcall RFmxSpecAn_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 p

### RFmxSpecAn_SEMFetchLowerOffsetPowerArray

Returns the arrays of lower offset segment power measurements.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalAbsolutePower | [out] | float64[] | This parameter returns the array of lower (negative) offset segment powers measured.The power is measured in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the SEM Power Units attribute to dBm/Hz. |
| totalRelativePower | [out] | float64[] | This parameter returns the array of powers in each lower (negative) offset segment relative to the integrated or peak power of the reference carrier.When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to Integration, the reference carrier power is the total power in the reference carrier. When you set the SEM Ref Type attribute to Peak, the reference carrier power is the peak power in the reference. |
| peakAbsolutePower | [out] | float64[] | This parameter returns the array of peak powers measured in each lower (negative) offset segment. The power is measured in dBm when you set the SEM Power Units attribute to dBm, and in dBm/Hz when you set the SEM Power Units attribute to dBm/Hz. |
| peakFrequency | [out] | float64[] | This parameter returns the array of frequencies, in Hz, at which the peak power occurred in each offset segment. |
| peakRelativePower | [out] | float64[] | This parameter returns the array of peak powers in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier.When you set the SEM Ref Type attribute to Integration, the reference carrier power is the total power in the reference carrier. When you set the SEM Ref Type attribute to Peak, the reference carrier power is the peak power in the reference carrier. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__spectrum.html language=enus -->
## TOPIC 00555: Spectrum

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__spectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__spectrum.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_SpectrumFetchMeasurementFetches the peak amplitude and frequency at which the peak occurred in the spectrum. RFmxSpecAn_SpectrumFetchPowerTraceFetches the power trace for the Spectrum measurement. RFmxSpecAn_SpectrumFetchSpectrumFetches the spectrum u

### Spectrum

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_SpectrumFetchMeasurement | Fetches the peak amplitude and frequency at which the peak occurred in the spectrum. |
| RFmxSpecAn_SpectrumFetchPowerTrace | Fetches the power trace for the Spectrum measurement. |
| RFmxSpecAn_SpectrumFetchSpectrum | Fetches the spectrum used for the Spectrum measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__spectrum_1gaa60fdcc95c5438b5cfbdcc8b2d00d09c.html language=enus -->
## TOPIC 00556: RFmxSpecAn_SpectrumFetchPowerTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__spectrum_1gaa60fdcc95c5438b5cfbdcc8b2d00d09c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__spectrum_1gaa60fdcc95c5438b5cfbdcc8b2d00d09c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power trace for the Spectrum measurement. Syntaxint32 __stdcall RFmxSpecAn_SpectrumFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 power[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDes

### RFmxSpecAn_SpectrumFetchPowerTrace

Fetches the power trace for the Spectrum measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_SpectrumFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 power[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| power | [out] | float32[] | This parameter returns the measured average power, in units specified by RFMXSPECAN_ATTR_SPECTRUM_POWER_UNITS attribute, at each time instance. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__spectrum_1gaf2cbc822e84ad852ea6f951c6ef5518b.html language=enus -->
## TOPIC 00557: RFmxSpecAn_SpectrumFetchMeasurement

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__spectrum_1gaf2cbc822e84ad852ea6f951c6ef5518b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__spectrum_1gaf2cbc822e84ad852ea6f951c6ef5518b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak amplitude and frequency at which the peak occurred in the spectrum. Syntaxint32 __stdcall RFmxSpecAn_SpectrumFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *peakAmplitude, float64 *peakFrequency, float64 *frequencyResolution)Para

### RFmxSpecAn_SpectrumFetchMeasurement

Fetches the peak amplitude and frequency at which the peak occurred in the spectrum.

#### Syntax

int32 __stdcall RFmxSpecAn_SpectrumFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *peakAmplitude, float64 *peakFrequency, float64 *frequencyResolution)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| peakAmplitude | [out] | float64 * | This parameter returns the peak amplitude, of the averaged spectrum. When you set the RFMXSPECAN_ATTR_SPECTRUM_SPAN attribute to 0, this function returns the peak amplitude in the time domain power trace. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency, in Hz, at the peak amplitude of the averaged spectrum. This parameter is not valid if you set the Spectrum Span attribute to 0. |
| frequencyResolution | [out] | float64 * | This parameter returns the frequency bin spacing, in Hz, of the spectrum acquired by the measurement. This parameter is not valid if you set the Spectrum Span attribute to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__spur_1ga72b2d9e75a983738ce1a5c4903614ce9.html language=enus -->
## TOPIC 00558: RFmxSpecAn_SpurFetchRangeStatusArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__spur_1ga72b2d9e75a983738ce1a5c4903614ce9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__spur_1ga72b2d9e75a983738ce1a5c4903614ce9.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the range status for Spur measurements. Syntaxint32 __stdcall RFmxSpecAn_SpurFetchRangeStatusArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 rangeStatus[], int32 numberOfDetectedSpurs[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTy

### RFmxSpecAn_SpurFetchRangeStatusArray

Fetches the range status for Spur measurements.

#### Syntax

int32 __stdcall RFmxSpecAn_SpurFetchRangeStatusArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 rangeStatus[], int32 numberOfDetectedSpurs[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rangeStatus | [out] | int32[] | This parameter indicates the array of measurement statuses for each frequency range. |
| numberOfDetectedSpurs | [out] | int32[] | This parameter returns the array of number of detected spurious emissions (Spur) in each frequency range. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__marker.html language=enus -->
## TOPIC 00559: Marker

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__marker.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__marker.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_MarkerCfgBandSpanConfigures the band span of the selected marker. Use "marker<n>" as the selector string to configure this function. RFmxSpecAn_MarkerCfgFunctionTypeConfigures the marker function type. RFmxSpecAn_MarkerCfgNumberOfMarkersConfigures the

### Marker

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_MarkerCfgBandSpan | Configures the band span of the selected marker. Use "marker<n>" as the selector string to configure this function. |
| RFmxSpecAn_MarkerCfgFunctionType | Configures the marker function type. |
| RFmxSpecAn_MarkerCfgNumberOfMarkers | Configures the number of markers. |
| RFmxSpecAn_MarkerCfgPeakExcursion | Configures the peak excursion. |
| RFmxSpecAn_MarkerCfgReferenceMarker | Configures the reference marker to a delta marker. |
| RFmxSpecAn_MarkerCfgThreshold | Configures the threshold to use for peak search. |
| RFmxSpecAn_MarkerCfgTrace | Configures the measurement trace to be used by the marker. Use "marker<n>" as the selector string to configure this function. |
| RFmxSpecAn_MarkerCfgType | Configures the marker type. Use "marker<n>" as the selector string to configure this function. |
| RFmxSpecAn_MarkerCfgXLocation | Configures the X location of the marker. You must configure the reference marker X location or perform peak search on the reference marker before configuring the X location for the Delta marker. Use "marker<n>" as the selector string to configure this function. |
| RFmxSpecAn_MarkerCfgYLocation | Configures the Y location of the marker. You must configure the reference marker Y location or perform peak search on the reference marker before configuring the X location for the Delta marker. |
| RFmxSpecAn_MarkerFetchFunctionValue | Returns the function value of the selected marker function type. |
| RFmxSpecAn_MarkerFetchXY | Returns the X and Y locations of the marker. |
| RFmxSpecAn_MarkerNextPeak | Moves the marker to the next highest or next left or next right peak above the threshold on the configured trace. Use "marker<n>" as the selector string to read results from this function. |
| RFmxSpecAn_MarkerPeakSearch | Moves the marker to the highest peak that satisfies peak threshold and peak excursion criteria. Use "marker<n>" as the selector string to read results from this function. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__marker_1ga06b7233f4f23169c516514b9af7ba7b2.html language=enus -->
## TOPIC 00560: RFmxSpecAn_MarkerCfgYLocation

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__marker_1ga06b7233f4f23169c516514b9af7ba7b2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__marker_1ga06b7233f4f23169c516514b9af7ba7b2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Y location of the marker. You must configure the reference marker Y location or perform peak search on the reference marker before configuring the X location for the Delta marker. Syntaxint32 __stdcall RFmxSpecAn_MarkerCfgYLocation(niRFmxInstrHandle instrumentHandle, char selectorStri

### RFmxSpecAn_MarkerCfgYLocation

Configures the Y location of the marker. You must configure the reference marker Y location or perform peak search on the reference marker before configuring the X location for the Delta marker.

#### Syntax

int32 __stdcall RFmxSpecAn_MarkerCfgYLocation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 markerYLocation)

#### Remarks

Use "marker<n>" as the selector string to configure this function.

Note

You can configure the Y location of the marker only if you set the Marker Type parameter to **Fixed**.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used.Example:"marker0""signal::sig1/marker0"You can use the RFmxSpecAn_BuildMarkerString2 function to build the selector string. |
| markerYLocation | [in] | float64 | This parameter specifies the Y location of the marker when you set the Marker Type parameter to Fixed. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__marker_1ga08fe3e1cf337c0d28a0cc670e0e269e6.html language=enus -->
## TOPIC 00561: RFmxSpecAn_MarkerCfgNumberOfMarkers

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__marker_1ga08fe3e1cf337c0d28a0cc670e0e269e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__marker_1ga08fe3e1cf337c0d28a0cc670e0e269e6.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of markers. Syntaxint32 __stdcall RFmxSpecAn_MarkerCfgNumberOfMarkers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfMarkers)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. In

### RFmxSpecAn_MarkerCfgNumberOfMarkers

Configures the number of markers.

#### Syntax

int32 __stdcall RFmxSpecAn_MarkerCfgNumberOfMarkers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfMarkers)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| numberOfMarkers | [in] | int32 | This parameter specifies the number of markers. The default value is 12. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__marker_1ga136267c33bb37b9c2c9c3ebafd532927.html language=enus -->
## TOPIC 00562: RFmxSpecAn_MarkerCfgThreshold

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__marker_1ga136267c33bb37b9c2c9c3ebafd532927.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__marker_1ga136267c33bb37b9c2c9c3ebafd532927.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the threshold to use for peak search. Syntaxint32 __stdcall RFmxSpecAn_MarkerCfgThreshold(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 thresholdEnabled, float64 threshold)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifie

### RFmxSpecAn_MarkerCfgThreshold

Configures the threshold to use for peak search.

#### Syntax

int32 __stdcall RFmxSpecAn_MarkerCfgThreshold(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 thresholdEnabled, float64 threshold)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| thresholdEnabled | [in] | int32 | This parameter specifies whether to enable the threshold for the trace while finding the peaks. The default value is False.Name (Value)DescriptionFalse (0)Disables the threshold for the trace while finding the peaksTrue (1)Enables the threshold for the trace while finding the peaks |
| Name (Value) | Description |  |  |
| False (0) | Disables the threshold for the trace while finding the peaks |  |  |
| True (1) | Enables the threshold for the trace while finding the peaks |  |  |
| threshold | [in] | float64 | This parameter specifies the threshold for finding the peaks on the trace. The default value is -90. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__marker_1ga1fe9d3abfff441615aef198bfe90719c.html language=enus -->
## TOPIC 00563: RFmxSpecAn_MarkerCfgXLocation

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__marker_1ga1fe9d3abfff441615aef198bfe90719c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__marker_1ga1fe9d3abfff441615aef198bfe90719c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the X location of the marker. You must configure the reference marker X location or perform peak search on the reference marker before configuring the X location for the Delta marker. Use "marker<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_Marke

### RFmxSpecAn_MarkerCfgXLocation

Configures the X location of the marker. You must configure the reference marker X location or perform peak search on the reference marker before configuring the X location for the Delta marker. Use "marker<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_MarkerCfgXLocation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 markerXLocation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used.Example:"marker0""signal::sig1/marker0"You can use the RFmxSpecAn_BuildMarkerString2 function to build the selector string. |
| markerXLocation | [in] | float64 | This parameter specifies the X location of the marker on the trace when you set the Marker Type parameter to Normal or Fixed. The X location is relative to the value of the reference marker when you set the Marker Type parameter to Delta. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__marker_1ga30de076b91a83e077713d266f2e0f8c3.html language=enus -->
## TOPIC 00564: RFmxSpecAn_MarkerCfgBandSpan

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__marker_1ga30de076b91a83e077713d266f2e0f8c3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__marker_1ga30de076b91a83e077713d266f2e0f8c3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the band span of the selected marker. Use "marker<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_MarkerCfgBandSpan(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 span)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niR

### RFmxSpecAn_MarkerCfgBandSpan

Configures the band span of the selected marker. Use "marker<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_MarkerCfgBandSpan(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 span)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used.Example:"marker0""signal::sig1/marker0"You can use the RFmxSpecAn_BuildMarkerString2 function to build the selector string. |
| span | [in] | float64 | This parameter specifies the width of the span for the selected marker. This attribute selects the trace data within the specified span to perform specified marker function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__marker_1ga42289e47205d85a6346992cc610c2947.html language=enus -->
## TOPIC 00565: RFmxSpecAn_MarkerNextPeak

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__marker_1ga42289e47205d85a6346992cc610c2947.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__marker_1ga42289e47205d85a6346992cc610c2947.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the marker to the next highest or next left or next right peak above the threshold on the configured trace. Use "marker<n>" as the selector string to read results from this function. Syntaxint32 __stdcall RFmxSpecAn_MarkerNextPeak(niRFmxInstrHandle instrumentHandle, char selectorString[], int3

### RFmxSpecAn_MarkerNextPeak

Moves the marker to the next highest or next left or next right peak above the threshold on the configured trace. Use "marker<n>" as the selector string to read results from this function.

#### Syntax

int32 __stdcall RFmxSpecAn_MarkerNextPeak(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 nextPeak, int32 *nextPeakFound)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and marker number. If you do not specify the signal name, the default signal instance is used.Example:"marker0""signal::sig1/marker0""result::r1/marker0""signal::sig1/result::r1/marker0"You can use the RFmxSpecAn_BuildMarkerString2 function to build the selector string. |
| nextPeak | [in] | int32 | This parameter specifies the next peak on the trace. The default value is Next Highest.Name (Value)DescriptionNext Highest (0)Moves the marker to the next highest peak above the threshold on the configured trace.Next Left (1)Moves the marker to the next peak to the left of the configured trace.Next Right (2)Moves the marker to the next peak to the right of the configured trace. |
| Name (Value) | Description |  |  |
| Next Highest (0) | Moves the marker to the next highest peak above the threshold on the configured trace. |  |  |
| Next Left (1) | Moves the marker to the next peak to the left of the configured trace. |  |  |
| Next Right (2) | Moves the marker to the next peak to the right of the configured trace. |  |  |
| nextPeakFound | [out] | int32 * | This parameter indicates whether the function has found the next peak on the trace. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__marker_1gae85da68c127b0eee4978ae54b7eec0fb.html language=enus -->
## TOPIC 00566: RFmxSpecAn_MarkerCfgType

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__marker_1gae85da68c127b0eee4978ae54b7eec0fb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__marker_1gae85da68c127b0eee4978ae54b7eec0fb.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the marker type. Use "marker<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_MarkerCfgType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 markerType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis pa

### RFmxSpecAn_MarkerCfgType

Configures the marker type. Use "marker<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_MarkerCfgType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 markerType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used.Example:"marker0""signal::sig1/marker0"You can use the RFmxSpecAn_BuildMarkerString2 function to build the selector string. |
| markerType | [in] | int32 | This parameter specifies whether the marker is disabled (Off) or is enabled (On) as a normal marker, delta marker or a fixed marker. The default value is Off.Name (Value)DescriptionOff (0)The marker is disabled.Normal (1)The marker is enabled as a normal marker.Delta (3)The marker is enabled as a delta marker.Fixed (4)The marker is enabled as a fixed marker. |
| Name (Value) | Description |  |  |
| Off (0) | The marker is disabled. |  |  |
| Normal (1) | The marker is enabled as a normal marker. |  |  |
| Delta (3) | The marker is enabled as a delta marker. |  |  |
| Fixed (4) | The marker is enabled as a fixed marker. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__marker_1gaff76eda29d4522412d325188456efdc2.html language=enus -->
## TOPIC 00567: RFmxSpecAn_MarkerCfgPeakExcursion

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__marker_1gaff76eda29d4522412d325188456efdc2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__marker_1gaff76eda29d4522412d325188456efdc2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the peak excursion. Syntaxint32 __stdcall RFmxSpecAn_MarkerCfgPeakExcursion(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 peakExcursionEnabled, float64 peakExcursion)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxSpecAn_MarkerCfgPeakExcursion

Configures the peak excursion.

#### Syntax

int32 __stdcall RFmxSpecAn_MarkerCfgPeakExcursion(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 peakExcursionEnabled, float64 peakExcursion)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| peakExcursionEnabled | [in] | int32 | This parameter specifies whether to enable the peak excursion check for the trace while finding the peaks. The default value is False.Name (Value)DescriptionFalse (0)Disables the peak excursion check for the trace while finding the peaks.True (1)Enables the peak excursion check for the trace while finding the peaks. |
| Name (Value) | Description |  |  |
| False (0) | Disables the peak excursion check for the trace while finding the peaks. |  |  |
| True (1) | Enables the peak excursion check for the trace while finding the peaks. |  |  |
| peakExcursion | [in] | float64 | This parameter specifies the peak excursion value for finding the peaks on trace when you set the Peak Excursion Enabled parameter to True. The signal should rise and fall by at least the peak excursion value, above the threshold, to be considered as a peak. The default value is 6. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__read.html language=enus -->
## TOPIC 00568: Read

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__read.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__read.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_ACPReadConfigures hardware for acquisition, performs measurement on acquired data, and returns the adjacent channel power (ACP) measurement results. RFmxSpecAn_CCDFReadConfigures hardware for acquisition, performs measurement on acquired data, and ret

### Read

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_ACPRead | Configures hardware for acquisition, performs measurement on acquired data, and returns the adjacent channel power (ACP) measurement results. |
| RFmxSpecAn_CCDFRead | Configures hardware for acquisition, performs measurement on acquired data, and returns complementary cumulative distribution function (CCDF) measurement results. |
| RFmxSpecAn_CHPRead | Configures hardware for acquisition, performs measurement on acquired data, and returns the channel power (CHP) measurement results. |
| RFmxSpecAn_FCntRead | Configures hardware for acquisition, performs measurement on acquired data, and returns the frequency count (FCnt) measurement results. |
| RFmxSpecAn_HarmRead | Configures hardware for acquisition, performs measurement on acquired data, and returns Harmonics measurement results. |
| RFmxSpecAn_OBWRead | Configures hardware for acquisition, performs measurement on acquired data, and returns occupied bandwidth (OBW) measurement results. |
| RFmxSpecAn_SpectrumRead | Configures hardware for acquisition, performs measurement on acquired data, and returns Spectrum measurement results. |
| RFmxSpecAn_TXPRead | Configures hardware for acquisition, performs measurement on acquired data, and returns the transmit power (TXP) measurement results. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__read_1ga0e4a65435963c49689892d94e0e83c38.html language=enus -->
## TOPIC 00569: RFmxSpecAn_OBWRead

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__read_1ga0e4a65435963c49689892d94e0e83c38.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__read_1ga0e4a65435963c49689892d94e0e83c38.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns occupied bandwidth (OBW) measurement results. Syntaxint32 __stdcall RFmxSpecAn_OBWRead(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *averagePower

### RFmxSpecAn_OBWRead

Configures hardware for acquisition, performs measurement on acquired data, and returns occupied bandwidth (OBW) measurement results.

#### Syntax

int32 __stdcall RFmxSpecAn_OBWRead(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *averagePower, float64 *frequencyResolution, float64 *startFrequency, float64 *stopFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. The default value is 10. |
| occupiedBandwidth | [out] | float64 * | This parameter returns the occupied bandwidth, in Hz. |
| averagePower | [out] | float64 * | This parameter returns the total integrated power of the averaged spectrum acquired by the OBW measurement when you set the RFMXSPECAN_ATTR_OBW_POWER_UNITS attribute to dBm. This function returns the power spectral density when you set the OBW Power Units attribute to dBm/Hz. |
| frequencyResolution | [out] | float64 * | This parameter returns the frequency bin spacing, in Hz, of the spectrum acquired by the OBW measurement. |
| startFrequency | [out] | float64 * | This parameter returns the start frequency, in Hz, of the OBW. The OBW is calculated using the following formula: OBW = stop frequency - start frequency |
| stopFrequency | [out] | float64 * | This parameter returns the stop frequency, in Hz, of the OBW. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Read

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__read_1ga222286de2c157f1a3a728138cc56ca24.html language=enus -->
## TOPIC 00570: RFmxSpecAn_CCDFRead

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__read_1ga222286de2c157f1a3a728138cc56ca24.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__read_1ga222286de2c157f1a3a728138cc56ca24.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns complementary cumulative distribution function (CCDF) measurement results. Syntaxint32 __stdcall RFmxSpecAn_CCDFRead(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanPower,

### RFmxSpecAn_CCDFRead

Configures hardware for acquisition, performs measurement on acquired data, and returns complementary cumulative distribution function (CCDF) measurement results.

#### Syntax

int32 __stdcall RFmxSpecAn_CCDFRead(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanPower, float64 *meanPowerPercentile, float64 *peakPower, int32 *measuredSamplesCount)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. The default value is 10. |
| meanPower | [out] | float64 * | This parameter returns the average power, in dBm, of all the samples. If you set the RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED attribute to True, samples above the threshold are measured. |
| meanPowerPercentile | [out] | float64 * | This parameter returns the percentage of samples that have more power than the mean power. |
| peakPower | [out] | float64 * | This parameter returns the peak power of the acquired signal, relative to the mean power. |
| measuredSamplesCount | [out] | int32 * | This parameter returns the total number of samples measured. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Read

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__read_1ga50f340c50250458b7e8a6545c51e82a7.html language=enus -->
## TOPIC 00571: RFmxSpecAn_TXPRead

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__read_1ga50f340c50250458b7e8a6545c51e82a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__read_1ga50f340c50250458b7e8a6545c51e82a7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns the transmit power (TXP) measurement results. Syntaxint32 __stdcall RFmxSpecAn_TXPRead(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averageMeanPower, float64 *peakToAverage

### RFmxSpecAn_TXPRead

Configures hardware for acquisition, performs measurement on acquired data, and returns the transmit power (TXP) measurement results.

#### Syntax

int32 __stdcall RFmxSpecAn_TXPRead(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averageMeanPower, float64 *peakToAverageRatio, float64 *maximumPower, float64 *minimumPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. The default value is 10. |
| averageMeanPower | [out] | float64 * | This parameter returns the mean power, in dBm, of the signal. Only the samples above the threshold are used by the measurement when you set the RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED attribute to True. When you set the RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED attribute to True, the mean power is measured on the power trace averaged over multiple acquisitions. |
| peakToAverageRatio | [out] | float64 * | This parameter returns the ratio of the peak power of the signal to the mean power. Only the samples above the threshold are used by the measurement when you set the TXP Threshold Enabled attribute to True. When you set the TXP Averaging Enabled attribute to True, the peak and mean powers are measured using the power trace averaged over multiple acquisitions. |
| maximumPower | [out] | float64 * | This parameter returns the maximum power, in dBm, of the averaged power trace. |
| minimumPower | [out] | float64 * | This parameter returns the minimum power, in dBm, of the averaged power trace. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Read

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__read_1gae1abf7daaca029639b456d12ab9c6a95.html language=enus -->
## TOPIC 00572: RFmxSpecAn_ACPRead

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__read_1gae1abf7daaca029639b456d12ab9c6a95.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__read_1gae1abf7daaca029639b456d12ab9c6a95.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns the adjacent channel power (ACP) measurement results. Syntaxint32 __stdcall RFmxSpecAn_ACPRead(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsolutePower, float64 *o

### RFmxSpecAn_ACPRead

Configures hardware for acquisition, performs measurement on acquired data, and returns the adjacent channel power (ACP) measurement results.

#### Syntax

int32 __stdcall RFmxSpecAn_ACPRead(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsolutePower, float64 *offsetCh0LowerRelativePower, float64 *offsetCh0UpperRelativePower, float64 *offsetCh1LowerRelativePower, float64 *offsetCh1UpperRelativePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. The default value is 10. |
| carrierAbsolutePower | [out] | float64 * | This parameter returns the power measured in carrier 0. The carrier power is reported in dBm or dBm/Hz based on the value of the RFMXSPECAN_ATTR_ACP_POWER_UNITS attribute. |
| offsetCh0LowerRelativePower | [out] | float64 * | This parameter returns the power measured in offset 0 in the negative band, relative to the power measured in the reference carrier specified using the RFMXSPECAN_ATTR_ACP_RESULTS_LOWER_OFFSET_POWER_REFERENCE_CARRIER attribute. |
| offsetCh0UpperRelativePower | [out] | float64 * | This parameter returns the power measured in offset 0 in the positive band, relative to the power measured in the reference carrier specified using the RFMXSPECAN_ATTR_ACP_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER attribute. |
| offsetCh1LowerRelativePower | [out] | float64 * | This parameter returns the power measured in offset 1 in the negative band, relative to the power measured in the reference carrier specified using the ACP Results Lower Offset Pwr Ref Carrier attribute. |
| offsetCh1UpperRelativePower | [out] | float64 * | This parameter returns the power measured in offset 1 in the positive band, relative to the power measured in the reference carrier specified using the ACP Results Upper Offset Pwr Ref Carrier attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Read

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__select__measurement.html language=enus -->
## TOPIC 00573: Select Measurement

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__select__measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__select__measurement.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_SelectMeasurementsEnables all the measurements that you specify in the Measurements parameter and disables all other measurements. AttachmentsNone

### Select Measurement

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_SelectMeasurements | Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes.html language=enus -->
## TOPIC 00574: Get Attributes

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_GetAttributeF32Queries the value of an RFmx 32-bit floating point number (float32) attribute. RFmxSpecAn_GetAttributeF32ArrayQueries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buf

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_GetAttributeF32 | Queries the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxSpecAn_GetAttributeF32Array | Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxSpecAn_GetAttributeF64 | Queries the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxSpecAn_GetAttributeF64Array | Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxSpecAn_GetAttributeI16 | Queries the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxSpecAn_GetAttributeI32 | Queries the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxSpecAn_GetAttributeI32Array | Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxSpecAn_GetAttributeI64 | Queries the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxSpecAn_GetAttributeI64Array | Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxSpecAn_GetAttributeI8 | Queries the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxSpecAn_GetAttributeI8Array | Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxSpecAn_GetAttributeNIComplexDoubleArray | Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxSpecAn_GetAttributeNIComplexSingleArray | Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxSpecAn_GetAttributeString | Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxSpecAn_GetAttributeU16 | Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxSpecAn_GetAttributeU32 | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxSpecAn_GetAttributeU32Array | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxSpecAn_GetAttributeU64Array | Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxSpecAn_GetAttributeU8 | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxSpecAn_GetAttributeU8Array | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga0157e3e6aa884e74e8b5976828151a8b.html language=enus -->
## TOPIC 00575: RFmxSpecAn_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga0157e3e6aa884e74e8b5976828151a8b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga0157e3e6aa884e74e8b5976828151a8b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxSpecAn_GetAttributeNIComplexDoubleArray

Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexDouble[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga1358e4040bd7b3fc37671446b1612d03.html language=enus -->
## TOPIC 00576: RFmxSpecAn_GetAttributeString

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga1358e4040bd7b3fc37671446b1612d03.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga1358e4040bd7b3fc37671446b1612d03.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the a

### RFmxSpecAn_GetAttributeString

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 arraySize, char attrVal[])

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| attrVal | [out] | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga18dde0a4026f1cd0b386ab5019678865.html language=enus -->
## TOPIC 00577: RFmxSpecAn_GetAttributeI32

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga18dde0a4026f1cd0b386ab5019678865.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga18dde0a4026f1cd0b386ab5019678865.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxSpecAn_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxSpecAn_GetAttributeI32

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga4559fe83a750b3d98f1e6906bb73a1fc.html language=enus -->
## TOPIC 00578: RFmxSpecAn_GetAttributeU64Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga4559fe83a750b3d98f1e6906bb73a1fc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga4559fe83a750b3d98f1e6906bb73a1fc.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxSpecAn_GetAttributeU64Array

Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga54694ae9a0f54ce67e486f208d72bd95.html language=enus -->
## TOPIC 00579: RFmxSpecAn_GetAttributeU32

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga54694ae9a0f54ce67e486f208d72bd95.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga54694ae9a0f54ce67e486f208d72bd95.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxSpecAn_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifie

### RFmxSpecAn_GetAttributeU32

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga5afc1c6bbc2e6ce7f47d51230b5d9f34.html language=enus -->
## TOPIC 00580: RFmxSpecAn_GetAttributeF32

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga5afc1c6bbc2e6ce7f47d51230b5d9f34.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga5afc1c6bbc2e6ce7f47d51230b5d9f34.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxSpecAn_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleId

### RFmxSpecAn_GetAttributeF32

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga75573e5c943176545ff24b069dc8bb08.html language=enus -->
## TOPIC 00581: RFmxSpecAn_GetAttributeI16

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga75573e5c943176545ff24b069dc8bb08.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga75573e5c943176545ff24b069dc8bb08.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxSpecAn_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxSpecAn_GetAttributeI16

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga81b16eb1a5c74221c2f34deaa071f5b4.html language=enus -->
## TOPIC 00582: RFmxSpecAn_GetAttributeI8Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga81b16eb1a5c74221c2f34deaa071f5b4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga81b16eb1a5c74221c2f34deaa071f5b4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and

### RFmxSpecAn_GetAttributeI8Array

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga940ca7ca9c4c95686f1e9280d2352de6.html language=enus -->
## TOPIC 00583: RFmxSpecAn_GetAttributeF32Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga940ca7ca9c4c95686f1e9280d2352de6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1ga940ca7ca9c4c95686f1e9280d2352de6.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxSpecAn_GetAttributeF32Array

Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gac6a538800955b28d98c5b96d79ddd4cd.html language=enus -->
## TOPIC 00584: RFmxSpecAn_GetAttributeI8

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gac6a538800955b28d98c5b96d79ddd4cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gac6a538800955b28d98c5b96d79ddd4cd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxSpecAn_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sess

### RFmxSpecAn_GetAttributeI8

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaee385e17b82244fb291bd44f68c957a8.html language=enus -->
## TOPIC 00585: RFmxSpecAn_GetAttributeNIComplexSingleArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaee385e17b82244fb291bd44f68c957a8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaee385e17b82244fb291bd44f68c957a8.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxSpecAn_GetAttributeNIComplexSingleArray

Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexSingle[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf0effab98c1d632539657b4fb9ea6fdd.html language=enus -->
## TOPIC 00586: RFmxSpecAn_GetAttributeI64

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf0effab98c1d632539657b4fb9ea6fdd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf0effab98c1d632539657b4fb9ea6fdd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxSpecAn_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxSpecAn_GetAttributeI64

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf2e7b9d39b913cef923692e2e6c9463c.html language=enus -->
## TOPIC 00587: RFmxSpecAn_GetAttributeI32Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf2e7b9d39b913cef923692e2e6c9463c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf2e7b9d39b913cef923692e2e6c9463c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxSpecAn_GetAttributeI32Array

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf6c2e4b2493fc9d413ef1831c763594a.html language=enus -->
## TOPIC 00588: RFmxSpecAn_GetAttributeU16

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf6c2e4b2493fc9d413ef1831c763594a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf6c2e4b2493fc9d413ef1831c763594a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxSpecAn_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifie

### RFmxSpecAn_GetAttributeU16

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf7e4ff0d5ee39bca20caed2394da8425.html language=enus -->
## TOPIC 00589: RFmxSpecAn_GetAttributeU32Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf7e4ff0d5ee39bca20caed2394da8425.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf7e4ff0d5ee39bca20caed2394da8425.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxSpecAn_GetAttributeU32Array

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf8207749d17de640e24c685c644beba2.html language=enus -->
## TOPIC 00590: RFmxSpecAn_GetAttributeF64

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf8207749d17de640e24c685c644beba2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gaf8207749d17de640e24c685c644beba2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxSpecAn_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleId

### RFmxSpecAn_GetAttributeF64

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gafd24f1254355a5b6e15945258c42f47e.html language=enus -->
## TOPIC 00591: RFmxSpecAn_GetAttributeI64Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gafd24f1254355a5b6e15945258c42f47e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__get__attributes_1gafd24f1254355a5b6e15945258c42f47e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxSpecAn_GetAttributeI64Array

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxSpecAn_GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes.html language=enus -->
## TOPIC 00592: Set Attributes

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_SetAttributeF32Sets the value of an RFmx 32-bit floating point number (float32) attribute. RFmxSpecAn_SetAttributeF32ArraySets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer fo

### Set Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_SetAttributeF32 | Sets the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxSpecAn_SetAttributeF32Array | Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxSpecAn_SetAttributeF64 | Sets the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxSpecAn_SetAttributeF64Array | Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxSpecAn_SetAttributeI16 | Sets the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxSpecAn_SetAttributeI32 | Sets the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxSpecAn_SetAttributeI32Array | Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxSpecAn_SetAttributeI64 | Sets the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxSpecAn_SetAttributeI64Array | Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxSpecAn_SetAttributeI8 | Sets the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxSpecAn_SetAttributeI8Array | Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxSpecAn_SetAttributeNIComplexDoubleArray | Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxSpecAn_SetAttributeNIComplexSingleArray | Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxSpecAn_SetAttributeString | Sets the value of an RFmx string attribute. |
| RFmxSpecAn_SetAttributeU16 | Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxSpecAn_SetAttributeU32 | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxSpecAn_SetAttributeU32Array | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxSpecAn_SetAttributeU64Array | Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxSpecAn_SetAttributeU8 | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxSpecAn_SetAttributeU8Array | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga44c403cbd6c28b9aa9453eeb5b280b8a.html language=enus -->
## TOPIC 00593: RFmxSpecAn_SetAttributeF32Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga44c403cbd6c28b9aa9453eeb5b280b8a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga44c403cbd6c28b9aa9453eeb5b280b8a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, c

### RFmxSpecAn_SetAttributeF32Array

Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga6051a8e5907f6a62bc528f9ab7e460aa.html language=enus -->
## TOPIC 00594: RFmxSpecAn_SetAttributeI16

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga6051a8e5907f6a62bc528f9ab7e460aa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga6051a8e5907f6a62bc528f9ab7e460aa.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sess

### RFmxSpecAn_SetAttributeI16

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga667a7c06b3848ead512fb900760cfa72.html language=enus -->
## TOPIC 00595: RFmxSpecAn_SetAttributeI32Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga667a7c06b3848ead512fb900760cfa72.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga667a7c06b3848ead512fb900760cfa72.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorStri

### RFmxSpecAn_SetAttributeI32Array

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga75d47566a26ae29add704c7a85ed4263.html language=enus -->
## TOPIC 00596: RFmxSpecAn_SetAttributeI8

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga75d47566a26ae29add704c7a85ed4263.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga75d47566a26ae29add704c7a85ed4263.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session.

### RFmxSpecAn_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga7ff30af29558bc5cc3cb9bd912b87404.html language=enus -->
## TOPIC 00597: RFmxSpecAn_SetAttributeF64

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga7ff30af29558bc5cc3cb9bd912b87404.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga7ff30af29558bc5cc3cb9bd912b87404.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdenti

### RFmxSpecAn_SetAttributeF64

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga8f1d013956a51f5e00e500a9efa309d4.html language=enus -->
## TOPIC 00598: RFmxSpecAn_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga8f1d013956a51f5e00e500a9efa309d4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga8f1d013956a51f5e00e500a9efa309d4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selecto

### RFmxSpecAn_SetAttributeNIComplexDoubleArray

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga8f739a2f84dfd9a1c33850c5f0fa0b9f.html language=enus -->
## TOPIC 00599: RFmxSpecAn_SetAttributeU8Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga8f739a2f84dfd9a1c33850c5f0fa0b9f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga8f739a2f84dfd9a1c33850c5f0fa0b9f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selec

### RFmxSpecAn_SetAttributeU8Array

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga99db6d415dc5675c0bf4521dff419466.html language=enus -->
## TOPIC 00600: RFmxSpecAn_SetAttributeU64Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga99db6d415dc5675c0bf4521dff419466.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga99db6d415dc5675c0bf4521dff419466.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char se

### RFmxSpecAn_SetAttributeU64Array

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga9d1c355af38b822d793fb640b573b4d4.html language=enus -->
## TOPIC 00601: RFmxSpecAn_SetAttributeF64Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga9d1c355af38b822d793fb640b573b4d4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1ga9d1c355af38b822d793fb640b573b4d4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, c

### RFmxSpecAn_SetAttributeF64Array

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gaa51052fdb041811ab289e167fbe918c5.html language=enus -->
## TOPIC 00602: RFmxSpecAn_SetAttributeString

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gaa51052fdb041811ab289e167fbe918c5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gaa51052fdb041811ab289e167fbe918c5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx string attribute. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. You can

### RFmxSpecAn_SetAttributeString

Sets the value of an RFmx string attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | char[] | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gaae5e09bc64f905cf9b4aef4552d88340.html language=enus -->
## TOPIC 00603: RFmxSpecAn_SetAttributeI32

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gaae5e09bc64f905cf9b4aef4552d88340.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gaae5e09bc64f905cf9b4aef4552d88340.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sess

### RFmxSpecAn_SetAttributeI32

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gac42077ae3754df2c99a7b38eba897e7f.html language=enus -->
## TOPIC 00604: RFmxSpecAn_SetAttributeU8

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gac42077ae3754df2c99a7b38eba897e7f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gac42077ae3754df2c99a7b38eba897e7f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RF

### RFmxSpecAn_SetAttributeU8

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gacefb983804bb068c567fb8cb7a270a69.html language=enus -->
## TOPIC 00605: RFmxSpecAn_SetAttributeU16

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gacefb983804bb068c567fb8cb7a270a69.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gacefb983804bb068c567fb8cb7a270a69.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies th

### RFmxSpecAn_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gacf04837540a244a4f364b971df5678ef.html language=enus -->
## TOPIC 00606: RFmxSpecAn_SetAttributeI64Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gacf04837540a244a4f364b971df5678ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gacf04837540a244a4f364b971df5678ef.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorStri

### RFmxSpecAn_SetAttributeI64Array

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gad27eff3b7f9b9d2186e234e952e216b6.html language=enus -->
## TOPIC 00607: RFmxSpecAn_SetAttributeNIComplexSingleArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gad27eff3b7f9b9d2186e234e952e216b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gad27eff3b7f9b9d2186e234e952e216b6.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selecto

### RFmxSpecAn_SetAttributeNIComplexSingleArray

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gad77fbf70ad7ed9ebb4d17a6069d85d62.html language=enus -->
## TOPIC 00608: RFmxSpecAn_SetAttributeI8Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gad77fbf70ad7ed9ebb4d17a6069d85d62.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gad77fbf70ad7ed9ebb4d17a6069d85d62.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[

### RFmxSpecAn_SetAttributeI8Array

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gadf2f7e2e74f3ea41db10944d509f56c3.html language=enus -->
## TOPIC 00609: RFmxSpecAn_SetAttributeF32

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gadf2f7e2e74f3ea41db10944d509f56c3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gadf2f7e2e74f3ea41db10944d509f56c3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdenti

### RFmxSpecAn_SetAttributeF32

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gae13058a1005b1112afecf63a4916eb49.html language=enus -->
## TOPIC 00610: RFmxSpecAn_SetAttributeU32

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gae13058a1005b1112afecf63a4916eb49.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gae13058a1005b1112afecf63a4916eb49.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies th

### RFmxSpecAn_SetAttributeU32

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gae39596975e51d3a1a390326069db5581.html language=enus -->
## TOPIC 00611: RFmxSpecAn_SetAttributeU32Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gae39596975e51d3a1a390326069db5581.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gae39596975e51d3a1a390326069db5581.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char se

### RFmxSpecAn_SetAttributeU32Array

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gaf7e1247fe530ee99fe097b69b4dab144.html language=enus -->
## TOPIC 00612: RFmxSpecAn_SetAttributeI64

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gaf7e1247fe530ee99fe097b69b4dab144.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__set__and__get__attributes__set__attributes_1gaf7e1247fe530ee99fe097b69b4dab144.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxSpecAn_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sess

### RFmxSpecAn_SetAttributeI64

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxSpecAn_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__utility.html language=enus -->
## TOPIC 00613: Utility

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__utility.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_CheckMeasurementStatusChecks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. RFmxSpecAn_CommitCommits settings to the

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_CheckMeasurementStatus | Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxSpecAn_Commit | Commits settings to the hardware. Calling this function is optional. RFmxSpecAn commits settings to the hardware when you call the RFmxSpecAn_Initiate function or any of the measurement Read functions. |
| RFmxSpecAn_IDPDGetEqualizerReferenceWaveform | Gets the equalizer reference waveform used to perform the IDPD measurement. |
| RFmxSpecAn_IDPDGetEqualizerReferenceWaveformSplit | Gets the equalizer reference waveform used to perform the IDPD measurement. |
| RFmxSpecAn_InitializeFromNIRFSASession | Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. |
| RFmxSpecAn_ResetAttribute | Resets an attribute that you specify in the attributeID parameter to default values. |
| RFmxSpecAn_ResetToDefault | Resets a signal to the default values. |
| RFmxSpecAn_WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. |
| RFmxSpecAn_WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__utility_1ga0b1bbff43460309542c53d46fa8abc32.html language=enus -->
## TOPIC 00614: RFmxSpecAn_Commit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__utility_1ga0b1bbff43460309542c53d46fa8abc32.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__utility_1ga0b1bbff43460309542c53d46fa8abc32.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this function is optional. RFmxSpecAn commits settings to the hardware when you call the RFmxSpecAn_Initiate function or any of the measurement Read functions. Syntaxint32 __stdcall RFmxSpecAn_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])

### RFmxSpecAn_Commit

Commits settings to the hardware. Calling this function is optional. RFmxSpecAn commits settings to the hardware when you call the [RFmxSpecAn_Initiate](group____root__ni_r_fmx_spec_an__functions_1gae942eb70eeba92480a883f3916f00a35.html) function or any of the measurement Read functions.

#### Syntax

int32 __stdcall RFmxSpecAn_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__utility_1ga2cba7003b96d808e078b822f30bf69cd.html language=enus -->
## TOPIC 00615: RFmxSpecAn_ResetAttribute

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__utility_1ga2cba7003b96d808e078b822f30bf69cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__utility_1ga2cba7003b96d808e078b822f30bf69cd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets an attribute that you specify in the attributeID parameter to default values. Syntaxint32 __stdcall RFmxSpecAn_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxSpecAn_ResetAttribute

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Syntax

int32 __stdcall RFmxSpecAn_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being reset. Refer to the Selector String (C or LabWindows/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__utility_1ga34c8120002e06ea4a3807832ea956634.html language=enus -->
## TOPIC 00616: RFmxSpecAn_WaitForMeasurementComplete

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__utility_1ga34c8120002e06ea4a3807832ea956634.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__utility_1ga34c8120002e06ea4a3807832ea956634.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. Syntaxint32 __stdcall RFmxSpecAn_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis para

### RFmxSpecAn_WaitForMeasurementComplete

Waits for the specified number for seconds for all the measurements to complete.

#### Syntax

int32 __stdcall RFmxSpecAn_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time, in seconds, for which the function waits for the measurement to complete. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__utility_1ga6fdd808ca692a39265132c97d5a81d58.html language=enus -->
## TOPIC 00617: RFmxSpecAn_CheckMeasurementStatus

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__utility_1ga6fdd808ca692a39265132c97d5a81d58.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__utility_1ga6fdd808ca692a39265132c97d5a81d58.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. Syntaxint32 __stdcall RFmxSpecAn_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString

### RFmxSpecAn_CheckMeasurementStatus

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

int32 __stdcall RFmxSpecAn_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *isDone)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| isDone | [out] | int32 * | This parameter indicates whether the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__utility_1ga785c2a04670c746e43907d7133101766.html language=enus -->
## TOPIC 00618: RFmxSpecAn_IDPDGetEqualizerReferenceWaveform

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__utility_1ga785c2a04670c746e43907d7133101766.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__utility_1ga785c2a04670c746e43907d7133101766.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the equalizer reference waveform used to perform the IDPD measurement. Syntaxint32 __stdcall RFmxSpecAn_IDPDGetEqualizerReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *x0, float64 *dx, NIComplexSingle equalizerReferenceWaveform[], float64 *papr, int32 array

### RFmxSpecAn_IDPDGetEqualizerReferenceWaveform

Gets the equalizer reference waveform used to perform the IDPD measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_IDPDGetEqualizerReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *x0, float64 *dx, NIComplexSingle equalizerReferenceWaveform[], float64 *papr, int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| equalizerReferenceWaveform | [out] | NIComplexSingle[] | This parameter returns the complex baseband samples, in volts. |
| papr | [out] | float64 * | This parameter returns the peak-to-average power ratio of the waveform obtained after applying digital predistortion. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__utility_1ga91cae3c9670607f26ad0bb8436f4cae2.html language=enus -->
## TOPIC 00619: RFmxSpecAn_ResetToDefault

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__utility_1ga91cae3c9670607f26ad0bb8436f4cae2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__utility_1ga91cae3c9670607f26ad0bb8436f4cae2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. Syntaxint32 __stdcall RFmxSpecAn_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obtain

### RFmxSpecAn_ResetToDefault

Resets a signal to the default values.

#### Syntax

int32 __stdcall RFmxSpecAn_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__utility_1gabeeaee697d8c0aab94828898f92307cc.html language=enus -->
## TOPIC 00620: RFmxSpecAn_IDPDGetEqualizerReferenceWaveformSplit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__utility_1gabeeaee697d8c0aab94828898f92307cc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__utility_1gabeeaee697d8c0aab94828898f92307cc.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the equalizer reference waveform used to perform the IDPD measurement. Syntaxint32 __stdcall RFmxSpecAn_IDPDGetEqualizerReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *x0, float64 *dx, float32 equalizerReferenceWaveformI[], float32 equalizerReferenceWa

### RFmxSpecAn_IDPDGetEqualizerReferenceWaveformSplit

Gets the equalizer reference waveform used to perform the IDPD measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_IDPDGetEqualizerReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *x0, float64 *dx, float32 equalizerReferenceWaveformI[], float32 equalizerReferenceWaveformQ[], float64 *papr, int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| equalizerReferenceWaveformI | [out] | float32[] | This parameter Returns the real part of complex baseband samples, in volts. |
| equalizerReferenceWaveformQ | [out] | float32[] | This parameter Returns the imaginary part of complex baseband samples, in volts. |
| papr | [out] | float64 * | This parameter returns the peak-to-average power ratio of the waveform obtained after applying digital predistortion. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__utility_1gacb809cac929b3473abc12401d4c3d138.html language=enus -->
## TOPIC 00621: RFmxSpecAn_InitializeFromNIRFSASession

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__utility_1gacb809cac929b3473abc12401d4c3d138.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__utility_1gacb809cac929b3473abc12401d4c3d138.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device

### RFmxSpecAn_InitializeFromNIRFSASession

Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxSpecAn_InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle *handleOut)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_InitializeFromNIRFSASession](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| nirfsaSession | [in] | uInt32 | Specifies the NIRFSA session handle of the device to initialize. |
| handleOut | [out] | niRFmxInstrHandle * | Returns an RFmx instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__utility_1gacce76c2c4b15b311f34d5dc319069a38.html language=enus -->
## TOPIC 00622: RFmxSpecAn_WaitForAcquisitionComplete

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__utility_1gacce76c2c4b15b311f34d5dc319069a38.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__utility_1gacce76c2c4b15b311f34d5dc319069a38.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. Syntaxint32 __stdcall RFmxSpecAn_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)RemarksThis function is a wrapper over the RFmx Instru

### RFmxSpecAn_WaitForAcquisitionComplete

Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function.

#### Syntax

int32 __stdcall RFmxSpecAn_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?context=rfmxinstr_rfmxinstrcref_function_wait_for_acquisition_complete) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| timeout | [in] | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group__root__ni_r_fmx_spec_an.html language=enus -->
## TOPIC 00623: niRFmxSpecAn.h

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group__root__ni_r_fmx_spec_an.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group__root__ni_r_fmx_spec_an.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niRFmxSpecAn.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
