# NI DOCUMENT BUNDLE: rfmxtdscdma-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxtdscdma-c-api-ref start=251 end=333 -->
<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaa033602e60a54326ded5a55262b175c0.html language=enus -->
## TOPIC 00251: RFmxTDSCDMA_ModAccFetchDataCDE

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaa033602e60a54326ded5a55262b175c0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaa033602e60a54326ded5a55262b175c0.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the measured data code domain errors (CDEs), along with the spreading factor and the channelization code of the corresponding channel. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchDataCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64

### RFmxTDSCDMA_ModAccFetchDataCDE

Returns the maximum value of the measured data code domain errors (CDEs), along with the spreading factor and the channelization code of the corresponding channel.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchDataCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumPeakDataCDE, int32 *peakDataCDESpreadingFactor, int32 *peakDataCDECode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumPeakDataCDE | [out] | float64 * | This parameter returns the maximum peak CDE among all active time slots and averaging iterations. This value is expressed in dB. |
| peakDataCDESpreadingFactor | [out] | int32 * | This parameter returns the spreading factor used for retrieving the peak CDE of the channel corresponding to measured value of the RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_CDE attribute. |
| peakDataCDECode | [out] | int32 * | This parameter returns the peak channelization code of the channel corresponding to the measured value of the RFMXTDSCDMA_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_DATA_CDE attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaa241aa8be3534d14100c2541abe13092.html language=enus -->
## TOPIC 00252: RFmxTDSCDMA_ModAccFetchPhaseErrorTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaa241aa8be3534d14100c2541abe13092.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaa241aa8be3534d14100c2541abe13092.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average of the phase error trace on the chip level. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)ParametersN

### RFmxTDSCDMA_ModAccFetchPhaseErrorTrace

Returns the average of the phase error trace on the chip level.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time of the trace. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sampling time of the trace. This value is expressed in seconds. |
| phaseError | [out] | float32[] | This parameter returns the phase error trace values as a real value array. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gabd8bbcae903aaee2e3dbcb9baf510fb5.html language=enus -->
## TOPIC 00253: RFmxTDSCDMA_ModAccFetchDetectedChannel

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gabd8bbcae903aaee2e3dbcb9baf510fb5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gabd8bbcae903aaee2e3dbcb9baf510fb5.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a detected channel by its channel name. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *detectedSlotIndex, int32 *detectedSpreadingFactor, int32 *detectedModulationType, int32 *detectedChannelizat

### RFmxTDSCDMA_ModAccFetchDetectedChannel

Returns a detected channel by its channel name.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *detectedSlotIndex, int32 *detectedSpreadingFactor, int32 *detectedModulationType, int32 *detectedChannelizationCode)

#### Remarks

Use "channel<i><n></i>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read results from this function.

If the averaging is enabled, the detected channels of the last averaging operation can be retrieved.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and channel number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"channel0""signal::sig1/channel0""result::r1/channel0""signal::sig1/result::r1/channel0"You can use the RFmxTDSCDMA_BuildChannelString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| detectedSlotIndex | [out] | int32 * | This parameter returns the slot index of the detected channel. |
| detectedSpreadingFactor | [out] | int32 * | This parameter returns the spreading factor of the detected channel. |
| detectedModulationType | [out] | int32 * | This parameter returns the modulation type for the detected channel.Name (value)DescriptionQPSK (0)The modulation type is QPSK.8PSK (1)The modulation type is 8-PSK.16QAM (2)The modulation type is16-QAM. |
| Name (value) | Description |  |  |
| QPSK (0) | The modulation type is QPSK. |  |  |
| 8PSK (1) | The modulation type is 8-PSK. |  |  |
| 16QAM (2) | The modulation type is16-QAM. |  |  |
| detectedChannelizationCode | [out] | int32 * | This parameter returns the channelization code of the detected channel. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaf1c23651efd275071c68a0ae17c1b211.html language=enus -->
## TOPIC 00254: RFmxTDSCDMA_ModAccFetchIQImpairments

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaf1c23651efd275071c68a0ae17c1b211.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaf1c23651efd275071c68a0ae17c1b211.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)Parameters

### RFmxTDSCDMA_ModAccFetchIQImpairments

Returns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iqOriginOffset | [out] | float64 * | This parameter returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. |
| iqGainImbalance | [out] | float64 * | This parameter returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. |
| iqQuadratureError | [out] | float64 * | This parameter returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaf97a2400d23b41ed4ef8f3590b8c9dbf.html language=enus -->
## TOPIC 00255: RFmxTDSCDMA_ModAccFetchMidambleAndDataPower

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaf97a2400d23b41ed4ef8f3590b8c9dbf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaf97a2400d23b41ed4ef8f3590b8c9dbf.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power of the midamble and the data channel. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchMidambleAndDataPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *midamblePower, float64 *dataField1Power, float64 *dataField2Power)ParametersNameDirectionType

### RFmxTDSCDMA_ModAccFetchMidambleAndDataPower

Returns the power of the midamble and the data channel.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchMidambleAndDataPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *midamblePower, float64 *dataField1Power, float64 *dataField2Power)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| midamblePower | [out] | float64 * | This parameter returns the power of the midamble, averaged over all measured slots. This value is expressed in dBm. |
| dataField1Power | [out] | float64 * | This parameter returns the power of the data field 1, averaged over all measured slots. This value is expressed in dBm. |
| dataField2Power | [out] | float64 * | This parameter returns the power of the data field 2, averaged over all measured slots. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaf9aaa0182b6b48a587d7766d02d7963d.html language=enus -->
## TOPIC 00256: RFmxTDSCDMA_ModAccFetchCodeDomainErrorTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaf9aaa0182b6b48a587d7766d02d7963d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__modacc_1gaf9aaa0182b6b48a587d7766d02d7963d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the value of the code domain error trace for the individual code channels in the domain of the base spreading factor. This value is averaged over all active time slots and averaging iterations. Syntaxint32 __stdcall RFmxTDSCDMA_ModAccFetchCodeDomainErrorTrace(niRFmxInstrHandle instrumentHand

### RFmxTDSCDMA_ModAccFetchCodeDomainErrorTrace

Fetches the value of the code domain error trace for the individual code channels in the domain of the base spreading factor. This value is averaged over all active time slots and averaging iterations.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ModAccFetchCodeDomainErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 codeDomainError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| codeDomainError | [out] | float32[] | This parameter returns an array of the code domain error traces for the individual code channels in the domain of the base spreading factor averaged over all active time slots and averaging iterations. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__obw.html language=enus -->
## TOPIC 00257: OBW

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__obw.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_OBWFetchMeasurementReturns the OBW measurement. RFmxTDSCDMA_OBWFetchSpectrumFetches the spectrum trace used for the OBW measurement. AttachmentsNone

