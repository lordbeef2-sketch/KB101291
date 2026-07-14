# NI DOCUMENT BUNDLE: rfmxnr-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxnr-c-api-ref start=251 end=336 -->
<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga64aef46c7ec705a78ad7549c03837584.html language=enus -->
## TOPIC 00251: RFmxNR_ModAccFetchPDSCH1024QAMConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga64aef46c7ec705a78ad7549c03837584.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga64aef46c7ec705a78ad7549c03837584.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PDSCH 1024 QAM constellation trace. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCH1024QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024ConstellationI[], float32 qam1024ConstellationQ[], int32 arraySize, int32 *actualArra

### RFmxNR_ModAccFetchPDSCH1024QAMConstellationTraceSplit

Fetches the PDSCH 1024 QAM constellation trace.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCH1024QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024ConstellationI[], float32 qam1024ConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam1024ConstellationI | [out] | float32[] | This parameter Returns the real part of 1024 QAM constellation trace. |
| qam1024ConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of 1024 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6789f1d38b76a87b165cfdfedfb4a642.html language=enus -->
## TOPIC 00252: RFmxNR_ModAccFetchPSSConstellationTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6789f1d38b76a87b165cfdfedfb4a642.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6789f1d38b76a87b165cfdfedfb4a642.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PSS constellation trace. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPSSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pssConstellation[], in

### RFmxNR_ModAccFetchPSSConstellationTrace

Fetches the PSS constellation trace. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPSSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pssConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pssConstellation | [out] | NIComplexSingle[] | This parameter returns the PSS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6a747bec13080ca98232f6c6b0caf86e.html language=enus -->
## TOPIC 00253: RFmxNR_ModAccFetchPDSCH8PSKConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6a747bec13080ca98232f6c6b0caf86e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6a747bec13080ca98232f6c6b0caf86e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH 8 PSK constellation trace. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCH8PSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8ConstellationI[], float32 psk8ConstellationQ[], int32 arraySize, int32 *actualArraySize)RemarksUse

### RFmxNR_ModAccFetchPDSCH8PSKConstellationTraceSplit

Fetches PDSCH 8 PSK constellation trace.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCH8PSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 psk8ConstellationI[], float32 psk8ConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| psk8ConstellationI | [out] | float32[] | This parameter Returns the real part of PDSCH 8 PSK constellation trace. |
| psk8ConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PDSCH 8 PSK constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6a94473c625418e0e481ae5543f57291.html language=enus -->
## TOPIC 00254: RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6a94473c625418e0e481ae5543f57291.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6a94473c625418e0e481ae5543f57291.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH PTRS trace. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschPTRSConstellationI[], float32 pdschPTRSConstellationQ[], int32 arraySize, int32 *actualArraySize)RemarksUse "use

### RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit

Fetches PDSCH PTRS trace.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschPTRSConstellationI[], float32 pdschPTRSConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<k>" or "carrier<<i>l</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>l</i>>/user<k>" as the selector string to read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0".Example:"subblock0/carrier0/user0""signal::sig1/subblock0/carrier0/user0""result::r1/subblock0/carrier0/user0""signal::sig1/result::r1/subblock0/carrier0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pdschPTRSConstellationI | [out] | float32[] | This parameter Returns the real part of PDSCH PTRS constellation trace. |
| pdschPTRSConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PDSCH PTRS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6f3cacba76ddebf0d584c2b1432445da.html language=enus -->
## TOPIC 00255: RFmxNR_ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6f3cacba76ddebf0d584c2b1432445da.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga6f3cacba76ddebf0d584c2b1432445da.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean PBCH data RMS EVM for each symbol. Syntaxint32 __stdcall RFmxNR_ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pbchDataRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArra

### RFmxNR_ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace

Fetches the mean PBCH data RMS EVM for each symbol.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pbchDataRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start symbol index from the frame start in terms of SSB numerology. |
| dx | [out] | float64 * | This parameter returns the width in terms of symbols. |
| pbchDataRMSEVMPerSymbolMean | [out] | float32[] | This parameter returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PBCH data within symbol. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga78b818c09fc82430962394e401e88393.html language=enus -->
## TOPIC 00256: RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga78b818c09fc82430962394e401e88393.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga78b818c09fc82430962394e401e88393.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH 16 QAM trace. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16ConstellationI[], float32 qam16ConstellationQ[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrier<

### RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit

Fetches PDSCH 16 QAM trace.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16ConstellationI[], float32 qam16ConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam16ConstellationI | [out] | float32[] | This parameter Returns the real part of 16 QAM constellation trace. |
| qam16ConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of 16 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga79e42a934b5278c39c60df6e83475589.html language=enus -->
## TOPIC 00257: RFmxNR_ModAccFetchPBCHDMRSConstellationTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga79e42a934b5278c39c60df6e83475589.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga79e42a934b5278c39c60df6e83475589.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PBCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPBCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchDMRSConstellation[],

### RFmxNR_ModAccFetchPBCHDMRSConstellationTrace

Fetches the PBCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPBCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchDMRSConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pbchDMRSConstellation | [out] | NIComplexSingle[] | This parameter returns the PBCH DMRS trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga7c68aacc9c218ae41c1222bc7464ae13.html language=enus -->
## TOPIC 00258: RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga7c68aacc9c218ae41c1222bc7464ae13.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga7c68aacc9c218ae41c1222bc7464ae13.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH 64 QAM trace. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam64Constellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrier<k>" or "subblock<n>" or "subb

### RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace

Fetches PDSCH 64 QAM trace.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam64Constellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam64Constellation | [out] | NIComplexSingle[] | This parameter returns the 64 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga81224d4c9ef0d37192f121149cbc3923.html language=enus -->
## TOPIC 00259: RFmxNR_ModAccFetchPUSCHPhaseOffsetTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga81224d4c9ef0d37192f121149cbc3923.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga81224d4c9ef0d37192f121149cbc3923.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the phase offset for the slots with respect to the reference slot. Syntaxint32 __stdcall RFmxNR_ModAccFetchPUSCHPhaseOffsetTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 puschPhaseOffset[], int32 arraySize, int32 *actualArr

### RFmxNR_ModAccFetchPUSCHPhaseOffsetTrace

