# NI DOCUMENT BUNDLE: rfmx-instr

<!--NI_BUNDLE_CHUNK bundle=rfmx-instr start=1 end=88 -->
<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstr/bp_help_file_title.html language=enus -->
## TOPIC 00001: RFmx Instruments Help

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstr/bp_help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstr/bp_help_file_title.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmx Instruments Help

October 2022

This help file contains introduction to RFmx Instruments programming reference information.

© 2014–2022 National Instruments Corporation. All rights reserved.

Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/bp_help_file_title.html language=enus -->
## TOPIC 00002: RFmx Instruments C Reference

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/bp_help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/bp_help_file_title.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmx Instruments C Reference

This help file contains information about the RFmxInstr functions, attributes, and values that you can use when programming your application.

© 2014–2022 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_buildcalibrationplanestring.html language=enus -->
## TOPIC 00003: RFmxInstr_BuildCalibrationPlaneString

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_buildcalibrationplanestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_buildcalibrationplanestring.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_BuildCalibrationPlaneString

int32 __stdcall RFmxInstr_BuildCalibrationPlaneString (char calibrationPlaneName[],
 int32 selectorStringLength,
 char selectorString[]);

#### Purpose

Creates the selector string to use with External Attenuation Table functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| calibrationPlaneName | char[] | Specifies the calibration plane name for building the selector string. This input accepts the calibration plane name with or without the "calplane::" prefix. example:"""calplane::plane0""plane0" |
| selectorStringLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_buildinstrumentstring.html language=enus -->
## TOPIC 00004: RFmxInstr_BuildInstrumentString

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_buildinstrumentstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_buildinstrumentstring.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_BuildInstrumentString

int32 __stdcall RFmxInstr_BuildInstrumentString (char selectorString[],
 int32 LOIndex,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the instrument string to use as the Selector String for reading the recommended settings.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies the selector string. example:"" |
| instrumentNumber | int32 | Specifies the instrument number for which you want the recommended settings to be read. |
| selectorStringOutLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. You can pass NULL for this parameter if selectorStringLength is set to 0, which will return the minimum buffer size required to create the signal string. If the selectorString buffer is not large enough to build the signal string, the function returns an error. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_buildportstring2.html language=enus -->
## TOPIC 00005: RFmxInstr_BuildPortString2

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_buildportstring2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_buildportstring2.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_BuildPortString2

int32 __stdcall RFmxInstr_BuildPortString2 (char selectorString[],
 char portName[],
 char deviceName[],
 int32 channelNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the port string to use as the selector string with External Attenuation Table functions. On a MIMO session, this function can be used to build port string to use as a selector string for configuring or reading port-specific properties and external attenuation table functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies the calibration plane string when used for building port string for the external attenuation table functions. If you do not specify the calibration plane string, the default calibration plane instance is used.example:"""calplane::plane0"You can use the RFmxInstr_BuildCalibrationPlaneString to build the selector string. |
| portName | char[] | Specifies the port for building the selector string. |
| deviceName | char[] | Specifies the device name for building the selector string. |
| channelNumber | int32 | Specifies the channel number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. You can pass NULL for this parameter if selectorStringLength is set to 0, which will return the minimum buffer size required to create the signal string. If the selectorString buffer is not large enough to build the signal string, the function returns an error. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_cfgexternalattenuationinterpolationlinear.html language=enus -->
## TOPIC 00006: RFmxInstr_CfgExternalAttenuationInterpolationLinear

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_cfgexternalattenuationinterpolationlinear.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_cfgexternalattenuationinterpolationlinear.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CfgExternalAttenuationInterpolationLinear

int32 __stdcall RFmxInstr_CfgExternalAttenuationInterpolationLinear(
 niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char tableName[],
 int32 format
 );

#### Purpose

Selects the linear interpolation method when interpolating S-parameters for the specified table.
If the carrier frequency does not match a row in the S-parameter table, this function performs a linear interpolation based on the entries above and below the rows in the table.

Currently interpolation is supported only for S-parameter tables.

Supported Devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the calibration plane name in which either S-parameter table or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. If you do not specify the calibration plane name, the default calibration plane instance is used. Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |  |
| tableName | char[] | Specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. Example: "" "table1" |
| format | int32 | Specifies the format of parameters to interpolate. RFMXINSTR_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY (0) Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. RFMXINSTR_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE (1) Results in a linear interpolation. RFMXINSTR_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE (2) Results in a linear interpolation. |
| RFMXINSTR_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY (0) | Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. |  |
| RFMXINSTR_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE (1) | Results in a linear interpolation. |  |
| RFMXINSTR_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE (2) | Results in a linear interpolation. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_cfgexternalattenuationinterpolationnearest.html language=enus -->
## TOPIC 00007: RFmxInstr_CfgExternalAttenuationInterpolationNearest

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_cfgexternalattenuationinterpolationnearest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_cfgexternalattenuationinterpolationnearest.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CfgExternalAttenuationInterpolationNearest

int32 __stdcall RFmxInstr_CfgExternalAttenuationInterpolationNearest (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char tableName[]);

#### Purpose

Selects the nearest interpolation method when interpolating S-parameters for a specified table. The parameters of the table nearest to the carrier frequency are used.

|  | Note Currently interpolation is supported only for S-parameter tables. |
| --- | --- |

Supported devices

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |  |
| tableName | char[] | Specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. example:"""table1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_cfgexternalattenuationinterpolationspline.html language=enus -->
## TOPIC 00008: RFmxInstr_CfgExternalAttenuationInterpolationSpline

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_cfgexternalattenuationinterpolationspline.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_cfgexternalattenuationinterpolationspline.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_CfgExternalAttenuationInterpolationSpline

int32 __stdcall RFmxInstr_CfgExternalAttenuationInterpolationSpline (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char tableName[]);

#### Purpose

Selects the spline interpolation method when interpolating parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this function performs a spline interpolation based on the entries above and below the row in the table.

|  | Note Currently interpolation is supported only for S-parameter tables. |
| --- | --- |

Supported devices

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |  |
| tableName | char[] | Specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. example:"""table1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_close.html language=enus -->
## TOPIC 00009: RFmxInstr_Close

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_close.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_close.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_Close

int32 __stdcall RFmxInstr_Close (niRFmxInstrHandle instrumentHandle, int32 forceDestroy);

#### Purpose

Closes the RFmx session.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| forceDestroy | int32 | Indicates whether to forcefully destroy the RFmx session. RFMXInstr_VAL_FALSE (0) Destroys the RFmx session only if you call the RFmxInstr_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. RFMXInstr_VAL_TRUE (1) Forcefully destroys the RFmx session. You do not have to call the RFmxInstr_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |
| RFMXInstr_VAL_FALSE (0) | Destroys the RFmx session only if you call the RFmxInstr_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. |  |
| RFMXInstr_VAL_TRUE (1) | Forcefully destroys the RFmx session. You do not have to call the RFmxInstr_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_disablecalibrationplane.html language=enus -->
## TOPIC 00010: RFmxInstr_DisableCalibrationPlane

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_disablecalibrationplane.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_disablecalibrationplane.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_DisableCalibrationPlane