### OBW

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_OBWFetchMeasurement | Returns the OBW measurement. |
| RFmxTDSCDMA_OBWFetchSpectrum | Fetches the spectrum trace used for the OBW measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__obw_1ga906d9cdbd6d400f8df02a31192bb3d9d.html language=enus -->
## TOPIC 00258: RFmxTDSCDMA_OBWFetchMeasurement

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__obw_1ga906d9cdbd6d400f8df02a31192bb3d9d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__obw_1ga906d9cdbd6d400f8df02a31192bb3d9d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the OBW measurement. Syntaxint32 __stdcall RFmxTDSCDMA_OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *absolutePower, float64 *startFrequency, float64 *stopFrequency)ParametersNameDirectionTypeDescriptionins

### RFmxTDSCDMA_OBWFetchMeasurement

Returns the OBW measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *absolutePower, float64 *startFrequency, float64 *stopFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| occupiedBandwidth | [out] | float64 * | This parameter returns the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency. |
| absolutePower | [out] | float64 * | This parameter returns the total integrated power of the averaged spectrum acquired by the OBW measurement. This value is expressed in dBm. |
| startFrequency | [out] | float64 * | This parameter returns the start frequency of the OBW. This value is expressed in Hz. |
| stopFrequency | [out] | float64 * | This parameter returns the stop frequency of the OBW. This value is expressed in Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__obw_1gaf6a2a8604eb7c3009d0f07e9bd7a9cc3.html language=enus -->
## TOPIC 00259: RFmxTDSCDMA_OBWFetchSpectrum

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__obw_1gaf6a2a8604eb7c3009d0f07e9bd7a9cc3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__obw_1gaf6a2a8604eb7c3009d0f07e9bd7a9cc3.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum trace used for the OBW measurement. Syntaxint32 __stdcall RFmxTDSCDMA_OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDes

### RFmxTDSCDMA_OBWFetchSpectrum

Fetches the spectrum trace used for the OBW measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt.html language=enus -->
## TOPIC 00260: PVT

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_PVTFetchMeasurementStatusFetches the overall status of the power versus time (PVT) measurement. RFmxTDSCDMA_PVTFetchPowersFetches the values of the Mean Absolute ON Power and Mean Absolute OFF Power parameters. RFmxTDSCDMA_PVTFetchSegmentMeasurementR

### PVT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_PVTFetchMeasurementStatus | Fetches the overall status of the power versus time (PVT) measurement. |
| RFmxTDSCDMA_PVTFetchPowers | Fetches the values of the Mean Absolute ON Power and Mean Absolute OFF Power parameters. |
| RFmxTDSCDMA_PVTFetchSegmentMeasurement | Returns the status of a specific power versus time (PVT) measurement segment along with the measured segment powers. |
| RFmxTDSCDMA_PVTFetchSegmentMeasurementArray | Fetches the status and measured powers for all the power versus time (PVT) measurement segments. |
| RFmxTDSCDMA_PVTFetchSignalPowerTrace | Fetches the signal power trace and the absolute limit trace. The limit trace is defined by the transmit ON/off time mask measurement in the 3GPP TS 34.122 specification. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1ga905ae666ff8ec2ff06b46e4fb6b98fcc.html language=enus -->
## TOPIC 00261: RFmxTDSCDMA_PVTFetchPowers

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1ga905ae666ff8ec2ff06b46e4fb6b98fcc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1ga905ae666ff8ec2ff06b46e4fb6b98fcc.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the values of the Mean Absolute ON Power and Mean Absolute OFF Power parameters. Syntaxint32 __stdcall RFmxTDSCDMA_PVTFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanAbsoluteOnPower, float64 *meanAbsoluteOffPower)ParametersNameDirectionTyp

### RFmxTDSCDMA_PVTFetchPowers

Fetches the values of the **Mean Absolute ON Power** and **Mean Absolute OFF Power** parameters.

#### Syntax

int32 __stdcall RFmxTDSCDMA_PVTFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanAbsoluteOnPower, float64 *meanAbsoluteOffPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanAbsoluteOnPower | [out] | float64 * | This parameter returns the mean on power of the measured burst, or the averaged bursts. This value is expressed in dBm. |
| meanAbsoluteOffPower | [out] | float64 * | This parameter returns the mean off power of the measured burst, or the averaged bursts. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1ga9e2da4a33b29fb4fe701ec1bfafb221c.html language=enus -->
## TOPIC 00262: RFmxTDSCDMA_PVTFetchSignalPowerTrace

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1ga9e2da4a33b29fb4fe701ec1bfafb221c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1ga9e2da4a33b29fb4fe701ec1bfafb221c.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the signal power trace and the absolute limit trace. The limit trace is defined by the transmit ON/off time mask measurement in the 3GPP TS 34.122 specification. Syntaxint32 __stdcall RFmxTDSCDMA_PVTFetchSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 time

### RFmxTDSCDMA_PVTFetchSignalPowerTrace

Fetches the signal power trace and the absolute limit trace. The limit trace is defined by the transmit ON/off time mask measurement in the 3GPP TS 34.122 specification.

#### Syntax

