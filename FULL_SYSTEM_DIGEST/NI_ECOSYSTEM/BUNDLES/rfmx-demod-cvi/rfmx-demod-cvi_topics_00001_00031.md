# NI DOCUMENT BUNDLE: rfmx-demod-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-demod-cvi start=1 end=31 -->
<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_deletesignalconfiguration.html language=enus -->
## TOPIC 00001: RFmxDemod_DeleteSignalConfiguration

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_deletesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_deletesignalconfiguration.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_DeleteSignalConfiguration

int32 __stdcall RFmxDemod_DeleteSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char signalName[]);

#### Purpose

Deletes an instance of the signal that you specify in the **signalName** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| signalName | char[] | Specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_getallnamedresultnames.html language=enus -->
## TOPIC 00002: RFmxDemod_GetAllNamedResultNames

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_getallnamedresultnames.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_getallnamedresultnames.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetAllNamedResultNames

int32 __stdcall RFmxDemod_GetAllNamedResultNames(
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
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| resultNamesBufferSize | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| Output |  |  |
| Name | Type | Description |
| resultNames | char[] | Returns the comma delimited result names. |
| actualResultNamesSize | int32* | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | int32* | Indicates whether the default result exists. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_getattributef32.html language=enus -->
## TOPIC 00003: RFmxDemod_GetAttributeF32

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_getattributef32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_getattributef32.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetAttributeF32

int32 __stdcall RFmxDemod_GetAttributeF32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_getattributei64.html language=enus -->
## TOPIC 00004: RFmxDemod_GetAttributeI64

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_getattributei64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_getattributei64.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetAttributeI64

int32 __stdcall RFmxDemod_GetAttributeI64 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 *attrVal);

#### Purpose

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int64* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_getattributei8.html language=enus -->
## TOPIC 00005: RFmxDemod_GetAttributeI8

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_getattributei8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_getattributei8.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetAttributeI8

int32 __stdcall RFmxDemod_GetAttributeI8 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_getattributei8array.html language=enus -->
## TOPIC 00006: RFmxDemod_GetAttributeI8Array

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_getattributei8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_getattributei8array.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetAttributeI8Array

int32 __stdcall RFmxDemod_GetAttributeI8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int8[] | Returns the current value of the attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_getattributenicomplexdoublearray.html language=enus -->
## TOPIC 00007: RFmxDemod_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_getattributenicomplexdoublearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_getattributenicomplexdoublearray.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetAttributeNIComplexDoubleArray

int32 __stdcall RFmxDemod_GetAttributeNIComplexDoubleArray (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | NIComplexDouble[] | Returns the current value of the attribute. |
| arraySize | int32 | Specifies the size of the array. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_getattributenicomplexsinglearray.html language=enus -->
## TOPIC 00008: RFmxDemod_GetAttributeNIComplexSingleArray

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_getattributenicomplexsinglearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_getattributenicomplexsinglearray.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetAttributeNIComplexSingleArray

int32 __stdcall RFmxDemod_GetAttributeNIComplexSingleArray (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | NIComplexSingle[] | Returns the current value of the attribute. |
| arraySize | int32 | Specifies the size of the array. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_getattributestring.html language=enus -->
## TOPIC 00009: RFmxDemod_GetAttributeString

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_getattributestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_getattributestring.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetAttributeString

int32 __stdcall RFmxDemod_GetAttributeString (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[]);

#### Purpose

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter.If you pass 0, you can pass NULL for the attrVal parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter.If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_getattributeu16.html language=enus -->
## TOPIC 00010: RFmxDemod_GetAttributeU16

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_getattributeu16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_getattributeu16.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetAttributeU16

int32 __stdcall RFmxDemod_GetAttributeU16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt16 *attrVal);

#### Purpose

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt16* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_getattributeu32array.html language=enus -->
## TOPIC 00011: RFmxDemod_GetAttributeU32Array

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_getattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_getattributeu32array.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetAttributeU32Array

int32 __stdcall RFmxDemod_GetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used. Example: "" "signal::sig1" You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt32[] | Returns the current value of the attribute. |
| arraySize | int32 | Specifies the size of the array. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_geterror.html language=enus -->
## TOPIC 00012: RFmxDemod_GetError

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_geterror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_geterror.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetError

int32 __stdcall RFmxDemod_GetError (niRFmxInstrHandle instrumentHandle,
 int32* errorCode,
 int32 errorDescriptionBufferSize,
 char errorDescription[]);

#### Purpose

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

errorDescriptionBufferSize

123456

4

123

7

errorDescriptionBufferSize

NULL

errorDescription

|  | Note Use the RFmxDemod_GetErrorString function if the RFmxDemod_GetError function does not return an error message. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. If a valid session handle is passed, the last error stored in that session is retrieved. You can pass NULL, to retrieve the last error stored in the current execution thread. |
| errorDescriptionBufferSize | int32 | Passes the number of bytes in the char array you specify in errorDescription. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize – 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| Output |  |  |
| Name | Type | Description |
| errorCode | int32* | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescription | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string. The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_geterrorstring.html language=enus -->
## TOPIC 00013: RFmxDemod_GetErrorString

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_geterrorstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_geterrorstring.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_GetErrorString

int32 __stdcall RFmxDemod_GetErrorString (niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[]);

#### Purpose

Converts a status code returned by an RFmxDemod function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

errorDescriptionBufferSize

errorDescriptionBufferSize

NULL

errorDescription

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| errorCode | int32 | Passes the statusOrRequiredSize parameter that is returned from any RFmxDemod function. |
| errorDescriptionBufferSize | int32 | Passes the number of bytes in the char array you specify in errorDescription. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize – 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| Output |  |  |
| Name | Type | Description |
| errorDescription | char[] | Returns the user-readable message string that corresponds to the status code you specify. If you pass 0 for errorDescriptionBufferSize, you can pass NULL for the errorDescription buffer parameter to get the size of error description message. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=cvirfmxdemod_initialize.html language=enus -->
## TOPIC 00014: RFmxDemod_Initialize

- bundle_id: `rfmx-demod-cvi`
- source_path: `cvirfmxdemod_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/cvirfmxdemod_initialize.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFmxDemod_Initialize

int32 __stdcall RFmxDemod_Initialize (char resourceName[], 
char optionString[],
niRFmxInstrHandle *handleOut, int32 *isNewSession);

#### Purpose

Creates an RFmx session to the NI-RFSA supported device you specify through the **resourceName** parameter and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

The RFmxDemod_Initialize function calls the [RFxInstr_Initialize](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_initialize.html) function.

[IMAGE alt='image' src='note.gif'] Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| resourceName | char[] | Specifies the resource name of the device to initialize. The following table shows examples of how to specify the resource name. Example # Device Type Syntax 1 myRFmxDevice RFmx device, device name is "myRFmxDevice" 2 myLogicalName IVI logical name or virtual instrument, name is "myLogicalName" For NI-DAQmx devices, the syntax is the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot2. You can rename an NI-DAQmx device by right-clicking the name in MAX, selecting Rename from the pull-down menu, and entering a new name. You can also pass the name of an IVI logical name configured with the IVI Configuration utility. For additional information about IVI, refer to the IVI section of the Measurement & Automation Explorer Help. |
| Example # | Device Type | Syntax |
| 1 | myRFmxDevice | RFmx device, device name is "myRFmxDevice" |
| 2 | myLogicalName | IVI logical name or virtual instrument, name is "myLogicalName" |
| optionString | char[] | Sets the initial value of certain attributes for the session. The following attributes are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about attributes used in this parameter, refer to NI RF Vector Signal Analyzers Help. The format of this string is "AttributeName=Value", where AttributeName is the name of the attribute and Value is the value to which the attribute is set. For example, you can simulate an NI 5663E using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple attributes, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx uses yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. Note To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the NI 5665. To use an external NI Source Measure Units (SMU) as the noise source power supply for the Noise Figure (NF) measurement, use "NoiseSourcePowerSupply" as the specifier within the RFmxSetup string. For example, "RFmxSetup= NoiseSourcePowerSupply:myDCPower[0]" configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You should allocate a dedicated SMU channel for RFmx. Note RFmx supports NI PXIe-4138 and NI PXIe-4139 SMUs. |
|  | Note To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the NI 5665. |  |
|  | Note RFmx supports NI PXIe-4138 and NI PXIe-4139 SMUs. |  |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Passes a reference of the instrument session to the next function. |
| isNewSession | int32* | Returns RFMXDEMOD_VAL_TRUE if the function created a new session or RFMXDEMOD_VAL_FALSE if the function returned a reference to an existing session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxDemod_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_fsk_mean_deviation.html language=enus -->
## TOPIC 00015: RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_DEVIATION

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_fsk_mean_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_fsk_mean_deviation.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns the reference FSK deviation used to measure the FSK error. This value is expressed in Hz. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsFSKMeanDeviation |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_iq_impairments_mean_iq_origin_offset.html language=enus -->
## TOPIC 00016: RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_IQ_ORIGIN_OFFSET

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_iq_impairments_mean_iq_origin_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_iq_impairments_mean_iq_origin_offset.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_IQ_ORIGIN_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns the offset from the ideal location of the constellation origin. This value is expressed in dB. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsIQImpairmentsMeanIQOriginOffset |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_iq_impairments_mean_quadrature_skew.html language=enus -->
## TOPIC 00017: RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_QUADRATURE_SKEW

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_iq_impairments_mean_quadrature_skew.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_iq_impairments_mean_quadrature_skew.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_QUADRATURE_SKEW

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns a measure of the I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsIQImpairmentsMeanQuadratureSkew |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_mean_amplitude_droop.html language=enus -->
## TOPIC 00018: RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_AMPLITUDE_DROOP

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_mean_amplitude_droop.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_mean_amplitude_droop.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_AMPLITUDE_DROOP

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns the mean amplitude droop per symbol. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsMeanAmplitudeDroop |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_mean_rho_factor.html language=enus -->
## TOPIC 00019: RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_RHO_FACTOR

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_mean_rho_factor.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_mean_rho_factor.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_RHO_FACTOR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns the correlation of the measurement waveform and the reference waveform. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsMeanRhoFactor |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_offset_evm_maximum_peak.html language=enus -->
## TOPIC 00020: RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_PEAK

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_offset_evm_maximum_peak.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_offset_evm_maximum_peak.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_PEAK

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns the maximum of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsOffsetEVMMaximumPeak |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_offset_evm_maximum_rms.html language=enus -->
## TOPIC 00021: RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_RMS

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_offset_evm_maximum_rms.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_offset_evm_maximum_rms.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_RMS

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns the maximum of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsOffsetEVMMaximumRMS |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_offset_evm_mean_peak.html language=enus -->
## TOPIC 00022: RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MEAN_PEAK

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_offset_evm_mean_peak.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_offset_evm_mean_peak.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MEAN_PEAK

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns the mean of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsOffsetEVMMeanPeak |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_offset_evm_mean_rms.html language=enus -->
## TOPIC 00023: RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MEAN_RMS

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_offset_evm_mean_rms.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_offset_evm_mean_rms.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MEAN_RMS

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns the mean of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsOffsetEVMMeanRMS |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_phase_error_maximum.html language=enus -->
## TOPIC 00024: RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MAXIMUM

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_phase_error_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_phase_error_maximum.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns the maximum of the phase error measured per acquisition. This value is expressed in degrees. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsPhaseErrorMaximum |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_phase_error_mean.html language=enus -->
## TOPIC 00025: RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MEAN

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_phase_error_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_phase_error_mean.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeF64 |
| Description: | Returns the mean of the phase error measured per acquisition. This value is expressed in degrees. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsPhaseErrorMean |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_results_sync_found.html language=enus -->
## TOPIC 00026: RFMXDEMOD_ATTR_DDEMOD_RESULTS_SYNC_FOUND

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_results_sync_found.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_results_sync_found.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_RESULTS_SYNC_FOUND

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxDemod_GetAttributeI32 |
| Description: | Indicates whether the synchronization sequence was found in the demodulated signal. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_DDemodGetResultsSyncFound |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_samples_per_symbol.html language=enus -->
## TOPIC 00027: RFMXDEMOD_ATTR_DDEMOD_SAMPLES_PER_SYMBOL

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_samples_per_symbol.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_samples_per_symbol.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_SAMPLES_PER_SYMBOL

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxDemod_SetAttributeI32RFmxDemod_GetAttributeI32 |
| Description: | Specifies the samples per symbol used to acquire the signal for the measurement. Sample rate = Symbol rate * Samples per symbol. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_AUTO. Get Function: RFmxDemod_DDemodGetSamplesPerSymbol Set function: RFmxDemod_DDemodSetSamplesPerSymbol |
| Values: | RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_AUTO (-1)The measurement uses appropriate samples per symbol (SPS) based on modulation type and pulse shaping filter. SPS=8 for FSK. SPS=4 for ASK, PSK, QAM, and MSK when pulse shape filter is not rectangular. SPS=8 for ASK, PSK, QAM, and MSK when pulse shape filter is rectangular. RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_4 (4)The SPS value is 4. RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_8 (8)The SPS value is 8. RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_16 (16)The SPS value is 16. |
| RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_AUTO (-1) | The measurement uses appropriate samples per symbol (SPS) based on modulation type and pulse shaping filter. SPS=8 for FSK. SPS=4 for ASK, PSK, QAM, and MSK when pulse shape filter is not rectangular. SPS=8 for ASK, PSK, QAM, and MSK when pulse shape filter is rectangular. |
| RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_4 (4) | The SPS value is 4. |
| RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_8 (8) | The SPS value is 8. |
| RFMXDEMOD_VAL_DDEMOD_SAMPLES_PER_SYMBOL_16 (16) | The SPS value is 16. |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_ddemod_signal_structure.html language=enus -->
## TOPIC 00028: RFMXDEMOD_ATTR_DDEMOD_SIGNAL_STRUCTURE

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_ddemod_signal_structure.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_ddemod_signal_structure.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_DDEMOD_SIGNAL_STRUCTURE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxDemod_SetAttributeI32RFmxDemod_GetAttributeI32 |
| Description: | Specifies whether the signal is either a bursty signal or a continuous signal. The default value is RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_CONTINUOUS. Get Function: RFmxDEMOD_GetSignalStructure Set Function: RFmxDEMOD_SetSignalStructure |
| Values: | RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_BURSTED (0)The signal is a bursty signal. RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_CONTINUOUS (1)The signal is a continuous signal. |
| RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_BURSTED (0) | The signal is a bursty signal. |
| RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_CONTINUOUS (1) | The signal is a continuous signal. |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_iq_power_edge_trigger_source.html language=enus -->
## TOPIC 00029: RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_iq_power_edge_trigger_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_iq_power_edge_trigger_source.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxDemod_SetAttributeStringRFmxDemod_GetAttributeString |
| Description: | Specifies the channel from which the device monitors the trigger. This attribute is applicable only when you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to RFMXDEMOD_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_GetIQPowerEdgeTriggerSource Set function: RFmxDemod_SetIQPowerEdgeTriggerSource |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_limited_configuration_change.html language=enus -->
## TOPIC 00030: RFMXDEMOD_ATTR_LIMITED_CONFIGURATION_CHANGE

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_limited_configuration_change.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_limited_configuration_change.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_LIMITED_CONFIGURATION_CHANGE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxDemod_SetAttributeI32RFmxDemod_GetAttributeI32 |
| Description: | Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at multiple frequencies and/or power levels repeatedly, enabling this attribute can help achieve faster measurements. When you set this attribute to a value other than RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this attribute, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. You can also use this attribute to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr attributes from a locked configuration. NI recommends you use this attribute in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this attribute to a value other than RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this attribute if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality attributes while testing each device under test. RFmx automatically optimizes that use case. Specify the named signal configuration you are setting this attribute in the selector string input. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED. Get Function: RFmxDemod_GetLimitedConfigurationChange Set function: RFmxDemod_SetLimitedConfigurationChange |
| Values: | RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED (0)This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE (1)Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY (2)Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the RFMXDEMOD_ATTR_CENTER_FREQUENCY and RFMXDEMOD_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL (3)Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXDEMOD_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXDEMOD_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL (4)Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only RFMXDEMOD_ATTR_CENTER_FREQUENCY, RFMXDEMOD_ATTR_REFERENCE_LEVEL, and RFMXDEMOD_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXDEMOD_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL (5)Signal configuration, other than center frequency, reference level, and external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only RFMXLTE_ATTR_CENTER_FREQUENCY, RFMXLTE_ATTR_REFERENCE_LEVEL, and RFMXLTE_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Trigger Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED (0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. |
| RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE (1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY (2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the RFMXDEMOD_ATTR_CENTER_FREQUENCY and RFMXDEMOD_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL (3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXDEMOD_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXDEMOD_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL (4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only RFMXDEMOD_ATTR_CENTER_FREQUENCY, RFMXDEMOD_ATTR_REFERENCE_LEVEL, and RFMXDEMOD_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXDEMOD_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXDEMOD_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL (5) | Signal configuration, other than center frequency, reference level, and external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only RFMXLTE_ATTR_CENTER_FREQUENCY, RFMXLTE_ATTR_REFERENCE_LEVEL, and RFMXLTE_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Trigger Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |

<!--NI_TOPIC bundle=rfmx-demod-cvi path=rfmxdemod_attr_trigger_delay.html language=enus -->
## TOPIC 00031: RFMXDEMOD_ATTR_TRIGGER_DELAY

- bundle_id: `rfmx-demod-cvi`
- source_path: `rfmxdemod_attr_trigger_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-cvi/raw/resource/enus/rfmxdemod_attr_trigger_delay.html
- document_id: `rfmx-demod-cvi`
- page_type: `leaf`
- content_type: ``

RFMXDEMOD_ATTR_TRIGGER_DELAY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxDemod_SetAttributeF64RFmxDemod_GetAttributeF64 |
| Description: | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. Pass the selectorString as Empty to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. Get Function: RFmxDemod_GetTriggerDelay Set function: RFmxDemod_SetTriggerDelay |