int32 __stdcall RFmxInstr_DisableCalibrationPlane (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Disables the calibration plane specified by the **selectorString** parameter for amplitude correction. 
**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. If you specify "calplane::all", all the calibration planes are disabled.example:"""calplane::plane0""calplane::all" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_getattributei32.html language=enus -->
## TOPIC 00011: RFmxInstr_GetAttributeI32

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_getattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_getattributei32.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_GetAttributeI32

int32 __stdcall RFmxInstr_GetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_getattributei8array.html language=enus -->
## TOPIC 00012: RFmxInstr_GetAttributeI8Array

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_getattributei8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_getattributei8array.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_GetAttributeI8Array

int32 __stdcall RFmxInstr_GetAttributeI8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/cvirfmxinstr_getattributeu32array.html language=enus -->
## TOPIC 00013: RFmxInstr_GetAttributeU32Array

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/cvirfmxinstr_getattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/cvirfmxinstr_getattributeu32array.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstr_GetAttributeU32Array

int32 __stdcall RFmxInstr_GetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Identifies the instrument session. This parameter is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxInstr_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_fft_width.html language=enus -->
## TOPIC 00014: RFMXINSTR_ATTR_FFT_WIDTH

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_fft_width.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_fft_width.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_FFT_WIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition. The lower limit for all devices that support setting the RFMXINSTR_ATTR_FFT_WIDTH attribute is 7.325 kHz. PXIe-5663/5663E: The FFT width upper limit for the PXIe-5663/5663E depends on the RF frequency and on the module revision of the PXIe-5601. For more information about determining which revision of the PXIe-5601 RF downconverter you have installed, refer to the Identifying Module Revision topic in the NI RF Vector Signal Analyzers Help. The maximum FFT width for your device is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. You can use the RFMXINSTR_ATTR_FFT_WIDTH attribute with in-band retuning. For more information about in-band retuning, refer to the Downconverter Center Frequency attribute. RFmx treats the device instantaneous bandwidth as the effective real-time bandwidth of the signal path. The span specifies the frequency range of the computed spectrum. A signal analyzer can acquire a bandwidth only within the device instantaneous bandwidth. If the span you choose is greater than the device instantaneous bandwidth, RFmx obtains multiple acquisitions and combines them into a single spectrum. By specifying the FFT width, you can control the specific bandwidth obtained in each signal acquisition. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. Supported devices: PXIe-5663/5663E/5665, PXIe-5668 Get Function: RFmxInstr_GetFFTWidth Set Function: RFmxInstr_SetFFTWidth |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_frequency_settling.html language=enus -->
## TOPIC 00015: RFMXINSTR_ATTR_FREQUENCY_SETTLING

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_frequency_settling.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_frequency_settling.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_FREQUENCY_SETTLING

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the value used for LO frequency settling. Specify the units and interpretation for this scalar value using the Frequency Settling Units attribute. Valid valuesYou do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax.Frequency Settling Units Attribute Value PXIe-5663/5663E PXIe-5665/5668 PXIe-5644/5645/5646 PXIe-5830/5831/5832/5840/5841/5842, PXIe-5831 with PXIe-5653 (using PXIe-3622 LO), PXIe-5832 with PXIe-5653 (using PXIe-3623 LO) PXIe-5831 with PXIe-5653 (using PXIe-5653 LO) and PXIe-5832 with PXIe-5653 (using PXIe-5653 LO) Seconds After Lock 2 Âµs to 80 ms, resolution of approximately 2 Âµs 4 Âµs to 80 ms, resolution of approximately 4 Âµs 1 Âµs to 65 ms, resolution of 1 Âµs 1 Âµs to 10s, resolution of 1 Âµs 4 Âµs to 80 ms, resolution of approximately 4 Âµs Seconds After I/O 0 Âµs to 80 ms, resolution of 1 Âµs 0 Âµs to 80 ms, resolution of 1 Âµs 1 Âµs to 65 ms, resolution of 1 Âµs 0 Âµs to 10s, resolution of 1 Âµs 0 Âµs to 80 ms, resolution of 1 Âµs PPM 1.0, 0.1, 0.01 1.0, 0.1, 0.01, 0.001 1.0, 0.1, 0.01 1.0 to 0.01 1.0 to 0.01 Note This attribute is not supported if you are using an external LO. The default value is 0.1. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetFrequencySettling Set Function: RFmxInstr_SetFrequencySettling |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_lo_export_enabled.html language=enus -->
## TOPIC 00016: RFMXINSTR_ATTR_LO_EXPORT_ENABLED

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_lo_export_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_lo_export_enabled.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_EXPORT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether to enable the LO OUT terminals on the installed devices. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use 'lo1' or 'lo2' as part of the selector string. You do not need to use a selector string or use 'lo1, lo2' as part of the selector string if you want to configure this attribute for both channels. You can also use RFmxInstr_BuildLOString utility function to create the LO String. For all other devices, lo channel string is not allowed.This attribute is not supported on a MIMO session.You do not need to use a selector string, if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the Selector string topic for information about the string syntax.TRUE Enables the LO OUT terminals. FALSE Disables the LO OUT terminals Default value:PXIe-5663/5663E: TRUE PXIe-5644/5645/5646, PXIe-5665/5668, PXIe-5830/5831/5832/5840/5841/5842: FALSE Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetLOExportEnabled Set Function: RFmxInstr_SetLOExportEnabled |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_lo_frequency.html language=enus -->
## TOPIC 00017: RFMXINSTR_ATTR_LO_FREQUENCY

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_lo_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_lo_frequency.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the LO signal frequency for the configured center frequency. This value is expressed in Hz. If you are using the vector signal analyzer with an external LO, use this attribute to specify the LO frequency that the external LO source passes into the LO IN or LO1 IN connector on the RF downconverter front panel. If you are using an external LO, reading the value of this attribute after configuring the rest of the parameters returns the LO frequency needed by the device. You can set this attribute to the actual LO frequency because RFmx corrects for any difference between expected and actual LO frequencies. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use 'lo1' or 'lo2' as part of the selector string. You do not need to use a selector string or use 'lo1, lo2' as part of the selector string if you want to configure this attribute for both channels. You can also use RFmxInstr_BuildLOString utility function to create the LO String. For all other devices, lo channel string is not allowed.This attribute is not supported on a MIMO session. You do not need to use a selector string, if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is 0. Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetLOFrequency Set Function: RFmxInstr_SetLOFrequency |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_lo_frequency_step_size.html language=enus -->
## TOPIC 00018: RFMXINSTR_ATTR_LO_FREQUENCY_STEP_SIZE

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_lo_frequency_step_size.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_lo_frequency_step_size.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_FREQUENCY_STEP_SIZE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the step size for tuning the LO phase-locked loop (PLL). You can only tune the LO frequency in multiples of the LO Frequency Step Size attribute. Therefore, the LO frequency can be offset from the requested center frequency by as much as half of the LO Frequency Step Size attribute. This offset is corrected by digitally frequency shifting the LO frequency to the value requested in Downconverter Center Frequency attribute. For PXIe-5831 with PXIe-5653, PXIe-5832 with PXIe-5653, this attribute is ignored if PXIe-5653 is used as the LO source. The valid values for this attribute depend on the RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE attribute. PXIe-5644/5645/5646: If you set the RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE attribute to RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_DISABLED, the specified value is coerced to the nearest valid value. PXIe-5840: If you set the RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE attribute to RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_DISABLED, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size. This attribute is not supported on a MIMO session.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED Attribute Setting LO Frequency Step Size Attribute Valid Values on PXIe-5644/5645 LO Frequency Step Size Attribute Valid Values on PXIe-5646 LO Frequency Step Size Attribute Valid Values on PXIe-5840/5841 LO Frequency Step Size Attribute Valid Values on PXIe-5830/5831/5832 LO Frequency Step Size Property Valid Values on PXIe-5841 with PXIe-5655, PXIe-5842* LO1 LO2 Enabled 50 kHz to 24 MHz 50 kHz to 25 MHz 50 kHz to 100 MHz 8 Hz to 400 MHz 4 kHz to 400 MHz 1 nHz to 50 MHz Disabled 4 MHz, 5 MHz, 6 MHz, 12 MHz, 24 MHz 2 MHz, 5 MHz, 10 MHz, 25 MHz 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, 100 MHz -- -- Default valuesPXIe-5644/5645/5646200 kHzPXIe-58302 MHz PXIe-5831/5832 (RF port)8 MHz PXIe-5831/5832 (IF port)2 MHz, 4 MHzPXIe-5840/5841500 kHzPXIe-58421 HzThe default value for PXIe-5831/5832 depends on the frequency range of the selected port for your instrument configuration. Use RFmxInstr Get Available Ports function to get the valid port names. Supported devices: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetLOFrequencyStepSize Set Function: RFmxInstr_SetLOFrequencyStepSize |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_lo_source.html language=enus -->
## TOPIC 00019: RFMXINSTR_ATTR_LO_SOURCE

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_lo_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_lo_source.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_LO_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the local oscillator (LO) signal source used to downconvert the RF input signal. If this attribute is set to '' (empty string), RFmx uses the internal LO source. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use 'lo1' or 'lo2' as part of the selector string. You do not need to use a selector string or use 'lo1, lo2' as part of the selector string if you want to configure this attribute for both channels. You can also use RFmxInstr_BuildLOString utility function to create the LO String. For all other devices, lo channel string is not allowed.If no signal downconversion is required, this attribute is ignored.This attribute is not supported on a MIMO session.You do not need to use a selector string, if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the Selector string topic for information about the string syntax. The default value is RFMXINSTR_VAL_LO_SOURCE_ONBOARD. Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetLOSource Set Function: RFmxInstr_SetLOSource |
| Values: | RFMXINSTR_VAL_LO_SOURCE_NONE (None)Specifies that no LO source is required to downconvert the RF input signal. RFMXINSTR_VAL_LO_SOURCE_ONBOARD (Onboard)Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal. RFMXINSTR_VAL_LO_SOURCE_LO_IN (LO_In)Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel. RFMXINSTR_VAL_LO_SOURCE_SECONDARY (Secondary)Specifies that the LO source uses the PXIe-5830/5831/5832/5840 internal LO. This value is valid on only the PXIe-5840 with PXIe-5653, PXIe-5831 with PXIe-5653 (LO1 stage only), or PXIe-5832 with PXIe-5653 (LO1 stage only). RFMXINSTR_VAL_LO_SOURCE_SG_SA_SHARED (SG_SA_Shared)Specifies that the internal LO can be shared between RFmx and RFSG sessions. RFmx selects an internal synthesizer and the synthesizer signal is switched to both the RX and TX mixers. This value is valid only on PXIe-5830/5831/5832/5841/5842. RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED (Automatic_SG_SA_Shared)Specifies whether RFmx automatically configures the signal analyzer to use the LO utilized by the signal generator on the same vector signal transceiver (VST) based on the configured measurements. When using instruments that do not have LOs with excellent phase noise and to minimize the contribution of the instrument's phase noise affecting your measurements, NI recommends to share the LO between the signal generator (SG) and the signal analyzer (SA). This value is recommended in test setups that use a VST with NI-RFSG to generate a signal at the DUT's input and RFmx to measure the signal at the DUT's output. This value automatically: determines whether the SG LO can be shared with SA based on the test instrument used, selected measurement, and the measurement settings.configures instrument specific attributes on SA to share the LO between the generator and analyzer, whenever possible. To enable automatically sharing SG LO with SA, you must first setup the required device specific physical connections mentioned below and then follow the steps in the recommended order. PXIe-5840/5841/5842: SG LO is shared with SA via an external path. Hence, you must connect RF Out LO Out to RF In LO In using a cable. PXIe-5830/5831/5832: SG LO is shared with SA via an internal path. Hence, an external cable connection is not required. NI recommends the following order of steps: 1. Set LO Source attribute to Automatic SG SA Shared in NI-RFSG (or enable Automatic SG SA shared LO on NI-RFSG Playback Library) 2. Set RFMXINSTR_ATTR_LO_SOURCE attribute to RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED in RFmx 3. Configure any additional settings on RFSG and RFmx, including selecting waveforms 4. Initiate RFSG 5. Initiate RFmx. Note: When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED attribute to RFMXINSTR_VAL_FALSE and RFMXINSTR_ATTR_LO_SOURCE attribute to RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED. Refer to following functions for examples in RFmx WLAN and RFmx NR that show the behavior of Automatic SG SA Shared LO. (LabVIEW directory)\\examples\\RFmx\\WLAN\\RFmxWLAN FEM Test with Automatic SG SA Shared LO.vi(LabVIEW directory)\\examples\\RFmx\\NR\\RFmxNR FEM Test with Automatic SG SA Shared LO.vi This value is valid only on PXIe-5830/5831/5832/5840/5841/5842. |
| RFMXINSTR_VAL_LO_SOURCE_NONE (None) | Specifies that no LO source is required to downconvert the RF input signal. |
| RFMXINSTR_VAL_LO_SOURCE_ONBOARD (Onboard) | Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal. |
| RFMXINSTR_VAL_LO_SOURCE_LO_IN (LO_In) | Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel. |
| RFMXINSTR_VAL_LO_SOURCE_SECONDARY (Secondary) | Specifies that the LO source uses the PXIe-5830/5831/5832/5840 internal LO. This value is valid on only the PXIe-5840 with PXIe-5653, PXIe-5831 with PXIe-5653 (LO1 stage only), or PXIe-5832 with PXIe-5653 (LO1 stage only). |
| RFMXINSTR_VAL_LO_SOURCE_SG_SA_SHARED (SG_SA_Shared) | Specifies that the internal LO can be shared between RFmx and RFSG sessions. RFmx selects an internal synthesizer and the synthesizer signal is switched to both the RX and TX mixers. This value is valid only on PXIe-5830/5831/5832/5841/5842. |
| RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED (Automatic_SG_SA_Shared) | Specifies whether RFmx automatically configures the signal analyzer to use the LO utilized by the signal generator on the same vector signal transceiver (VST) based on the configured measurements. When using instruments that do not have LOs with excellent phase noise and to minimize the contribution of the instrument's phase noise affecting your measurements, NI recommends to share the LO between the signal generator (SG) and the signal analyzer (SA). This value is recommended in test setups that use a VST with NI-RFSG to generate a signal at the DUT's input and RFmx to measure the signal at the DUT's output. This value automatically: determines whether the SG LO can be shared with SA based on the test instrument used, selected measurement, and the measurement settings.configures instrument specific attributes on SA to share the LO between the generator and analyzer, whenever possible. To enable automatically sharing SG LO with SA, you must first setup the required device specific physical connections mentioned below and then follow the steps in the recommended order. PXIe-5840/5841/5842: SG LO is shared with SA via an external path. Hence, you must connect RF Out LO Out to RF In LO In using a cable. PXIe-5830/5831/5832: SG LO is shared with SA via an internal path. Hence, an external cable connection is not required. NI recommends the following order of steps: 1. Set LO Source attribute to Automatic SG SA Shared in NI-RFSG (or enable Automatic SG SA shared LO on NI-RFSG Playback Library) 2. Set RFMXINSTR_ATTR_LO_SOURCE attribute to RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED in RFmx 3. Configure any additional settings on RFSG and RFmx, including selecting waveforms 4. Initiate RFSG 5. Initiate RFmx. Note: When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED attribute to RFMXINSTR_VAL_FALSE and RFMXINSTR_ATTR_LO_SOURCE attribute to RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED. Refer to following functions for examples in RFmx WLAN and RFmx NR that show the behavior of Automatic SG SA Shared LO. (LabVIEW directory)\\examples\\RFmx\\WLAN\\RFmxWLAN FEM Test with Automatic SG SA Shared LO.vi(LabVIEW directory)\\examples\\RFmx\\NR\\RFmxNR FEM Test with Automatic SG SA Shared LO.vi This value is valid only on PXIe-5830/5831/5832/5840/5841/5842. |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_mechanical_attenuation_auto.html language=enus -->
## TOPIC 00020: RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_AUTO

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_mechanical_attenuation_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_mechanical_attenuation_auto.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies whether RFmx chooses an attenuation setting based on the hardware settings. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE. Supported devices: PXIe-5663/5663E/5665/5668 Get Function: RFmxInstr_GetMechanicalAttenuationAuto Set Function: RFmxInstr_SetMechanicalAttenuationAuto |
| Values: | RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0)Specifies that RFmx uses the value configured in the Mechanical Attenuation Value attribute. RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1)Specifies that the measurement computes the mechanical attenuation. |
| RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) | Specifies that RFmx uses the value configured in the Mechanical Attenuation Value attribute. |
| RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) | Specifies that the measurement computes the mechanical attenuation. |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_mixer_level_offset.html language=enus -->
## TOPIC 00021: RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_mixer_level_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_mixer_level_offset.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the number of dB by which to adjust the device mixer level. Specifying a positive value for this attribute configures the device for moderate distortion and low noise, and specifying a negative value results in low distortion and higher noise. You cannot set the RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET and RFMXINSTR_ATTR_MIXER_LEVEL attributes at the same time.You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is 0. The default value specifies device settings that are the best compromise between distortion and noise. Supported devices: PXIe-5663/5663E/5665/5668 Get Function: RFmxInstr_GetMixerLevelOffset Set Function: RFmxInstr_SetMixerLevelOffset |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_number_of_lo_sharing_groups.html language=enus -->
## TOPIC 00022: RFMXINSTR_ATTR_NUMBER_OF_LO_SHARING_GROUPS

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_number_of_lo_sharing_groups.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_number_of_lo_sharing_groups.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_NUMBER_OF_LO_SHARING_GROUPS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeI32RFmxInstr_GetAttributeI32 |
| Description: | Specifies the RFmx session with the number of LO sharing groups. The default value is 1. The valid values are 1 and 2. Get Function: RFmxInstr_GetNumberOfLOSharingGroups Set Function: RFmxInstr_SetNumberOfLOSharingGroups |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_ready_for_advance_event_terminal_name.html language=enus -->
## TOPIC 00023: RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_ready_for_advance_event_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_ready_for_advance_event_terminal_name.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeString |
| Description: | Returns the fully qualified signal name as a string. The standard format is as follows:PXIe-5820/5840/5841/5842: /ModuleName/ai/0/ReadyForAdvanceEvent, where ModuleName is the name of your device in MAX.PXIe-5830/5831/5832: /BasebandModule/ai/0/ReadyForAdvanceEvent, where BasebandModule is the name of your device in MAX.All other devices: /DigitizerName/ReadyForAdvanceEvent, where DigitizerName is the name of your associated digitizer module in MAX.This attribute is not supported on a MIMO session. Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetReadyForAdvanceEventTerminalName |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_ready_for_reference_event_output_terminal.html language=enus -->
## TOPIC 00024: RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINAL

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_ready_for_reference_event_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_ready_for_reference_event_output_terminal.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINAL

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the destination terminal for the Ready for Reference event. This attribute is not supported on a MIMO session. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is Do not export signal. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetReadyForReferenceEventOutputTerminal Set Function: RFmxInstr_SetReadyForReferenceEventOutputTerminal |
| Values: | RFMXINSTR_VAL_DO_NOT_EXPORT_STR () Does not export the signal. RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. RFMXINSTR_VAL_REF_OUT_STR (RefOut) Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. RFMXINSTR_VAL_PFI0_STR (PFI0) Exports the signal to the PFI 0 connector. RFMXINSTR_VAL_PFI1_STR (PFI1) Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) Exports the signal to the PXI trigger line 0. RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) Exports the signal to the PXI trigger line 1. RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) Exports the signal to the PXI trigger line 2. RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) Exports the signal to the PXI trigger line 3. RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) Exports the signal to the PXI trigger line 4. RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) Exports the signal to the PXI trigger line 5. RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) Exports the signal to the PXI trigger line 6. RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) Exports the signal to the PXI trigger line 7. RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RFMXINSTR_VAL_DO_NOT_EXPORT_STR () | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR (PFI0) | Exports the signal to the PFI 0 connector. |
| RFMXINSTR_VAL_PFI1_STR (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_recommended_center_frequency.html language=enus -->
## TOPIC 00025: RFMXINSTR_ATTR_RECOMMENDED_CENTER_FREQUENCY

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_recommended_center_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_recommended_center_frequency.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_CENTER_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the recommended center frequency of the RF signal. This value is expressed in Hz. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedCenterFrequency |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_recommended_iq_acquisition_time.html language=enus -->
## TOPIC 00026: RFMXINSTR_ATTR_RECOMMENDED_IQ_ACQUISITION_TIME

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_recommended_iq_acquisition_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_recommended_iq_acquisition_time.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_IQ_ACQUISITION_TIME

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the recommended acquisition time for I/Q acquisition. This value is expressed in seconds. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedIQAcquisitionTime |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_recommended_spectral_fft_window.html language=enus -->
## TOPIC 00027: RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_FFT_WINDOW

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_recommended_spectral_fft_window.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_recommended_spectral_fft_window.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_FFT_WINDOW

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeI32 |
| Description: | Returns the recommended FFT window type for spectral acquisition. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedSpectralFFTWindow |
| Values: | RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_NONE (0)Indicates that the measurement does not use FFT windowing to reduce spectral leakage. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_FLAT_TOP (1)Indicates a Flat Top FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_HANNING (2)Indicates a Hanning FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_HAMMING (3)Indicates a Hamming FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_GAUSSIAN (4)Indicates a Gaussian FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_BLACKMAN (5)Indicates a Blackman FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_BLACKMAN_HARRIS (6)Indicates a Blackman-Harris FFT window type. RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_KAISER_BESSEL (7)Indicates a Kaiser-Bessel FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_NONE (0) | Indicates that the measurement does not use FFT windowing to reduce spectral leakage. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_FLAT_TOP (1) | Indicates a Flat Top FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_HANNING (2) | Indicates a Hanning FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_HAMMING (3) | Indicates a Hamming FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_GAUSSIAN (4) | Indicates a Gaussian FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_BLACKMAN (5) | Indicates a Blackman FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_BLACKMAN_HARRIS (6) | Indicates a Blackman-Harris FFT window type. |
| RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_KAISER_BESSEL (7) | Indicates a Kaiser-Bessel FFT window type. |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_recommended_spectral_resolution_bandwidth.html language=enus -->
## TOPIC 00028: RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_RESOLUTION_BANDWIDTH

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_recommended_spectral_resolution_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_recommended_spectral_resolution_bandwidth.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_RESOLUTION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the recommended FFT bin width for spectral acquisition. This value is expressed in Hz. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedSpectralResolutionBandwidth |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_recommended_trigger_minimum_quiet_time.html language=enus -->
## TOPIC 00029: RFMXINSTR_ATTR_RECOMMENDED_TRIGGER_MINIMUM_QUIET_TIME

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_recommended_trigger_minimum_quiet_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_recommended_trigger_minimum_quiet_time.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RECOMMENDED_TRIGGER_MINIMUM_QUIET_TIME

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeF64 |
| Description: | Returns the recommended minimum quiet time during which the signal level must be below the trigger value for triggering to occur. This value is expressed in seconds. This attribute is supported when 1. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1'. 2. RFmxInstr Initialize function is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this attribute. Get Function: RFmxInstr_GetRecommendedTriggerMinimumQuietTime |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_rf_attenuation_step_size.html language=enus -->
## TOPIC 00030: RFMXINSTR_ATTR_RF_ATTENUATION_STEP_SIZE

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_rf_attenuation_step_size.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_rf_attenuation_step_size.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_RF_ATTENUATION_STEP_SIZE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the step size for the RF attenuation level. This value is expressed in dB. The actual RF attenuation is coerced up to the next highest multiple of the specified step size. If the mechanical attenuators are not available to implement the coerced RF attenuation, the solid state attenuators are used. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. Default values: PXIe-5601/5663/5663E0.0PXIe-5603/5665 (3.6 GHz)1.0PXIe-5605/5665 (14 GHz), PXIe-5606/56685.0 Valid values: PXIe-5601/5663/5663E0.0 to 93.0, continuousPXIe-5603/5665 (3.6 GHz)1.0 to 74.0, in 1 dB stepsPXIe-5605/5665 (14 GHz) (low band), PXIe-5606/5668 (low band)1.0 to 106.0, in 1 dB stepsPXIe-5605/5665 (14 GHz) (high band), PXIe-5606/5668 (high band)5.0 to 75.0, in 5 dB steps Supported devices: PXIe-5663, PXIe-5665, PXIe-5668 Get Function: RFmxInstr_GetRFAttenuationStepSize Set Function: RFmxInstr_SetRFAttenuationStepSize |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_self_calibration_validity_check_time_interval.html language=enus -->
## TOPIC 00031: RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK_TIME_INTERVAL

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_self_calibration_validity_check_time_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_self_calibration_validity_check_time_interval.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK_TIME_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the minimum time between two self calibration validity checks. This value is expressed in seconds. When you call RFmx Commit or Initiate functions by enabling the RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK attribute, RFmx checks if the amount of time specified by the Self Calibration Validity Check Time Interval attribute has elapsed before validating the calibration data. The default value is 30 seconds. Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5833/5840/5841/5842 Get Function: RFmxInstr_GetSelfCalibrationValidityCheckTimeInterval Set Function: RFmxInstr_SetSelfCalibrationValidityCheckTimeInterval |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_start_trigger_export_output_terminal.html language=enus -->
## TOPIC 00032: RFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINAL

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_start_trigger_export_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_start_trigger_export_output_terminal.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINAL

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeStringRFmxInstr_GetAttributeString |
| Description: | Specifies the destination terminal for the exported start trigger. You can also choose not to export any signal. This attribute is not supported on a MIMO session. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. The default value is Do not export signal. Supported devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetStartTriggerExportOutputTerminal Set Function: RFmxInstr_SetStartTriggerExportOutputTerminal |
| Values: | RFMXINSTR_VAL_DO_NOT_EXPORT_STR () Does not export the signal. RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. RFMXINSTR_VAL_REF_OUT_STR (RefOut) Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. RFMXINSTR_VAL_PFI0_STR (PFI0) Exports the signal to the PFI 0 connector. RFMXINSTR_VAL_PFI1_STR (PFI1) Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) Exports the signal to the PXI trigger line 0. RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) Exports the signal to the PXI trigger line 1. RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) Exports the signal to the PXI trigger line 2. RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) Exports the signal to the PXI trigger line 3. RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) Exports the signal to the PXI trigger line 4. RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) Exports the signal to the PXI trigger line 5. RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) Exports the signal to the PXI trigger line 6. RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) Exports the signal to the PXI trigger line 7. RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RFMXINSTR_VAL_DO_NOT_EXPORT_STR () | Does not export the signal. |
| RFMXINSTR_VAL_CLK_OUT_STR (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RFMXINSTR_VAL_REF_OUT_STR (RefOut) | Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RFMXINSTR_VAL_REF_OUT2_STR (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| RFMXINSTR_VAL_PFI0_STR (PFI0) | Exports the signal to the PFI 0 connector. |
| RFMXINSTR_VAL_PFI1_STR (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| RFMXINSTR_VAL_PXI_TRIG0_STR (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| RFMXINSTR_VAL_PXI_TRIG1_STR (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| RFMXINSTR_VAL_PXI_TRIG2_STR (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| RFMXINSTR_VAL_PXI_TRIG3_STR (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| RFMXINSTR_VAL_PXI_TRIG4_STR (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| RFMXINSTR_VAL_PXI_TRIG5_STR (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| RFMXINSTR_VAL_PXI_TRIG6_STR (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| RFMXINSTR_VAL_PXI_TRIG7_STR (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| RFMXINSTR_VAL_PXI_STAR_STR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| RFMXINSTR_VAL_PXIE_DSTARC_STR (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_start_trigger_terminal_name.html language=enus -->
## TOPIC 00033: RFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAME

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_start_trigger_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_start_trigger_terminal_name.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAME

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxInstr_GetAttributeString |
| Description: | Returns the fully qualified signal name as a string. The standard format is as follows:PXIe-5820/5840/5841/5842: /ModuleName/ai/0/StartTrigger, where ModuleName is the name of your device in MAX.PXIe-5830/5831/5832: /BasebandModule/ai/0/StartTrigger, where BasebandModule is the name of your device in MAX.All other devices: /DigitizerName/StartTrigger, where DigitizerName is the name of your associated digitizer module in MAX.This attribute is not supported on a MIMO session. Supported devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetStartTriggerTerminalName |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrcvi/rfmxinstr_attr_thermal_correction_temperature_resolution.html language=enus -->
## TOPIC 00034: RFMXINSTR_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrcvi/rfmxinstr_attr_thermal_correction_temperature_resolution.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrcvi/rfmxinstr_attr_thermal_correction_temperature_resolution.html
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFMXINSTR_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxInstr_SetAttributeF64RFmxInstr_GetAttributeF64 |
| Description: | Specifies the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius. You do not need to use a selector string if you want to configure this attribute for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for information about the string syntax. Default valuePXIe-5830/5831/5832/58420.2PXIe-5840/58411.0 Supported devices: PXIe-5830/5831/5832/5840/5841/5842 Get Function: RFmxInstr_GetThermalCorrectionTemperatureResolution Set Function: RFmxInstr_SetThermalCorrectionTemperatureResolution |

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/14297c07-ca45-14f6-4a89-2ce3cc326f54.htm language=enus -->
## TOPIC 00035: rfmxinstrdotnet/html/14297c07-ca45-14f6-4a89-2ce3cc326f54.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/14297c07-ca45-14f6-4a89-2ce3cc326f54.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/14297c07-ca45-14f6-4a89-2ce3cc326f54.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetInstrumentModel Method

RFmxInstrMXGetInstrumentModel Method

Gets a string that contains the model number or name of the RF device that you are currently using.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetInstrumentModel(
	string channelName,
	out string value
)
```

```text
Public Function GetInstrumentModel ( 
	channelName As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value**
  - Type: SystemStringUpon return, contains a string that contains the model number or name of the RF device that you are currently using.

###### Return Value

Int32

##### Remarks

InstrumentModel

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/143662e0-5ce3-26e9-3535-81f2689ecff8.htm language=enus -->
## TOPIC 00036: rfmxinstrdotnet/html/143662e0-5ce3-26e9-3535-81f2689ecff8.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/143662e0-5ce3-26e9-3535-81f2689ecff8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/143662e0-5ce3-26e9-3535-81f2689ecff8.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXRecommendedSpectralFftWindow Enumeration

RFmxInstrMXRecommendedSpectralFftWindow Enumeration

RFmxInstrMX(String, String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXRecommendedSpectralFftWindow
```

```text
Public Enumeration RFmxInstrMXRecommendedSpectralFftWindow
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | Indicates that the measurement does not use FFT windowing to reduce spectral leakage. |
|  | FlatTop | 1 | Indicates a Flat Top FFT window type. |
|  | Hanning | 2 | Indicates a Hanning FFT window type. |
|  | Hamming | 3 | Indicates a Hamming FFT window type. |
|  | Gaussian | 4 | Indicates a Gaussian FFT window type. |
|  | Blackman | 5 | Indicates a Blackman FFT window type. |
|  | BlackmanHarris | 6 | Indicates a Blackman-Harris FFT window type. |
|  | KaiserBessel | 7 | Indicates a Kaiser-Bessel FFT window type. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/154bb041-1076-4519-b500-e2a53516bd32.htm language=enus -->
## TOPIC 00037: rfmxinstrdotnet/html/154bb041-1076-4519-b500-e2a53516bd32.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/154bb041-1076-4519-b500-e2a53516bd32.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/154bb041-1076-4519-b500-e2a53516bd32.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetStartTriggerExportOutputTerminal Method

RFmxInstrMXSetStartTriggerExportOutputTerminal Method

Sets the destination terminal for the exported start trigger.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetStartTriggerExportOutputTerminal(
	string selectorString,
	string value
)
```

```text
Public Function SetStartTriggerExportOutputTerminal ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemStringSpecifies the destination terminal for the exported start trigger.

###### Return Value

Int32

##### Remarks

StartTriggerExportOutputTerminal

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/15b1309b-7220-506f-f31d-3fe6e9be5600.htm language=enus -->
## TOPIC 00038: rfmxinstrdotnet/html/15b1309b-7220-506f-f31d-3fe6e9be5600.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/15b1309b-7220-506f-f31d-3fe6e9be5600.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/15b1309b-7220-506f-f31d-3fe6e9be5600.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeShort Method

RFmxInstrMXSetAttributeShort Method

Sets the value of a Short attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeShort(
	string channelName,
	int attributeIdentifier,
	short value
)
```

```text
Public Function SetAttributeShort ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As Short
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringSpecifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemInt16Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/16678260-a08e-795c-fa33-963702464f37.htm language=enus -->
## TOPIC 00039: rfmxinstrdotnet/html/16678260-a08e-795c-fa33-963702464f37.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/16678260-a08e-795c-fa33-963702464f37.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/16678260-a08e-795c-fa33-963702464f37.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetCommonModeLevel Method

RFmxInstrMXGetCommonModeLevel Method

Gets the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetCommonModeLevel(
	string channelName,
	out double value
)
```

```text
Public Function GetCommonModeLevel ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts.

###### Return Value

Int32

##### Remarks

CommonModeLevel

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/17f63704-96ff-8f4b-ccee-a3436bb68faf.htm language=enus -->
## TOPIC 00040: rfmxinstrdotnet/html/17f63704-96ff-8f4b-ccee-a3436bb68faf.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/17f63704-96ff-8f4b-ccee-a3436bb68faf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/17f63704-96ff-8f4b-ccee-a3436bb68faf.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.IsDisposed Property

RFmxInstrMXIsDisposed Property

Gets a value that indicates whether the signal has been disposed.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public bool IsDisposed { get; }
```

```text
Public ReadOnly Property IsDisposed As Boolean
	Get
```

###### Property Value

Boolean

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/19d5a618-d84c-a102-e66b-7ca4fb241190.htm language=enus -->
## TOPIC 00041: rfmxinstrdotnet/html/19d5a618-d84c-a102-e66b-7ca4fb241190.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/19d5a618-d84c-a102-e66b-7ca4fb241190.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/19d5a618-d84c-a102-e66b-7ca4fb241190.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXLOInjectionSide Enumeration

RFmxInstrMXLOInjectionSide Enumeration

Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXLOInjectionSide
```

```text
Public Enumeration RFmxInstrMXLOInjectionSide
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HighSide | 0 | Configures the LO signal that the device generates at a frequency higher than the RF signal. This LO frequency is given by the following formula: fLO = fRF + fIF |
|  | LowSide | 1 | Configures the LO signal that the device generates at a frequency lower than the RF signal. This LO frequency is given by the following formula: fLO = fRF – fIF |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/1a66f93c-bb96-dc71-dc4e-33bd07d8b3a4.htm language=enus -->
## TOPIC 00042: rfmxinstrdotnet/html/1a66f93c-bb96-dc71-dc4e-33bd07d8b3a4.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/1a66f93c-bb96-dc71-dc4e-33bd07d8b3a4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/1a66f93c-bb96-dc71-dc4e-33bd07d8b3a4.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetPhaseOffset Method

RFmxInstrMXSetPhaseOffset Method

Sets the offset to apply to the initial I and Q phases.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetPhaseOffset(
	string channelName,
	double value
)
```

```text
Public Function SetPhaseOffset ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleSpecifies the offset to apply to the initial I and Q phases.

###### Return Value

Int32

##### Remarks

PhaseOffset

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/1bfdc7cc-1c29-963d-605a-80253c4f5df9.htm language=enus -->
## TOPIC 00043: rfmxinstrdotnet/html/1bfdc7cc-1c29-963d-605a-80253c4f5df9.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/1bfdc7cc-1c29-963d-605a-80253c4f5df9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/1bfdc7cc-1c29-963d-605a-80253c4f5df9.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.PxiClockMaster Field

RFmxInstrMXConstantsPxiClockMaster Field

PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clock as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.

PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clock as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.

PXIe-5840 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock, and configures the PXIe-5840 to use PXI_Clock. For best performance, configure all other devices in the system to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-5840 REF IN connector for this configuration.

PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840: This configuration does not apply.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string PxiClockMaster = "PXI_ClkMaster"
```

```text
Public Const PxiClockMaster As String = "PXI_ClkMaster"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/1f24b4ef-fdfc-f711-4cbb-b3cb10be9ad5.htm language=enus -->
## TOPIC 00044: rfmxinstrdotnet/html/1f24b4ef-fdfc-f711-4cbb-b3cb10be9ad5.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/1f24b4ef-fdfc-f711-4cbb-b3cb10be9ad5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/1f24b4ef-fdfc-f711-4cbb-b3cb10be9ad5.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeULongArray Method

RFmxInstrMXGetAttributeULongArray Method

Gets the value of a ulong array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeULongArray(
	string channelName,
	int attributeIdentifier,
	ref ulong[] value
)
```

```text
Public Function GetAttributeULongArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	ByRef value As ULong()
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringSpecifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemUInt64Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/1ffff5ea-f4ed-921d-a9e1-8a3a50959adc.htm language=enus -->
## TOPIC 00045: rfmxinstrdotnet/html/1ffff5ea-f4ed-921d-a9e1-8a3a50959adc.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/1ffff5ea-f4ed-921d-a9e1-8a3a50959adc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/1ffff5ea-f4ed-921d-a9e1-8a3a50959adc.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetMixerLevelOffset Method

RFmxInstrMXSetMixerLevelOffset Method

Sets the number of dB by which to adjust the device mixer level.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetMixerLevelOffset(
	string channelName,
	double value
)
```

```text
Public Function SetMixerLevelOffset ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleSpecifies the number of dB by which to adjust the device mixer level.

###### Return Value

Int32

##### Remarks

MixerLevelOffset

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/211a9f7f-e69c-ed08-73a7-859ce984a639.htm language=enus -->
## TOPIC 00046: rfmxinstrdotnet/html/211a9f7f-e69c-ed08-73a7-859ce984a639.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/211a9f7f-e69c-ed08-73a7-859ce984a639.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/211a9f7f-e69c-ed08-73a7-859ce984a639.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXAdvanceTriggerType Enumeration

RFmxInstrMXAdvanceTriggerType Enumeration

Specifies whether the advance trigger is a digital edge or a software trigger.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXAdvanceTriggerType
```

```text
Public Enumeration RFmxInstrMXAdvanceTriggerType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | No advance trigger is configured. |
|  | DigitalEdge | 1 | The advance trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the SetAdvanceTriggerDigitalEdgeSource(String, String) method. |
|  | Software | 3 | The advance trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the RFmxInstr_SendSoftwareEdgeTrigger function. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/29ee45fc-6fa9-8e45-7e4a-66fedb7f6cec.htm language=enus -->
## TOPIC 00047: rfmxinstrdotnet/html/29ee45fc-6fa9-8e45-7e4a-66fedb7f6cec.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/29ee45fc-6fa9-8e45-7e4a-66fedb7f6cec.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/29ee45fc-6fa9-8e45-7e4a-66fedb7f6cec.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.ConfigureSParameterExternalAttenuationTable Method

RFmxInstrMXConfigureSParameterExternalAttenuationTable Method

selectorString

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureSParameterExternalAttenuationTable(
	string selectorString,
	string tableName,
	double[] frequency,
	ComplexDouble[,,] sParameters,
	RFmxInstrMXSParameterOrientation sParameterOrientation
)
```

```text
Public Function ConfigureSParameterExternalAttenuationTable ( 
	selectorString As String,
	tableName As String,
	frequency As Double(),
	sParameters As ComplexDouble(,,),
	sParameterOrientation As RFmxInstrMXSParameterOrientation
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemString Specifies the calibration plane name in which external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure S-parameter external attenuation table for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::(calplaneName)/port::(deviceName)/(channelNumber)/(portName)". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstrMX.GetAvailablePorts method to get the valid port names.Example:"""calplane::plane0""calplane::plane0/port::if0""port::if0""calplane::plane0/port::all"
- **tableName**
  - Type: SystemString Specifies the name to be associated with S-parameter table within a calibration plane. Provide a unique name, such as "table1" to configure the table.
- **frequency**
  - Type: SystemDouble Specifies an array of frequencies in the S-parameter table. This value is expressed in Hz.
- **sParameters**
  - Type: NationalInstrumentsComplexDouble Specifies the S-parameters for each frequency. The first index indicates the corresponding frequency entry, the second index corresponds to the target port for the S-parameter, and the third index corresponds to the the source port. For example, to index the s21 parameter for the fourth frequency in the table, you would use {3, 1, 0} as the indexes since they are zero-based.
- **sParameterOrientation**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXSParameterOrientationSpecifies the orientation of the data in the S-parameter table relative to the port you specify.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/2f1aa7d2-81af-ac32-e6cb-c24f1c02bd49.htm language=enus -->
## TOPIC 00048: rfmxinstrdotnet/html/2f1aa7d2-81af-ac32-e6cb-c24f1c02bd49.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/2f1aa7d2-81af-ac32-e6cb-c24f1c02bd49.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/2f1aa7d2-81af-ac32-e6cb-c24f1c02bd49.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.ForceClose Method

RFmxInstrMXForceClose Method

Closes all RFmx sessions. Calling this method once will destroy the session, irrespective of the many references obtained for the session for a particular resource name.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public void ForceClose()
```

```text
Public Sub ForceClose
```

##### Remarks

This method maps to the RFmxInstr_Close() function in C.

##### Remarks

If you have used an existing instrument handle to create this session; calling the Dispose, Close, or ForceClose methods will only dispose the .NET resources associated with this session. The pre-existing instrument handle will NOT be released.

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/313b314f-c529-3af8-dc3c-af11aebdc142.htm language=enus -->
## TOPIC 00049: rfmxinstrdotnet/html/313b314f-c529-3af8-dc3c-af11aebdc142.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/313b314f-c529-3af8-dc3c-af11aebdc142.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/313b314f-c529-3af8-dc3c-af11aebdc142.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeLong Method

RFmxInstrMXSetAttributeLong Method

Sets the value of a Long attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeLong(
	string channelName,
	int attributeIdentifier,
	long value
)
```

```text
Public Function SetAttributeLong ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As Long
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemInt64Specifies the value to which you want to set the attribute.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/335c54de-2b7b-2959-fb13-df6a5c37d3f9.htm language=enus -->
## TOPIC 00050: rfmxinstrdotnet/html/335c54de-2b7b-2959-fb13-df6a5c37d3f9.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/335c54de-2b7b-2959-fb13-df6a5c37d3f9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/335c54de-2b7b-2959-fb13-df6a5c37d3f9.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeSByteArray Method

RFmxInstrMXGetAttributeSByteArray Method

Gets the value of a sbyte array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeSByteArray(
	string channelName,
	int attributeIdentifier,
	ref sbyte[] value
)
```

```text
Public Function GetAttributeSByteArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	ByRef value As SByte()
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringSpecifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemSByteUpon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/363c8970-a952-e1a9-4db5-82d13e42e2fc.htm language=enus -->
## TOPIC 00051: rfmxinstrdotnet/html/363c8970-a952-e1a9-4db5-82d13e42e2fc.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/363c8970-a952-e1a9-4db5-82d13e42e2fc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/363c8970-a952-e1a9-4db5-82d13e42e2fc.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeLong Method

RFmxInstrMXGetAttributeLong Method

Gets the value of an RFmx 64-bit integer (int64) attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeLong(
	string channelName,
	int attributeIdentifier,
	out long value
)
```

```text
Public Function GetAttributeLong ( 
	channelName As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As Long
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemInt64Upon return, contains a value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/37965ce6-a099-a488-f7f2-95f8456b7761.htm language=enus -->
## TOPIC 00052: rfmxinstrdotnet/html/37965ce6-a099-a488-f7f2-95f8456b7761.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/37965ce6-a099-a488-f7f2-95f8456b7761.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/37965ce6-a099-a488-f7f2-95f8456b7761.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetFftWidth Method

RFmxInstrMXGetFftWidth Method

Gets the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFftWidth(
	string channelName,
	out double value
)
```

```text
Public Function GetFftWidth ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition.

###### Return Value

Int32

##### Remarks

FftWidth

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/37c202ef-480d-b267-56cd-d70de03886bf.htm language=enus -->
## TOPIC 00053: rfmxinstrdotnet/html/37c202ef-480d-b267-56cd-d70de03886bf.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/37c202ef-480d-b267-56cd-d70de03886bf.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/37c202ef-480d-b267-56cd-d70de03886bf.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

IList.ListType Property

IListListType Property

Gets the type of the current list object.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
Type ListType { get; }
```

```text
ReadOnly Property ListType As Type
	Get
```

###### Property Value

Type

##### See Also

###### Reference

IList Interface

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/39796630-d427-c02f-4ea4-704c1f4b7184.htm language=enus -->
## TOPIC 00054: rfmxinstrdotnet/html/39796630-d427-c02f-4ea4-704c1f4b7184.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/39796630-d427-c02f-4ea4-704c1f4b7184.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/39796630-d427-c02f-4ea4-704c1f4b7184.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetTuningSpeed Method

RFmxInstrMXSetTuningSpeed Method

Makes tradeoffs between tuning speed and phase noise.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetTuningSpeed(
	string channelName,
	RFmxInstrMXTuningSpeed value
)
```

```text
Public Function SetTuningSpeed ( 
	channelName As String,
	value As RFmxInstrMXTuningSpeed
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the losource number. Example: "losource0". You can use the BuildLOString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXTuningSpeedMakes tradeoffs between tuning speed and phase noise.

###### Return Value

Int32

##### Remarks

TuningSpeed

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/399d3eb4-c87c-e817-b980-02aecc514a9e.htm language=enus -->
## TOPIC 00055: rfmxinstrdotnet/html/399d3eb4-c87c-e817-b980-02aecc514a9e.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/399d3eb4-c87c-e817-b980-02aecc514a9e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/399d3eb4-c87c-e817-b980-02aecc514a9e.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeFloat Method

RFmxInstrMXGetAttributeFloat Method

Gets the value of a Float attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeFloat(
	string channelName,
	int attributeIdentifier,
	out float value
)
```

```text
Public Function GetAttributeFloat ( 
	channelName As String,
	attributeIdentifier As Integer,
	<OutAttribute> ByRef value As Single
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringSpecifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemSingleUpon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/3cdf4165-e893-0a9e-953a-d23d8780bdf1.htm language=enus -->
## TOPIC 00056: rfmxinstrdotnet/html/3cdf4165-e893-0a9e-953a-d23d8780bdf1.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/3cdf4165-e893-0a9e-953a-d23d8780bdf1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/3cdf4165-e893-0a9e-953a-d23d8780bdf1.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAttributeLongArray Method

RFmxInstrMXSetAttributeLongArray Method

Sets the value of a long array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAttributeLongArray(
	string channelName,
	int attributeIdentifier,
	long[] value
)
```

```text
Public Function SetAttributeLongArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	value As Long()
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringSpecifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemInt64Upon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/3d093497-3c3c-e0ff-6bbb-b9a334e29bc8.htm language=enus -->
## TOPIC 00057: rfmxinstrdotnet/html/3d093497-3c3c-e0ff-6bbb-b9a334e29bc8.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/3d093497-3c3c-e0ff-6bbb-b9a334e29bc8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/3d093497-3c3c-e0ff-6bbb-b9a334e29bc8.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetStartTriggerDigitalEdgeSource Method

RFmxInstrMXGetStartTriggerDigitalEdgeSource Method

SetStartTriggerType(String, RFmxInstrMXStartTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetStartTriggerDigitalEdgeSource(
	string selectorString,
	out string value
)
```

```text
Public Function GetStartTriggerDigitalEdgeSource ( 
	selectorString As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemString Upon return, contains the source terminal for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

StartTriggerDigitalEdgeSource

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/425d7905-533d-de34-07b5-2a0a91557b17.htm language=enus -->
## TOPIC 00058: rfmxinstrdotnet/html/425d7905-533d-de34-07b5-2a0a91557b17.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/425d7905-533d-de34-07b5-2a0a91557b17.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/425d7905-533d-de34-07b5-2a0a91557b17.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetPreselectorPresent Method

RFmxInstrMXGetPreselectorPresent Method

Indicates whether a preselector is available on the RF downconverter module.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPreselectorPresent(
	string channelName,
	out bool value
)
```

```text
Public Function GetPreselectorPresent ( 
	channelName As String,
	<OutAttribute> ByRef value As Boolean
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value**
  - Type: SystemBooleanIndicates whether a preselector is available on the RF downconverter module.

###### Return Value

Int32

##### Remarks

PreselectorPresent

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/443291ad-7f34-fa33-75e3-4a1dc8c5e7ed.htm language=enus -->
## TOPIC 00059: rfmxinstrdotnet/html/443291ad-7f34-fa33-75e3-4a1dc8c5e7ed.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/443291ad-7f34-fa33-75e3-4a1dc8c5e7ed.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/443291ad-7f34-fa33-75e3-4a1dc8c5e7ed.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetStartTriggerDigitalEdge Method

RFmxInstrMXSetStartTriggerDigitalEdge Method

SetStartTriggerType(String, RFmxInstrMXStartTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetStartTriggerDigitalEdge(
	string selectorString,
	RFmxInstrMXStartTriggerDigitalEdge value
)
```

```text
Public Function SetStartTriggerDigitalEdge ( 
	selectorString As String,
	value As RFmxInstrMXStartTriggerDigitalEdge
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXStartTriggerDigitalEdge Specifies the active edge for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

StartTriggerDigitalEdge

Rising

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/48bb912a-06c2-afbe-1229-1737a28dea63.htm language=enus -->
## TOPIC 00060: rfmxinstrdotnet/html/48bb912a-06c2-afbe-1229-1737a28dea63.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/48bb912a-06c2-afbe-1229-1737a28dea63.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/48bb912a-06c2-afbe-1229-1737a28dea63.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetTuningSpeed Method

RFmxInstrMXGetTuningSpeed Method

Makes tradeoffs between tuning speed and phase noise.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTuningSpeed(
	string channelName,
	out RFmxInstrMXTuningSpeed value
)
```

```text
Public Function GetTuningSpeed ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXTuningSpeed
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the losource number. Example: "losource0". You can use the BuildLOString(String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXTuningSpeedMakes tradeoffs between tuning speed and phase noise.

###### Return Value

Int32

##### Remarks

TuningSpeed

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/49868d53-2289-42fe-9e47-23ab866fa291.htm language=enus -->
## TOPIC 00061: rfmxinstrdotnet/html/49868d53-2289-42fe-9e47-23ab866fa291.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/49868d53-2289-42fe-9e47-23ab866fa291.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/49868d53-2289-42fe-9e47-23ab866fa291.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetLOInjectionSide Method

RFmxInstrMXSetLOInjectionSide Method

Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLOInjectionSide(
	string channelName,
	RFmxInstrMXLOInjectionSide value
)
```

```text
Public Function SetLOInjectionSide ( 
	channelName As String,
	value As RFmxInstrMXLOInjectionSide
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXLOInjectionSideEnables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

LOInjectionSide

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/540be57c-f1b9-46c6-29ee-678a100d3a93.htm language=enus -->
## TOPIC 00062: rfmxinstrdotnet/html/540be57c-f1b9-46c6-29ee-678a100d3a93.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/540be57c-f1b9-46c6-29ee-678a100d3a93.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/540be57c-f1b9-46c6-29ee-678a100d3a93.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.OnboardClock Field

RFmxInstrMXConstantsOnboardClock Field

PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.

PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.

PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624.

PXIe-5644/5645/5646, PXIe-5820/5840: RFmx locks the device to its onboard clock.

PXIe-5830/5831/5832: For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector.

PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector.

PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector.

PXIe-5840 with PXIe-5653: Lock onto the PXIe-5653 onboard clock. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. Configure open NI-RFSG sessions to the device to use ReferenceIn for PXIe-5840 or ReferenceIn2 for the PXIe-5840 with the PXIe-5653.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string OnboardClock = "OnboardClock"
```

```text
Public Const OnboardClock As String = "OnboardClock"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/54b36583-7b5f-0375-7227-05c0bcbb2650.htm language=enus -->
## TOPIC 00063: rfmxinstrdotnet/html/54b36583-7b5f-0375-7227-05c0bcbb2650.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/54b36583-7b5f-0375-7227-05c0bcbb2650.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/54b36583-7b5f-0375-7227-05c0bcbb2650.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.DangerousGetNIRfsaHandle Method

RFmxInstrMXDangerousGetNIRfsaHandle Method

| Note |
| --- |
| Do not close the NI-RFSA driver session before calling RFmx close. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. |

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int DangerousGetNIRfsaHandle(
	out IntPtr niRfsaHandle
)
```

```text
Public Function DangerousGetNIRfsaHandle ( 
	<OutAttribute> ByRef niRfsaHandle As IntPtr
) As Integer
```

###### Parameters

- **niRfsaHandle**
  - Type: SystemIntPtr Upon return, contains the value of the underlying instrument handle.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/59c1c7fd-11af-f32b-c115-8cb1ef099b99.htm language=enus -->
## TOPIC 00064: rfmxinstrdotnet/html/59c1c7fd-11af-f32b-c115-8cb1ef099b99.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/59c1c7fd-11af-f32b-c115-8cb1ef099b99.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/59c1c7fd-11af-f32b-c115-8cb1ef099b99.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.LOSourceNone Field

RFmxInstrMXConstantsLOSourceNone Field

Specifies that no LO source is required to downconvert the RF input signal.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string LOSourceNone = "None"
```

```text
Public Const LOSourceNone As String = "None"
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/5d6e92ce-919e-a7b2-f07c-4960ff66adf5.htm language=enus -->
## TOPIC 00065: rfmxinstrdotnet/html/5d6e92ce-919e-a7b2-f07c-4960ff66adf5.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/5d6e92ce-919e-a7b2-f07c-4960ff66adf5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/5d6e92ce-919e-a7b2-f07c-4960ff66adf5.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetPreampEnabled Method

RFmxInstrMXGetPreampEnabled Method

Gets whether the RF preamplifier is enabled in the system.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetPreampEnabled(
	string channelName,
	out RFmxInstrMXPreampEnabled value
)
```

```text
Public Function GetPreampEnabled ( 
	channelName As String,
	<OutAttribute> ByRef value As RFmxInstrMXPreampEnabled
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXPreampEnabledUpon return, contains whether the RF preamplifier is enabled in the system.

###### Return Value

Int32

##### Remarks

PreampEnabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/5e5805ae-8128-c244-598e-9179c09e6fe4.htm language=enus -->
## TOPIC 00066: rfmxinstrdotnet/html/5e5805ae-8128-c244-598e-9179c09e6fe4.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/5e5805ae-8128-c244-598e-9179c09e6fe4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/5e5805ae-8128-c244-598e-9179c09e6fe4.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX Constructor

RFmxInstrMX Constructor

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | RFmxInstrMX(IntPtr) | Creates a new RFmx session from an existing RFmx instrument handle. |
|  | RFmxInstrMX(String, String) | Creates an RFmx session to the device you specify through the resourceName parameter. Note Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |
| Note |  |  |
| Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |  |  |
|  | RFmxInstrMX(String, String) | Creates an RFmx session to the device you specify through the resourceName parameter. Note Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |
| Note |  |  |
| Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |  |  |

Top

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/60439421-72c9-0ce2-6922-944a14ad5ee4.htm language=enus -->
## TOPIC 00067: rfmxinstrdotnet/html/60439421-72c9-0ce2-6922-944a14ad5ee4.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/60439421-72c9-0ce2-6922-944a14ad5ee4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/60439421-72c9-0ce2-6922-944a14ad5ee4.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetLO2ExportEnabled Method

RFmxInstrMXSetLO2ExportEnabled Method

Sets whether to enable the LO2 OUT terminals in the installed devices.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLO2ExportEnabled(
	string channelName,
	RFmxInstrMXLO2ExportEnabled value
)
```

```text
Public Function SetLO2ExportEnabled ( 
	channelName As String,
	value As RFmxInstrMXLO2ExportEnabled
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXLO2ExportEnabledSpecifies whether to enable the LO2 OUT terminals in the installed devices.

###### Return Value

Int32

##### Remarks

LO2ExportEnabled

Disabled

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/6bb6de0c-fef6-8057-1c1f-4504061c7020.htm language=enus -->
## TOPIC 00068: rfmxinstrdotnet/html/6bb6de0c-fef6-8057-1c1f-4504061c7020.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/6bb6de0c-fef6-8057-1c1f-4504061c7020.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/6bb6de0c-fef6-8057-1c1f-4504061c7020.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetInstrumentHandle Method

RFmxInstrMXGetInstrumentHandle Method

SafeHandle

RFmxInstrMX

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public SafeHandle GetInstrumentHandle()
```

```text
Public Function GetInstrumentHandle As SafeHandle
```

###### Return Value

SafeHandle

SafeHandle

RFmxInstrMX

##### Remarks

SafeHandle

IntPtr

IntPtr

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/6d1100bd-c9d6-ce20-88c1-6274ed07ea24.htm language=enus -->
## TOPIC 00069: rfmxinstrdotnet/html/6d1100bd-c9d6-ce20-88c1-6274ed07ea24.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/6d1100bd-c9d6-ce20-88c1-6274ed07ea24.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/6d1100bd-c9d6-ce20-88c1-6274ed07ea24.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetLOOutPower Method

RFmxInstrMXSetLOOutPower Method

SetLOExportEnabled(String, Boolean)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetLOOutPower(
	string channelName,
	double value
)
```

```text
Public Function SetLOOutPower ( 
	channelName As String,
	value As Double
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the losource number. Example: "losource0". You can use the BuildLOString(String, Int32) method to build the selector string.
- **value**
  - Type: SystemDouble Specifies the power level of the signal at the LO OUT terminal when the SetLOExportEnabled(String, Boolean) method is set to TRUE. This value is expressed in dBm.

###### Return Value

Int32

##### Remarks

LOOutPower

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/766a7116-6c49-a036-b297-d7e291d087bb.htm language=enus -->
## TOPIC 00070: rfmxinstrdotnet/html/766a7116-6c49-a036-b297-d7e291d087bb.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/766a7116-6c49-a036-b297-d7e291d087bb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/766a7116-6c49-a036-b297-d7e291d087bb.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetAttributeByteArray Method

RFmxInstrMXGetAttributeByteArray Method

Gets the value of a byte array attribute.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetAttributeByteArray(
	string channelName,
	int attributeIdentifier,
	ref byte[] value
)
```

```text
Public Function GetAttributeByteArray ( 
	channelName As String,
	attributeIdentifier As Integer,
	ByRef value As Byte()
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringSpecifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Instr Help for more information about configuring the selector string.
- **attributeIdentifier**
  - Type: SystemInt32Specifies the ID of an attribute.
- **value**
  - Type: SystemByteUpon return, contains the value of the specified attribute ID.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/78dc1655-b9ce-6272-cdbd-b50973d8a0fb.htm language=enus -->
## TOPIC 00071: rfmxinstrdotnet/html/78dc1655-b9ce-6272-cdbd-b50973d8a0fb.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/78dc1655-b9ce-6272-cdbd-b50973d8a0fb.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/78dc1655-b9ce-6272-cdbd-b50973d8a0fb.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetFrequencyReferenceExportedTerminal Method

RFmxInstrMXGetFrequencyReferenceExportedTerminal Method

Gets a comma-separated list of the terminals at which to export the frequency reference.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetFrequencyReferenceExportedTerminal(
	string channelName,
	out string value
)
```

```text
Public Function GetFrequencyReferenceExportedTerminal ( 
	channelName As String,
	<OutAttribute> ByRef value As String
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value**
  - Type: SystemStringUpon return, contains a comma-separated list of the terminals at which to export the frequency reference.

###### Return Value

Int32

##### Remarks

FrequencyReferenceExportedTerminal

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/7933afaa-9203-a2c9-37a8-396ab4f15231.htm language=enus -->
## TOPIC 00072: rfmxinstrdotnet/html/7933afaa-9203-a2c9-37a8-396ab4f15231.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/7933afaa-9203-a2c9-37a8-396ab4f15231.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/7933afaa-9203-a2c9-37a8-396ab4f15231.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.BuildModuleString Method

RFmxInstrMXBuildModuleString Method

Selector String

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public static string BuildModuleString(
	string selectorString,
	string moduleName
)
```

```text
Public Shared Function BuildModuleString ( 
	selectorString As String,
	moduleName As String
) As String
```

###### Parameters

- **selectorString**
  - Type: SystemString specifies the selector string. The default value is "" (empty string).
- **moduleName**
  - Type: SystemString specifies the module for which you want the temperature to be read.

###### Return Value

String

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/7977dce9-72d3-4df4-3396-be3331bc1d3f.htm language=enus -->
## TOPIC 00073: rfmxinstrdotnet/html/7977dce9-72d3-4df4-3396-be3331bc1d3f.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/7977dce9-72d3-4df4-3396-be3331bc1d3f.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/7977dce9-72d3-4df4-3396-be3331bc1d3f.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSignalConfigurationNames Method

RFmxInstrMXGetSignalConfigurationNames Method

Returns the signal names and corresponding personality type, for the personality type selected in the personalityFilter parameter.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSignalConfigurationNames(
	string selectorString,
	RFmxInstrMXPersonalities personalityFilter,
	ref string[] signalNames,
	ref RFmxInstrMXPersonalities[] personality
)
```

```text
Public Function GetSignalConfigurationNames ( 
	selectorString As String,
	personalityFilter As RFmxInstrMXPersonalities,
	ByRef signalNames As String(),
	ByRef personality As RFmxInstrMXPersonalities()
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecifies the selector string. Pass an empty string.
- **personalityFilter**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXPersonalities Specifies the personality filter to get the signal configuration names. You can specify one or more of the following personalities. The default value is All. To get all the signal names of SpecAn, personalityFilter parameter should be RFmxInstrMXPersonalities.SpecAn. To get the signal names of SpecAn and LTE, personalityFilter parameter should be RFmxInstrMXPersonalities.SpecAn and RFmxInstrMXPersonalities.Lte. To get the signal names of all personalities, personalityFilter parameter should be RFmxInstrMXPersonalities.All.
- **signalNames**
  - Type: SystemStringReturns an array of the signal names.
- **personality**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXPersonalities Returns an array of personalities where each entry corresponds to the personality of each signal name in the signalNames array.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/7c4f6aad-c13e-93cd-1fee-5a0c9bb9a51c.htm language=enus -->
## TOPIC 00074: rfmxinstrdotnet/html/7c4f6aad-c13e-93cd-1fee-5a0c9bb9a51c.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/7c4f6aad-c13e-93cd-1fee-5a0c9bb9a51c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/7c4f6aad-c13e-93cd-1fee-5a0c9bb9a51c.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetIFOutputPowerLevelOffset Method

RFmxInstrMXGetIFOutputPowerLevelOffset Method

Gets the power offset by which to adjust the default IF output power level. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetIFOutputPowerLevelOffset(
	string channelName,
	out double value
)
```

```text
Public Function GetIFOutputPowerLevelOffset ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the power offset by which to adjust the default IF output power level. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

IFOutputPowerLevelOffset

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/978008dd-2cbd-6da5-143b-b38bf104cd4a.htm language=enus -->
## TOPIC 00075: rfmxinstrdotnet/html/978008dd-2cbd-6da5-143b-b38bf104cd4a.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/978008dd-2cbd-6da5-143b-b38bf104cd4a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/978008dd-2cbd-6da5-143b-b38bf104cd4a.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXConstants.DoNotExportSignal Field

RFmxInstrMXConstantsDoNotExportSignal Field

Specifies that the signal should not be exported.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public const string DoNotExportSignal = ""
```

```text
Public Const DoNotExportSignal As String = ""
```

###### Field Value

String

##### See Also

###### Reference

RFmxInstrMXConstants Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/97ba61fa-fe1d-fdb9-16eb-6438ff17f5dd.htm language=enus -->
## TOPIC 00076: rfmxinstrdotnet/html/97ba61fa-fe1d-fdb9-16eb-6438ff17f5dd.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/97ba61fa-fe1d-fdb9-16eb-6438ff17f5dd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/97ba61fa-fe1d-fdb9-16eb-6438ff17f5dd.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetStartTriggerType Method

RFmxInstrMXGetStartTriggerType Method

Gets whether the start trigger is a digital edge or a software trigger.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetStartTriggerType(
	string selectorString,
	out RFmxInstrMXStartTriggerType value
)
```

```text
Public Function GetStartTriggerType ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxInstrMXStartTriggerType
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXStartTriggerTypeUpon return, contains whether the start trigger is a digital edge or a software trigger.

###### Return Value

Int32

##### Remarks

StartTriggerType

None

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/a6429b7a-ca2a-f8bd-3cb2-25e5d1daf96a.htm language=enus -->
## TOPIC 00077: rfmxinstrdotnet/html/a6429b7a-ca2a-f8bd-3cb2-25e5d1daf96a.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/a6429b7a-ca2a-f8bd-3cb2-25e5d1daf96a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/a6429b7a-ca2a-f8bd-3cb2-25e5d1daf96a.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SelfCalibrateRange Method

RFmxInstrMXSelfCalibrateRange Method

niRFSA Self Calibrate Range

NI RF Vector Signal Analyzers Help

supporteddevices:

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SelfCalibrateRange(
	string selectorString,
	RFmxInstrMXSelfCalibrateSteps stepsToOmit,
	double minimumFrequency,
	double maximumFrequency,
	double minimumReferenceLevel,
	double maximumReferenceLevel
)
```

```text
Public Function SelfCalibrateRange ( 
	selectorString As String,
	stepsToOmit As RFmxInstrMXSelfCalibrateSteps,
	minimumFrequency As Double,
	maximumFrequency As Double,
	minimumReferenceLevel As Double,
	maximumReferenceLevel As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringSpecify an empty string as the value of this parameter.
- **stepsToOmit**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXSelfCalibrateSteps Specifies which calibration steps to skip during the self-calibration process. PreselectorAlignmentNot used by this method.GainReferenceNot used by this method.IFFlatnessNot used by this method.DigitizerSelfcalNot used by this method.LOSelfCalOmits the LO Self Cal step. If you omit this step and the NI-RFSA IsSelfCalibrationValid method indicates the calibration data for this step is invalid, the LO PLL may fail to lock.AmplitudeAccuracyOmits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted. ResidualLOPowerOmits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted. ImageSuppressionOmits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.SynthesizerAlignmentOmits the VCO Alignment step. If you omit this step, the LO PLL will not get adjusted. DCOffsetOmits the DC Offset step.
- **minimumFrequency**
  - Type: SystemDouble specifies the minimum frequency for the custom self calibration range. This value is expressed in Hz. Note For the PXIe-5830/5831/5832, only the applicable ports within the specified frequency range are calibrated.
- **maximumFrequency**
  - Type: SystemDoublespecifies the maximum frequency for the custom self calibration range. This value is expressed in Hz.
- **minimumReferenceLevel**
  - Type: SystemDouble specifies the minimum reference level for the custom self calibration range. This value is expressed in dBm.
- **maximumReferenceLevel**
  - Type: SystemDoublespecifies the maximum reference level for the custom self calibration range. This value is expressed dBm.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/a6ab1f4f-e9d4-ad94-8ce2-5a424e0ef782.htm language=enus -->
## TOPIC 00078: rfmxinstrdotnet/html/a6ab1f4f-e9d4-ad94-8ce2-5a424e0ef782.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/a6ab1f4f-e9d4-ad94-8ce2-5a424e0ef782.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/a6ab1f4f-e9d4-ad94-8ce2-5a424e0ef782.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetAdvanceTriggerExportOutputTerminal Method

RFmxInstrMXSetAdvanceTriggerExportOutputTerminal Method

Sets the destination terminal for the exported advance trigger.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetAdvanceTriggerExportOutputTerminal(
	string selectorString,
	string value
)
```

```text
Public Function SetAdvanceTriggerExportOutputTerminal ( 
	selectorString As String,
	value As String
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemStringSpecifies the destination terminal for the exported advance trigger.

###### Return Value

Int32

##### Remarks

AdvanceTriggerExportOutputTerminal

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/a7498d83-19e7-a325-7422-cf29b19bf62d.htm language=enus -->
## TOPIC 00079: rfmxinstrdotnet/html/a7498d83-19e7-a325-7422-cf29b19bf62d.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/a7498d83-19e7-a325-7422-cf29b19bf62d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/a7498d83-19e7-a325-7422-cf29b19bf62d.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SendSoftwareEdgeAdvanceTrigger Method

RFmxInstrMXSendSoftwareEdgeAdvanceTrigger Method

- You configure an invalid trigger.
- You have not previously called the RFmx Initiate method.

supporteddevices

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SendSoftwareEdgeAdvanceTrigger()
```

```text
Public Function SendSoftwareEdgeAdvanceTrigger As Integer
```

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/a8b8439a-a9e1-e9f2-0008-662209f4d724.htm language=enus -->
## TOPIC 00080: rfmxinstrdotnet/html/a8b8439a-a9e1-e9f2-0008-662209f4d724.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/a8b8439a-a9e1-e9f2-0008-662209f4d724.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/a8b8439a-a9e1-e9f2-0008-662209f4d724.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.SetOptimizePathForSignalBandwidth Method

RFmxInstrMXSetOptimizePathForSignalBandwidth Method

Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int SetOptimizePathForSignalBandwidth(
	string channelName,
	RFmxInstrMXOptimizePathForSignalBandwidth value
)
```

```text
Public Function SetOptimizePathForSignalBandwidth ( 
	channelName As String,
	value As RFmxInstrMXOptimizePathForSignalBandwidth
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXOptimizePathForSignalBandwidthOptimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency.

###### Return Value

Int32

##### Remarks

OptimizePathForSignalBandwidth

Automatic

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/af88f818-6265-76da-37fd-8ea88b703be4.htm language=enus -->
## TOPIC 00081: rfmxinstrdotnet/html/af88f818-6265-76da-37fd-8ea88b703be4.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/af88f818-6265-76da-37fd-8ea88b703be4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/af88f818-6265-76da-37fd-8ea88b703be4.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetSelfCalibrationValidityCheckTimeInterval Method

RFmxInstrMXGetSelfCalibrationValidityCheckTimeInterval Method

Gets the minimum time between two self calibration validity checks. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetSelfCalibrationValidityCheckTimeInterval(
	string selectorString,
	out double value
)
```

```text
Public Function GetSelfCalibrationValidityCheckTimeInterval ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum time between two self calibration validity checks. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

SelfCalibrationValidityCheckTimeInterval

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/b2679149-20d7-34c4-6372-641551e9bcb6.htm language=enus -->
## TOPIC 00082: rfmxinstrdotnet/html/b2679149-20d7-34c4-6372-641551e9bcb6.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/b2679149-20d7-34c4-6372-641551e9bcb6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/b2679149-20d7-34c4-6372-641551e9bcb6.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetRecommendedCenterFrequency Method

RFmxInstrMXGetRecommendedCenterFrequency Method

RFmxInstrMX(String, String)

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetRecommendedCenterFrequency(
	string channelName,
	out double value
)
```

```text
Public Function GetRecommendedCenterFrequency ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemString Specifies the port number. Example: "port0". You can use the BuildPortString2(String, String, String, Int32) method to build the selector string.
- **value**
  - Type: SystemDoubleUpon return, contains the recommended center frequency of the RF signal. This value is expressed in Hz.

###### Return Value

Int32

##### Remarks

RecommendedCenterFrequency

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/b4eb7b8f-3ebe-d6ca-b96a-0357185c4826.htm language=enus -->
## TOPIC 00083: rfmxinstrdotnet/html/b4eb7b8f-3ebe-d6ca-b96a-0357185c4826.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/b4eb7b8f-3ebe-d6ca-b96a-0357185c4826.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/b4eb7b8f-3ebe-d6ca-b96a-0357185c4826.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.CheckIfListExists Method

RFmxInstrMXCheckIfListExists Method

listname

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int CheckIfListExists(
	string listName,
	out bool listExists,
	out RFmxInstrMXPersonalities personality
)
```

```text
Public Function CheckIfListExists ( 
	listName As String,
	<OutAttribute> ByRef listExists As Boolean,
	<OutAttribute> ByRef personality As RFmxInstrMXPersonalities
) As Integer
```

###### Parameters

- **listName**
  - Type: SystemString Specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix.
- **listExists**
  - Type: SystemBoolean Indicates whether the list exists or not.
- **personality**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXPersonalities Indicates the personality of the list if the list exists.

###### Return Value

Int32

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/c45eebd2-3fd3-e423-575b-a2f6b1790da1.htm language=enus -->
## TOPIC 00084: rfmxinstrdotnet/html/c45eebd2-3fd3-e423-575b-a2f6b1790da1.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/c45eebd2-3fd3-e423-575b-a2f6b1790da1.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/c45eebd2-3fd3-e423-575b-a2f6b1790da1.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMXMechanicalAttenuationAuto Enumeration

RFmxInstrMXMechanicalAttenuationAuto Enumeration

Specifies whether RFmx chooses an attenuation setting based on the hardware settings.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public enum RFmxInstrMXMechanicalAttenuationAuto
```

```text
Public Enumeration RFmxInstrMXMechanicalAttenuationAuto
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | False | 0 | Specifies that RFmx uses the value configured in the Mechanical Attenuation Value method. |
|  | True | 1 | Specifies that the measurement computes the mechanical attenuation. |

##### See Also

###### Reference

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/c866291c-86d9-ad82-c9ef-64496fe3e2cc.htm language=enus -->
## TOPIC 00085: rfmxinstrdotnet/html/c866291c-86d9-ad82-c9ef-64496fe3e2cc.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/c866291c-86d9-ad82-c9ef-64496fe3e2cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/c866291c-86d9-ad82-c9ef-64496fe3e2cc.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetTemperatureReadInterval Method

RFmxInstrMXGetTemperatureReadInterval Method

Gets the minimum time difference between temperature sensor readings. This value is expressed in seconds.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetTemperatureReadInterval(
	string selectorString,
	out double value
)
```

```text
Public Function GetTemperatureReadInterval ( 
	selectorString As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the minimum time difference between temperature sensor readings. This value is expressed in seconds.

###### Return Value

Int32

##### Remarks

TemperatureReadInterval

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/cc224795-2a1e-1e5f-058c-bd2d5c89d87a.htm language=enus -->
## TOPIC 00086: rfmxinstrdotnet/html/cc224795-2a1e-1e5f-058c-bd2d5c89d87a.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/cc224795-2a1e-1e5f-058c-bd2d5c89d87a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/cc224795-2a1e-1e5f-058c-bd2d5c89d87a.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetStartTriggerDigitalEdge Method

RFmxInstrMXGetStartTriggerDigitalEdge Method

SetStartTriggerType(String, RFmxInstrMXStartTriggerType)

DigitalEdge

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetStartTriggerDigitalEdge(
	string selectorString,
	out RFmxInstrMXStartTriggerDigitalEdge value
)
```

```text
Public Function GetStartTriggerDigitalEdge ( 
	selectorString As String,
	<OutAttribute> ByRef value As RFmxInstrMXStartTriggerDigitalEdge
) As Integer
```

###### Parameters

- **selectorString**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: NationalInstruments.RFmx.InstrMXRFmxInstrMXStartTriggerDigitalEdge Upon return, contains the active edge for the start trigger. This method is used only when you set the SetStartTriggerType(String, RFmxInstrMXStartTriggerType) method to DigitalEdge.

###### Return Value

Int32

##### Remarks

StartTriggerDigitalEdge

Rising

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/cd74e29c-2d99-20d1-d83f-b986e70e591a.htm language=enus -->
## TOPIC 00087: rfmxinstrdotnet/html/cd74e29c-2d99-20d1-d83f-b986e70e591a.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/cd74e29c-2d99-20d1-d83f-b986e70e591a.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/cd74e29c-2d99-20d1-d83f-b986e70e591a.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.Dispose Method

RFmxInstrMXDispose Method

Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any.

Namespace:

NationalInstruments.RFmx.InstrMX

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

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-instr path=rfmxinstrdotnet/html/dd28d3d8-3ebf-fe5a-25a7-a5953e5bff69.htm language=enus -->
## TOPIC 00088: rfmxinstrdotnet/html/dd28d3d8-3ebf-fe5a-25a7-a5953e5bff69.htm

- bundle_id: `rfmx-instr`
- source_path: `rfmxinstrdotnet/html/dd28d3d8-3ebf-fe5a-25a7-a5953e5bff69.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr/raw/resource/enus/rfmxinstrdotnet/html/dd28d3d8-3ebf-fe5a-25a7-a5953e5bff69.htm
- document_id: `rfmx-instr`
- page_type: `leaf`
- content_type: ``

RFmxInstrMX.GetMechanicalAttenuationValue Method

RFmxInstrMXGetMechanicalAttenuationValue Method

Gets the level of mechanical attenuation for the RF path. This value is expressed in dB.

Namespace:

NationalInstruments.RFmx.InstrMX

Assembly:

##### Syntax

C#

VB

```text
public int GetMechanicalAttenuationValue(
	string channelName,
	out double value
)
```

```text
Public Function GetMechanicalAttenuationValue ( 
	channelName As String,
	<OutAttribute> ByRef value As Double
) As Integer
```

###### Parameters

- **channelName**
  - Type: SystemStringPass an empty string. The signal name that is passed when creating the signal configuration is used.
- **value**
  - Type: SystemDoubleUpon return, contains the level of mechanical attenuation for the RF path. This value is expressed in dB.

###### Return Value

Int32

##### Remarks

MechanicalAttenuationValue

##### See Also

###### Reference

RFmxInstrMX Class

NationalInstruments.RFmx.InstrMX Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