int32 __stdcall RFmxTDSCDMA_PVTFetchSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 signalPower[], float32 absoluteLimit[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time of the trace relative to the start of the analyzed burst. |
| dx | [out] | float64 * | This parameter returns the time difference between successive trace samples. |
| signalPower | [out] | float32[] | This parameter returns an array of values for the signal power trace. These values are expressed in dBm. |
| absoluteLimit | [out] | float32[] | This parameter returns an array of values for the signal power trace. These values are expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1gacc2b32aa1c0db50e03c37ce611c0b477.html language=enus -->
## TOPIC 00263: RFmxTDSCDMA_PVTFetchSegmentMeasurementArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1gacc2b32aa1c0db50e03c37ce611c0b477.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1gacc2b32aa1c0db50e03c37ce611c0b477.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the status and measured powers for all the power versus time (PVT) measurement segments. Syntaxint32 __stdcall RFmxTDSCDMA_PVTFetchSegmentMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 segmentStatus[], float64 segmentMargin[], float64 segme

### RFmxTDSCDMA_PVTFetchSegmentMeasurementArray

Fetches the status and measured powers for all the power versus time (PVT) measurement segments.

#### Syntax

int32 __stdcall RFmxTDSCDMA_PVTFetchSegmentMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 segmentStatus[], float64 segmentMargin[], float64 segmentMarginTime[], float64 segmentMeanAbsolutePower[], float64 segmentMaximumAbsolutePower[], float64 segmentMinimumAbsolutePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| segmentStatus | [out] | int32[] | This parameter returns an array of the measurement status values for an individual PVT measurement segment.Name (value)DescriptionFail (0)Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit.Pass (1)Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |
| Name (value) | Description |  |  |
| Fail (0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |  |  |
| Pass (1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |  |  |
| segmentMargin | [out] | float64[] | This parameter returns an array of the power margins for an individual PVT measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB. |
| segmentMarginTime | [out] | float64[] | This parameter returns an array of the positions in time corresponding to the Segment Margin parameter. This value is expressed in seconds. |
| segmentMeanAbsolutePower | [out] | float64[] | This parameter returns an array of the mean measured powers corresponding to the Segment Margin parameter. This value is expressed in dBm. |
| segmentMaximumAbsolutePower | [out] | float64[] | This parameter returns an array of the maximum measured powers of an individual PVT measurement segment. This value is expressed in dBm. |
| segmentMinimumAbsolutePower | [out] | float64[] | This parameter returns an array of the minimum measured powers of an individual PVT measurement segment. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1gad3127b9e1bc71014e641bc88d1ca6d11.html language=enus -->
## TOPIC 00264: RFmxTDSCDMA_PVTFetchMeasurementStatus

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1gad3127b9e1bc71014e641bc88d1ca6d11.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1gad3127b9e1bc71014e641bc88d1ca6d11.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall status of the power versus time (PVT) measurement. Syntaxint32 __stdcall RFmxTDSCDMA_PVTFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInst

### RFmxTDSCDMA_PVTFetchMeasurementStatus

Fetches the overall status of the power versus time (PVT) measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_PVTFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the overall status of the PVT measurement.Name (value)DescriptionFail (0)Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit.Pass (1)Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |
| Name (value) | Description |  |  |
| Fail (0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |  |  |
| Pass (1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1gaef99e8dc6dc61dc02fff5b40ed814e4e.html language=enus -->
## TOPIC 00265: RFmxTDSCDMA_PVTFetchSegmentMeasurement

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1gaef99e8dc6dc61dc02fff5b40ed814e4e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__pvt_1gaef99e8dc6dc61dc02fff5b40ed814e4e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the status of a specific power versus time (PVT) measurement segment along with the measured segment powers. Syntaxint32 __stdcall RFmxTDSCDMA_PVTFetchSegmentMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *segmentStatus, float64 *segmentMargin,

### RFmxTDSCDMA_PVTFetchSegmentMeasurement

Returns the status of a specific power versus time (PVT) measurement segment along with the measured segment powers.

#### Syntax

int32 __stdcall RFmxTDSCDMA_PVTFetchSegmentMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *segmentStatus, float64 *segmentMargin, float64 *segmentMarginTime, float64 *segmentMeanAbsolutePower, float64 *segmentMaximumAbsolutePower, float64 *segmentMinimumAbsolutePower)

#### Remarks

Use "segment<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"segment0""signal::sig1/segment0""result::r1/segment0""signal::sig1/result::r1/segment0"You can use the RFmxTDSCDMA_BuildSegmentString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| segmentStatus | [out] | int32 * | This parameter returns the measurement status for an individual PVT measurement segment.Name (value)DescriptionFail (0)Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit.Pass (1)Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |
| Name (value) | Description |  |  |
| Fail (0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |  |  |
| Pass (1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |  |  |
| segmentMargin | [out] | float64 * | This parameter returns the power margin for an individual PVT measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB. |
| segmentMarginTime | [out] | float64 * | This parameter returns the position in time corresponding to the Segment Margin parameter. This value is expressed in seconds. |
| segmentMeanAbsolutePower | [out] | float64 * | This parameter returns the mean measured power corresponding to the Segment Margin parameter. This value is expressed in dBm. |
| segmentMaximumAbsolutePower | [out] | float64 * | This parameter returns the maximum measured power of an individual PVT measurement segment. This value is expressed in dBm. |
| segmentMinimumAbsolutePower | [out] | float64 * | This parameter returns the minimum measured power of an individual PVT measurement segment. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem.html language=enus -->
## TOPIC 00266: SEM

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_SEMFetchCarrierAbsoluteIntegratedPowerReturns the absolute carrier integrated power of the SEM measurement. RFmxTDSCDMA_SEMFetchLowerOffsetMarginReturns the measurement status and margin from the limit line measured in the lower offset segment. RFmxT

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_SEMFetchCarrierAbsoluteIntegratedPower | Returns the absolute carrier integrated power of the SEM measurement. |
| RFmxTDSCDMA_SEMFetchLowerOffsetMargin | Returns the measurement status and margin from the limit line measured in the lower offset segment. |
| RFmxTDSCDMA_SEMFetchLowerOffsetMarginArray | Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments. |
| RFmxTDSCDMA_SEMFetchLowerOffsetPower | Returns the lower offset segment power measurements. Use "offset<n>" as the selector string to read results from this function. |
| RFmxTDSCDMA_SEMFetchLowerOffsetPowerArray | Returns the arrays of lower offset segment power measurements. |
| RFmxTDSCDMA_SEMFetchMeasurementStatus | Returns the SEM measurement status. |
| RFmxTDSCDMA_SEMFetchSpectrum | Fetches the spectrum used for the SEM measurement. |
| RFmxTDSCDMA_SEMFetchUpperOffsetMargin | Returns the measurement status and margin from the limit line measured in the upper offset segment. |
| RFmxTDSCDMA_SEMFetchUpperOffsetMarginArray | Returns the measurement status and margin from the limit line measured in the upper offset segments. |
| RFmxTDSCDMA_SEMFetchUpperOffsetPower | Returns the upper offset segment power measurements. |
| RFmxTDSCDMA_SEMFetchUpperOffsetPowerArray | Returns the arrays of upper offset segment power measurements. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga3359a1402ef9e1c0645b49989b8fb2ad.html language=enus -->
## TOPIC 00267: RFmxTDSCDMA_SEMFetchUpperOffsetPowerArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga3359a1402ef9e1c0645b49989b8fb2ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga3359a1402ef9e1c0645b49989b8fb2ad.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of upper offset segment power measurements. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[]

### RFmxTDSCDMA_SEMFetchUpperOffsetPowerArray

Returns the arrays of upper offset segment power measurements.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64[] | This parameter returns the array of upper (positive) offset segment powers measured. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64[] | This parameter returns the array of powers measured in each positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | [out] | float64[] | This parameter returns the array of peak powers measured in each upper (positive) offset segment. This value is expressed in dBm. |
| peakFrequency | [out] | float64[] | This parameter returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
| relativePeakPower | [out] | float64[] | This parameter returns the array of peak powers measured in each upper (positive) offset segment relative to the integrated power of the reference carrier. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga5b70c09e163eb71fc9be7fd7dabe22d9.html language=enus -->
## TOPIC 00268: RFmxTDSCDMA_SEMFetchSpectrum

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga5b70c09e163eb71fc9be7fd7dabe22d9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga5b70c09e163eb71fc9be7fd7dabe22d9.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the SEM measurement. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32 *actu

### RFmxTDSCDMA_SEMFetchSpectrum

Fetches the spectrum used for the SEM measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| relativeMask | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| absoluteMask | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga6131d968f32c3d42324ad750395842f3.html language=enus -->
## TOPIC 00269: RFmxTDSCDMA_SEMFetchMeasurementStatus

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga6131d968f32c3d42324ad750395842f3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga6131d968f32c3d42324ad750395842f3.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the SEM measurement status. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxTDSCDMA_SEMFetchMeasurementStatus

Returns the SEM measurement status.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the status of the measurement based on measurement limits and the failure criteria specified by the standard.Name (value)DescriptionFail (0)The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff.Pass (1)The signal does not exceed the spectrum emission limits. |
| Name (value) | Description |  |  |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |  |  |
| Pass (1) | The signal does not exceed the spectrum emission limits. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga6a3e603c545c990b7c4c88a5f4fd2fa6.html language=enus -->
## TOPIC 00270: RFmxTDSCDMA_SEMFetchUpperOffsetMargin

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga6a3e603c545c990b7c4c88a5f4fd2fa6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga6a3e603c545c990b7c4c88a5f4fd2fa6.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segment. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFreque

### RFmxTDSCDMA_SEMFetchUpperOffsetMargin

Returns the measurement status and margin from the limit line measured in the upper offset segment.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxTDSCDMA_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the upper offset measurement status based on measurement limits and the failure criteria specified by the standard.Name (value)DescriptionFail (0)The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff.Pass (1)The signal does not exceed the spectrum emission limits. |
| Name (value) | Description |  |  |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |  |  |
| Pass (1) | The signal does not exceed the spectrum emission limits. |  |  |
| margin | [out] | float64 * | This parameter returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginFrequency | [out] | float64 * | This parameter returns the frequency at which the margin occurs in the positive offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power at which the margin occurs in the positive offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64 * | This parameter returns the power at which the margin occurs in the positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga9025262ea01228d2c3595b455f227e78.html language=enus -->
## TOPIC 00271: RFmxTDSCDMA_SEMFetchLowerOffsetMargin

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga9025262ea01228d2c3595b455f227e78.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga9025262ea01228d2c3595b455f227e78.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the lower offset segment. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFreque

### RFmxTDSCDMA_SEMFetchLowerOffsetMargin

Returns the measurement status and margin from the limit line measured in the lower offset segment.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxTDSCDMA_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the lower offset measurement status based on measurement limits and the failure criteria specified by the standard.Name (value)DescriptionFail (0)The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff.Pass (1)The signal does not exceed the spectrum emission limits. |
| Name (value) | Description |  |  |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |  |  |
| Pass (1) | The signal does not exceed the spectrum emission limits. |  |  |
| margin | [out] | float64 * | This parameter returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginFrequency | [out] | float64 * | This parameter returns the frequency at which the margin occurs in the negative offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power at which the margin occurs in the negative offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64 * | This parameter returns the power at which the margin occurs in the negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga9922d77348e2033c3421ecf719c6d195.html language=enus -->
## TOPIC 00272: RFmxTDSCDMA_SEMFetchUpperOffsetMarginArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga9922d77348e2033c3421ecf719c6d195.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga9922d77348e2033c3421ecf719c6d195.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segments. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 margi

### RFmxTDSCDMA_SEMFetchUpperOffsetMarginArray

Returns the measurement status and margin from the limit line measured in the upper offset segments.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns the array of upper offset measurement statuses based on measurement limits and the failure criteria specified by the standard.Name (value)DescriptionFail (0)The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff.Pass (1)The signal does not exceed the spectrum emission limits. |
| Name (value) | Description |  |  |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |  |  |
| Pass (1) | The signal does not exceed the spectrum emission limits. |  |  |
| margin | [out] | float64[] | This parameter returns the array of margins from the limit mask value specified by the standard. This value is expressed in dB. The margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginFrequency | [out] | float64[] | This parameter returns the array of frequencies at which the margin occurs in each positive offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64[] | This parameter returns the array of powers at which the margin occurs in each positive offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64[] | This parameter returns the array of powers at which the margin occurs in each positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga9b17eb21ebc105a293ac0d2f9877f6b5.html language=enus -->
## TOPIC 00273: RFmxTDSCDMA_SEMFetchCarrierAbsoluteIntegratedPower

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga9b17eb21ebc105a293ac0d2f9877f6b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1ga9b17eb21ebc105a293ac0d2f9877f6b5.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier integrated power of the SEM measurement. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchCarrierAbsoluteIntegratedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsoluteIntegratedPower)ParametersNameDirectionTypeDescriptionins

### RFmxTDSCDMA_SEMFetchCarrierAbsoluteIntegratedPower

Returns the absolute carrier integrated power of the SEM measurement.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchCarrierAbsoluteIntegratedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsoluteIntegratedPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| carrierAbsoluteIntegratedPower | [out] | float64 * | This parameter returns the carrier power. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gaa5061071f8aabae5b29434f0ac0d18fe.html language=enus -->
## TOPIC 00274: RFmxTDSCDMA_SEMFetchLowerOffsetMarginArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gaa5061071f8aabae5b29434f0ac0d18fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gaa5061071f8aabae5b29434f0ac0d18fe.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], f

### RFmxTDSCDMA_SEMFetchLowerOffsetMarginArray

Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns the array of lower offset measurement statuses based on measurement limits and the failure criteria specified by the standard.Name (value)DescriptionFail (0)The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff.Pass (1)The signal does not exceed the spectrum emission limits. |
| Name (value) | Description |  |  |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |  |  |
| Pass (1) | The signal does not exceed the spectrum emission limits. |  |  |
| margin | [out] | float64[] | This parameter returns the array of margins from the limit mask value specified by the standard. This value is expressed in dB. The margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginFrequency | [out] | float64[] | This parameter returns the array of frequencies at which the margin occurs in each negative offset segment. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64[] | This parameter returns the array of powers at which the margin occurs in the negative offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64[] | This parameter returns the array of powers at which the margin occurs in each negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gab50d33ee24006099c54b43a7ce06edc8.html language=enus -->
## TOPIC 00275: RFmxTDSCDMA_SEMFetchLowerOffsetPower

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gab50d33ee24006099c54b43a7ce06edc8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gab50d33ee24006099c54b43a7ce06edc8.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower offset segment power measurements. Use "offset<n>" as the selector string to read results from this function. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, flo

### RFmxTDSCDMA_SEMFetchLowerOffsetPower

Returns the lower offset segment power measurements. Use "offset<n>" as the selector string to read results from this function.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFrequency, float64 *relativePeakPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxTDSCDMA_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64 * | This parameter returns the lower (negative) offset segment power measured. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64 * | This parameter returns the power in the negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | [out] | float64 * | This parameter returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
| relativePeakPower | [out] | float64 * | This parameter returns the peak power in the lower (negative) offset segment relative to the integrated power of the reference carrier. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gad013eddc076f05cb3fbbcce08b58c7a1.html language=enus -->
## TOPIC 00276: RFmxTDSCDMA_SEMFetchUpperOffsetPower

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gad013eddc076f05cb3fbbcce08b58c7a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gad013eddc076f05cb3fbbcce08b58c7a1.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper offset segment power measurements. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFre

### RFmxTDSCDMA_SEMFetchUpperOffsetPower

Returns the upper offset segment power measurements.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFrequency, float64 *relativePeakPower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxTDSCDMA_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64 * | This parameter returns the upper (positive) offset segment power measured. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64 * | This parameter returns the power in the positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | [out] | float64 * | This parameter returns the peak power measured in the upper (positive) offset segment. This value is expressed in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
| relativePeakPower | [out] | float64 * | This parameter returns the peak power in the upper (positive) offset segment relative to the integrated power of the reference carrier. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gaf8a1b43c11b379776b1c6cfd499a919a.html language=enus -->
## TOPIC 00277: RFmxTDSCDMA_SEMFetchLowerOffsetPowerArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gaf8a1b43c11b379776b1c6cfd499a919a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__sem_1gaf8a1b43c11b379776b1c6cfd499a919a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of lower offset segment power measurements. Syntaxint32 __stdcall RFmxTDSCDMA_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[]

### RFmxTDSCDMA_SEMFetchLowerOffsetPowerArray

Returns the arrays of lower offset segment power measurements.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64[] | This parameter returns the array of lower (negative) offset segment powers measured. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64[] | This parameter returns the array of powers in each negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| absolutePeakPower | [out] | float64[] | This parameter returns the array of peak powers measured in each lower (negative) offset segment. This value is expressed in dBm. |
| peakFrequency | [out] | float64[] | This parameter returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
| relativePeakPower | [out] | float64[] | This parameter returns the array of peak powers in the lower (negative) offset segment relative to the integrated power of the reference carrier. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__slotpower.html language=enus -->
## TOPIC 00278: SlotPower

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__slotpower.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_SlotPowerFetchPowersFetches the Slot Power and Slot Power Delta values. AttachmentsNone

### SlotPower

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_SlotPowerFetchPowers | Fetches the Slot Power and Slot Power Delta values. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__slotpower_1ga0da84968939b203470ff6a04f219dc48.html language=enus -->
## TOPIC 00279: RFmxTDSCDMA_SlotPowerFetchPowers

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__slotpower_1ga0da84968939b203470ff6a04f219dc48.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__fetch__slotpower_1ga0da84968939b203470ff6a04f219dc48.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the Slot Power and Slot Power Delta values. Syntaxint32 __stdcall RFmxTDSCDMA_SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPower[], float64 slotPowerDelta[], int32 arraySize, int32 *actualArraySize)RemarksThe SlotPower measureme

### RFmxTDSCDMA_SlotPowerFetchPowers

Fetches the **Slot Power** and **Slot Power Delta** values.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPower[], float64 slotPowerDelta[], int32 arraySize, int32 *actualArraySize)

#### Remarks

The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received signal.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| slotPower | [out] | float64[] | This parameter returns an array of mean powers of the active traffic time slots being measured. This value is expressed in dBm. The power of each traffic slot is measured by first excluding the gap period of 12.5 microseconds at the end of the time slot, and then excluding the transient duration of 25 microseconds at the start and the end of the remaining portion of the slot. |
| slotPowerDelta | [out] | float64[] | This parameter returns an array of the power differences between active traffic slots in adjacent subframes. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__select__measurement.html language=enus -->
## TOPIC 00280: Select Measurement

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__select__measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__select__measurement.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_SelectMeasurementsEnables all the measurements that you specify in the Measurements parameter and disables all other measurements. AttachmentsNone

### Select Measurement

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_SelectMeasurements | Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__select__measurement_1ga2738a9ad10b529a0a1aeba77ef7ff8fd.html language=enus -->
## TOPIC 00281: RFmxTDSCDMA_SelectMeasurements

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__select__measurement_1ga2738a9ad10b529a0a1aeba77ef7ff8fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__select__measurement_1ga2738a9ad10b529a0a1aeba77ef7ff8fd.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. Syntaxint32 __stdcall RFmxTDSCDMA_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)ParametersNameDirectionTypeDescr

### RFmxTDSCDMA_SelectMeasurements

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| measurements | [in] | uInt32 | This parameter specifies the measurement to perform.Name (value)DescriptionModAcc (0)Enables the ModAcc measurement.ACP (1)Enables the ACP measurement.CHP (2)Enables the CHP measurement.OBW (3)Enables the OBW measurement.SEM (4)Enables the SEM measurement.CDA (5)Enables the code domain analysis (CDA) measurement.PVT (6)Enables the power versus time (PVT) measurement.SlotPower (7)Enables the SlotPower measurement.The default is an empty array. |
| Name (value) | Description |  |  |
| ModAcc (0) | Enables the ModAcc measurement. |  |  |
| ACP (1) | Enables the ACP measurement. |  |  |
| CHP (2) | Enables the CHP measurement. |  |  |
| OBW (3) | Enables the OBW measurement. |  |  |
| SEM (4) | Enables the SEM measurement. |  |  |
| CDA (5) | Enables the code domain analysis (CDA) measurement. |  |  |
| PVT (6) | Enables the power versus time (PVT) measurement. |  |  |
| SlotPower (7) | Enables the SlotPower measurement. |  |  |
| enableAllTraces | [in] | int32 | This parameter specifies whether to enable all traces for the selected measurement. The default value is FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Select Measurement

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00282: Set and Get Attributes

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsGet AttributesSet AttributesGroup membersNoneAttachmentsNone

### Set and Get Attributes

#### Groups

- Get Attributes
- Set Attributes

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes.html language=enus -->
## TOPIC 00283: Get Attributes

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_GetAttributeF32Queries the value of an RFmx 32-bit floating point number (float32) attribute. RFmxTDSCDMA_GetAttributeF32ArrayQueries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a b

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_GetAttributeF32 | Queries the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxTDSCDMA_GetAttributeF32Array | Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxTDSCDMA_GetAttributeF64 | Queries the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxTDSCDMA_GetAttributeF64Array | Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxTDSCDMA_GetAttributeI16 | Queries the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxTDSCDMA_GetAttributeI32 | Queries the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxTDSCDMA_GetAttributeI32Array | Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxTDSCDMA_GetAttributeI64 | Queries the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxTDSCDMA_GetAttributeI64Array | Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxTDSCDMA_GetAttributeI8 | Queries the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxTDSCDMA_GetAttributeI8Array | Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxTDSCDMA_GetAttributeNIComplexDoubleArray | Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxTDSCDMA_GetAttributeNIComplexSingleArray | Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxTDSCDMA_GetAttributeString | Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxTDSCDMA_GetAttributeU16 | Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxTDSCDMA_GetAttributeU32 | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxTDSCDMA_GetAttributeU32Array | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxTDSCDMA_GetAttributeU64Array | Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxTDSCDMA_GetAttributeU8 | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxTDSCDMA_GetAttributeU8Array | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga109c96ac0a2b4afb2dc2f4c430475ccf.html language=enus -->
## TOPIC 00284: RFmxTDSCDMA_GetAttributeU16

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga109c96ac0a2b4afb2dc2f4c430475ccf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga109c96ac0a2b4afb2dc2f4c430475ccf.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifi

### RFmxTDSCDMA_GetAttributeU16

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga23378ac8fef52b972f0afdd3da3fae75.html language=enus -->
## TOPIC 00285: RFmxTDSCDMA_GetAttributeI64Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga23378ac8fef52b972f0afdd3da3fae75.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga23378ac8fef52b972f0afdd3da3fae75.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxTDSCDMA_GetAttributeI64Array

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga27b9be72b94e2bdd9bf883bad8ee9790.html language=enus -->
## TOPIC 00286: RFmxTDSCDMA_GetAttributeU32Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga27b9be72b94e2bdd9bf883bad8ee9790.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga27b9be72b94e2bdd9bf883bad8ee9790.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxTDSCDMA_GetAttributeU32Array

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga28ba7845deb0dc00de75af71531697d1.html language=enus -->
## TOPIC 00287: RFmxTDSCDMA_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga28ba7845deb0dc00de75af71531697d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga28ba7845deb0dc00de75af71531697d1.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxTDSCDMA_GetAttributeNIComplexDoubleArray

Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexDouble[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga44f82059153ce408eadefa3f2e3a74ab.html language=enus -->
## TOPIC 00288: RFmxTDSCDMA_GetAttributeI64

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga44f82059153ce408eadefa3f2e3a74ab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga44f82059153ce408eadefa3f2e3a74ab.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxTDSCDMA_GetAttributeI64

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga4ad5cb5adc9620d51ebc621e4980f88c.html language=enus -->
## TOPIC 00289: RFmxTDSCDMA_GetAttributeString

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga4ad5cb5adc9620d51ebc621e4980f88c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga4ad5cb5adc9620d51ebc621e4980f88c.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the a

### RFmxTDSCDMA_GetAttributeString

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 arraySize, char attrVal[])

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| attrVal | [out] | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga5a11225a9b4494ccf2d209d825f6cb05.html language=enus -->
## TOPIC 00290: RFmxTDSCDMA_GetAttributeI8Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga5a11225a9b4494ccf2d209d825f6cb05.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga5a11225a9b4494ccf2d209d825f6cb05.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and

### RFmxTDSCDMA_GetAttributeI8Array

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga6479f4a0f1a970f501d4e1f9bdb43931.html language=enus -->
## TOPIC 00291: RFmxTDSCDMA_GetAttributeU8Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga6479f4a0f1a970f501d4e1f9bdb43931.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga6479f4a0f1a970f501d4e1f9bdb43931.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arra

### RFmxTDSCDMA_GetAttributeU8Array

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga66f81f9d376c114ba29a7453f925bccf.html language=enus -->
## TOPIC 00292: RFmxTDSCDMA_GetAttributeNIComplexSingleArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga66f81f9d376c114ba29a7453f925bccf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga66f81f9d376c114ba29a7453f925bccf.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxTDSCDMA_GetAttributeNIComplexSingleArray

Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexSingle[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga7679753b3d7febaeed2d83d2f73fc55b.html language=enus -->
## TOPIC 00293: RFmxTDSCDMA_GetAttributeI8

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga7679753b3d7febaeed2d83d2f73fc55b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga7679753b3d7febaeed2d83d2f73fc55b.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx ses

### RFmxTDSCDMA_GetAttributeI8

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga7e82653731b6af8b176c904bc38568ed.html language=enus -->
## TOPIC 00294: RFmxTDSCDMA_GetAttributeU64Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga7e82653731b6af8b176c904bc38568ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga7e82653731b6af8b176c904bc38568ed.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxTDSCDMA_GetAttributeU64Array

Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga808830045222b5649c9224970ef22cf9.html language=enus -->
## TOPIC 00295: RFmxTDSCDMA_GetAttributeU8

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga808830045222b5649c9224970ef22cf9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga808830045222b5649c9224970ef22cf9.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies t

### RFmxTDSCDMA_GetAttributeU8

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga8cb444bf4318195ed7aefa32c27fbfb7.html language=enus -->
## TOPIC 00296: RFmxTDSCDMA_GetAttributeI16

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga8cb444bf4318195ed7aefa32c27fbfb7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga8cb444bf4318195ed7aefa32c27fbfb7.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxTDSCDMA_GetAttributeI16

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaa01e6f22f6508a5fd35a80d85f536a66.html language=enus -->
## TOPIC 00297: RFmxTDSCDMA_GetAttributeF64

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaa01e6f22f6508a5fd35a80d85f536a66.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaa01e6f22f6508a5fd35a80d85f536a66.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleI

### RFmxTDSCDMA_GetAttributeF64

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaacb72951b1dc7248462dd5bd009c2030.html language=enus -->
## TOPIC 00298: RFmxTDSCDMA_GetAttributeU32

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaacb72951b1dc7248462dd5bd009c2030.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaacb72951b1dc7248462dd5bd009c2030.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifi

### RFmxTDSCDMA_GetAttributeU32

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gab3793d059503768bc67678a7a2851ab3.html language=enus -->
## TOPIC 00299: RFmxTDSCDMA_GetAttributeI32

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gab3793d059503768bc67678a7a2851ab3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gab3793d059503768bc67678a7a2851ab3.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxTDSCDMA_GetAttributeI32

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaceb5990292ee61f62c59f297d306c039.html language=enus -->
## TOPIC 00300: RFmxTDSCDMA_GetAttributeF32Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaceb5990292ee61f62c59f297d306c039.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaceb5990292ee61f62c59f297d306c039.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxTDSCDMA_GetAttributeF32Array

Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gad035d6507e01b94e4833dc34378b8da8.html language=enus -->
## TOPIC 00301: RFmxTDSCDMA_GetAttributeF64Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gad035d6507e01b94e4833dc34378b8da8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gad035d6507e01b94e4833dc34378b8da8.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxTDSCDMA_GetAttributeF64Array

Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gae0a210dd75639f177d32e5c3431fa840.html language=enus -->
## TOPIC 00302: RFmxTDSCDMA_GetAttributeF32

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gae0a210dd75639f177d32e5c3431fa840.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gae0a210dd75639f177d32e5c3431fa840.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleI

### RFmxTDSCDMA_GetAttributeF32

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaf705c49d9f7d83112b4c964449bbe14e.html language=enus -->
## TOPIC 00303: RFmxTDSCDMA_GetAttributeI32Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaf705c49d9f7d83112b4c964449bbe14e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaf705c49d9f7d83112b4c964449bbe14e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxTDSCDMA_GetAttributeI32Array

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxTDSCDMA_GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes.html language=enus -->
## TOPIC 00304: Set Attributes

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_SetAttributeF32Sets the value of an RFmx 32-bit floating point number (float32) attribute. RFmxTDSCDMA_SetAttributeF32ArraySets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer

### Set Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_SetAttributeF32 | Sets the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxTDSCDMA_SetAttributeF32Array | Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxTDSCDMA_SetAttributeF64 | Sets the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxTDSCDMA_SetAttributeF64Array | Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxTDSCDMA_SetAttributeI16 | Sets the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxTDSCDMA_SetAttributeI32 | Sets the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxTDSCDMA_SetAttributeI32Array | Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxTDSCDMA_SetAttributeI64 | Sets the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxTDSCDMA_SetAttributeI64Array | Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxTDSCDMA_SetAttributeI8 | Sets the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxTDSCDMA_SetAttributeI8Array | Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxTDSCDMA_SetAttributeNIComplexDoubleArray | Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxTDSCDMA_SetAttributeNIComplexSingleArray | Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxTDSCDMA_SetAttributeString | Sets the value of an RFmx string attribute. |
| RFmxTDSCDMA_SetAttributeU16 | Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxTDSCDMA_SetAttributeU32 | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxTDSCDMA_SetAttributeU32Array | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxTDSCDMA_SetAttributeU64Array | Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxTDSCDMA_SetAttributeU8 | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxTDSCDMA_SetAttributeU8Array | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga00651f78a86894673b147d11f5a8ebef.html language=enus -->
## TOPIC 00305: RFmxTDSCDMA_SetAttributeNIComplexSingleArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga00651f78a86894673b147d11f5a8ebef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga00651f78a86894673b147d11f5a8ebef.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char select

### RFmxTDSCDMA_SetAttributeNIComplexSingleArray

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga02cb8533f55f3bb218897bd15095c3e2.html language=enus -->
## TOPIC 00306: RFmxTDSCDMA_SetAttributeF32Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga02cb8533f55f3bb218897bd15095c3e2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga02cb8533f55f3bb218897bd15095c3e2.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle,

### RFmxTDSCDMA_SetAttributeF32Array

Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga0bb1bad675e6f980326b12249d460559.html language=enus -->
## TOPIC 00307: RFmxTDSCDMA_SetAttributeString

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga0bb1bad675e6f980326b12249d460559.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga0bb1bad675e6f980326b12249d460559.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx string attribute. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. You ca

### RFmxTDSCDMA_SetAttributeString

Sets the value of an RFmx string attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | char[] | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga149b1b8a6aee37d3e95c4631efe2fc2e.html language=enus -->
## TOPIC 00308: RFmxTDSCDMA_SetAttributeU16

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga149b1b8a6aee37d3e95c4631efe2fc2e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga149b1b8a6aee37d3e95c4631efe2fc2e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies t

### RFmxTDSCDMA_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga15125e5563fc68a627bd4a7855f4ec85.html language=enus -->
## TOPIC 00309: RFmxTDSCDMA_SetAttributeF64

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga15125e5563fc68a627bd4a7855f4ec85.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga15125e5563fc68a627bd4a7855f4ec85.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdent

### RFmxTDSCDMA_SetAttributeF64

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga15bfdf698daf8ae47568d0e9a62182c1.html language=enus -->
## TOPIC 00310: RFmxTDSCDMA_SetAttributeI8Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga15bfdf698daf8ae47568d0e9a62182c1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga15bfdf698daf8ae47568d0e9a62182c1.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString

### RFmxTDSCDMA_SetAttributeI8Array

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga15e149873b26df3187e662d426fd8a1e.html language=enus -->
## TOPIC 00311: RFmxTDSCDMA_SetAttributeU8

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga15e149873b26df3187e662d426fd8a1e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga15e149873b26df3187e662d426fd8a1e.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the R

### RFmxTDSCDMA_SetAttributeU8

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga2b4f4e7eb49d54bba45332b8fa65995d.html language=enus -->
## TOPIC 00312: RFmxTDSCDMA_SetAttributeI64

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga2b4f4e7eb49d54bba45332b8fa65995d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga2b4f4e7eb49d54bba45332b8fa65995d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx ses

### RFmxTDSCDMA_SetAttributeI64

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga3384317fd239ea3b413f35f8d5c65f0a.html language=enus -->
## TOPIC 00313: RFmxTDSCDMA_SetAttributeI32

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga3384317fd239ea3b413f35f8d5c65f0a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga3384317fd239ea3b413f35f8d5c65f0a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx ses

### RFmxTDSCDMA_SetAttributeI32

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga390d9592f74423b398d0c56073e22d4c.html language=enus -->
## TOPIC 00314: RFmxTDSCDMA_SetAttributeI32Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga390d9592f74423b398d0c56073e22d4c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga390d9592f74423b398d0c56073e22d4c.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorStr

### RFmxTDSCDMA_SetAttributeI32Array

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga4f3e171cf320a8d0f5675401ca9d7774.html language=enus -->
## TOPIC 00315: RFmxTDSCDMA_SetAttributeI64Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga4f3e171cf320a8d0f5675401ca9d7774.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga4f3e171cf320a8d0f5675401ca9d7774.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorStr

### RFmxTDSCDMA_SetAttributeI64Array

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga5e7a74f28c41f73b7519741bd5e37e3f.html language=enus -->
## TOPIC 00316: RFmxTDSCDMA_SetAttributeF32

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga5e7a74f28c41f73b7519741bd5e37e3f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga5e7a74f28c41f73b7519741bd5e37e3f.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdent

### RFmxTDSCDMA_SetAttributeF32

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga6e15cd6543ae17ee2731dd882fe40ea1.html language=enus -->
## TOPIC 00317: RFmxTDSCDMA_SetAttributeI8

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga6e15cd6543ae17ee2731dd882fe40ea1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga6e15cd6543ae17ee2731dd882fe40ea1.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session

### RFmxTDSCDMA_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga74fc657b5a5f0e4c75dc2be808bd0d1d.html language=enus -->
## TOPIC 00318: RFmxTDSCDMA_SetAttributeF64Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga74fc657b5a5f0e4c75dc2be808bd0d1d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga74fc657b5a5f0e4c75dc2be808bd0d1d.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle,

### RFmxTDSCDMA_SetAttributeF64Array

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga96fb54721062f96145d8bd52aaad031b.html language=enus -->
## TOPIC 00319: RFmxTDSCDMA_SetAttributeU64Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga96fb54721062f96145d8bd52aaad031b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga96fb54721062f96145d8bd52aaad031b.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char s

### RFmxTDSCDMA_SetAttributeU64Array

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gaa2004e1e2c56729588ed7a8af0ef0395.html language=enus -->
## TOPIC 00320: RFmxTDSCDMA_SetAttributeU32

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gaa2004e1e2c56729588ed7a8af0ef0395.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gaa2004e1e2c56729588ed7a8af0ef0395.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies t

### RFmxTDSCDMA_SetAttributeU32

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gacb1a325caee72435882620c02a8d3793.html language=enus -->
## TOPIC 00321: RFmxTDSCDMA_SetAttributeU8Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gacb1a325caee72435882620c02a8d3793.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gacb1a325caee72435882620c02a8d3793.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char sele

### RFmxTDSCDMA_SetAttributeU8Array

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gad9b1c9aca6b0eae10e840653cbbb66b7.html language=enus -->
## TOPIC 00322: RFmxTDSCDMA_SetAttributeI16

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gad9b1c9aca6b0eae10e840653cbbb66b7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gad9b1c9aca6b0eae10e840653cbbb66b7.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx ses

### RFmxTDSCDMA_SetAttributeI16

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gaee1ac4dddd0247c88df335a661faec95.html language=enus -->
## TOPIC 00323: RFmxTDSCDMA_SetAttributeU32Array

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gaee1ac4dddd0247c88df335a661faec95.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gaee1ac4dddd0247c88df335a661faec95.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char s

### RFmxTDSCDMA_SetAttributeU32Array

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gaf894562227c82ad15581839eb455f17c.html language=enus -->
## TOPIC 00324: RFmxTDSCDMA_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gaf894562227c82ad15581839eb455f17c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gaf894562227c82ad15581839eb455f17c.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxTDSCDMA_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char select

### RFmxTDSCDMA_SetAttributeNIComplexDoubleArray

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxTDSCDMA_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility.html language=enus -->
## TOPIC 00325: Utility

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxTDSCDMA_CheckMeasurementStatusChecks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. RFmxTDSCDMA_CommitCommits settings to t

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxTDSCDMA_CheckMeasurementStatus | Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxTDSCDMA_Commit | Commits settings to the hardware. Calling this function is optional. RFmxTDSCDMA commits settings to the hardware when you call the RFmxTDSCDMA_Initiate function. |
| RFmxTDSCDMA_InitializeFromNIRFSASession | Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. |
| RFmxTDSCDMA_ResetAttribute | Resets an attribute that you specify in the attributeID parameter to default values. |
| RFmxTDSCDMA_ResetToDefault | Resets a signal to the default values. |
| RFmxTDSCDMA_WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. |
| RFmxTDSCDMA_WaitForMeasurementComplete | Waits for the specified number of seconds for all the measurements to complete. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1ga487ced59c14ac790ce2af2a041ada115.html language=enus -->
## TOPIC 00326: RFmxTDSCDMA_InitializeFromNIRFSASession

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1ga487ced59c14ac790ce2af2a041ada115.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1ga487ced59c14ac790ce2af2a041ada115.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device

### RFmxTDSCDMA_InitializeFromNIRFSASession

Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxTDSCDMA_InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle *handleOut)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_InitializeFromNIRFSASession](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| nirfsaSession | [in] | uInt32 | Specifies the NIRFSA session handle of the device to initialize. |
| handleOut | [out] | niRFmxInstrHandle * | Returns an RFmx instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1ga4d30b0fbba5db3a58674f307bf387b86.html language=enus -->
## TOPIC 00327: RFmxTDSCDMA_ResetToDefault

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1ga4d30b0fbba5db3a58674f307bf387b86.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1ga4d30b0fbba5db3a58674f307bf387b86.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. Syntaxint32 __stdcall RFmxTDSCDMA_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. This parameter is obtained fr

### RFmxTDSCDMA_ResetToDefault

Resets a signal to the default values.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gabc14af37bc05dd6bdf1a3acf6252a9b0.html language=enus -->
## TOPIC 00328: RFmxTDSCDMA_Commit

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gabc14af37bc05dd6bdf1a3acf6252a9b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gabc14af37bc05dd6bdf1a3acf6252a9b0.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this function is optional. RFmxTDSCDMA commits settings to the hardware when you call the RFmxTDSCDMA_Initiate function. Syntaxint32 __stdcall RFmxTDSCDMA_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescription

### RFmxTDSCDMA_Commit

Commits settings to the hardware. Calling this function is optional. RFmxTDSCDMA commits settings to the hardware when you call the [RFmxTDSCDMA_Initiate](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1gaa56fe53b840183812166224dfb1bd11f.html) function.

#### Syntax

int32 __stdcall RFmxTDSCDMA_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gabd537269922701deb35c179b3cd6eb09.html language=enus -->
## TOPIC 00329: RFmxTDSCDMA_WaitForAcquisitionComplete

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gabd537269922701deb35c179b3cd6eb09.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gabd537269922701deb35c179b3cd6eb09.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. Syntaxint32 __stdcall RFmxTDSCDMA_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)RemarksThis function is a wrapper over the RFmx Instr

### RFmxTDSCDMA_WaitForAcquisitionComplete

Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function.

#### Syntax

int32 __stdcall RFmxTDSCDMA_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?context=rfmxinstr_rfmxinstrcref_function_wait_for_acquisition_complete) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| timeout | [in] | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gac4a9a2325844149b1a4f3f91d464ee78.html language=enus -->
## TOPIC 00330: RFmxTDSCDMA_CheckMeasurementStatus

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gac4a9a2325844149b1a4f3f91d464ee78.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gac4a9a2325844149b1a4f3f91d464ee78.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. Syntaxint32 __stdcall RFmxTDSCDMA_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorStrin

### RFmxTDSCDMA_CheckMeasurementStatus

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

int32 __stdcall RFmxTDSCDMA_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *done)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| done | [out] | int32 * | This parameter indicates whether the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gae29202c3085a7be24967a72c44e889bc.html language=enus -->
## TOPIC 00331: RFmxTDSCDMA_WaitForMeasurementComplete

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gae29202c3085a7be24967a72c44e889bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gae29202c3085a7be24967a72c44e889bc.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number of seconds for all the measurements to complete. Syntaxint32 __stdcall RFmxTDSCDMA_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis para

### RFmxTDSCDMA_WaitForMeasurementComplete

Waits for the specified number of seconds for all the measurements to complete.

#### Syntax

int32 __stdcall RFmxTDSCDMA_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gaff896ef1553d17ff387ce3f623f5aeb4.html language=enus -->
## TOPIC 00332: RFmxTDSCDMA_ResetAttribute

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gaff896ef1553d17ff387ce3f623f5aeb4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_t_d_s_c_d_m_a__functions__utility_1gaff896ef1553d17ff387ce3f623f5aeb4.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets an attribute that you specify in the attributeID parameter to default values. Syntaxint32 __stdcall RFmxTDSCDMA_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxTDSCDMA_ResetAttribute

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Syntax

int32 __stdcall RFmxTDSCDMA_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being reset. Refer to the Selector String (C or LabWindows/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxTDSCDMA_GetError](group____root__ni_r_fmx_t_d_s_c_d_m_a__functions_1ga926552471461086ede8d1df9043a3ac4.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxtdscdma-c-api-ref path=group__root__ni_r_fmx_t_d_s_c_d_m_a.html language=enus -->
## TOPIC 00333: niRFmxTDSCDMA.h

- bundle_id: `rfmxtdscdma-c-api-ref`
- source_path: `group__root__ni_r_fmx_t_d_s_c_d_m_a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-c-api-ref/raw/resource/enus/group__root__ni_r_fmx_t_d_s_c_d_m_a.html
- document_id: `rfmxtdscdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niRFmxTDSCDMA.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