Returns the phase offset for the slots with respect to the reference slot.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPUSCHPhaseOffsetTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 puschPhaseOffset[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<k>" or "carrier<<i>l</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>l</i>>/user<k>" or "subblock<n>/carrier<k>/user<k>/layer<<i>q</i>>" as the selector string to read this function.

The length of the trace is equal to the number of slots within the measurement length.

For each burst of continuously allocated slots, the first active slot in the burst is used as the reference slot.

The reference slot is reset at frame boundary.

The phase offset is calculated for slots that are contiguous to the reference slot and have overlapping subcarrier allocations. For all other slots, NaN is provided.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, user number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0/layer0".Example:"subblock0/carrier0/user0/layer0""signal::sig1/subblock0/carrier0/user0/layer0""result::r1/subblock0/carrier0/user0/layer0""signal::sig1/result::r1/subblock0/carrier0/user0/layer0"You can use the RFmxNR_BuildUserString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the index of the first active slot. |
| dx | [out] | float64 * | This parameter returns the increment value. This is always set to one slot. |
| puschPhaseOffset | [out] | float32[] | This parameter returns an array of the maximum value across averaging counts of the phase error per slot for all slots within the measurement length. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga8d7e32b9076bdf463b99b9b65dbb8ec2.html language=enus -->
## TOPIC 00260: RFmxNR_ModAccFetchPDSCHDataConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga8d7e32b9076bdf463b99b9b65dbb8ec2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga8d7e32b9076bdf463b99b9b65dbb8ec2.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the recovered PDSCH data constellation points. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 p

### RFmxNR_ModAccFetchPDSCHDataConstellationTraceSplit

Fetches the recovered PDSCH data constellation points. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDataConstellationI[], float32 pdschDataConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<k>" or "carrier<<i>l</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>l</i>>/user<k>" as the selector string to read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0".Example:"subblock0/carrier0/user0""signal::sig1/subblock0/carrier0/user0""result::r1/subblock0/carrier0/user0""signal::sig1/result::r1/subblock0/carrier0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pdschDataConstellationI | [out] | float32[] | This parameter Returns the real part of PDSCH data constellation trace. |
| pdschDataConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PDSCH data constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga929e333465b510d5255b3e02a86bef3c.html language=enus -->
## TOPIC 00261: RFmxNR_ModAccFetchInBandEmissionTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga929e333465b510d5255b3e02a86bef3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga929e333465b510d5255b3e02a86bef3c.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the in-band emission trace and limits trace for the component carrier. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier l

### RFmxNR_ModAccFetchInBandEmissionTrace

Fetches the in-band emission trace and limits trace for the component carrier. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4.2.3 of *3GPP 38.101-1*, and section 6.4.2.3 of *3GPP 38.101-2*. The trace is not returned when there is full allocation of bandwidth, or there is clustered PUSCH or there is more than one active component carrier.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchInBandEmissionTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 inBandEmission[], float32 inBandEmissionMask[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/chain<<i>r</i>>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/chain0".Example:"subblock0/carrier0/chain0""signal::sig1/subblock0/carrier0/chain0""result::r1/subblock0/carrier0/chain0""signal::sig1/result::r1/subblock0/carrier0/chain0"You can use the RFmxNR_BuildCarrierString and RFmxNR_BuildChainStringVIs to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start point of the of the resource block. |
| dx | [out] | float64 * | This parameter returns the subcarrier spacing. |
| inBandEmission | [out] | float32[] | This parameter returns an array of the in-band emission value as an array for each of the resource blocks. In-band emission is the interference falling into non-allocated resource blocks. This value is expressed in dB. |
| inBandEmissionMask | [out] | float32[] | This parameter returns an array of the in-band emission value as an array for each of the resource blocks. In-band emission is the interference falling into non-allocated resource blocks. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga942d39d5717764c36c5b1cc6dc184bb9.html language=enus -->
## TOPIC 00262: RFmxNR_ModAccFetchPSSConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga942d39d5717764c36c5b1cc6dc184bb9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga942d39d5717764c36c5b1cc6dc184bb9.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PSS constellation trace. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPSSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellationI[], floa

### RFmxNR_ModAccFetchPSSConstellationTraceSplit

Fetches the PSS constellation trace. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPSSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pssConstellationI[], float32 pssConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pssConstellationI | [out] | float32[] | This parameter Returns the real part of PSS constellation trace. |
| pssConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PSS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga9527028f4edcf9c1921a55eb56201f95.html language=enus -->
## TOPIC 00263: RFmxNR_ModAccFetchPUSCHDMRSConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga9527028f4edcf9c1921a55eb56201f95.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga9527028f4edcf9c1921a55eb56201f95.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PUSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPUSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDMRSConstellationI[], flo

### RFmxNR_ModAccFetchPUSCHDMRSConstellationTraceSplit

Fetches PUSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPUSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDMRSConstellationI[], float32 puschDMRSConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<k>" or "carrier<<i>l</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>l</i>>/user<k>" or "subblock<n>/carrier<k>/user<k>/layer<<i>q</i>>" as the selector string to read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, user number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0/layer0".Example:"subblock0/carrier0/user0/layer0""signal::sig1/subblock0/carrier0/user0/layer0""result::r1/subblock0/carrier0/user0/layer0""signal::sig1/result::r1/subblock0/carrier0/user0/layer0"You can use the RFmxNR_BuildUserString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| puschDMRSConstellationI | [out] | float32[] | This parameter Returns the real part of PDSCH DMRS constellation trace. |
| puschDMRSConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PDSCH DMRS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga98e7ae45b3dd61bab4efa7879a99e3d1.html language=enus -->
## TOPIC 00264: RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga98e7ae45b3dd61bab4efa7879a99e3d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga98e7ae45b3dd61bab4efa7879a99e3d1.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH 16 QAM trace. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrier<k>" or "subblock<n>" or "subb

### RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace

Fetches PDSCH 16 QAM trace.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam16Constellation | [out] | NIComplexSingle[] | This parameter returns the 16 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga9ba1dc1153e30287f6aec1dd17ae9dc8.html language=enus -->
## TOPIC 00265: RFmxNR_ModAccFetchPBCHDataConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga9ba1dc1153e30287f6aec1dd17ae9dc8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga9ba1dc1153e30287f6aec1dd17ae9dc8.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PBCH data trace. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPBCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellationI[], fl

### RFmxNR_ModAccFetchPBCHDataConstellationTraceSplit

Fetches the PBCH data trace. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPBCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchDataConstellationI[], float32 pbchDataConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pbchDataConstellationI | [out] | float32[] | This parameter Returns the real part of PBCH data trace. |
| pbchDataConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PBCH data trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga9d44451ce7f8faf6da449a8057eac946.html language=enus -->
## TOPIC 00266: RFmxNR_ModAccFetchSubblockInBandEmissionTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga9d44451ce7f8faf6da449a8057eac946.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1ga9d44451ce7f8faf6da449a8057eac946.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the in-band emission trace and limit trace for the the subblocks aggregated bandwidth. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (ge

### RFmxNR_ModAccFetchSubblockInBandEmissionTrace

Returns the in-band emission trace and limit trace for the the subblocks aggregated bandwidth. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4A.2.2.2 of *3GPP 38.101-1*, and section 6.4A.2.3 of *3GPP 38.101-2*. The trace is not returned when there is clustered PUSCH allocation, or when there is more than one active carrier, or when there is full allocation of resource blocks, or when carriers with different sub-carrier spacing are aggregated, or when the number of carriers is greater than 2.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchSubblockInBandEmissionTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 subblockInBandEmission[], float64 subblockInBandEmissionMask[], float64 subblockInBandEmissionRbIndices[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" or "subblock<n>/chain<<i>r</i>>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/chain0".Example:"subblock0/chain0""signal::sig1/subblock0/chain0""result::r1/subblock0/chain0""signal::sig1/result::r1/subblock0/chain0"You can use the RFmxNR_BuildSubblockString and RFmxNR_BuildChainString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| subblockInBandEmission | [out] | float64[] | This parameter returns the array of subblock in-band emission measurement trace. |
| subblockInBandEmissionMask | [out] | float64[] | This parameter returns the array of subblock in-band emission mask trace. |
| subblockInBandEmissionRbIndices | [out] | float64[] | This parameter returns the array of resource block indices for the subblock in-band emission trace. It can have non integer values depending upon the spacing between carriers. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa08020547fc78945e2f74a8a2b7776ed.html language=enus -->
## TOPIC 00267: RFmxNR_ModAccFetchFrequencyErrorPerSlotMaximumTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa08020547fc78945e2f74a8a2b7776ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa08020547fc78945e2f74a8a2b7776ed.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz. Syntaxint32 __stdcall RFmxNR_ModAccFetchFrequencyErrorPerSlotMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[

### RFmxNR_ModAccFetchFrequencyErrorPerSlotMaximumTrace

Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchFrequencyErrorPerSlotMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 frequencyErrorPerSlotMaximum[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the selector string to read this result.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0".Example:"subblock0/carrier0/layer0""signal::sig1/subblock0/carrier0/layer0""result::r1/subblock0/carrier0/layer0""signal::sig1/result::r1/subblock0/carrier0/layer0"You can use the RFmxNR_BuildCarrierString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the index of the first active slot. |
| dx | [out] | float64 * | This parameter returns the increment value. This is always set to one slot. |
| frequencyErrorPerSlotMaximum | [out] | float32[] | This parameter returns an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa21f590312a83550c38c498c98539005.html language=enus -->
## TOPIC 00268: RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa21f590312a83550c38c498c98539005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa21f590312a83550c38c498c98539005.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDMRSConstellationI[], flo

### RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit

Fetches PDSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pdschDMRSConstellationI[], float32 pdschDMRSConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<k>" or "carrier<<i>l</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>l</i>>/user<k>" as the selector string to read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0".Example:"subblock0/carrier0/user0""signal::sig1/subblock0/carrier0/user0""result::r1/subblock0/carrier0/user0""signal::sig1/result::r1/subblock0/carrier0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pdschDMRSConstellationI | [out] | float32[] | This parameter Returns the real part of PDSCH DMRS constellation trace. |
| pdschDMRSConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PDSCH DMRS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa2b790c5d13b6f79ac42a004a3fe0c39.html language=enus -->
## TOPIC 00269: RFmxNR_ModAccFetchSSSRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa2b790c5d13b6f79ac42a004a3fe0c39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa2b790c5d13b6f79ac42a004a3fe0c39.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean SSS RMS EVM of each symbol. Syntaxint32 __stdcall RFmxNR_ModAccFetchSSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 sssRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArraySize)RemarksUse

### RFmxNR_ModAccFetchSSSRMSEVMPerSymbolMeanTrace

Fetches the mean SSS RMS EVM of each symbol.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchSSSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 sssRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start symbol index from the frame start in terms of SSB numerology. |
| dx | [out] | float64 * | This parameter returns the width in terms of symbols. |
| sssRMSEVMPerSymbolMean | [out] | float32[] | This parameter returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with SSS within symbol. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa37711cbdb4d78ae8f71407933c4f983.html language=enus -->
## TOPIC 00270: RFmxNR_ModAccFetchRMSEVMPerSlotMeanTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa37711cbdb4d78ae8f71407933c4f983.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaa37711cbdb4d78ae8f71407933c4f983.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot. Syntaxint32 __stdcall RFmxNR_ModAccFetchRMSEVMPerSlotMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rmsEVMPerSlotM

### RFmxNR_ModAccFetchRMSEVMPerSlotMeanTrace

Fetches the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchRMSEVMPerSlotMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rmsEVMPerSlotMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0".Example:"subblock0/carrier0/layer0""signal::sig1/subblock0/carrier0/layer0""result::r1/subblock0/carrier0/layer0""signal::sig1/result::r1/subblock0/carrier0/layer0"You can use the RFmxNR_BuildCarrierString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start point of the of the resource block. |
| dx | [out] | float64 * | This parameter returns the subcarrier spacing. |
| rmsEVMPerSlotMean | [out] | float32[] | This parameter returns an array the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaac26b71b94d508e2ab4c54670d8a036b.html language=enus -->
## TOPIC 00271: RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaac26b71b94d508e2ab4c54670d8a036b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaac26b71b94d508e2ab4c54670d8a036b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C-W/2. Syntaxint32 __stdcall RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, f

### RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace

Fetches the peak EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C-W/2.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 peakEVMLowPerSymbolMaximum[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0".Example:"subblock0/carrier0/layer0""signal::sig1/subblock0/carrier0/layer0""result::r1/subblock0/carrier0/layer0""signal::sig1/result::r1/subblock0/carrier0/layer0"You can use the RFmxNR_BuildCarrierString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM symbol position corresponding to the RFMXNR_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns 1 as the value. |
| peakEVMLowPerSymbolMaximum | [out] | float32[] | This parameter returns an array of the peak EVM per symbol for all confgured slots. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gab872c5e8e2cf9d1b2e8c6f464113280f.html language=enus -->
## TOPIC 00272: RFmxNR_ModAccFetchRMSEVMPerSubcarrierMeanTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gab872c5e8e2cf9d1b2e8c6f464113280f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gab872c5e8e2cf9d1b2e8c6f464113280f.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. Syntaxint32 __stdcall RFmxNR_ModAccFetchRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rmsEVMPerSubc

### RFmxNR_ModAccFetchRMSEVMPerSubcarrierMeanTrace

Fetches the EVM of each allocated subcarrier averaged across all the symbols within the measurement length.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rmsEVMPerSubcarrierMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0".Example:"subblock0/carrier0/layer0""signal::sig1/subblock0/carrier0/layer0""result::r1/subblock0/carrier0/layer0""signal::sig1/result::r1/subblock0/carrier0/layer0"You can use the RFmxNR_BuildCarrierString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start point of the of the resource block. |
| dx | [out] | float64 * | This parameter returns the subcarrier spacing. |
| rmsEVMPerSubcarrierMean | [out] | float32[] | This parameter returns an array the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac06712807f0080c4bdce623227bbbd43.html language=enus -->
## TOPIC 00273: RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac06712807f0080c4bdce623227bbbd43.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac06712807f0080c4bdce623227bbbd43.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean PBCH DMRS RMS EVM for each subcarrier. Syntaxint32 __stdcall RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pbchDMRSRMSEVMPerSubcarrierMean[], int32 arraySize, int32

### RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace

Fetches the mean PBCH DMRS RMS EVM for each subcarrier.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pbchDMRSRMSEVMPerSubcarrierMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start point of the of the resource grid. |
| dx | [out] | float64 * | This parameter returns the subcarrier spacing of SSB. |
| pbchDMRSRMSEVMPerSubcarrierMean | [out] | float32[] | This parameter returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PBCH DMRS within the measurement length. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac13948344bcdc8b7af2ac18492fb0258.html language=enus -->
## TOPIC 00274: RFmxNR_ModAccFetchTransientPeriodLocationsTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac13948344bcdc8b7af2ac18492fb0258.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac13948344bcdc8b7af2ac18492fb0258.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol indices that were identified to have a transient period. Syntaxint32 __stdcall RFmxNR_ModAccFetchTransientPeriodLocationsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 transientPeriodLocations[], int32 arraySize,

### RFmxNR_ModAccFetchTransientPeriodLocationsTrace

Returns the symbol indices that were identified to have a transient period.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchTransientPeriodLocationsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 transientPeriodLocations[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

The length of the trace is equal to the number of symbols within the measurement length.

The trace returns a 1 for the symbol index that was identified to have a transient period; otherwise returns a 0.

- RMS EVM per Symbol Mean Trace
- RMS EVM-High per Symbol Mean Trace
- RMS EVM-Low per Symbol Mean Trace

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start symbol index from the frame start. |
| dx | [out] | float64 * | This parameter returns the width in terms of symbols. |
| transientPeriodLocations | [out] | float32[] | This parameter returns a 1 for the symbol index that was identified to have a transient period; otherwise returns a 0. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac4452303960f5c1091bb2fb15a1873ab.html language=enus -->
## TOPIC 00275: RFmxNR_ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac4452303960f5c1091bb2fb15a1873ab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac4452303960f5c1091bb2fb15a1873ab.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean PSS RMS EVM of each subcarrier. Syntaxint32 __stdcall RFmxNR_ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pssRMSEVMPerSubcarrierMean[], int32 arraySize, int32 *actualArraySize

### RFmxNR_ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace

Fetches the mean PSS RMS EVM of each subcarrier.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pssRMSEVMPerSubcarrierMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start point of the of the resource grid. |
| dx | [out] | float64 * | This parameter returns the subcarrier spacing of SSB. |
| pssRMSEVMPerSubcarrierMean | [out] | float32[] | This parameter returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PSS within the measurement length. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac5015db2b2c1ccd3d81edf53962d6b38.html language=enus -->
## TOPIC 00276: RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac5015db2b2c1ccd3d81edf53962d6b38.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gac5015db2b2c1ccd3d81edf53962d6b38.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschDMRSConstellation[], i

### RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace

Fetches PDSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschDMRSConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<k>" or "carrier<<i>l</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>l</i>>/user<k>" as the selector string to read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0".Example:"subblock0/carrier0/user0""signal::sig1/subblock0/carrier0/user0""result::r1/subblock0/carrier0/user0""signal::sig1/result::r1/subblock0/carrier0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pdschDMRSConstellation | [out] | NIComplexSingle[] | This parameter returns the PDSCH DMRS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaca52c4fcfd8751410c5006b3a3640af4.html language=enus -->
## TOPIC 00277: RFmxNR_ModAccFetchPDSCHDataConstellationTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaca52c4fcfd8751410c5006b3a3640af4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaca52c4fcfd8751410c5006b3a3640af4.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the recovered PDSCH data constellation points. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingl

### RFmxNR_ModAccFetchPDSCHDataConstellationTrace

Fetches the recovered PDSCH data constellation points. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCHDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pdschDataConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<k>" or "carrier<<i>l</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>l</i>>/user<k>" as the selector string to read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0".Example:"subblock0/carrier0/user0""signal::sig1/subblock0/carrier0/user0""result::r1/subblock0/carrier0/user0""signal::sig1/result::r1/subblock0/carrier0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pdschDataConstellation | [out] | NIComplexSingle[] | This parameter returns the PDSCH data constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gacbfedb6e975faeda31abee8a402b0f34.html language=enus -->
## TOPIC 00278: RFmxNR_ModAccFetchFrequencyErrorMean

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gacbfedb6e975faeda31abee8a402b0f34.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gacbfedb6e975faeda31abee8a402b0f34.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz. Syntaxint32 __stdcall RFmxNR_ModAccFetchFrequencyErrorMean(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *frequencyErrorMean)RemarksUse "carrier<k>" o

### RFmxNR_ModAccFetchFrequencyErrorMean

Fetches the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchFrequencyErrorMean(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *frequencyErrorMean)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the selector string to read this result.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0".Example:"subblock0/carrier0/layer0""signal::sig1/subblock0/carrier0/layer0""result::r1/subblock0/carrier0/layer0""signal::sig1/result::r1/subblock0/carrier0/layer0"You can use the RFmxNR_BuildCarrierString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| frequencyErrorMean | [out] | float64 * | This parameter returns the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gad4daa94571b07b668e10beb55b3a575f.html language=enus -->
## TOPIC 00279: RFmxNR_ModAccFetchCompositeEVM

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gad4daa94571b07b668e10beb55b3a575f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gad4daa94571b07b668e10beb55b3a575f.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the composite EVM for ModAcc measurements. Syntaxint32 __stdcall RFmxNR_ModAccFetchCompositeEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *compositeRMSEVMMean, float64 *compositePeakEVMMaximum)RemarksUse "carrier<k>" or "subblock<n>/carrier<k>" or "s

### RFmxNR_ModAccFetchCompositeEVM

Fetches the composite EVM for ModAcc measurements.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchCompositeEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *compositeRMSEVMMean, float64 *compositePeakEVMMaximum)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<<i>q</i>>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0".Example:"subblock0/carrier0/layer0""signal::sig1/subblock0/carrier0/layer0""result::r1/subblock0/carrier0/layer0""signal::sig1/result::r1/subblock0/carrier0/layer0"You can use the RFmxNR_BuildCarrierString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| compositeRMSEVMMean | [out] | float64 * | This parameter returns the mean value of the RMS EVMs calculated on all configured channels over the slots specified by the RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to Percentage, the measurement returns this result as a percentage.When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to dB, the measurement returns this result in dB. |
| compositePeakEVMMaximum | [out] | float64 * | This parameter returns the maximum value of the peak EVMs calculated on all configured channels over the slots specified by the RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to Percentage, the measurement returns this result as a percentage.When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to dB, the measurement returns this result in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gad9bf9c10533d363b66962b33b9aa2728.html language=enus -->
## TOPIC 00280: RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gad9bf9c10533d363b66962b33b9aa2728.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gad9bf9c10533d363b66962b33b9aa2728.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean PBCH DMRS RMS EVM for each symbol. Syntaxint32 __stdcall RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pbchDMRSRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArra

### RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace

Fetches the mean PBCH DMRS RMS EVM for each symbol.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pbchDMRSRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start symbol index from the frame start in terms of SSB numerology. |
| dx | [out] | float64 * | This parameter returns the width in terms of symbols. |
| pbchDMRSRMSEVMPerSymbolMean | [out] | float32[] | This parameter returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PBCH DMRS within symbol. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gada2e0c4c1b9d1a9e312fe8cddf1e0688.html language=enus -->
## TOPIC 00281: RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gada2e0c4c1b9d1a9e312fe8cddf1e0688.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gada2e0c4c1b9d1a9e312fe8cddf1e0688.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PUSCH Data Constellation trace. The constellation points of different slots in the measurement length is concatenated. Syntaxint32 __stdcall RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstel

### RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit

Fetches PUSCH Data Constellation trace. The constellation points of different slots in the measurement length is concatenated.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 puschDataConstellationI[], float32 puschDataConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<k>" or "carrier<<i>l</i>>" or "subblock<n>" or "subblock<n>/carrier<<i>l</i>>/user<k>" or "subblock<n>/carrier<k>/user<k>/layer<<i>q</i>>" as the selector string to read this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, user number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0/layer0".Example:"subblock0/carrier0/user0/layer0""signal::sig1/subblock0/carrier0/user0/layer0""result::r1/subblock0/carrier0/user0/layer0""signal::sig1/result::r1/subblock0/carrier0/user0/layer0"You can use the RFmxNR_BuildUserString and RFmxNR_BuildLayerString functions to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| puschDataConstellationI | [out] | float32[] | This parameter Returns the real part of PUSCH data constellation trace. |
| puschDataConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PUSCH data constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaf2a0ca1f5129f4c6ca01c24f06c64bfa.html language=enus -->
## TOPIC 00282: RFmxNR_ModAccFetchPDSCHQPSKConstellationTraceSplit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaf2a0ca1f5129f4c6ca01c24f06c64bfa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__modacc_1gaf2a0ca1f5129f4c6ca01c24f06c64bfa.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH QPSK trace. Syntaxint32 __stdcall RFmxNR_ModAccFetchPDSCHQPSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellationI[], float32 qpskConstellationQ[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrier<k>" o

### RFmxNR_ModAccFetchPDSCHQPSKConstellationTraceSplit

Fetches PDSCH QPSK trace.

#### Syntax

int32 __stdcall RFmxNR_ModAccFetchPDSCHQPSKConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellationI[], float32 qpskConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qpskConstellationI | [out] | float32[] | This parameter Returns the real part of QPSK constellation trace. |
| qpskConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of QPSK constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__obw_1ga3dcfdfc7cead644c34e39fa95489c931.html language=enus -->
## TOPIC 00283: RFmxNR_OBWFetchMeasurement

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__obw_1ga3dcfdfc7cead644c34e39fa95489c931.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__obw_1ga3dcfdfc7cead644c34e39fa95489c931.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock. Syntaxint32 __stdcall RFmxNR_OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *absolutePower, flo

### RFmxNR_OBWFetchMeasurement

Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock.

#### Syntax

int32 __stdcall RFmxNR_OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *absolutePower, float64 *startFrequency, float64 *stopFrequency)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| occupiedBandwidth | [out] | float64 * | This parameter returns the bandwidth that occupies the specified percentage of the total power of the signal. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation:Occupied bandwidth = Stop frequency - Start frequency |
| absolutePower | [out] | float64 * | This parameter returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |
| startFrequency | [out] | float64 * | This parameter returns the start frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. |
| stopFrequency | [out] | float64 * | This parameter returns the stop frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__obw_1gabe7d1931ba8e973b8d4a73712ace37a7.html language=enus -->
## TOPIC 00284: RFmxNR_OBWFetchSpectrum

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__obw_1gabe7d1931ba8e973b8d4a73712ace37a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__obw_1gabe7d1931ba8e973b8d4a73712ace37a7.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for OBW measurements. Syntaxint32 __stdcall RFmxNR_OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstru

### RFmxNR_OBWFetchSpectrum

Fetches the spectrum used for OBW measurements.

#### Syntax

int32 __stdcall RFmxNR_OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency of the channel. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__pvt.html language=enus -->
## TOPIC 00285: PVT

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__pvt.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_PVTFetchMeasurementFetches PVT ON and OFF powers along with measurement status and burst width. RFmxNR_PVTFetchMeasurementArrayFetches an array of PVT ON and OFF powers along with measurement status and burst width. RFmxNR_PVTFetchSignalPowerTraceFetches

### PVT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_PVTFetchMeasurement | Fetches PVT ON and OFF powers along with measurement status and burst width. |
| RFmxNR_PVTFetchMeasurementArray | Fetches an array of PVT ON and OFF powers along with measurement status and burst width. |
| RFmxNR_PVTFetchSignalPowerTrace | Fetches an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz. |
| RFmxNR_PVTFetchWindowedSignalPowerTrace | Fetches the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__pvt_1ga572ac2a0aa4182db6c7db8236ab3b944.html language=enus -->
## TOPIC 00286: RFmxNR_PVTFetchSignalPowerTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__pvt_1ga572ac2a0aa4182db6c7db8236ab3b944.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__pvt_1ga572ac2a0aa4182db6c7db8236ab3b944.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz. Syntaxint32 __stdcall RFmxNR_PVTFetchSignalPowerTrace(niRFmxInstrHan

### RFmxNR_PVTFetchSignalPowerTrace

Fetches an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz.

#### Syntax

int32 __stdcall RFmxNR_PVTFetchSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 signalPower[], float32 absoluteLimit[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. |
| x0 | [out] | float64 * | This parameter returns start time of the signal. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the time bin spacing. This value is expressed in seconds. |
| signalPower | [out] | float32[] | This parameter returns the instantaneous signal power trace. This value is expressed in dBm. |
| absoluteLimit | [out] | float32[] | This parameter returns the instantaneous signal power trace. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__pvt_1gac8e53d046aeddd9e8878e79e99028025.html language=enus -->
## TOPIC 00287: RFmxNR_PVTFetchMeasurementArray

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__pvt_1gac8e53d046aeddd9e8878e79e99028025.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__pvt_1gac8e53d046aeddd9e8878e79e99028025.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of PVT ON and OFF powers along with measurement status and burst width. Syntaxint32 __stdcall RFmxNR_PVTFetchMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 absoluteOffPowerBefore[], float64 absoluteOffP

### RFmxNR_PVTFetchMeasurementArray

Fetches an array of PVT ON and OFF powers along with measurement status and burst width.

#### Syntax

int32 __stdcall RFmxNR_PVTFetchMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 absoluteOffPowerBefore[], float64 absoluteOffPowerAfter[], float64 absoluteOnPower[], float64 burstWidth[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns the measurement status indicating whether the off power before and after is within the standard defined limit.NameValueDescriptionRFMXNR_VAL_PVT_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXNR_VAL_PVT_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXNR_VAL_PVT_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXNR_VAL_PVT_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| absoluteOffPowerBefore | [out] | float64[] | This parameter returns the OFF power in the segment before the captured burst. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. |
| absoluteOffPowerAfter | [out] | float64[] | This parameter returns the OFF power in the segment after the captured burst. The segment is defined as one slot after the burst and a short transient segment. This value is expressed in dBm. |
| absoluteOnPower | [out] | float64[] | This parameter returns the power of the subframes within the captured burst. This value is expressed in dBm. |
| burstWidth | [out] | float64[] | This parameter returns the width of the captured burst. This value is expressed in seconds. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__sem.html language=enus -->
## TOPIC 00288: SEM

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__sem.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_SEMFetchComponentCarrierMeasurementReturns the absolute and relative powers measured in the component carriers. RFmxNR_SEMFetchComponentCarrierMeasurementArrayReturns an array of the absolute and relative powers measured in the component carriers. RFmxNR_

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_SEMFetchComponentCarrierMeasurement | Returns the absolute and relative powers measured in the component carriers. |
| RFmxNR_SEMFetchComponentCarrierMeasurementArray | Returns an array of the absolute and relative powers measured in the component carriers. |
| RFmxNR_SEMFetchLowerOffsetMargin | Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for lower offset segments. The relative power is relative to the total aggregated power. |
| RFmxNR_SEMFetchLowerOffsetMarginArray | Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for lower offset segments. The relative power is relative to the total aggregated power. |
| RFmxNR_SEMFetchLowerOffsetPower | Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power. |
| RFmxNR_SEMFetchLowerOffsetPowerArray | Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power. |
| RFmxNR_SEMFetchMeasurementStatus | Returns the overall measurement status based on the standard mask type that you configure. |
| RFmxNR_SEMFetchSpectrum | Fetches the spectrum used for SEM measurements. |
| RFmxNR_SEMFetchSubblockMeasurement | Fetches the power, integration bandwidth, and center frequency of the subblock. |
| RFmxNR_SEMFetchTotalAggregatedPower | Returns the sum of powers in all the subblocks. |
| RFmxNR_SEMFetchUpperOffsetMargin | Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power. |
| RFmxNR_SEMFetchUpperOffsetMarginArray | Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for upper offset segments. The relative power is relative to the total aggregated power. |
| RFmxNR_SEMFetchUpperOffsetPower | Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the upper offset segment. The relative power is relative to the total aggregated power. |
| RFmxNR_SEMFetchUpperOffsetPowerArray | Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga18ad3c8facc3003cbe84ce482cab2c75.html language=enus -->
## TOPIC 00289: RFmxNR_SEMFetchUpperOffsetMargin

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga18ad3c8facc3003cbe84ce482cab2c75.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga18ad3c8facc3003cbe84ce482cab2c75.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power. Syntaxint32 __stdcall RFmxNR_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorSt

### RFmxNR_SEMFetchUpperOffsetMargin

Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power.

#### Syntax

int32 __stdcall RFmxNR_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Remarks

Use "offset<n>" or "subblock<n>/offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/offset0""signal::sig1/subblock0/offset0""signal::sig1/result::r1/subblock0/offset0""result::r1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the measurement status indicating whether the power before and after the burst is within the standard defined limit.NameValueDescriptionRFMXNR_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXNR_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXNR_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXNR_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| margin | [out] | float64 * | This parameter returns the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
| marginFrequency | [out] | float64 * | This parameter returns the frequency at which the margin occurs in the upper offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power at which the margin occurs in the upper offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64 * | This parameter returns the power at which the margin occurs in the upper offset segment. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga21f48652a5edd8f98b19ee05a7983be4.html language=enus -->
## TOPIC 00290: RFmxNR_SEMFetchUpperOffsetMarginArray

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga21f48652a5edd8f98b19ee05a7983be4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga21f48652a5edd8f98b19ee05a7983be4.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for upper offset segments. The relative power is relative to the total aggregated power. Syntaxint32 __stdcall RFmxNR_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char se

### RFmxNR_SEMFetchUpperOffsetMarginArray

Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for upper offset segments. The relative power is relative to the total aggregated power.

#### Syntax

int32 __stdcall RFmxNR_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns an array of the measurement status indicating whether the power before and after the burst is within the standard defined limit.NameValueDescriptionRFMXNR_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXNR_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXNR_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXNR_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| margin | [out] | float64[] | This parameter returns an array of the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
| marginFrequency | [out] | float64[] | This parameter returns an array of the frequency at which the margin occurs in the upper offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64[] | This parameter returns an array of the power at which the margin occurs in the upper offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64[] | This parameter returns an array of the power at which the margin occurs in the upper (positive) offset segment. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga32410d799e9c89856afc07b524c8295c.html language=enus -->
## TOPIC 00291: RFmxNR_SEMFetchSpectrum

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga32410d799e9c89856afc07b524c8295c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga32410d799e9c89856afc07b524c8295c.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for SEM measurements. Syntaxint32 __stdcall RFmxNR_SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], float32 compositeMask[], int32 arraySize, int32 *actualArraySize)ParametersNameDirec

### RFmxNR_SEMFetchSpectrum

Fetches the spectrum used for SEM measurements.

#### Syntax

int32 __stdcall RFmxNR_SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], float32 compositeMask[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency of the channel. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
| compositeMask | [out] | float32[] | This parameter returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga344d993e60403c18f61b54aeb76336eb.html language=enus -->
## TOPIC 00292: RFmxNR_SEMFetchMeasurementStatus

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga344d993e60403c18f61b54aeb76336eb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga344d993e60403c18f61b54aeb76336eb.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the overall measurement status based on the standard mask type that you configure. Syntaxint32 __stdcall RFmxNR_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)ParametersNameDirectionTypeDescriptioninstrumentHandl

### RFmxNR_SEMFetchMeasurementStatus

Returns the overall measurement status based on the standard mask type that you configure.

#### Syntax

int32 __stdcall RFmxNR_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the measurement status indicating whether the power before and after the burst is within the standard defined limit.NameValueDescriptionRFMXNR_VAL_SEM_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXNR_VAL_SEM_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXNR_VAL_SEM_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXNR_VAL_SEM_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga469d896f7d58b610d980db37d478182e.html language=enus -->
## TOPIC 00293: RFmxNR_SEMFetchUpperOffsetPowerArray

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga469d896f7d58b610d980db37d478182e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga469d896f7d58b610d980db37d478182e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power. Syntaxint32 __stdcall RFmxNR_SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instru

### RFmxNR_SEMFetchUpperOffsetPowerArray

Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power.

#### Syntax

int32 __stdcall RFmxNR_SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalAbsolutePower | [out] | float64[] | This parameter returns an array of the upper segment power. This value is expressed in dBm. |
| totalRelativePower | [out] | float64[] | This parameter returns an array of the power in the upper offset segment relative to total aggregated power. This value is expressed in dB. |
| peakAbsolutePower | [out] | float64[] | This parameter returns an array of the peak power in the upper offset segment. This value is expressed in dBm. |
| peakFrequency | [out] | float64[] | This parameter returns an array of the frequency at which the peak power occurs in the upper offset segment. This value is expressed in Hz. |
| peakRelativePower | [out] | float64[] | This parameter returns an array of the peak power in the upper offset segment relative to total aggregated power. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga4df73d77f3acaa8ccbf7bc433011fc07.html language=enus -->
## TOPIC 00294: RFmxNR_SEMFetchLowerOffsetMargin

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga4df73d77f3acaa8ccbf7bc433011fc07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga4df73d77f3acaa8ccbf7bc433011fc07.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for lower offset segments. The relative power is relative to the total aggregated power. Syntaxint32 __stdcall RFmxNR_SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorSt

### RFmxNR_SEMFetchLowerOffsetMargin

Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for lower offset segments. The relative power is relative to the total aggregated power.

#### Syntax

int32 __stdcall RFmxNR_SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Remarks

Use "offset<n>" or "subblock<n>/offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/offset0""signal::sig1/subblock0/offset0""signal::sig1/result::r1/subblock0/offset0""result::r1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the measurement status indicating whether the power before and after the burst is within the standard defined limit.NameValueDescriptionRFMXNR_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXNR_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXNR_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXNR_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| margin | [out] | float64 * | This parameter returns the margin from the absolute limit mask for lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
| marginFrequency | [out] | float64 * | This parameter returns the frequency at which the margin occurs in the lower offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power at which the margin occurs in the lower offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64 * | This parameter returns the power at which the margin occurs in the lower offset segment. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga56d735be380e341a7821e223948d2273.html language=enus -->
## TOPIC 00295: RFmxNR_SEMFetchComponentCarrierMeasurementArray

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga56d735be380e341a7821e223948d2273.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga56d735be380e341a7821e223948d2273.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of the absolute and relative powers measured in the component carriers. Syntaxint32 __stdcall RFmxNR_SEMFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 peakAbsolutePower[], float64 pea

### RFmxNR_SEMFetchComponentCarrierMeasurementArray

Returns an array of the absolute and relative powers measured in the component carriers.

#### Syntax

int32 __stdcall RFmxNR_SEMFetchComponentCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 relativePower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absolutePower | [out] | float64[] | This parameter returns an array of the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |
| peakAbsolutePower | [out] | float64[] | This parameter returns an array of the peak power in the component carrier. This value is expressed in dBm. |
| peakFrequency | [out] | float64[] | This parameter returns an array of the frequency at which peak power occurs in the component carrier. This value is expressed in Hz. |
| relativePower | [out] | float64[] | This parameter returns an array of the component carrier power relative to its subblock power. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga5adf3ceb25802e1822f1427b19f80bc4.html language=enus -->
## TOPIC 00296: RFmxNR_SEMFetchLowerOffsetPower

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga5adf3ceb25802e1822f1427b19f80bc4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga5adf3ceb25802e1822f1427b19f80bc4.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power. Syntaxint32 __stdcall RFmxNR_SEMFetchLowerOffsetPower(niRFmxInstrHandle instrum

### RFmxNR_SEMFetchLowerOffsetPower

Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power.

#### Syntax

int32 __stdcall RFmxNR_SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAbsolutePower, float64 *totalRelativePower, float64 *peakAbsolutePower, float64 *peakFrequency, float64 *peakRelativePower)

#### Remarks

Use "offset<n>" or "subblock<n>/offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/offset0""signal::sig1/subblock0/offset0""signal::sig1/result::r1/subblock0/offset0""result::r1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalAbsolutePower | [out] | float64 * | This parameter returns the lower (negative) offset segment power. This value is expressed in dBm. |
| totalRelativePower | [out] | float64 * | This parameter returns the power in the lower offset segment relative to total aggregated power. This value is expressed in dB. |
| peakAbsolutePower | [out] | float64 * | This parameter returns the peak power in the lower offset segment. This value is expressed in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency at which the peak power occurs in the lower offset segment. This value is expressed in Hz. |
| peakRelativePower | [out] | float64 * | This parameter returns the peak power in the lower offset segment relative to total aggregated power. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga5f5e5e05ceeff7d0490ae3c91cfb348e.html language=enus -->
## TOPIC 00297: RFmxNR_SEMFetchUpperOffsetPower

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga5f5e5e05ceeff7d0490ae3c91cfb348e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__sem_1ga5f5e5e05ceeff7d0490ae3c91cfb348e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the upper offset segment. The relative power is relative to the total aggregated power. Syntaxint32 __stdcall RFmxNR_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrum

### RFmxNR_SEMFetchUpperOffsetPower

Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the upper offset segment. The relative power is relative to the total aggregated power.

#### Syntax

int32 __stdcall RFmxNR_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAbsolutePower, float64 *totalRelativePower, float64 *peakAbsolutePower, float64 *peakFrequency, float64 *peakRelativePower)

#### Remarks

Use "offset<n>" or "subblock<n>/offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/offset0""signal::sig1/subblock0/offset0""signal::sig1/result::r1/subblock0/offset0""result::r1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalAbsolutePower | [out] | float64 * | This parameter returns the upper (positive) offset segment power. This value is expressed in dBm. |
| totalRelativePower | [out] | float64 * | This parameter returns the power in the upper offset segment relative to total aggregated power. This value is expressed in dB. |
| peakAbsolutePower | [out] | float64 * | This parameter returns the peak power in the upper offset segment. This value is expressed in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency at which the peak power occurs in the upper offset segment. This value is expressed in Hz. |
| peakRelativePower | [out] | float64 * | This parameter returns the peak power in the upper offset segment relative to total aggregated power. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__fetch__txp_1ga6cb8342e6fdd9902f746950dc8c3d3f5.html language=enus -->
## TOPIC 00298: RFmxNR_TXPFetchPowerTrace

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__fetch__txp_1ga6cb8342e6fdd9902f746950dc8c3d3f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__fetch__txp_1ga6cb8342e6fdd9902f746950dc8c3d3f5.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches power versus time trace. Syntaxint32 __stdcall RFmxNR_TXPFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 power[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrier<k>" or "subblock<n>/carrier<k>" as the s

### RFmxNR_TXPFetchPowerTrace

Fetches power versus time trace.

#### Syntax

int32 __stdcall RFmxNR_TXPFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 power[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| power | [out] | float32[] | This parameter returns the measured average power at each time instance, in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__select__measurement_1gaf6bea61b18da66d4152c649f893a1d11.html language=enus -->
## TOPIC 00299: RFmxNR_SelectMeasurements

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__select__measurement_1gaf6bea61b18da66d4152c649f893a1d11.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__select__measurement_1gaf6bea61b18da66d4152c649f893a1d11.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurement parameter and disables all other measurements. Syntaxint32 __stdcall RFmxNR_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)ParametersNameDirectionTypeDescription

### RFmxNR_SelectMeasurements

Enables all the measurements that you specify in the **Measurement** parameter and disables all other measurements.

#### Syntax

int32 __stdcall RFmxNR_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| measurements | [in] | uInt32 | This parameter specifies the measurements to perform. You can specify one or more of the following measurements. The default value is an empty array.Name (Value)DescriptionModAcc (0)Enables the ModAcc measurement.SEM (1)Enables the SEM measurement.ACP (2)Enables the ACP measurement.CHP (3)Enables the CHP measurement.OBW (4)Enables the OBW measurement.PVT (5)Enables the PVT measurement.TXP (6)Enables the TXP measurement. |
| Name (Value) | Description |  |  |
| ModAcc (0) | Enables the ModAcc measurement. |  |  |
| SEM (1) | Enables the SEM measurement. |  |  |
| ACP (2) | Enables the ACP measurement. |  |  |
| CHP (3) | Enables the CHP measurement. |  |  |
| OBW (4) | Enables the OBW measurement. |  |  |
| PVT (5) | Enables the PVT measurement. |  |  |
| TXP (6) | Enables the TXP measurement. |  |  |
| enableAllTraces | [in] | int32 | This parameter specifies whether to enable all traces for the selected measurement. The default value is FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Select Measurement

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00300: Set and Get Attributes

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes.html
- document_id: `rfmxnr-c-api-ref`
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

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes.html language=enus -->
## TOPIC 00301: Get Attributes

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_GetAttributeF32Queries the value of an RFmx 32-bit floating point number (float32) attribute. RFmxNR_GetAttributeF32ArrayQueries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_GetAttributeF32 | Queries the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxNR_GetAttributeF32Array | Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxNR_GetAttributeF64 | Queries the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxNR_GetAttributeF64Array | Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxNR_GetAttributeI16 | Queries the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxNR_GetAttributeI32 | Queries the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxNR_GetAttributeI32Array | Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxNR_GetAttributeI64 | Queries the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxNR_GetAttributeI64Array | Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxNR_GetAttributeI8 | Queries the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxNR_GetAttributeI8Array | Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxNR_GetAttributeNIComplexDoubleArray | Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxNR_GetAttributeNIComplexSingleArray | Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxNR_GetAttributeString | Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxNR_GetAttributeU16 | Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxNR_GetAttributeU32 | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxNR_GetAttributeU32Array | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxNR_GetAttributeU64Array | Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxNR_GetAttributeU8 | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxNR_GetAttributeU8Array | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga09fd79ec95d946773d48e78e1825fafb.html language=enus -->
## TOPIC 00302: RFmxNR_GetAttributeI64

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga09fd79ec95d946773d48e78e1825fafb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga09fd79ec95d946773d48e78e1825fafb.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxNR_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sess

### RFmxNR_GetAttributeI64

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxNR_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga2a5e688de8f17ae2f0b8000bcb2f0b14.html language=enus -->
## TOPIC 00303: RFmxNR_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga2a5e688de8f17ae2f0b8000bcb2f0b14.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga2a5e688de8f17ae2f0b8000bcb2f0b14.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxNR_GetAttributeNIComplexDoubleArray

Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxNR_GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexDouble[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga46ccc5d3ec314b5d72e0afa1889f31a2.html language=enus -->
## TOPIC 00304: RFmxNR_GetAttributeString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga46ccc5d3ec314b5d72e0afa1889f31a2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga46ccc5d3ec314b5d72e0afa1889f31a2.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the a

### RFmxNR_GetAttributeString

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxNR_GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 arraySize, char attrVal[])

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| attrVal | [out] | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga7a46617aa2c8fc398539da47d4342ddf.html language=enus -->
## TOPIC 00305: RFmxNR_GetAttributeU32Array

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga7a46617aa2c8fc398539da47d4342ddf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga7a46617aa2c8fc398539da47d4342ddf.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxNR_GetAttributeU32Array

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxNR_GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga90c93467d5b7cefc4800acd1da77e42c.html language=enus -->
## TOPIC 00306: RFmxNR_GetAttributeU8Array

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga90c93467d5b7cefc4800acd1da77e42c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga90c93467d5b7cefc4800acd1da77e42c.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arra

### RFmxNR_GetAttributeU8Array

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxNR_GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga92ab07c22c646892b0cda0cde4ffe92e.html language=enus -->
## TOPIC 00307: RFmxNR_GetAttributeI16

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga92ab07c22c646892b0cda0cde4ffe92e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1ga92ab07c22c646892b0cda0cde4ffe92e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxNR_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sess

### RFmxNR_GetAttributeI16

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxNR_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1gacade21ee14019ec66613bee6752ac391.html language=enus -->
## TOPIC 00308: RFmxNR_GetAttributeI8Array

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1gacade21ee14019ec66613bee6752ac391.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1gacade21ee14019ec66613bee6752ac391.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and

### RFmxNR_GetAttributeI8Array

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxNR_GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1gacf78fba78a1c1358ba0ec8b795e2f292.html language=enus -->
## TOPIC 00309: RFmxNR_GetAttributeU32

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1gacf78fba78a1c1358ba0ec8b795e2f292.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1gacf78fba78a1c1358ba0ec8b795e2f292.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxNR_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies th

### RFmxNR_GetAttributeU32

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxNR_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1gaddc379a162642e0ff3d4f7405e4c0385.html language=enus -->
## TOPIC 00310: RFmxNR_GetAttributeI8

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1gaddc379a162642e0ff3d4f7405e4c0385.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__get__attributes_1gaddc379a162642e0ff3d4f7405e4c0385.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxNR_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session.

### RFmxNR_GetAttributeI8

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxNR_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga0dbb38c548a86cee85254077e63fbc95.html language=enus -->
## TOPIC 00311: RFmxNR_SetAttributeI32

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga0dbb38c548a86cee85254077e63fbc95.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga0dbb38c548a86cee85254077e63fbc95.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxNR_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session.

### RFmxNR_SetAttributeI32

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga1946b6a846c32c63313ec31826c081ea.html language=enus -->
## TOPIC 00312: RFmxNR_SetAttributeU16

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga1946b6a846c32c63313ec31826c081ea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga1946b6a846c32c63313ec31826c081ea.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxNR_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RF

### RFmxNR_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga2f699c927d3b76992a5e18c9db8d291f.html language=enus -->
## TOPIC 00313: RFmxNR_SetAttributeU8

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga2f699c927d3b76992a5e18c9db8d291f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga2f699c927d3b76992a5e18c9db8d291f.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxNR_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxNR_SetAttributeU8

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga787388e502ffe6ee20acfe3ad1fd4fe0.html language=enus -->
## TOPIC 00314: RFmxNR_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga787388e502ffe6ee20acfe3ad1fd4fe0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga787388e502ffe6ee20acfe3ad1fd4fe0.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxNR_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorStr

### RFmxNR_SetAttributeNIComplexDoubleArray

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga7bf37f226c7a3624e01de6c2b37a0f20.html language=enus -->
## TOPIC 00315: RFmxNR_SetAttributeI16

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga7bf37f226c7a3624e01de6c2b37a0f20.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga7bf37f226c7a3624e01de6c2b37a0f20.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxNR_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session.

### RFmxNR_SetAttributeI16

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga7cd1fe192aa31958f54a84cfb16fb88b.html language=enus -->
## TOPIC 00316: RFmxNR_SetAttributeNIComplexSingleArray

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga7cd1fe192aa31958f54a84cfb16fb88b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga7cd1fe192aa31958f54a84cfb16fb88b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxNR_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorStr

### RFmxNR_SetAttributeNIComplexSingleArray

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga9212d92f56e446fc0b1b11b2956896dc.html language=enus -->
## TOPIC 00317: RFmxNR_SetAttributeF32Array

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga9212d92f56e446fc0b1b11b2956896dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga9212d92f56e446fc0b1b11b2956896dc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxNR_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char

### RFmxNR_SetAttributeF32Array

Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga94dea5bb88bc61c6a0a4d6cf45e22619.html language=enus -->
## TOPIC 00318: RFmxNR_SetAttributeI64

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga94dea5bb88bc61c6a0a4d6cf45e22619.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga94dea5bb88bc61c6a0a4d6cf45e22619.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxNR_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session.

### RFmxNR_SetAttributeI64

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga97b730048ce27b4291268c497835ce68.html language=enus -->
## TOPIC 00319: RFmxNR_SetAttributeU32

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga97b730048ce27b4291268c497835ce68.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga97b730048ce27b4291268c497835ce68.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxNR_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RF

### RFmxNR_SetAttributeU32

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga9a89ad7f9e7af65f04c51afed15b3da9.html language=enus -->
## TOPIC 00320: RFmxNR_SetAttributeI8Array

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga9a89ad7f9e7af65f04c51afed15b3da9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1ga9a89ad7f9e7af65f04c51afed15b3da9.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxNR_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], i

### RFmxNR_SetAttributeI8Array

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaadded575fdc7984a6a111c496c4308fe.html language=enus -->
## TOPIC 00321: RFmxNR_SetAttributeI8

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaadded575fdc7984a6a111c496c4308fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaadded575fdc7984a6a111c496c4308fe.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxNR_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. You

### RFmxNR_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gab9ef90ae3fc5a7768df8d3d8ed9dfb30.html language=enus -->
## TOPIC 00322: RFmxNR_SetAttributeF32

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gab9ef90ae3fc5a7768df8d3d8ed9dfb30.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gab9ef90ae3fc5a7768df8d3d8ed9dfb30.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxNR_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxNR_SetAttributeF32

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gad4cb5f6bb2e2893b903784ebc41bf0bb.html language=enus -->
## TOPIC 00323: RFmxNR_SetAttributeF64

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gad4cb5f6bb2e2893b903784ebc41bf0bb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gad4cb5f6bb2e2893b903784ebc41bf0bb.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxNR_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxNR_SetAttributeF64

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gae475b7190379e20a382cd30a7322ac8d.html language=enus -->
## TOPIC 00324: RFmxNR_SetAttributeI32Array

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gae475b7190379e20a382cd30a7322ac8d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gae475b7190379e20a382cd30a7322ac8d.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxNR_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[]

### RFmxNR_SetAttributeI32Array

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaeb835f8661bac6ccb8aeab8a96c7c225.html language=enus -->
## TOPIC 00325: RFmxNR_SetAttributeI64Array

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaeb835f8661bac6ccb8aeab8a96c7c225.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaeb835f8661bac6ccb8aeab8a96c7c225.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxNR_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[]

### RFmxNR_SetAttributeI64Array

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaed8ab741494b989351d59d2b1310bc0c.html language=enus -->
## TOPIC 00326: RFmxNR_SetAttributeF64Array

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaed8ab741494b989351d59d2b1310bc0c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaed8ab741494b989351d59d2b1310bc0c.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxNR_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char

### RFmxNR_SetAttributeF64Array

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gafe8f2b155102a1461ff5beec1f1ebbd1.html language=enus -->
## TOPIC 00327: RFmxNR_SetAttributeString

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gafe8f2b155102a1461ff5beec1f1ebbd1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gafe8f2b155102a1461ff5beec1f1ebbd1.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx string attribute. Syntaxint32 __stdcall RFmxNR_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. You can obt

### RFmxNR_SetAttributeString

Sets the value of an RFmx string attribute.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | char[] | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaff0eb27b9473e71661c5c1a468ae4f6e.html language=enus -->
## TOPIC 00328: RFmxNR_SetAttributeU8Array

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaff0eb27b9473e71661c5c1a468ae4f6e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__set__and__get__attributes__set__attributes_1gaff0eb27b9473e71661c5c1a468ae4f6e.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxNR_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorS

### RFmxNR_SetAttributeU8Array

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxNR_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__utility.html language=enus -->
## TOPIC 00329: Utility

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__utility.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxNR_CheckMeasurementStatusChecks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. RFmxNR_CommitCommits settings to the hardwar

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxNR_CheckMeasurementStatus | Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxNR_Commit | Commits settings to the hardware. Calling this function is optional. RFmxNR commits settings to the hardware when you call the RFmxNR_Initiate function. |
| RFmxNR_InitializeFromNIRFSASession | Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. |
| RFmxNR_LoadFromGenerationConfigurationFile | Loads the attributes saved in an RFWS/TDMS file onto the RFmx session. This file can be saved using the NR Modulation Scheme in RFmx Waveform Creator. Make sure to select the 'store configuration' option while saving the TDMS file. |
| RFmxNR_ResetAttribute | Resets an attribute that you specify in the attributeID parameter to default values. |
| RFmxNR_ResetToDefault | Resets a signal to the default values. |
| RFmxNR_WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. |
| RFmxNR_WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__utility_1ga1c37b93c6e45121252305b57e7bf81d8.html language=enus -->
## TOPIC 00330: RFmxNR_Commit

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__utility_1ga1c37b93c6e45121252305b57e7bf81d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__utility_1ga1c37b93c6e45121252305b57e7bf81d8.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this function is optional. RFmxNR commits settings to the hardware when you call the RFmxNR_Initiate function. Syntaxint32 __stdcall RFmxNR_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandl

### RFmxNR_Commit

Commits settings to the hardware. Calling this function is optional. RFmxNR commits settings to the hardware when you call the [RFmxNR_Initiate](group____root__ni_r_fmx_n_r__functions_1ga1feff952d2974304538c63402d9188e6.html) function.

#### Syntax

int32 __stdcall RFmxNR_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__utility_1ga6663f492337a1cecdf2ad4ffe6705c7b.html language=enus -->
## TOPIC 00331: RFmxNR_WaitForMeasurementComplete

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__utility_1ga6663f492337a1cecdf2ad4ffe6705c7b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__utility_1ga6663f492337a1cecdf2ad4ffe6705c7b.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. Syntaxint32 __stdcall RFmxNR_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramete

### RFmxNR_WaitForMeasurementComplete

Waits for the specified number for seconds for all the measurements to complete.

#### Syntax

int32 __stdcall RFmxNR_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__utility_1ga6de3d436bd9e3410c3478ea4531388f1.html language=enus -->
## TOPIC 00332: RFmxNR_CheckMeasurementStatus

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__utility_1ga6de3d436bd9e3410c3478ea4531388f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__utility_1ga6de3d436bd9e3410c3478ea4531388f1.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. Syntaxint32 __stdcall RFmxNR_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[],

### RFmxNR_CheckMeasurementStatus

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

int32 __stdcall RFmxNR_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *isDone)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| isDone | [out] | int32 * | This parameter indicates whether the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__utility_1ga9e953bc2c20c5a8a11f79ea76670d022.html language=enus -->
## TOPIC 00333: RFmxNR_LoadFromGenerationConfigurationFile

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__utility_1ga9e953bc2c20c5a8a11f79ea76670d022.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__utility_1ga9e953bc2c20c5a8a11f79ea76670d022.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the attributes saved in an RFWS/TDMS file onto the RFmx session. This file can be saved using the NR Modulation Scheme in RFmx Waveform Creator. Make sure to select the 'store configuration' option while saving the TDMS file. Syntaxint32 __stdcall RFmxNR_LoadFromGenerationConfigurationFile(niR

### RFmxNR_LoadFromGenerationConfigurationFile

Loads the attributes saved in an RFWS/TDMS file onto the RFmx session. This file can be saved using the NR Modulation Scheme in RFmx Waveform Creator. Make sure to select the 'store configuration' option while saving the TDMS file.

#### Syntax

int32 __stdcall RFmxNR_LoadFromGenerationConfigurationFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char filePath[], int32 configurationIndex)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| filePath | [in] | char[] | This parameter specifies the complete path to the RFWS/TDMS file from which the configurations are to be loaded. |
| configurationIndex | [in] | int32 | This parameter specifies the index of the carrier set to be loaded from the RFWS/TDMS file. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__utility_1gab4f506450d79503c4cb66830185688bc.html language=enus -->
## TOPIC 00334: RFmxNR_ResetToDefault

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__utility_1gab4f506450d79503c4cb66830185688bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__utility_1gab4f506450d79503c4cb66830185688bc.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. Syntaxint32 __stdcall RFmxNR_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obtained f

