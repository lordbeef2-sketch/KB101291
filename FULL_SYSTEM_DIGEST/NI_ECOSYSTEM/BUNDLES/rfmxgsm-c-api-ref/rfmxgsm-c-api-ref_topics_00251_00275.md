# NI DOCUMENT BUNDLE: rfmxgsm-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxgsm-c-api-ref start=251 end=275 -->
<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga1254b330b989ec4ad0a12abe32ab9993.html language=enus -->
## TOPIC 00251: RFmxGSM_SetAttributeI8Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga1254b330b989ec4ad0a12abe32ab9993.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga1254b330b989ec4ad0a12abe32ab9993.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxGSM_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[],

### RFmxGSM_SetAttributeI8Array

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga1c4f87f29d9797142c0b43acad4631b7.html language=enus -->
## TOPIC 00252: RFmxGSM_SetAttributeF32

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga1c4f87f29d9797142c0b43acad4631b7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga1c4f87f29d9797142c0b43acad4631b7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxGSM_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifie

### RFmxGSM_SetAttributeF32

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga29c2a49aa1306472679dfaf1be188740.html language=enus -->
## TOPIC 00253: RFmxGSM_SetAttributeU32Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga29c2a49aa1306472679dfaf1be188740.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga29c2a49aa1306472679dfaf1be188740.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxGSM_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selec

### RFmxGSM_SetAttributeU32Array

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga2ed9b0cc5e1f7189c0ed87d1b1a6ac90.html language=enus -->
## TOPIC 00254: RFmxGSM_SetAttributeI64

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga2ed9b0cc5e1f7189c0ed87d1b1a6ac90.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga2ed9b0cc5e1f7189c0ed87d1b1a6ac90.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxGSM_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session

### RFmxGSM_SetAttributeI64

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga3434a283bb69a5e1fbc0e054362743b6.html language=enus -->
## TOPIC 00255: RFmxGSM_SetAttributeF64Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga3434a283bb69a5e1fbc0e054362743b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga3434a283bb69a5e1fbc0e054362743b6.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxGSM_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char

### RFmxGSM_SetAttributeF64Array

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga393cbc65284f46f26887f3c3f7caac0e.html language=enus -->
## TOPIC 00256: RFmxGSM_SetAttributeString

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga393cbc65284f46f26887f3c3f7caac0e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga393cbc65284f46f26887f3c3f7caac0e.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx string attribute. Syntaxint32 __stdcall RFmxGSM_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. You can ob

### RFmxGSM_SetAttributeString

Sets the value of an RFmx string attribute.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | char[] | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga51d76af1f39466546ef12c584365fadc.html language=enus -->
## TOPIC 00257: RFmxGSM_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga51d76af1f39466546ef12c584365fadc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga51d76af1f39466546ef12c584365fadc.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxGSM_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorSt

### RFmxGSM_SetAttributeNIComplexDoubleArray

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga5216c5d0292bf3af1827da7d5cac76b0.html language=enus -->
## TOPIC 00258: RFmxGSM_SetAttributeI32Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga5216c5d0292bf3af1827da7d5cac76b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga5216c5d0292bf3af1827da7d5cac76b0.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxGSM_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[

### RFmxGSM_SetAttributeI32Array

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga607305f6efc939bdb94e4b83c2180114.html language=enus -->
## TOPIC 00259: RFmxGSM_SetAttributeI32

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga607305f6efc939bdb94e4b83c2180114.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga607305f6efc939bdb94e4b83c2180114.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxGSM_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session

### RFmxGSM_SetAttributeI32

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga6ffeb3580f746b1fdac0278dfdbdd4f0.html language=enus -->
## TOPIC 00260: RFmxGSM_SetAttributeU8

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga6ffeb3580f746b1fdac0278dfdbdd4f0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga6ffeb3580f746b1fdac0278dfdbdd4f0.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxGSM_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxGSM_SetAttributeU8

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga7ec851b6ca31ce364c0955842da64ae5.html language=enus -->
## TOPIC 00261: RFmxGSM_SetAttributeU8Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga7ec851b6ca31ce364c0955842da64ae5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga7ec851b6ca31ce364c0955842da64ae5.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxGSM_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selector

### RFmxGSM_SetAttributeU8Array

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga83150f1807768bae759cdf7bec5294e0.html language=enus -->
## TOPIC 00262: RFmxGSM_SetAttributeU16

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga83150f1807768bae759cdf7bec5294e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga83150f1807768bae759cdf7bec5294e0.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxGSM_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the R

### RFmxGSM_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga956e3ff38713eda5b431a27102796c9a.html language=enus -->
## TOPIC 00263: RFmxGSM_SetAttributeI64Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga956e3ff38713eda5b431a27102796c9a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga956e3ff38713eda5b431a27102796c9a.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxGSM_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[

### RFmxGSM_SetAttributeI64Array

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1gace70df1d65286f651d9f416962522e17.html language=enus -->
## TOPIC 00264: RFmxGSM_SetAttributeNIComplexSingleArray

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1gace70df1d65286f651d9f416962522e17.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1gace70df1d65286f651d9f416962522e17.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxGSM_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorSt

### RFmxGSM_SetAttributeNIComplexSingleArray

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1gaebaa510f2c127b6275d1aab00cb9f0ee.html language=enus -->
## TOPIC 00265: RFmxGSM_SetAttributeF64

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1gaebaa510f2c127b6275d1aab00cb9f0ee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1gaebaa510f2c127b6275d1aab00cb9f0ee.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxGSM_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifie

### RFmxGSM_SetAttributeF64

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1gafdd7d004e7159484c746d84e97208c0a.html language=enus -->
## TOPIC 00266: RFmxGSM_SetAttributeU32

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1gafdd7d004e7159484c746d84e97208c0a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1gafdd7d004e7159484c746d84e97208c0a.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxGSM_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the R

### RFmxGSM_SetAttributeU32

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__utility.html language=enus -->
## TOPIC 00267: Utility

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__utility.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_CheckMeasurementStatusChecks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. RFmxGSM_CommitCommits settings to the hardw

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_CheckMeasurementStatus | Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxGSM_Commit | Commits settings to the hardware. Calling this function is optional. RFmxGSM commits settings to the hardware when you call the RFmxGSM_Initiate function. |
| RFmxGSM_InitializeFromNIRFSASession | Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. |
| RFmxGSM_ResetAttribute | Resets an attribute that you specify in the attributeID parameter to default values. |
| RFmxGSM_ResetToDefault | Resets a signal to the default values. |
| RFmxGSM_WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. |
| RFmxGSM_WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__utility_1ga0c93189813b56023f0bfbb7da5133608.html language=enus -->
## TOPIC 00268: RFmxGSM_WaitForAcquisitionComplete

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__utility_1ga0c93189813b56023f0bfbb7da5133608.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__utility_1ga0c93189813b56023f0bfbb7da5133608.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. Syntaxint32 __stdcall RFmxGSM_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)RemarksThis function is a wrapper over the RFmx Instrumen

### RFmxGSM_WaitForAcquisitionComplete

Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function.

#### Syntax

int32 __stdcall RFmxGSM_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?context=rfmxinstr_rfmxinstrcref_function_wait_for_acquisition_complete) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| timeout | [in] | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__utility_1ga0ee9d904e11a323a3b12056ed7254bbc.html language=enus -->
## TOPIC 00269: RFmxGSM_InitializeFromNIRFSASession

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__utility_1ga0ee9d904e11a323a3b12056ed7254bbc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__utility_1ga0ee9d904e11a323a3b12056ed7254bbc.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device

### RFmxGSM_InitializeFromNIRFSASession

Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxGSM_InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle *handleOut)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_InitializeFromNIRFSASession](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| nirfsaSession | [in] | uInt32 | Specifies the NIRFSA session handle of the device to initialize. |
| handleOut | [out] | niRFmxInstrHandle * | Returns an RFmx instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__utility_1ga4f1bf50bcbb458e02cd7ca13142af838.html language=enus -->
## TOPIC 00270: RFmxGSM_ResetAttribute

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__utility_1ga4f1bf50bcbb458e02cd7ca13142af838.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__utility_1ga4f1bf50bcbb458e02cd7ca13142af838.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets an attribute that you specify in the attributeID parameter to default values. Syntaxint32 __stdcall RFmxGSM_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFm

### RFmxGSM_ResetAttribute

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Syntax

int32 __stdcall RFmxGSM_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being reset. Refer to the Selector String (C or LabWindows/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__utility_1gabfb36f46527de57744bd6afb786ab791.html language=enus -->
## TOPIC 00271: RFmxGSM_Commit

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__utility_1gabfb36f46527de57744bd6afb786ab791.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__utility_1gabfb36f46527de57744bd6afb786ab791.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this function is optional. RFmxGSM commits settings to the hardware when you call the RFmxGSM_Initiate function. Syntaxint32 __stdcall RFmxGSM_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHa

### RFmxGSM_Commit

Commits settings to the hardware. Calling this function is optional. RFmxGSM commits settings to the hardware when you call the [RFmxGSM_Initiate](group____root__ni_r_fmx_g_s_m__functions_1ga238434c5965e22ce849f557252113cbe.html) function.

#### Syntax

int32 __stdcall RFmxGSM_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__utility_1gacbc41fa3fccc5ac797a954b8a8f18034.html language=enus -->
## TOPIC 00272: RFmxGSM_WaitForMeasurementComplete

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__utility_1gacbc41fa3fccc5ac797a954b8a8f18034.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__utility_1gacbc41fa3fccc5ac797a954b8a8f18034.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. Syntaxint32 __stdcall RFmxGSM_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramet

### RFmxGSM_WaitForMeasurementComplete

Waits for the specified number for seconds for all the measurements to complete.

#### Syntax

int32 __stdcall RFmxGSM_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__utility_1gacec6c52c15959eb2f9d02479f22dbe00.html language=enus -->
## TOPIC 00273: RFmxGSM_CheckMeasurementStatus

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__utility_1gacec6c52c15959eb2f9d02479f22dbe00.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__utility_1gacec6c52c15959eb2f9d02479f22dbe00.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. Syntaxint32 __stdcall RFmxGSM_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[],

### RFmxGSM_CheckMeasurementStatus

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

int32 __stdcall RFmxGSM_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *done)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| done | [out] | int32 * | This parameter indicates whether the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__utility_1gaf3faa9d3024cccafb70a1e38d437c37b.html language=enus -->
## TOPIC 00274: RFmxGSM_ResetToDefault

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__utility_1gaf3faa9d3024cccafb70a1e38d437c37b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__utility_1gaf3faa9d3024cccafb70a1e38d437c37b.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. Syntaxint32 __stdcall RFmxGSM_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obtained

### RFmxGSM_ResetToDefault

Resets a signal to the default values.

#### Syntax

int32 __stdcall RFmxGSM_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group__root__ni_r_fmx_g_s_m.html language=enus -->
## TOPIC 00275: niRFmxGSM.h

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group__root__ni_r_fmx_g_s_m.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group__root__ni_r_fmx_g_s_m.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niRFmxGSM.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