### RFmxNR_ResetToDefault

Resets a signal to the default values.

#### Syntax

int32 __stdcall RFmxNR_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group____root__ni_r_fmx_n_r__functions__utility_1gae7d58c4663422d278ef10acab1e56eb9.html language=enus -->
## TOPIC 00335: RFmxNR_WaitForAcquisitionComplete

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group____root__ni_r_fmx_n_r__functions__utility_1gae7d58c4663422d278ef10acab1e56eb9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_n_r__functions__utility_1gae7d58c4663422d278ef10acab1e56eb9.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. Syntaxint32 __stdcall RFmxNR_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)RemarksThis function is a wrapper over the RFmx Instrument

### RFmxNR_WaitForAcquisitionComplete

Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function.

#### Syntax

int32 __stdcall RFmxNR_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?context=rfmxinstr_rfmxinstrcref_function_wait_for_acquisition_complete) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxNR_Initialize function. |
| timeout | [in] | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxNR_GetError](group____root__ni_r_fmx_n_r__functions_1ga753476325ccafd23435b4d0152116abe.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxnr-c-api-ref path=group__root__ni_r_fmx_n_r.html language=enus -->
## TOPIC 00336: niRFmxNR.h

- bundle_id: `rfmxnr-c-api-ref`
- source_path: `group__root__ni_r_fmx_n_r.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-c-api-ref/raw/resource/enus/group__root__ni_r_fmx_n_r.html
- document_id: `rfmxnr-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niRFmxNR.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
