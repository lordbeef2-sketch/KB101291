# NI DOCUMENT BUNDLE: rfmx-vna-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-vna-cvi start=1 end=132 -->
<!--NI_TOPIC bundle=rfmx-vna-cvi path=bp_help_file_title.html language=enus -->
## TOPIC 00001: RFmx VNA C Reference

- bundle_id: `rfmx-vna-cvi`
- source_path: `bp_help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/bp_help_file_title.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmx VNA C Reference

This help file contains information about the RFmx VNA functions, attributes, and values that you can use when programming your application.

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_abortmeasurements.html language=enus -->
## TOPIC 00002: RFmxVNA_AbortMeasurements

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_abortmeasurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_abortmeasurements.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_AbortMeasurements

int32 __stdcall RFmxVNA_AbortMeasurements (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Stops acquisition and measurements associated with signal instance that you specify in the **selectorString** parameter, which were previously initiated by the [RFmxVNA_InitiateVI](/csh?topicname=rfmxvnacvi/cvirfmxvna_initiatevi.html) or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxVNA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildcalibrationelementstring.html language=enus -->
## TOPIC 00003: RFmxVNA_BuildCalibrationElementString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildcalibrationelementstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildcalibrationelementstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildCalibrationElementString

int32 __stdcall RFmxVNA_BuildCalibrationElementString (char selectorString[],
 char calibrationElementID[],
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a selector string specifying the Calibration Element within the Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calibrationElementID | char[] | Specifies the ID of the Calibration Element within the Calkit. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildcalkitstring.html language=enus -->
## TOPIC 00004: RFmxVNA_BuildCalkitString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildcalkitstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildcalkitstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildCalkitString

int32 __stdcall RFmxVNA_BuildCalkitString (char selectorString[],
 char calkitID[],
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a selector string specifying the Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calkitID | char[] | Specifies the ID for the Calkit in Calkit Manager. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildcalstepstring.html language=enus -->
## TOPIC 00005: RFmxVNA_BuildCalstepString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildcalstepstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildcalstepstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildCalstepString

int32 __stdcall RFmxVNA_BuildCalstepString (char selectorString[],
 int32 calstepNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the calibration step string to use as the selector string with the [RFmxVNA_CalibrationAcquire](/csh?topicname=rfmxvnacvi/cvirfmxvna_calibrationacquire.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calstepNumber | int32 | Specifies the calibration step number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildconnectorstring.html language=enus -->
## TOPIC 00006: RFmxVNA_BuildConnectorString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildconnectorstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildconnectorstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildConnectorString

int32 __stdcall RFmxVNA_BuildConnectorString (char selectorString[],
 char connectorID[],
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a selector string specifying the Connector within the Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| connectorID | char[] | Specifies the ID of the Connector within the Calkit. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildmarkerstring.html language=enus -->
## TOPIC 00007: RFmxVNA_BuildMarkerString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildmarkerstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildmarkerstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildMarkerString

int32 __stdcall RFmxVNA_BuildMarkerString (char selectorString[],
 int32 markerNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates selector string for use with marker configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| markerNumber | int32 | Specifies the marker number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | returns the selector string created by this VI. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildportstring.html language=enus -->
## TOPIC 00008: RFmxVNA_BuildPortString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildportstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildportstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildPortString

int32 __stdcall RFmxVNA_BuildPortString (char selectorString[],
 char portString[],
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates selector string specifying the port(s) for use with configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| portString | char[] | Specifies the signal name for building the selector string. This input accepts the port name with or without the "port::" prefix. The default value is "" (empty string). |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildpulsegeneratorstring.html language=enus -->
## TOPIC 00009: RFmxVNA_BuildPulseGeneratorString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildpulsegeneratorstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildpulsegeneratorstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildPulseGeneratorString

int32 __stdcall RFmxVNA_BuildPulseGeneratorString (char selectorString[],
 int32 pulseGeneratorNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the selector string specifying the Pulse Generator for use with configuration or fetch attributes.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| pulseGeneratorNumber | int32 | Specifies the pulse generator index for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildsegmentstring.html language=enus -->
## TOPIC 00010: RFmxVNA_BuildSegmentString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildsegmentstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildsegmentstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildSegmentString

int32 __stdcall RFmxVNA_BuildSegmentString (char selectorString[],
 int32 segmentNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a selector string specifying the segment number for use with configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| segmentNumber | int32 | Specifies the segment for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildsignalstring.html language=enus -->
## TOPIC 00011: RFmxVNA_BuildSignalString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildsignalstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildsignalstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildSignalString

int32 __stdcall RFmxVNA_BuildSignalString (char signalName[],
 char resultName[],
 int32 selectorStringLength,
 char selectorString[]);

#### Purpose

Creates selector string for use with configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| signalName | char[] | Specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. Example:"""signal::sig1""sig1" |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"""result::r1""r1" |
| selectorStringLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildsparameterstring.html language=enus -->
## TOPIC 00012: RFmxVNA_BuildSParameterString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildsparameterstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildsparameterstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildSParameterString

int32 __stdcall RFmxVNA_BuildSParameterString (char selectorString[],
 int32 sParameterNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the selector string to use with S-Parameter configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| sParameterNumber | int32 | Specifies the s-parameter index for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_buildwavesstring.html language=enus -->
## TOPIC 00013: RFmxVNA_BuildWavesString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_buildwavesstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_buildwavesstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_BuildWavesString

int32 __stdcall RFmxVNA_BuildWavesString (char selectorString[],
 int32 wavesNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the selector string to use with Wave configuration or fetch properties and functions

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| wavesNumber | int32 | Specifies the wave index for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitaddconnector.html language=enus -->
## TOPIC 00014: RFmxVNA_CalkitManagerCalkitAddConnector

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitaddconnector.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitaddconnector.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitAddConnector

int32 __stdcall RFmxVNA_CalkitManagerCalkitAddConnector (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char connectorID[]);

#### Purpose

Adds a new Connector with a user defined Connector ID to the Calkit. The user defined Connector ID has to be unique among all Connectors in the Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies a selector string comprising of the Calkit ID. Example:"ckit::MyCkitID"You can use the RFmxVNA_CalkitManagerBuildCalkitString function to build the selector string. |
| connectorID | char[] | Specifies the ID of the Connector within the Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementgetmaximumfrequency.html language=enus -->
## TOPIC 00015: RFmxVNA_CalkitManagerCalkitCalibrationElementGetMaximumFrequency

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementgetmaximumfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementgetmaximumfrequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementGetMaximumFrequency

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetMaximumFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64* maximumFrequency);

#### Purpose

Returns the Maximum Frequency of the Calibration Element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| maximumFrequency | float64* | Returns the Maximum Frequency of the Calibration Element. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementgetminimumfrequency.html language=enus -->
## TOPIC 00016: RFmxVNA_CalkitManagerCalkitCalibrationElementGetMinimumFrequency

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementgetminimumfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementgetminimumfrequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementGetMinimumFrequency

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetMinimumFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64* minimumFrequency);

#### Purpose

Returns the Minimum Frequency of the Calibration Element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| minimumFrequency | float64* | Returns the Minimum Frequency of the Calibration Element. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementgetportconnectors.html language=enus -->
## TOPIC 00017: RFmxVNA_CalkitManagerCalkitCalibrationElementGetPortConnectors

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementgetportconnectors.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementgetportconnectors.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementGetPortConnectors

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetPortConnectors (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 arraySize,
 char connectorIDs[]);

#### Purpose

Returns the array of Connectors associated with the Calibration Element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| connectorIDs | char[] | Returns the array of Connectors associated with the Calibration Element. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementgetsparameterdefinition.html language=enus -->
## TOPIC 00018: RFmxVNA_CalkitManagerCalkitCalibrationElementGetSParameterDefinition

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementgetsparameterdefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementgetsparameterdefinition.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementGetSParameterDefinition

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetSParameterDefinition (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32* sParameterDefinition);

#### Purpose

Returns the S-Parameter definition of the Calibration Element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| sParameterDefinition | int32* | Returns the S-Parameter definition of the Calibration Element. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementgettypes.html language=enus -->
## TOPIC 00019: RFmxVNA_CalkitManagerCalkitCalibrationElementGetTypes

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementgettypes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementgettypes.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementGetTypes

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetTypes (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 calibrationElementTypes[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the type(s) of the Calibration Element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| calibrationElementTypes | int32[] | Returns the type(s) of the Calibration Element. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementreflectmodelgetc1.html language=enus -->
## TOPIC 00020: RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetC1

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementreflectmodelgetc1.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementreflectmodelgetc1.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetC1

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetC1 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64* c1);

#### Purpose

Returns the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| c1 | float64* | Returns the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementreflectmodelgetc3.html language=enus -->
## TOPIC 00021: RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetC3

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementreflectmodelgetc3.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementreflectmodelgetc3.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetC3

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetC3 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64* c3);

#### Purpose

Returns the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| c3 | float64* | Returns the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementsetmaximumfrequency.html language=enus -->
## TOPIC 00022: RFmxVNA_CalkitManagerCalkitCalibrationElementSetMaximumFrequency

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementsetmaximumfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementsetmaximumfrequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementSetMaximumFrequency

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetMaximumFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 maximumFrequency);

#### Purpose

Sets the Maximum Frequency of the Calibration Element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| maximumFrequency | float64 | Specifies the Maximum Frequency of the Calibration Element. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementsetminimumfrequency.html language=enus -->
## TOPIC 00023: RFmxVNA_CalkitManagerCalkitCalibrationElementSetMinimumFrequency

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementsetminimumfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementsetminimumfrequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementSetMinimumFrequency

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetMinimumFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 minimumFrequency);

#### Purpose

Sets the Minimum Frequency of the Calibration Element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| minimumFrequency | float64 | Specifies the Minimum Frequency of the Calibration Element. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementsetportconnectors.html language=enus -->
## TOPIC 00024: RFmxVNA_CalkitManagerCalkitCalibrationElementSetPortConnectors

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementsetportconnectors.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementsetportconnectors.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementSetPortConnectors

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetPortConnectors (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char connectorIDs[],
 int32 arraySize);

#### Purpose

Defines the connectors of the Calibration Element by providing an array of Connector IDs where the 1st array element refers to the connector of the 1st port of the Calibration element. The array size has to be equal to the number of ports of the Calibration Element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| connectorIDs | char[] | Specifies the array of Connectors associated with the Calibration Element. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementsetsparameterdefinition.html language=enus -->
## TOPIC 00025: RFmxVNA_CalkitManagerCalkitCalibrationElementSetSParameterDefinition

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementsetsparameterdefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementsetsparameterdefinition.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementSetSParameterDefinition

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetSParameterDefinition (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 sParameterDefinition);

#### Purpose

Defines the way how the S-Parameters of the Calibration Element are specified.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| sParameterDefinition | int32 | Specifies the S-Parameter definition of the Calibration Element. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementsettypes.html language=enus -->
## TOPIC 00026: RFmxVNA_CalkitManagerCalkitCalibrationElementSetTypes

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementsettypes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementsettypes.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementSetTypes

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetTypes (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 calibrationElementTypes[],
 int32 arraySize);

#### Purpose

Sets the type(s) of the Calibration Element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| calibrationElementTypes | int32[] | Specifies the type(s) of the Calibration Element. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergetfrequency.html language=enus -->
## TOPIC 00027: RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetFrequency

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergetfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergetfrequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetFrequency

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 frequency[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the frequency array for the S-Parameter definition of the Calibration Element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| frequency | float64[] | Returns the frequency array for the S-Parameter definition of the Calibration Element. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets11.html language=enus -->
## TOPIC 00028: RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS11

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets11.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets11.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS11

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS11 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 NIComplexDouble s11[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the S11 S-Parameter for the calibration element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| s11 | NIComplexDouble[] | Returns the S11 S-Parameter for the calibration element. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets12.html language=enus -->
## TOPIC 00029: RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS12

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets12.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets12.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS12

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS12 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 NIComplexDouble s12[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the S12 S-Parameter for the calibration element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| s12 | NIComplexDouble[] | Returns the S12 S-Parameter for the calibration element. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets21.html language=enus -->
## TOPIC 00030: RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS21

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets21.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets21.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS21

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS21 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 NIComplexDouble s21[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the S21 S-Parameter for the calibration element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| s21 | NIComplexDouble[] | Returns the S21 S-Parameter for the calibration element. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets22.html language=enus -->
## TOPIC 00031: RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS22

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets22.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitcalibrationelementsparametergets22.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS22

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS22 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 NIComplexDouble s22[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the S22 S-Parameter for the calibration element.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID. Example:"ckit::MyCkitID/calel::MyCalelID"You can use the RFmxVNA_CalkitManagerBuildCalkitCalibrationElementString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| s22 | NIComplexDouble[] | Returns the S22 S-Parameter for the calibration element. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitconnectorgetdescription.html language=enus -->
## TOPIC 00032: RFmxVNA_CalkitManagerCalkitConnectorGetDescription

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitconnectorgetdescription.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitconnectorgetdescription.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitConnectorGetDescription

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetDescription (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 arraySize,
 char description[]);

#### Purpose

Returns the description of a Connector of a specific Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example:"ckit::MyCkitID/conn::MyConnID"You can use the RFmxVNA_CalkitManagerBuildCalkitConnectorString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| description | char[] |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitconnectorgetimpedance.html language=enus -->
## TOPIC 00033: RFmxVNA_CalkitManagerCalkitConnectorGetImpedance

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitconnectorgetimpedance.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitconnectorgetimpedance.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitConnectorGetImpedance

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetImpedance (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64* impedance);

#### Purpose

Returns the Impedance of a Connector of a specific Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example:"ckit::MyCkitID/conn::MyConnID"You can use the RFmxVNA_CalkitManagerBuildCalkitConnectorString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| impedance | float64* | Returns the Impedance of a Connector of a specific Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitconnectorgetmaximumfrequency.html language=enus -->
## TOPIC 00034: RFmxVNA_CalkitManagerCalkitConnectorGetMaximumFrequency

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitconnectorgetmaximumfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitconnectorgetmaximumfrequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitConnectorGetMaximumFrequency

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetMaximumFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64* maximumFrequency);

#### Purpose

Returns the Maximum Frequency of a Connector of a specific Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example:"ckit::MyCkitID/conn::MyConnID"You can use the RFmxVNA_CalkitManagerBuildCalkitConnectorString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| maximumFrequency | float64* | Returns the Maximum Frequency of a Connector of a specific Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitconnectorgetminimumfrequency.html language=enus -->
## TOPIC 00035: RFmxVNA_CalkitManagerCalkitConnectorGetMinimumFrequency

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitconnectorgetminimumfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitconnectorgetminimumfrequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitConnectorGetMinimumFrequency

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetMinimumFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64* minimumFrequency);

#### Purpose

Returns the Minimum Frequency of a Connector of a specific Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example:"ckit::MyCkitID/conn::MyConnID"You can use the RFmxVNA_CalkitManagerBuildCalkitConnectorString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| minimumFrequency | float64* | Returns the Minimum Frequency of a Connector of a specific Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitconnectorsetdescription.html language=enus -->
## TOPIC 00036: RFmxVNA_CalkitManagerCalkitConnectorSetDescription

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitconnectorsetdescription.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitconnectorsetdescription.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitConnectorSetDescription

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetDescription (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char description[]);

#### Purpose

Sets the description for a Connector of a specific Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example:"ckit::MyCkitID/conn::MyConnID"You can use the RFmxVNA_CalkitManagerBuildCalkitConnectorString function to build the selector string. |
| description | char[] | Specifies the description for a Connector of a specific Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitconnectorsetmaximumfrequency.html language=enus -->
## TOPIC 00037: RFmxVNA_CalkitManagerCalkitConnectorSetMaximumFrequency

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitconnectorsetmaximumfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitconnectorsetmaximumfrequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitConnectorSetMaximumFrequency

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetMaximumFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 maximumFrequency);

#### Purpose

Sets the Maximum Frequency of a Connector of a specific Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example:"ckit::MyCkitID/conn::MyConnID"You can use the RFmxVNA_CalkitManagerBuildCalkitConnectorString function to build the selector string. |
| maximumFrequency | float64 | Specifies the Maximum Frequency of a Connector of a specific Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitconnectorsetminimumfrequency.html language=enus -->
## TOPIC 00038: RFmxVNA_CalkitManagerCalkitConnectorSetMinimumFrequency

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitconnectorsetminimumfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitconnectorsetminimumfrequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitConnectorSetMinimumFrequency

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetMinimumFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 minimumFrequency);

#### Purpose

Sets the Minimum Frequency of a Connector of a specific Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example:"ckit::MyCkitID/conn::MyConnID"You can use the RFmxVNA_CalkitManagerBuildCalkitConnectorString function to build the selector string. |
| minimumFrequency | float64 | Specifies the Minimum Frequency of a Connector of a specific Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitconnectorsettype.html language=enus -->
## TOPIC 00039: RFmxVNA_CalkitManagerCalkitConnectorSetType

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitconnectorsettype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitconnectorsettype.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitConnectorSetType

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char connectorType[]);

#### Purpose

Sets the Type of a Connector of a specific Calkit. Connector type is a user defined string (for example 'SMA', '1.8mm', etc.).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example:"ckit::MyCkitID/conn::MyConnID"You can use the RFmxVNA_CalkitManagerBuildCalkitConnectorString function to build the selector string. |
| connectorType | char[] | Specifies the Type of a Connector of a specific Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitgetcalibrationelementids.html language=enus -->
## TOPIC 00040: RFmxVNA_CalkitManagerCalkitGetCalibrationElementIDs

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitgetcalibrationelementids.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitgetcalibrationelementids.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitGetCalibrationElementIDs

int32 __stdcall RFmxVNA_CalkitManagerCalkitGetCalibrationElementIDs (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 arraySize,
 char calibrationElementIDs[]);

#### Purpose

Returns a list of Calibration Element IDs of all Calibration Elements of the Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies a selector string comprising of the Calkit ID. Example:"ckit::MyCkitID"You can use the RFmxVNA_CalkitManagerBuildCalkitString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. Set the <strong>arraySize</strong> parameter to 0 to get the size of all the arrays in the <strong>actualArraySize</strong> parameter. |
| calibrationElementIDs | char[] | Returns the list of Calibration Element IDs of all Calibration Elements of the Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitgetconnectorids.html language=enus -->
## TOPIC 00041: RFmxVNA_CalkitManagerCalkitGetConnectorIDs

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitgetconnectorids.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitgetconnectorids.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitGetConnectorIDs

int32 __stdcall RFmxVNA_CalkitManagerCalkitGetConnectorIDs (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 arraySize,
 char connectorIDs[]);

#### Purpose

Returns the list of Connector IDs for all connectors in the Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies a selector string comprising of the Calkit ID. Example:"ckit::MyCkitID"You can use the RFmxVNA_CalkitManagerBuildCalkitString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. Set the <strong>arraySize</strong> parameter to 0 to get the size of all the arrays in the <strong>actualArraySize</strong> parameter. |
| connectorIDs | char[] | Returns the list of Connector IDs for all connectors in the Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercalkitremoveconnector.html language=enus -->
## TOPIC 00042: RFmxVNA_CalkitManagerCalkitRemoveConnector

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercalkitremoveconnector.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercalkitremoveconnector.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCalkitRemoveConnector

int32 __stdcall RFmxVNA_CalkitManagerCalkitRemoveConnector (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char connectorID[]);

#### Purpose

Removes a Connector element from the Calkit.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies a selector string comprising of the Calkit ID. Example:"ckit::MyCkitID"You can use the RFmxVNA_CalkitManagerBuildCalkitString function to build the selector string. |
| connectorID | char[] | Specifies the ID of the Connector within the Calkit. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagercreatecalkit.html language=enus -->
## TOPIC 00043: RFmxVNA_CalkitManagerCreateCalkit

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagercreatecalkit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagercreatecalkit.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerCreateCalkit

int32 __stdcall RFmxVNA_CalkitManagerCreateCalkit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char calkitID[]);

#### Purpose

Creates a new empty Calkit with the user defined Calkit ID in Calkit Manager. The user defined Calkit ID has to be unique among all Calkits in Calkit Manager.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calkitID | char[] | Specifies the ID for the Calkit in Calkit Manager. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calkitmanagervalidatecalkit.html language=enus -->
## TOPIC 00044: RFmxVNA_CalkitManagerValidateCalkit

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calkitmanagervalidatecalkit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calkitmanagervalidatecalkit.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalkitManagerValidateCalkit

int32 __stdcall RFmxVNA_CalkitManagerValidateCalkit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char calkitID[]);

#### Purpose

Validates the consistency of a Calkit definition and returns the status of the validation.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calkitID | char[] | Specifies the ID for the Calkit in Calkit Manager. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calsetgetfrequencygrid.html language=enus -->
## TOPIC 00045: RFmxVNA_CalsetGetFrequencyGrid

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calsetgetfrequencygrid.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calsetgetfrequencygrid.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalsetGetFrequencyGrid

int32 __stdcall RFmxVNA_CalsetGetFrequencyGrid (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char calsetName[],
 int32 errorTermIdentifier,
 float64 frequencyGrid[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the calibration frequency grid from either the default calset of the specified signal or a named calset accessible across all signals. 
Behaviors for different combinations of Calset Name and Signal Name strings are as follows:

- Calset Name is "" (empty string): RFmx returns the calibration frequency grid from the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx returns the calibration frequency grid from the named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calsetName | char[] | Reserved for future use. |
| errorTermIdentifier | int32 | Specifies the type of error term in the calset. The error term can take the following values: Directivity Directivity measured at Measurement Port (Source Port ignored). Source Match Source Match measured at Measurement Port (Source Port ignored). Reflection Tracking Reflection Tracking measured at Measurement Port (Source Port ignored). Transmission Tracking Transmission Tracking measured at Measurement Port with Source Port being the source port. Load Match Load Match measured at Measurement Port with Source Port being the source port. K K measured at Measurement Port (Source Port ignored). alpha alpha measured at Measurement Port (Source Port ignored). beta beta measured at Measurement Port (Source Port ignored). gamma gamma measured at Measurement Port (Source Port ignored). delta delta measured at Measurement Port (Source Port ignored). Switch Term Switch term measured at Measurement Port (Source Port ignored). The error term K, alpha, beta, gamma, and delta describe the relation of the outgoing and incident waves at the calibration plane (waves a and b) and the waves measured at VNA reference and measurement receiver (waves r and s) by the following matrix equation: + + + ++ + ¦ a ¦ ¦ alpha beta ¦¦ r ¦ ¦ ¦ = K * ¦ ¦¦ ¦ ¦ b ¦ ¦ gamma delta ¦¦ s ¦ + + + ++ + , where alpha, beta, gamma, and delta represent the complex elements of a transmission matrix and K represents a complex scaling factor. |
| arraySize | int32 | Specifies the size of the array. Set the <strong>arraySize</strong> parameter to 0 to get the size of all the arrays in the <strong>actualArraySize</strong> parameter. |
| Output |  |  |
| Name | Type | Description |
| frequencyGrid | float64[] | Returns the calibration frequency grid from the calset. This value is expressed in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the <strong>arraySize</strong> parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_calsetloadfromfile.html language=enus -->
## TOPIC 00046: RFmxVNA_CalsetLoadFromFile

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_calsetloadfromfile.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_calsetloadfromfile.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_CalsetLoadFromFile

int32 __stdcall RFmxVNA_CalsetLoadFromFile (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char calsetName[],
 char calsetFilePath[]);

#### Purpose

Loads calset from a calset file (*.ncst), either to the default calset of the specified signal or to a named calset accessible across all signals. 
Behaviors for different combinations of Calset Name and Signal Name strings are as follows:

- Calset Name is "" (empty string): RFmx loads calset from file to the default calset of the signal instance specified in the Selector String and selects the default calset as active calset for the signal. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx loads calset from file to a named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Passes a reference of your RFmx session to the next function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| calsetName | char[] | Reserved for future use. |
| calsetFilePath | char[] | Specifies the complete path to the file with .ncst extension to which the calset is to be saved. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_clearallnamedresults.html language=enus -->
## TOPIC 00047: RFmxVNA_ClearAllNamedResults

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_clearallnamedresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_clearallnamedresults.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_ClearAllNamedResults

int32 __stdcall RFmxVNA_ClearAllNamedResults (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears all results for the signal that you specify in the Selector String parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxVNA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_clearcalset.html language=enus -->
## TOPIC 00048: RFmxVNA_ClearCalset

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_clearcalset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_clearcalset.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_ClearCalset

int32 __stdcall RFmxVNA_ClearCalset (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char calsetName[]);

#### Purpose

Clears either the default calset of the specified signal or a named calset accessible across all signals. 
Behaviors for different combinations of Calset Name and Signal Name strings are as follows:

- Calset Name is "" (empty string): RFmx clears the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx clears the named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxVNA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| calsetName | char[] | Reserved for future use. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_clearnamedresult.html language=enus -->
## TOPIC 00049: RFmxVNA_ClearNamedResult

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_clearnamedresult.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_clearnamedresult.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_ClearNamedResult

int32 __stdcall RFmxVNA_ClearNamedResult (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears a result instance specified by the result name in the Selector String parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxVNA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_geterrorstring.html language=enus -->
## TOPIC 00050: RFmxVNA_GetErrorString

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_geterrorstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_geterrorstring.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_GetErrorString

int32 __stdcall RFmxVNA_GetErrorString (niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[]);

#### Purpose

Converts a status code returned by an RFmxVNA function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter. 
 

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For **Example**, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. 
 

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. If a valid session handle is passed, the last error stored in that session is retrieved. You can pass NULL to retrieve the last error stored in the current execution thread. |
| errorCode | int32* | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescriptionBufferSize | int32 | Passes the number of bytes in the char array you specify in the errorDescription parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize – 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string. The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_initialize.html language=enus -->
## TOPIC 00051: rfmxvna_Initialize

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_initialize.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_Initialize

int32 __stdcall RFmxVNA_Initialize (char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession);

#### Purpose

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Initialize](/csh?topicname=rfmxinstrcvi/) function.

[IMAGE alt='image' src='note.gif'] Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug.

- On a 64-bit Windows, SFP debug can be enabled/disabled from either the RFmx Soft Front Panel, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility.
- On a 32-bit Windows, SFP debug can be enabled/disabled from RFSA Soft Front Panel or the RFmx Debug Configuration Utility.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| resourceName | char[] | Specifies the resource name of the device to initialize. The following table shows examples of how to specify the resource name. Example # Device Type Syntax 1 myRFmxDevice RFmx device, device name is "myRFmxDevice" 2 myLogicalName IVI logical name or virtual instrument, name is "myLogicalName" For NI-DAQmx devices, the syntax is the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot2. You can rename an NI-DAQmx device by right-clicking the name in MAX, selecting Rename from the pull-down menu, and entering a new name. You can also pass the name of an IVI logical name configured with the IVI Configuration utility. For additional information about IVI, refer to the IVI section of the Measurement & Automation Explorer Help. |
| Example # | Device Type | Syntax |
| 1 | myRFmxDevice | RFmx device, device name is "myRFmxDevice" |
| 2 | myLogicalName | IVI logical name or virtual instrument, name is "myLogicalName" |
| optionString | char[] | Sets the initial value of certain attributes for the session. The following attributes are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about attributes used in this parameter, refer to the NI RF Vector Signal Analyzers Help. The format of this string is "AttributeName=Value", where AttributeName is the name of the attribute and Value is the value to which the attribute is set. For example, you can simulate an NI 5663E using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple attributes, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx uses yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. Note To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |
|  | Note To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |  |
| isNewSession | int32* | Returns RFMXVNA_VAL_TRUE if the function created a new session, or RFMXVNA_VAL_FALSE if the function returned a reference to an existing session. |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Identifies your instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_initiate.html language=enus -->
## TOPIC 00052: RFmxVNA_Initiate

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_initiate.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_Initiate

int32 __stdcall RFmxVNA_Initiate (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[]);

#### Purpose

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the [RFmxVNA_WaitforMeasurementComplete](/csh?topicname=rfmxvnacvi/cvirfmxvna_waitformeasurementcomplete.html) function or [RFmxVNA_CheckMeasurementStatus](/csh?topicname=rfmxvnacvi/cvirfmxvna_checkmeasurementstatus.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxVNA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"""result::r1""r1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_markercfgdatasource.html language=enus -->
## TOPIC 00053: RFmxVNA_MarkerCfgDataSource

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_markercfgdatasource.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_markercfgdatasource.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_MarkerCfgDataSource

int32 __stdcall RFmxVNA_MarkerCfgDataSource (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char dataSource[]);

#### Purpose

Configures the data source on which marker operations are performed. 
Use "marker<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. is obtained from the RFmxInstr_InitializeNIRFSA function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used.Example:"marker0""signal::sig1/marker0"You can use the RFmxVNA_Build_Marker_String_ function to build the selector string. |
| dataSource | char[] | Specifies the measurement data on which markers are placed. If you want to place markers on data from SParams measurement data, then specify this parameter as "sparam<n>". Similarly, if you want to place markers on data from waves measurement, then specify this parameter as "wave<n>". |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_markercfgpeaksearchexcursion.html language=enus -->
## TOPIC 00054: RFmxVNA_MarkerCfgPeakSearchExcursion

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_markercfgpeaksearchexcursion.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_markercfgpeaksearchexcursion.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_MarkerCfgPeakSearchExcursion

int32 __stdcall RFmxVNA_MarkerCfgPeakSearchExcursion (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 peakExcursionEnabled,
 float64 peakExcursion);

#### Purpose

Configures the peak-search excursion. When peak-excursion is enabled, peak search using Marker Search function finds a peak such that the data value rises and falls around the peak by at least the specified peak excursion value. 
Use "marker<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. is obtained from the RFmxInstr_InitializeNIRFSA function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used.Example:"marker0""signal::sig1/marker0"You can use the RFmxVNA_Build_Marker_String_ function to build the selector string. |
| peakExcursionEnabled | int32 | Specifies whether Marker_SearchVI finds a peak such that the data value rises and falls around the peak by atleast the specified peak excursion value or finds a peak without considering any peak excursion constraint. |
| peakExcursion | float64 | Specifies the peak excursion value that Marker_SearchVI uses to find a peak such that the data value rises and falls around the peak by atleast the specified peak excursion value. The threshold is expressed in the same units as the source data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_markercfgpeaksearchthreshold.html language=enus -->
## TOPIC 00055: RFmxVNA_MarkerCfgPeakSearchThreshold

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_markercfgpeaksearchthreshold.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_markercfgpeaksearchthreshold.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_MarkerCfgPeakSearchThreshold

int32 __stdcall RFmxVNA_MarkerCfgPeakSearchThreshold (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 thresholdEnabled,
 float64 threshold);

#### Purpose

Configures the peak-search threshold. When peak-thresholding is enabled, Marker Search function in peak search mode finds the peaks that exceed this value and discards all other peaks. 
Use "marker<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. is obtained from the RFmxInstr_InitializeNIRFSA function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used.Example:"marker0""signal::sig1/marker0"You can use the RFmxVNA_Build_Marker_String_ function to build the selector string. |
| thresholdEnabled | int32 | Specifies whether Marker_SearchVI finds a peak above specified Threshold or finds a peak without considering any Threshold constraint. |
| threshold | float64 | Specifies the threshold value that a valid peak must exceed when you use Marker_SearchVI to find peaks. The threshold is expressed in the same units as the source data. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_markerfetchx.html language=enus -->
## TOPIC 00056: RFmxVNA_MarkerFetchX

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_markerfetchx.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_markerfetchx.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_MarkerFetchX

int32 __stdcall RFmxVNA_MarkerFetchX (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64* markerX);

#### Purpose

Returns the X value of the marker. X value of the **delta** marker is relative to its reference marker.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. is obtained from the RFmxInstr_InitializeNIRFSA function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name and marker number. If you do not specify the signal name, the default signal instance is used.Example:"marker0""signal::sig1/marker0""result::r1/marker0""signal::sig1/result::r1/marker0"You can use the RFmxVNA_Build_Marker_String_ function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| markerX | float64* | Returns the marker X value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_markersearch.html language=enus -->
## TOPIC 00057: RFmxVNA_MarkerSearch

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_markersearch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_markersearch.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_MarkerSearch

int32 __stdcall RFmxVNA_MarkerSearch (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 searchMode);

#### Purpose

Performs the marker search operation that you specify using Search Mode.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. is obtained from the RFmxInstr_InitializeNIRFSA function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name and marker number. If you do not specify the signal name, the default signal instance is used.Example:"marker0""signal::sig1/marker0""result::r1/marker0""signal::sig1/result::r1/marker0"You can use the RFmxVNA_Build_Marker_String_ function to build the selector string. |
| searchMode | int32 | Specifies the search-target. If search is successful, RFmx updates the marker X and Y values to the location at which search-target is found. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_selectactivecalset.html language=enus -->
## TOPIC 00058: RFmxVNA_SelectActiveCalset

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_selectactivecalset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_selectactivecalset.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_SelectActiveCalset

int32 __stdcall RFmxVNA_SelectActiveCalset (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char calsetName[],
 int32 restoreConfiguration);

#### Purpose

Selects either the default calset of the specified signal or a named calset accessible across all signals as active calset for the specified signal. 
Behaviors for different combinations of Calset Name and Signal Name strings specified are as follows: 
You can use [RFmxVNA_GetAllCalsetNames](/csh?topicname=rfmxvnacvi/cvirfmxvna_getallcalsetnames.html) function to get the list of available named calsets.

- Calset Name is "" (empty string): RFmx selects the default calset as the active calset for the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: RFmx selects the named calset as the active calset for the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calsetName | char[] | Specifies the name of the calset. |
| restoreConfiguration | int32 | Specifies whether the stimulus settings from the specified calset should be applied to the signal. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_selectmeasurements.html language=enus -->
## TOPIC 00059: RFmxVNA_SelectMeasurements

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_selectmeasurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_selectmeasurements.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_SelectMeasurements

int32 __stdcall RFmxVNA_SelectMeasurements (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 uInt32 measurements,
 int32 enableAllTraces);

#### Purpose

Enables all the measurements that you specify in the Measurements parameter and disables all other measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxVNA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| measurements | uInt32 | Specifies the measurement to perform. You can specify one or more of the following measurements. RFMXVNA_VAL_SPARAMS (1) Enables S-Parameter measurement. RFMXVNA_VAL_WAVES (2) Enables Wave measurement. |
| RFMXVNA_VAL_SPARAMS (1) | Enables S-Parameter measurement. |  |
| RFMXVNA_VAL_WAVES (2) | Enables Wave measurement. |  |
| enableAllTraces | int32 | Specifies whether to enable all traces for the selected measurement. The default value is FALSE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00060: RFmxVNA_SendSoftwareEdgeTrigger

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_sendsoftwareedgetrigger.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_SendSoftwareEdgeTrigger

int32 __stdcall RFmxVNA_SendSoftwareEdgeTrigger (niRFmxInstrHandle instrumentHandle);

#### Purpose

Sends a trigger to the device when you set [RFMXVNA_ATTR_TRIGGER_TYPE](/csh?topicname=rfmxvnacvi/rfmxvna_attr_trigger_type.html) to Software and the device is waiting for the trigger to be sent.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxVNA_Initialize function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_sparamscfgsparameter.html language=enus -->
## TOPIC 00061: RFmxVNA_SParamsCfgSParameter

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_sparamscfgsparameter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_sparamscfgsparameter.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_SParamsCfgSParameter

int32 __stdcall RFmxVNA_SParamsCfgSParameter (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char sParameter[]);

#### Purpose

Configures the S-Parameter to be measured in format S<*receiver port number*><*source port number*> 
Use "sparam<*n*>" as the selector string to configure this function. 
This function sets [RFMXVNA_ATTR_SPARAMS_SOURCE_PORT](/csh?topicname=rfmxvnacvi/rfmxvna_attr_sparams_source_port.html) and [RFMXVNA_ATTR_SPARAMS_RECEIVER_PORT](/csh?topicname=rfmxvnacvi/rfmxvna_attr_sparams_receiver_port.html) attributes. 
**Supporteddevices**: NI PXIe-5633

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxVNA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"sparam0""signal::sig1/sparam0""result::r1/sparam0""signal::sig1/result::r1/sparam0"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |
| sParameter | char[] | Specifies the S-Parameter to be measured. Supported devices: NI-5663 |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_wavesfetchydata.html language=enus -->
## TOPIC 00062: RFmxVNA_WavesFetchYData

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_wavesfetchydata.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_wavesfetchydata.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_WavesFetchYData

int32 __stdcall RFmxVNA_WavesFetchYData (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 Y1[],
 float32 Y2[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the wave data for all [RFMXVNA_ATTR_WAVES_FORMAT](/csh?topicname=rfmxvnacvi/rfmxvna_attr_waves_format.html) types. 
Use "wave<*n*>" as the selector string to read results from this function. 
 For different [RFMXVNA_ATTR_WAVES_FORMAT](/csh?topicname=rfmxvnacvi/rfmxvna_attr_waves_format.html), the data is returned as follows:

| RFMXVNA_ATTR_WAVES_FORMAT | Y1 | Y2 |
| --- | --- | --- |
| Magnitude (0) | Magnitude of the wave data | Empty array |
| Phase (1) | Phase of the wave data | Empty array |
| Complex (2) | Real part of the complex wave data | Imaginary part of the complex wave data |
| SWR (3) | Standing wave ratio computed from the wave data | Empty array |
| Smith Impedance (4) | Real part of the complex impedance computed from the wave data | Imaginary part of the complex impedance computed from the wave data |
| Smith Admittance (5) | Real part of the complex admittance computed from the wave data | Imaginary part of the complex admittance computed from the wave data |
| Polar (6) | Magnitude of the wave data | Phase of the wave data |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxVNA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"sparam0""signal::sig1/sparam0""result::r1/sparam0""signal::sig1/result::r1/sparam0"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| Y1 | float32[] | Returns the measured wave real data array corresponding to the RFMXVNA_ATTR_FREQUENCY_LIST. |
| Y2 | float32[] | Returns the measured wave real data array corresponding to the RFMXVNA_ATTR_FREQUENCY_LIST. For different RFMXVNA_ATTR_WAVES_FORMAT, the data is returned as follows: Waves Format Y1 Y2 Magnitude (0) Magnitude of the wave data Empty array Phase (1) Phase of the wave data Empty array Complex (2) Real part of the complex wave data Imaginary part of the complex wave data SWR (3) Standing wave ratio computed from the wave data Empty array Smith Impedance (4) Real part of the complex impedance computed from the wave data Imaginary part of the complex impedance computed from the wave data Smith Admittance (5) Real part of the complex admittance computed from the wave data Imaginary part of the complex admittance computed from the wave data Polar (6) Magnitude of the wave data Phase of the wave data |
| Waves Format | Y1 | Y2 |
| Magnitude (0) | Magnitude of the wave data | Empty array |
| Phase (1) | Phase of the wave data | Empty array |
| Complex (2) | Real part of the complex wave data | Imaginary part of the complex wave data |
| SWR (3) | Standing wave ratio computed from the wave data | Empty array |
| Smith Impedance (4) | Real part of the complex impedance computed from the wave data | Imaginary part of the complex impedance computed from the wave data |
| Smith Admittance (5) | Real part of the complex admittance computed from the wave data | Imaginary part of the complex admittance computed from the wave data |
| Polar (6) | Magnitude of the wave data | Phase of the wave data |
| actualArraySize | int32* | Returns the actual size of the array. If you set the arraySize parameter to 0, it returns the required array size. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvirfmxvna_wavesgetwave.html language=enus -->
## TOPIC 00063: RFmxVNA_WavesGetWave

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvirfmxvna_wavesgetwave.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvirfmxvna_wavesgetwave.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmxVNA_WavesGetWave

int32 __stdcall RFmxVNA_WavesGetWave (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 arraySize,
 char wave[]);

#### Purpose

Returns the wave being measured in format a<*receiver port number*><*source port number*> or b<*receiver port number*><*source port number*>, where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver.
 
Use "wave<*n*>" as the selector string for this function. 
**Supporteddevices**: NI PXIe-5633

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and wave number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used."wave0""signal::sig1/wave0""result::r1/wave0""signal::sig1/result::r1/wave0"You can use the RFmxVNA_BuildWaveString function to build the selector string. |
| arraySize | int32 | Specifies the size of the array. |
| wave | char[] | Specifies the wave to be measured. supporteddevices: NI-5663 |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxVNA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvivnaattributestitle.html language=enus -->
## TOPIC 00064: RFmx VNA Attributes

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvivnaattributestitle.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvivnaattributestitle.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmx VNA Attributes

Contains the RFmx VNA attributes to access configuration options for the VNA measurements.

<!--NI_TOPIC bundle=rfmx-vna-cvi path=cvivnafunctionstitle.html language=enus -->
## TOPIC 00065: RFmx VNA Functions

- bundle_id: `rfmx-vna-cvi`
- source_path: `cvivnafunctionstitle.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/cvivnafunctionstitle.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFmx VNA Functions

Contains the RFmx VNA functions to perform the VNA measurements.

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_auto_if_bandwidth_scaling_enabled.html language=enus -->
## TOPIC 00066: RFMXVNA_ATTR_AUTO_IF_BANDWIDTH_SCALING_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_auto_if_bandwidth_scaling_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_auto_if_bandwidth_scaling_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_AUTO_IF_BANDWIDTH_SCALING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether IF Bandwidth is automatically scaled down to account for the increased VNA receiver noise at low frequencies. Consider disabling automatic IF Bandwidth scaling by setting this attribute to False if you want faster measurement speed but with higher measurment noise at low frequencies. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_AUTO_IF_BANDWIDTH_SCALING_ENABLED_TRUE. Get Function: RFmxVNA_GetAutoIFBandwidthScalingEnabled Set Function: RFmxVNA_SetAutoIFBandwidthScalingEnabled |
| Values: | RFMXVNA_VAL_AUTO_IF_BANDWIDTH_SCALING_ENABLED_FALSE (0) Disables automatic IF Bandwidth scaling that compensates for the increased VNA receiver noise at low frequencies. RFMXVNA_VAL_AUTO_IF_BANDWIDTH_SCALING_ENABLED_TRUE (1) Enables automatic IF Bandwidth scaling that compensates for the increased VNA receiver noise at low frequencies. |
| RFMXVNA_VAL_AUTO_IF_BANDWIDTH_SCALING_ENABLED_FALSE (0) | Disables automatic IF Bandwidth scaling that compensates for the increased VNA receiver noise at low frequencies. |
| RFMXVNA_VAL_AUTO_IF_BANDWIDTH_SCALING_ENABLED_TRUE (1) | Enables automatic IF Bandwidth scaling that compensates for the increased VNA receiver noise at low frequencies. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_averaging_count.html language=enus -->
## TOPIC 00067: RFMXVNA_ATTR_AVERAGING_COUNT

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_averaging_count.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the number of times each measurement is repeated and averaged-over. This attribute is used only when you set the RFMXVNA_ATTR_AVERAGING_ENABLED attribute to RFMXVNA_VAL_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxVNA_GetAveragingCount Set Function: RFmxVNA_SetAveragingCount |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_averaging_enabled.html language=enus -->
## TOPIC 00068: RFMXVNA_ATTR_AVERAGING_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_averaging_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether to enable measurement averaging. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_AVERAGING_ENABLED_FALSE. Get Function: RFmxVNA_GetAveragingEnabled Set Function: RFmxVNA_SetAveragingEnabled |
| Values: | RFMXVNA_VAL_AVERAGING_ENABLED_FALSE (0)Disables measurement averaging. RFMXVNA_VAL_AVERAGING_ENABLED_TRUE (1)Enables measurement averaging. You can set number of times each measurement is repeated and averaged-over using the RFMXVNA_ATTR_AVERAGING_COUNT attribute. |
| RFMXVNA_VAL_AVERAGING_ENABLED_FALSE (0) | Disables measurement averaging. |
| RFMXVNA_VAL_AVERAGING_ENABLED_TRUE (1) | Enables measurement averaging. You can set number of times each measurement is repeated and averaged-over using the RFMXVNA_ATTR_AVERAGING_COUNT attribute. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_correction_calibration_calkit_electronic_orientation.html language=enus -->
## TOPIC 00069: RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_ELECTRONIC_ORIENTATION

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_correction_calibration_calkit_electronic_orientation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_correction_calibration_calkit_electronic_orientation.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_ELECTRONIC_ORIENTATION

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies the orientation of the vCal fixture ports with respect to vCal ports. Use 'portA:portname, portB:portname' format to specify vCal orientation.When using NI-PXIe 5633 without an NI switch module, if vCal orientation is not specified, it is assumed to be 'portA:port1, portB:port2'.When using NI-PXIe 5633 with an NI switch module, you must set vCal orientation for all the specified Calibration Ports. The default value is an empty string. Get Function: RFmxVNA_GetCorrectionCalibrationCalkitElectronicOrientation Set Function: RFmxVNA_SetCorrectionCalibrationCalkitElectronicOrientation |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_correction_calibration_calkit_mechanical_name.html language=enus -->
## TOPIC 00070: RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_MECHANICAL_NAME

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_correction_calibration_calkit_mechanical_name.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_correction_calibration_calkit_mechanical_name.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_MECHANICAL_NAME

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies the name of the mechanical calkit used for calibration. This attribute is used only when you set the RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_TYPE attribute to RFMXVNA_VAL_CORRECTION_CALIBRATION_CALKIT_TYPE_MECHANICAL. You must set a valid calkit name. Use _RFmxVNACalkitManagerGetCalkitIDs function to get list of available mechanical calkits. Currently, RFmxVNA only supports the use of same calkit type and same calkit name for all calibration ports in a guided calibration procedure.Use 'port::all' as the selector string to specify the same calkit name for all VNA ports. Use 'port::(portname)' as the selector string to read this attribute for a specific VNA port. The default value is an empty string. Get Function: RFmxVNA_GetCorrectionCalibrationCalkitMechanicalName Set Function: RFmxVNA_SetCorrectionCalibrationCalkitMechanicalName |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_correction_calibration_ports.html language=enus -->
## TOPIC 00071: RFMXVNA_ATTR_CORRECTION_CALIBRATION_PORTS

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_correction_calibration_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_correction_calibration_ports.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_CORRECTION_CALIBRATION_PORTS

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies the ports that are selected for calibration. Use comma-separated list of ports to specify multiple ports. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is an empty string. Get Function: RFmxVNA_GetCorrectionCalibrationPorts Set Function: RFmxVNA_SetCorrectionCalibrationPorts |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_correction_calibration_step_description.html language=enus -->
## TOPIC 00072: RFMXVNA_ATTR_CORRECTION_CALIBRATION_STEP_DESCRIPTION

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_correction_calibration_step_description.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_correction_calibration_step_description.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_CORRECTION_CALIBRATION_STEP_DESCRIPTION

| Data Type: | char [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxVNA_GetAttributeString |
| Description: | Returns the description for the specified calibration step. You can use the description for each calibration step to determine which mechanical cal standard or electronic calkit module should you connect to which VNA port(s). Use 'calstep(n)' as the selector string to read this attribute.You must configure all the calibration related attributes and call _RFmxVNACalibrationInitiate function before you query this attribute. Get Function: RFmxVNA_GetCorrectionCalibrationStepDescription |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_correction_calibration_thru_coax_delay.html language=enus -->
## TOPIC 00073: RFMXVNA_ATTR_CORRECTION_CALIBRATION_THRU_COAX_DELAY

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_correction_calibration_thru_coax_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_correction_calibration_thru_coax_delay.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_CORRECTION_CALIBRATION_THRU_COAX_DELAY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the delay of the Thru mechanical standard when RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_TYPE attribute is set to RFMXVNA_VAL_CORRECTION_CALIBRATION_CALKIT_TYPE_MECHANICAL and Thru Method attribute is set to Auto or Undefined Thru. This value is expressed in seconds. Use this attribute to specify an approximate delay value of an unknown-thru cal standard. Measurement uses this value to eliminate the uncertainty of Â± 180 degrees in the estimated phase response of the Thru.If you set this attribute to 0, the VNA automatically determines the delay of the Thru. You only need to set this attribute to an approximate non-zero delay value when Max Frequency Step Size ) 1/(2 x Thru Delay). Here, Frequency Step Size refers to the difference between 2 consecutive frequency points in the set of frequencies sorted in ascending order. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0 s. Get Function: RFmxVNA_GetCorrectionCalibrationThruCoaxDelay Set Function: RFmxVNA_SetCorrectionCalibrationThruCoaxDelay |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_correction_port_extension_delay.html language=enus -->
## TOPIC 00074: RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_correction_port_extension_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_correction_port_extension_delay.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the port extension electrical delay. This value is expressed in seconds. This attribute is used only when you set the RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED attribute to RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_ENABLED_TRUE. Use 'port::(portname)' as the selector string to configure or read this attribute for a specific VNA port. Use 'port::all' to configure the same delay value for all VNA ports. The default value is 0 s. Get Function: RFmxVNA_GetCorrectionPortExtensionDelay Set Function: RFmxVNA_SetCorrectionPortExtensionDelay |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_correction_port_extension_enabled.html language=enus -->
## TOPIC 00075: RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_correction_port_extension_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_correction_port_extension_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether to enable port extension. Use 'port::(portname)' as the selector string to configure or read this attribute for a specific VNA port. Use 'port::all' to configure for all VNA ports. The default value is RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_ENABLED_FALSE. Get Function: RFmxVNA_GetCorrectionPortExtensionEnabled Set Function: RFmxVNA_SetCorrectionPortExtensionEnabled |
| Values: | RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_ENABLED_FALSE (0)The measurement disables port extension. RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_ENABLED_TRUE (1)The measurement enables port extension. |
| RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_ENABLED_FALSE (0) | The measurement disables port extension. |
| RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_ENABLED_TRUE (1) | The measurement enables port extension. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_correction_port_subset_enabled.html language=enus -->
## TOPIC 00076: RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_correction_port_subset_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_correction_port_subset_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether to enable correction for a subset of ports for which calibration data is avaialble in the calset. This attribute is used only when you set the RFMXVNA_ATTR_CORRECTION_ENABLED attribute to RFMXVNA_VAL_CORRECTION_ENABLED_TRUE. Enable port subset, when calibration or loaded calset contains error correction terms for more ports than the number of ports in device under test (DUT), to achieve faster measurement speed by avoiding extra acquisitions. For example when performing error corrected measurement for a 1 port DUT using a 2-port VNA and a 2-port calset, generally VNA will acquire data by setting source to port1 first and then source as port2. In this case, setting this attribute to True and setting RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_PORTS attribute to port1, lets the VNA acquire data using source port as port1 and skips acquiring data with source port as port2. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_CORRECTION_PORT_SUBSET_ENABLED_FALSE. Get Function: RFmxVNA_GetCorrectionPortSubsetEnabled Set Function: RFmxVNA_SetCorrectionPortSubsetEnabled |
| Values: | RFMXVNA_VAL_CORRECTION_PORT_SUBSET_ENABLED_FALSE (0)The measurement disables port-subsetting for error correction. RFMXVNA_VAL_CORRECTION_PORT_SUBSET_ENABLED_TRUE (1)The measurement enabes port-subsetting for error correction. |
| RFMXVNA_VAL_CORRECTION_PORT_SUBSET_ENABLED_FALSE (0) | The measurement disables port-subsetting for error correction. |
| RFMXVNA_VAL_CORRECTION_PORT_SUBSET_ENABLED_TRUE (1) | The measurement enabes port-subsetting for error correction. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_digital_edge_trigger_edge.html language=enus -->
## TOPIC 00077: RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_digital_edge_trigger_edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_digital_edge_trigger_edge.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the edge of the digital-signal used to assert a digital edge trigger. This attribute is used only when you set the RFMXVNA_ATTR_TRIGGER_TYPE attribute to RFMXVNA_VAL_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_DIGITAL_EDGE_RISING_EDGE. Get Function: RFmxVNA_GetDigitalEdgeTriggerEdge Set Function: RFmxVNA_SetDigitalEdgeTriggerEdge |
| Values: | RFMXVNA_VAL_DIGITAL_EDGE_RISING_EDGE (0)The trigger asserts on the rising edge of the digital-signal. RFMXVNA_VAL_DIGITAL_EDGE_FALLING_EDGE (1)The trigger asserts on the falling edge of the digital-signal. |
| RFMXVNA_VAL_DIGITAL_EDGE_RISING_EDGE (0) | The trigger asserts on the rising edge of the digital-signal. |
| RFMXVNA_VAL_DIGITAL_EDGE_FALLING_EDGE (1) | The trigger asserts on the falling edge of the digital-signal. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_digital_edge_trigger_source.html language=enus -->
## TOPIC 00078: RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_digital_edge_trigger_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_digital_edge_trigger_source.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies the terminal name used as the source for asserting a digital edge trigger. This attribute is used only when you set the RFMXVNA_ATTR_TRIGGER_TYPE attribute to RFMXVNA_VAL_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default oof this attribute is '' (empty string). Get Function: RFmxVNA_GetDigitalEdgeTriggerSource Set Function: RFmxVNA_SetDigitalEdgeTriggerSource |
| Values: | RFMXVNA_VAL_PFI0_STR (PFI0)The trigger is received on PFI 0. RFMXVNA_VAL_PFI1_STR (PFI1)The trigger is received on PFI 1. RFMXVNA_VAL_PXI_TRIG0_STR (PXI_Trig0)The trigger is received on PXI trigger line 0. RFMXVNA_VAL_PXI_TRIG1_STR (PXI_Trig1)The trigger is received on PXI trigger line 1. RFMXVNA_VAL_PXI_TRIG2_STR (PXI_Trig2)The trigger is received on PXI trigger line 2. RFMXVNA_VAL_PXI_TRIG3_STR (PXI_Trig3)The trigger is received on PXI trigger line 3. RFMXVNA_VAL_PXI_TRIG4_STR (PXI_Trig4)The trigger is received on PXI trigger line 4. RFMXVNA_VAL_PXI_TRIG5_STR (PXI_Trig5)The trigger is received on PXI trigger line 5. RFMXVNA_VAL_PXI_TRIG6_STR (PXI_Trig6)The trigger is received on PXI trigger line 6. RFMXVNA_VAL_PXI_TRIG7_STR (PXI_Trig7)The trigger is received on PXI trigger line 7. RFMXVNA_VAL_PXI_STAR_STR (PXI_STAR)The trigger is received on the PXI star trigger line. Note that, currently, RFmxVNA does not support this trigger line. RFMXVNA_VAL_PXIE_DSTARB_STR (PXIe_DStarB)The trigger is received on the PXIe DStar B trigger line. |
| RFMXVNA_VAL_PFI0_STR (PFI0) | The trigger is received on PFI 0. |
| RFMXVNA_VAL_PFI1_STR (PFI1) | The trigger is received on PFI 1. |
| RFMXVNA_VAL_PXI_TRIG0_STR (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| RFMXVNA_VAL_PXI_TRIG1_STR (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| RFMXVNA_VAL_PXI_TRIG2_STR (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| RFMXVNA_VAL_PXI_TRIG3_STR (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| RFMXVNA_VAL_PXI_TRIG4_STR (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| RFMXVNA_VAL_PXI_TRIG5_STR (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| RFMXVNA_VAL_PXI_TRIG6_STR (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| RFMXVNA_VAL_PXI_TRIG7_STR (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| RFMXVNA_VAL_PXI_STAR_STR (PXI_STAR) | The trigger is received on the PXI star trigger line. Note that, currently, RFmxVNA does not support this trigger line. |
| RFMXVNA_VAL_PXIE_DSTARB_STR (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_frequency_list.html language=enus -->
## TOPIC 00079: RFMXVNA_ATTR_FREQUENCY_LIST

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_frequency_list.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_frequency_list.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_FREQUENCY_LIST

| Data Type: | float64 [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64ArrayRFmxVNA_GetAttributeF64Array |
| Description: | Specifies the frequency values for the configured measurements. The frequencies must be in ascending order and must not contain duplicates. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_LIST. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is an empty array. Get Function: RFmxVNA_GetFrequencyList Set Function: RFmxVNA_SetFrequencyList |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_if_bandwidth.html language=enus -->
## TOPIC 00080: RFMXVNA_ATTR_IF_BANDWIDTH

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_if_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_if_bandwidth.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_IF_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the digital IF filter bandwidth. This value is expressed in Hz. NI PXIe-5633 supports the following IF Bandwidths: 1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 100 kHz. Get Function: RFmxVNA_GetIFBandwidth Set Function: RFmxVNA_SetIFBandwidth |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_limited_configuration_change.html language=enus -->
## TOPIC 00081: RFMXVNA_ATTR_LIMITED_CONFIGURATION_CHANGE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_limited_configuration_change.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_limited_configuration_change.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_LIMITED_CONFIGURATION_CHANGE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the set of attributes that are considered by NI-RFmx in the locked signal configuration state. If your test system performs the same measurement repeatedly, enabling this attribute will help achieve faster measurements. When you set this attribute to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks.You can also use this attribute to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr attributes from a locked configuration.NI recommends you use this attribute in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this attribute to a value other than Disabled for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this attribute if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality attributes while testing each device under test. RFmx automatically optimizes that use case.Specify the named signal configuration you are setting this attribute in the Selector String input. The default value is RFMXVNA_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED. Get Function: RFmxVNA_GetLimitedConfigurationChange Set Function: RFmxVNA_SetLimitedConfigurationChange |
| Values: | RFMXVNA_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED (0)This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or RFmxVNA attributes will be applied during RFmx Commit. RFMXVNA_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE (1)Signal configuration and RFmxInstr configuration are locked after the first Commit or Initiate of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXVNA_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED (0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or RFmxVNA attributes will be applied during RFmx Commit. |
| RFMXVNA_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE (1) | Signal configuration and RFmxInstr configuration are locked after the first Commit or Initiate of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_number_of_segments.html language=enus -->
## TOPIC 00082: RFMXVNA_ATTR_NUMBER_OF_SEGMENTS

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_number_of_segments.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_number_of_segments.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_NUMBER_OF_SEGMENTS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the number of sweep segments. This attribute is used only when you set RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT If you increase this attribute value from N to N+K, then existing N segments are not affected but K new segments are added. If you reduce number of segments from N to N-K, then last K segments are deleted without affecting the remaining N-K segments. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxVNA_GetNumberOfSegments Set Function: RFmxVNA_SetNumberOfSegments |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_power_level.html language=enus -->
## TOPIC 00083: RFMXVNA_ATTR_POWER_LEVEL

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_power_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_power_level.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_POWER_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the power level for the VNA source port. This value is expressed in dBm. Use 'port::(portname)' as the selector string to configure or read this attribute for a specific VNA port. Use 'port::all' to configure same power level for all VNA ports. The default value is -10 dBm. Get Function: RFmxVNA_GetPowerLevel Set Function: RFmxVNA_SetPowerLevel |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_pulse_acquisition_delay.html language=enus -->
## TOPIC 00084: RFMXVNA_ATTR_PULSE_ACQUISITION_DELAY

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_pulse_acquisition_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_pulse_acquisition_delay.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_PULSE_ACQUISITION_DELAY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the delay in the start of the pulse acquisition relative to the pulse trigger. Pulse trigger can be internal or external. When you set RFMXVNA_ATTR_PULSE_TRIGGER_TYPE to RFMXVNA_VAL_PULSE_TRIGGER_TYPE_NONE then the VNA creates appropriate periodic pulse triggers internally. This attribute is used only when you set RFMXVNA_ATTR_PULSE_MODE_ENABLED attribute to RFMXVNA_VAL_PULSE_MODE_ENABLED_TRUE, Pulse Modulator Enabled attribute to RFMXVNA_VAL_PULSE_MODE_ENABLED_TRUE and RFMXVNA_ATTR_PULSE_ACQUISITION_AUTO attribute to RFMXVNA_VAL_PULSE_MODE_ENABLED_FALSE. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0 s. Get Function: RFmxVNA_GetPulseAcquisitionDelay Set Function: RFmxVNA_SetPulseAcquisitionDelay |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_pulse_acquisition_width.html language=enus -->
## TOPIC 00085: RFMXVNA_ATTR_PULSE_ACQUISITION_WIDTH

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_pulse_acquisition_width.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_pulse_acquisition_width.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_PULSE_ACQUISITION_WIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the acquisition-time per point for pulse measurements. This attribute is used only when you set RFMXVNA_ATTR_PULSE_MODE_ENABLED attribute to RFMXVNA_VAL_PULSE_MODE_ENABLED_TRUE, Pulse Modulator Enabled attribute to RFMXVNA_VAL_PULSE_MODE_ENABLED_TRUE and RFMXVNA_ATTR_PULSE_ACQUISITION_AUTO attribute to RFMXVNA_VAL_PULSE_MODE_ENABLED_FALSE. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0 s. Get Function: RFmxVNA_GetPulseAcquisitionWidth Set Function: RFmxVNA_SetPulseAcquisitionWidth |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_pulse_generator_delay.html language=enus -->
## TOPIC 00086: RFMXVNA_ATTR_PULSE_GENERATOR_DELAY

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_pulse_generator_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_pulse_generator_delay.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_PULSE_GENERATOR_DELAY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the delay between the pulse trigger and digital pulse generated by the selected Pulse Generator. You must set the value of the this attribute such that Delay + RFMXVNA_ATTR_PULSE_GENERATOR_WIDTH attribute does not exceed RFMXVNA_ATTR_PULSE_PERIOD attribute. This value is expressed in seconds. Use 'pulsegen(n)' as the selector string to configure or read this attribute. The default value is 0 s. Get Function: RFmxVNA_GetPulseGeneratorDelay Set Function: RFmxVNA_SetPulseGeneratorDelay |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_pulse_generator_enabled.html language=enus -->
## TOPIC 00087: RFMXVNA_ATTR_PULSE_GENERATOR_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_pulse_generator_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_pulse_generator_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_PULSE_GENERATOR_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether to enable a pulse generator. This attribute is used only when you set RFMXVNA_ATTR_PULSE_MODE_ENABLED attribute to RFMXVNA_VAL_PULSE_MODE_ENABLED_TRUE. Use 'pulsegen(n)' as the selector string to configure or read this attribute. The default value is RFMXVNA_VAL_PULSE_GENERATOR_ENABLED_FALSE. Get Function: RFmxVNA_GetPulseGeneratorEnabled Set Function: RFmxVNA_SetPulseGeneratorEnabled |
| Values: | RFMXVNA_VAL_PULSE_GENERATOR_ENABLED_FALSE (0)Disables the selected pulse generator. RFMXVNA_VAL_PULSE_GENERATOR_ENABLED_TRUE (1)Enables the selected pulse generator. |
| RFMXVNA_VAL_PULSE_GENERATOR_ENABLED_FALSE (0) | Disables the selected pulse generator. |
| RFMXVNA_VAL_PULSE_GENERATOR_ENABLED_TRUE (1) | Enables the selected pulse generator. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_pulse_generator_export_output_terminal.html language=enus -->
## TOPIC 00088: RFMXVNA_ATTR_PULSE_GENERATOR_EXPORT_OUTPUT_TERMINAL

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_pulse_generator_export_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_pulse_generator_export_output_terminal.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_PULSE_GENERATOR_EXPORT_OUTPUT_TERMINAL

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies the destination terminal for an exported Pulse Generator. This attribute is used only when you set RFMXVNA_ATTR_PULSE_MODE_ENABLED attribute to RFMXVNA_VAL_PULSE_MODE_ENABLED_TRUE and RFMXVNA_ATTR_PULSE_GENERATOR_ENABLED attribute to RFMXVNA_VAL_PULSE_MODE_ENABLED_TRUE. Use 'pulsegen(n)' as the selector string to configure or read this attribute. The default value is Do not export signal. Get Function: RFmxVNA_GetPulseGeneratorExportOutputTerminal Set Function: RFmxVNA_SetPulseGeneratorExportOutputTerminal |
| Values: | RFMXVNA_VAL_PFI0_STR (PFI0) The trigger is exported on PFI 0. RFMXVNA_VAL_PFI1_STR (PFI1) The trigger is exported on PFI 1. RFMXVNA_VAL_PXI_TRIG0_STR (PXI_Trig0) The trigger is exported on PXI trigger line 0. RFMXVNA_VAL_PXI_TRIG1_STR (PXI_Trig1) The trigger is exported on PXI trigger line 1. RFMXVNA_VAL_PXI_TRIG2_STR (PXI_Trig2) The trigger is exported on PXI trigger line 2. RFMXVNA_VAL_PXI_TRIG3_STR (PXI_Trig3) The trigger is exported on PXI trigger line 3. RFMXVNA_VAL_PXI_TRIG4_STR (PXI_Trig4) The trigger is exported on PXI trigger line 4. RFMXVNA_VAL_PXI_TRIG5_STR (PXI_Trig5) The trigger is exported on PXI trigger line 5. RFMXVNA_VAL_PXI_TRIG6_STR (PXI_Trig6) The trigger is exported on PXI trigger line 6. RFMXVNA_VAL_PXI_TRIG7_STR (PXI_Trig7) The trigger is exported on PXI trigger line 7. RFMXVNA_VAL_PXI_STAR_STR (PXI_STAR) The trigger is exported on the PXI star trigger line. Note that, RFmxVNA does not yet support this trigger line. RFMXVNA_VAL_PXIE_DSTARB_STR (PXIe_DStarB) The trigger is exported on the PXIe DStar B trigger line. |
| RFMXVNA_VAL_PFI0_STR (PFI0) | The trigger is exported on PFI 0. |
| RFMXVNA_VAL_PFI1_STR (PFI1) | The trigger is exported on PFI 1. |
| RFMXVNA_VAL_PXI_TRIG0_STR (PXI_Trig0) | The trigger is exported on PXI trigger line 0. |
| RFMXVNA_VAL_PXI_TRIG1_STR (PXI_Trig1) | The trigger is exported on PXI trigger line 1. |
| RFMXVNA_VAL_PXI_TRIG2_STR (PXI_Trig2) | The trigger is exported on PXI trigger line 2. |
| RFMXVNA_VAL_PXI_TRIG3_STR (PXI_Trig3) | The trigger is exported on PXI trigger line 3. |
| RFMXVNA_VAL_PXI_TRIG4_STR (PXI_Trig4) | The trigger is exported on PXI trigger line 4. |
| RFMXVNA_VAL_PXI_TRIG5_STR (PXI_Trig5) | The trigger is exported on PXI trigger line 5. |
| RFMXVNA_VAL_PXI_TRIG6_STR (PXI_Trig6) | The trigger is exported on PXI trigger line 6. |
| RFMXVNA_VAL_PXI_TRIG7_STR (PXI_Trig7) | The trigger is exported on PXI trigger line 7. |
| RFMXVNA_VAL_PXI_STAR_STR (PXI_STAR) | The trigger is exported on the PXI star trigger line. Note that, RFmxVNA does not yet support this trigger line. |
| RFMXVNA_VAL_PXIE_DSTARB_STR (PXIe_DStarB) | The trigger is exported on the PXIe DStar B trigger line. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_pulse_generator_width.html language=enus -->
## TOPIC 00089: RFMXVNA_ATTR_PULSE_GENERATOR_WIDTH

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_pulse_generator_width.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_pulse_generator_width.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_PULSE_GENERATOR_WIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the pulse width of the selected pulse generator.You must set the values of the RFMXVNA_ATTR_PULSE_GENERATOR_DELAY attribute and RFMXVNA_ATTR_PULSE_GENERATOR_WIDTH attribute such that Delay + Width does not exceed the value of RFMXVNA_ATTR_PULSE_PERIOD attribute. This value is expressed in seconds. Use 'pulsegen(n)' as the selector string to configure or read this attribute. The default value is 100us. Get Function: RFmxVNA_GetPulseGeneratorWidth Set Function: RFmxVNA_SetPulseGeneratorWidth |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_result_fetch_timeout.html language=enus -->
## TOPIC 00090: RFMXVNA_ATTR_RESULT_FETCH_TIMEOUT

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_result_fetch_timeout.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_result_fetch_timeout.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_RESULT_FETCH_TIMEOUT

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxVNA_GetResultFetchTimeout Set Function: RFmxVNA_SetResultFetchTimeout |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_dwell_time.html language=enus -->
## TOPIC 00091: RFMXVNA_ATTR_SEGMENT_DWELL_TIME

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_dwell_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_dwell_time.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_DWELL_TIME

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the dwell time for the selected segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT and RFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLED attribute to RFMXVNA_VAL_SEGMENT_DWELL_TIME_ENABLED_TRUE. This value is expressed in seconds. Dwell Time specifies the time for which the analyzer waits before acquiring the signal for each measured frequency point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. Use 'segment::(segmentnumber)' as the selector string to configure or read this attribute for a specific segment. Use 'segment::all' as the selector string to configure this attribute for all segments. The default value is 0 s. Get Function: RFmxVNA_GetSegmentDwellTime Set Function: RFmxVNA_SetSegmentDwellTime |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_dwell_time_enabled.html language=enus -->
## TOPIC 00092: RFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_dwell_time_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_dwell_time_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether VNA performs measurements using the same dwell time value for all segments or uses different dwell time for each segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_SEGMENT_DWELL_TIME_ENABLED_FALSE. Get Function: RFmxVNA_GetSegmentDwellTimeEnabled Set Function: RFmxVNA_SetSegmentDwellTimeEnabled |
| Values: | RFMXVNA_VAL_SEGMENT_DWELL_TIME_ENABLED_FALSE (0) All segments are measured with the dwell time that you specify using RFMXVNA_ATTR_DWELL_TIME attribute. RFMXVNA_VAL_SEGMENT_DWELL_TIME_ENABLED_TRUE (1) The selected segment is measured with the dwell time that you specify using RFMXVNA_ATTR_SEGMENT_DWELL_TIME attribute. |
| RFMXVNA_VAL_SEGMENT_DWELL_TIME_ENABLED_FALSE (0) | All segments are measured with the dwell time that you specify using RFMXVNA_ATTR_DWELL_TIME attribute. |
| RFMXVNA_VAL_SEGMENT_DWELL_TIME_ENABLED_TRUE (1) | The selected segment is measured with the dwell time that you specify using RFMXVNA_ATTR_SEGMENT_DWELL_TIME attribute. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_enabled.html language=enus -->
## TOPIC 00093: RFMXVNA_ATTR_SEGMENT_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether to enable the selected segment for the sweep. This attribute is used only when you set RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT Use 'segment::(segmentnumber)' as the selector string to configure or read this attribute for a specific segment. The default value is RFMXVNA_VAL_SEGMENT_ENABLED_FALSE. Get Function: RFmxVNA_GetSegmentEnabled Set Function: RFmxVNA_SetSegmentEnabled |
| Values: | RFMXVNA_VAL_SEGMENT_ENABLED_FALSE (0) Disables the selected segment. RFMXVNA_VAL_SEGMENT_ENABLED_TRUE (1) Enables the selected segment. |
| RFMXVNA_VAL_SEGMENT_ENABLED_FALSE (0) | Disables the selected segment. |
| RFMXVNA_VAL_SEGMENT_ENABLED_TRUE (1) | Enables the selected segment. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_if_bandwidth.html language=enus -->
## TOPIC 00094: RFMXVNA_ATTR_SEGMENT_IF_BANDWIDTH

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_if_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_if_bandwidth.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_IF_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the digital IF filter bandwidth for the selected segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT and RFMXVNA_ATTR_SEGMENT_IF_BANDWIDTH_ENABLED attribute to RFMXVNA_VAL_SEGMENT_IF_BANDWIDTH_ENABLED_TRUE. This value is expressed in Hz. NI PXIe-5633 supports the following IF Bandwidths: 1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M. If you set this attribute to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth.Use 'segment::(segmentnumber)' as the selector string to configure or read this attribute for a specific segment. Use 'segment::all' as the selector string to configure this attribute for all segments. The default value is 100 kHz. Get Function: RFmxVNA_GetSegmentIFBandwidth Set Function: RFmxVNA_SetSegmentIFBandwidth |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_if_bandwidth_enabled.html language=enus -->
## TOPIC 00095: RFMXVNA_ATTR_SEGMENT_IF_BANDWIDTH_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_if_bandwidth_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_if_bandwidth_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_IF_BANDWIDTH_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether VNA performs measurements using the same digital IF filter bandwidth for all segments or uses different digital IF filter bandwidth for each segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_SEGMENT_IF_BANDWIDTH_ENABLED_FALSE. Get Function: RFmxVNA_GetSegmentIFBandwidthEnabled Set Function: RFmxVNA_SetSegmentIFBandwidthEnabled |
| Values: | RFMXVNA_VAL_SEGMENT_IF_BANDWIDTH_ENABLED_FALSE (0) All segments are measured with the digital IF filter bandwidth that you specify using RFMXVNA_ATTR_IF_BANDWIDTH attribute. RFMXVNA_VAL_SEGMENT_IF_BANDWIDTH_ENABLED_TRUE (1) The selected segment is measured with the digital IF filter bandwidth that you specify using RFMXVNA_ATTR_SEGMENT_IF_BANDWIDTH attribute. |
| RFMXVNA_VAL_SEGMENT_IF_BANDWIDTH_ENABLED_FALSE (0) | All segments are measured with the digital IF filter bandwidth that you specify using RFMXVNA_ATTR_IF_BANDWIDTH attribute. |
| RFMXVNA_VAL_SEGMENT_IF_BANDWIDTH_ENABLED_TRUE (1) | The selected segment is measured with the digital IF filter bandwidth that you specify using RFMXVNA_ATTR_SEGMENT_IF_BANDWIDTH attribute. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_number_of_frequency_points.html language=enus -->
## TOPIC 00096: RFMXVNA_ATTR_SEGMENT_NUMBER_OF_FREQUENCY_POINTS

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_number_of_frequency_points.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_number_of_frequency_points.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_NUMBER_OF_FREQUENCY_POINTS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the number of frequency points measured in the selected segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT. Use 'segment::(segmentnumber)' as the selector string to configure or read this attribute for a specific segment. The default value is 10. Get Function: RFmxVNA_GetSegmentNumberOfFrequencyPoints Set Function: RFmxVNA_SetSegmentNumberOfFrequencyPoints |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_power_level.html language=enus -->
## TOPIC 00097: RFMXVNA_ATTR_SEGMENT_POWER_LEVEL

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_power_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_power_level.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_POWER_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the source power level for the selected segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT and RFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLED attribute to RFMXVNA_VAL_SEGMENT_POWER_LEVEL_ENABLED_TRUE. This value is expressed in dBm. Use 'port::(portname)' as the selector string to configure or read this attribute for a specific VNA port for segment0. Use 'port::all' to configure this attribute for all VNA ports for segment0. Use 'segment::(segmentnumber)/port::(portname)' as the selector string to configure or read this attribute for a specific segment and for a specific VNA port. Use 'segment::all/port::all' as the selector string to configure this attribute for all segments and for all VNA ports. The default value is -10 dBm. Get Function: RFmxVNA_GetSegmentPowerLevel Set Function: RFmxVNA_SetSegmentPowerLevel |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_power_level_enabled.html language=enus -->
## TOPIC 00098: RFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_power_level_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_power_level_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether VNA performs measurements using the same source power level for all segments or uses different source power level for each segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_SEGMENT_POWER_LEVEL_ENABLED_FALSE. Get Function: RFmxVNA_GetSegmentPowerLevelEnabled Set Function: RFmxVNA_SetSegmentPowerLevelEnabled |
| Values: | RFMXVNA_VAL_SEGMENT_POWER_LEVEL_ENABLED_FALSE (0) All segments are measured with the source power level that you specify using RFMXVNA_ATTR_POWER_LEVEL attribute. RFMXVNA_VAL_SEGMENT_POWER_LEVEL_ENABLED_TRUE (1) The selected segment is measured with the source power level that you specify using RFMXVNA_ATTR_SEGMENT_POWER_LEVEL attribute. |
| RFMXVNA_VAL_SEGMENT_POWER_LEVEL_ENABLED_FALSE (0) | All segments are measured with the source power level that you specify using RFMXVNA_ATTR_POWER_LEVEL attribute. |
| RFMXVNA_VAL_SEGMENT_POWER_LEVEL_ENABLED_TRUE (1) | The selected segment is measured with the source power level that you specify using RFMXVNA_ATTR_SEGMENT_POWER_LEVEL attribute. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_start_frequency.html language=enus -->
## TOPIC 00099: RFMXVNA_ATTR_SEGMENT_START_FREQUENCY

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_start_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_start_frequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_START_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the lowest frequency of the selected segment at which measurements are performed. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT. This value is expressed in Hz. Use 'segment::(segmentnumber)' as the selector string to configure or read this attribute for a specific segment. The default value is 1 GHz. Get Function: RFmxVNA_GetSegmentStartFrequency Set Function: RFmxVNA_SetSegmentStartFrequency |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_stop_frequency.html language=enus -->
## TOPIC 00100: RFMXVNA_ATTR_SEGMENT_STOP_FREQUENCY

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_stop_frequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_STOP_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the highest frequency of the selected segment at which measurements are performed. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT. This value is expressed in Hz. Use 'segment::(segmentnumber)' as the selector string to configure or read this attribute for a specific segment. The default value is 2 GHz. Get Function: RFmxVNA_GetSegmentStopFrequency Set Function: RFmxVNA_SetSegmentStopFrequency |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_test_receiver_attenuation.html language=enus -->
## TOPIC 00101: RFMXVNA_ATTR_SEGMENT_TEST_RECEIVER_ATTENUATION

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_test_receiver_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_test_receiver_attenuation.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_TEST_RECEIVER_ATTENUATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the test receiver attenuation for the selected segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT and Segment Test Receiver Attenuation Enabled attribute to True. This value is expressed in dB. The receiver that measures the scattered waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. VNA uses Test Receiver Attenuation to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver.Use 'port::(portname)' as the selector string to configure or read this attribute for a specific VNA port for segment0. Use 'port::all' to configure this attribute for all VNA ports for segment0. Use 'segment::(segmentnumber)/port::(portname)' as the selector string to configure or read this attribute for a specific segment and for a specific VNA port. Use 'segment::all/port::all' as the selector string to configure this attribute for all segment and for all VNA ports. The default value is 0 dB. Get Function: RFmxVNA_GetSegmentTestReceiverAttenuation Set Function: RFmxVNA_SetSegmentTestReceiverAttenuation |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_segment_test_receiver_attenuation_enabled.html language=enus -->
## TOPIC 00102: RFMXVNA_ATTR_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_segment_test_receiver_attenuation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_segment_test_receiver_attenuation_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether VNA performs measurements using the same test receiver attenuation for all segments or uses different test receiver attenuation for each segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_SEGMENT. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED_FALSE. Get Function: RFmxVNA_GetSegmentTestReceiverAttenuationEnabled Set Function: RFmxVNA_SetSegmentTestReceiverAttenuationEnabled |
| Values: | RFMXVNA_VAL_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED_FALSE (0) All segments are measured with the test receiver attenuation that you specify using Test Receiver Attenuation attribute. RFMXVNA_VAL_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED_TRUE (1) The selected segment is measured with the test receiver attenuation that you specify using Segment Test Receiver Attenuation attribute. |
| RFMXVNA_VAL_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED_FALSE (0) | All segments are measured with the test receiver attenuation that you specify using Test Receiver Attenuation attribute. |
| RFMXVNA_VAL_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED_TRUE (1) | The selected segment is measured with the test receiver attenuation that you specify using Segment Test Receiver Attenuation attribute. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_source_power_mode.html language=enus -->
## TOPIC 00103: RFMXVNA_ATTR_SOURCE_POWER_MODE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_source_power_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_source_power_mode.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SOURCE_POWER_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether to make VNA measurements with source turned off. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_SOURCE_POWER_MODE_AUTO. Get Function: RFmxVNA_GetSourcePowerMode Set Function: RFmxVNA_SetSourcePowerMode |
| Values: | RFMXVNA_VAL_SOURCE_POWER_MODE_AUTO (0)The source is turned on when making the measurement. RFMXVNA_VAL_SOURCE_POWER_MODE_OFF (1)The source is turned off for all the ports when making the measurements. |
| RFMXVNA_VAL_SOURCE_POWER_MODE_AUTO (0) | The source is turned on when making the measurement. |
| RFMXVNA_VAL_SOURCE_POWER_MODE_OFF (1) | The source is turned off for all the ports when making the measurements. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_format.html language=enus -->
## TOPIC 00104: RFMXVNA_ATTR_SPARAMS_FORMAT

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_format.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_format.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_FORMAT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the format of S-Parameter measurement. Use 'sparam(n)' as the selector string to configure or read this attribute. The default value is RFMXVNA_VAL_SPARAMS_FORMAT_MAGNITUDE. Get Function: RFmxVNA_SParamsGetFormat Set Function: RFmxVNA_SParamsSetFormat |
| Values: | RFMXVNA_VAL_SPARAMS_FORMAT_MAGNITUDE (0)Sets the format of the selected S-Parameter to Magnitude. You can specify RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS. RFMXVNA_VAL_SPARAMS_FORMAT_PHASE (1)Sets the format of the selected S-Parameter to Phase. Phase values are expressed in degrees. Phase can be represented in various, mathematically equivalent ways such as phase wrapped between the range [-180, 180) degrees, or phase can be represented in an unwrapped manner. You can specify the phase representation by configuring RFMXVNA_ATTR_SPARAMS_PHASE_TRACE_TYPE. RFMXVNA_VAL_SPARAMS_FORMAT_COMPLEX (2)Sets the format of the selected S-Parameter as complex numbers in cartesian co-ordinates. RFMXVNA_VAL_SPARAMS_FORMAT_SWR (3)Sets the format of the selected S-Parameter to Standing Wave Ratio (SWR). SWR is a unitless quantity. RFMXVNA_VAL_SPARAMS_FORMAT_SMITH_IMPEDANCE (4)Sets the format of the selected S-Parameter to Smith Impedance. S-Parameter values are transformed into impedence values. Impedence values are expressed in ohms. You can use these values to plot on a Smith Chart. RFMXVNA_VAL_SPARAMS_FORMAT_SMITH_ADMITTANCE (5)Sets the format of the selected S-Parameter to Smith Admittance. S-Parameter values are transformed into admittance values. Admittance values are expressed in siemens. You can use these values to plot on an Inverted Smith Chart. RFMXVNA_VAL_SPARAMS_FORMAT_POLAR (6)Sets the format of the selected S-Parameter as complex numbers in polar co-ordinates, where the radial axis (i.e., magnitude of the complex numbers) is always in linear scale and angular axis (phase) is represented in degrees and always wrapped between Â±180 deg. |
| RFMXVNA_VAL_SPARAMS_FORMAT_MAGNITUDE (0) | Sets the format of the selected S-Parameter to Magnitude. You can specify RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS. |
| RFMXVNA_VAL_SPARAMS_FORMAT_PHASE (1) | Sets the format of the selected S-Parameter to Phase. Phase values are expressed in degrees. Phase can be represented in various, mathematically equivalent ways such as phase wrapped between the range [-180, 180) degrees, or phase can be represented in an unwrapped manner. You can specify the phase representation by configuring RFMXVNA_ATTR_SPARAMS_PHASE_TRACE_TYPE. |
| RFMXVNA_VAL_SPARAMS_FORMAT_COMPLEX (2) | Sets the format of the selected S-Parameter as complex numbers in cartesian co-ordinates. |
| RFMXVNA_VAL_SPARAMS_FORMAT_SWR (3) | Sets the format of the selected S-Parameter to Standing Wave Ratio (SWR). SWR is a unitless quantity. |
| RFMXVNA_VAL_SPARAMS_FORMAT_SMITH_IMPEDANCE (4) | Sets the format of the selected S-Parameter to Smith Impedance. S-Parameter values are transformed into impedence values. Impedence values are expressed in ohms. You can use these values to plot on a Smith Chart. |
| RFMXVNA_VAL_SPARAMS_FORMAT_SMITH_ADMITTANCE (5) | Sets the format of the selected S-Parameter to Smith Admittance. S-Parameter values are transformed into admittance values. Admittance values are expressed in siemens. You can use these values to plot on an Inverted Smith Chart. |
| RFMXVNA_VAL_SPARAMS_FORMAT_POLAR (6) | Sets the format of the selected S-Parameter as complex numbers in polar co-ordinates, where the radial axis (i.e., magnitude of the complex numbers) is always in linear scale and angular axis (phase) is represented in degrees and always wrapped between Â±180 deg. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_magnitude_units.html language=enus -->
## TOPIC 00105: RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_magnitude_units.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_magnitude_units.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the magnitude units for all S-Parameters for which you set RFMXVNA_ATTR_SPARAMS_FORMAT attribute to Magnitude. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_SPARAMS_MAGNITUDE_UNITS_DB. Get Function: RFmxVNA_SParamsGetMagnitudeUnits Set Function: RFmxVNA_SParamsSetMagnitudeUnits |
| Values: | RFMXVNA_VAL_SPARAMS_MAGNITUDE_UNITS_DB (0)Sets S-Parameter magnitude units to dB. RFMXVNA_VAL_SPARAMS_MAGNITUDE_UNITS_LINEAR (1)Sets S-Parameter magnitude units to linear such that S-Parameters are reported in linear scale (V/V). |
| RFMXVNA_VAL_SPARAMS_MAGNITUDE_UNITS_DB (0) | Sets S-Parameter magnitude units to dB. |
| RFMXVNA_VAL_SPARAMS_MAGNITUDE_UNITS_LINEAR (1) | Sets S-Parameter magnitude units to linear such that S-Parameters are reported in linear scale (V/V). |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_measurement_enabled.html language=enus -->
## TOPIC 00106: RFMXVNA_ATTR_SPARAMS_MEASUREMENT_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_measurement_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether to enable the Sparams measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the selector string topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_FALSE. Get Function: RFmxVNA_SParamsGetMeasurementEnabled Set Function: RFmxVNA_SParamsSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_number_of_sparameters.html language=enus -->
## TOPIC 00107: RFMXVNA_ATTR_SPARAMS_NUMBER_OF_SPARAMETERS

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_number_of_sparameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_number_of_sparameters.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_NUMBER_OF_SPARAMETERS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the number of S-Parameters to measure. Note1: S-Parameters of a N-port DUT can be represented by N^2 canonical S-Parameters viz. S11, S12,...,S1N, S21, S22,...,S2N, SN1, SN2,...,SNN such that B = S Awhere S denotes the S-Parameter matrix with Sij being the element in the ith row and jth column. Similarly A denotes the matrix composed of the incident waves. Element Aij denotes the wave parameter aij i.e., wave measured at the reference reciever on port (i) with port (j) as the source. Similarly B denotes the matrix composed of the scatterred waves. Element Bij denotes the wave parameter bij i.e., wave measured at the test reciever on port (i) with port (j) as the source.You can configure each measured S-Parameter in RFmxVNA SParams measurement to be returned in one of several supported formats using RFMXVNA_ATTR_SPARAMS_FORMAT attribute. Example1: If you want to fetch magnitude and phase information of S11, then set Number of S-Parameters attribute to 2, then for both SParam indices 0 and 1, set Parameter attribute to 'S11'. Then set RFMXVNA_ATTR_SPARAMS_FORMAT attribute to Magnitude for Sparam index 0 and to Phase for SParam index 1. Note2: You can set many SParam indices to share the same Parameter and Format attribute values making them duplicates of each other.If you increase this attribute value from N to N+K, then existing N SParams are not affected but K new SParams are added. If you reduce number of SParams from N to N-K, then last K SParams are deleted without affecting the remaining N-K SParams.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxVNA_SParamsGetNumberOfSParameters Set Function: RFmxVNA_SParamsSetNumberOfSParameters |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_phase_trace_type.html language=enus -->
## TOPIC 00108: RFMXVNA_ATTR_SPARAMS_PHASE_TRACE_TYPE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_phase_trace_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_phase_trace_type.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_PHASE_TRACE_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the phase type for all S-Parameters for which RFMXVNA_ATTR_SPARAMS_FORMAT attribute is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_SPARAMS_PHASE_TRACE_TYPE_WRAPPED. Get Function: RFmxVNA_SParamsGetPhaseTraceType Set Function: RFmxVNA_SParamsSetPhaseTraceType |
| Values: | RFMXVNA_VAL_SPARAMS_PHASE_TRACE_TYPE_WRAPPED (0)The reported S-Parameter phase is wrapped between -180 degress to +180 degrees. RFMXVNA_VAL_SPARAMS_PHASE_TRACE_TYPE_UNWRAPPED (1)The reported S-Parameter phase is unwrapped. |
| RFMXVNA_VAL_SPARAMS_PHASE_TRACE_TYPE_WRAPPED (0) | The reported S-Parameter phase is wrapped between -180 degress to +180 degrees. |
| RFMXVNA_VAL_SPARAMS_PHASE_TRACE_TYPE_UNWRAPPED (1) | The reported S-Parameter phase is unwrapped. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_receiver_port.html language=enus -->
## TOPIC 00109: RFMXVNA_ATTR_SPARAMS_RECEIVER_PORT

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_receiver_port.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_receiver_port.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_RECEIVER_PORT

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies the receiver port name of the S-Parameter. S-Parameter is denoted by 'S_(receiver port name)_(source port name)'. For example, to measure S21, set this attribute to 'port2'. Use 'sparam(n)' as the selector string to configure or read this attribute. The default value is 'port1'. Get Function: RFmxVNA_SParamsGetReceiverPort Set Function: RFmxVNA_SParamsSetReceiverPort |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_results_correction_state.html language=enus -->
## TOPIC 00110: RFMXVNA_ATTR_SPARAMS_RESULTS_CORRECTION_STATE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_results_correction_state.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_results_correction_state.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_RESULTS_CORRECTION_STATE

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxVNA_GetAttributeI32 |
| Description: | Get Function: RFmxVNA_SParamsGetResultsCorrectionState |
| Values: | RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_NONE (0)Error correction is not applied. RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_CORRECTED (1)Error correction is applied without interpolation using the error terms from the calset. RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_INTERPOLATED (2)Error correction is applied with error terms for at least one sweep point interpolated from the calset error terms. RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_SETTINGS_MODIFIED (3)Settings during the measurment differ from those used during calibration. |
| RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_NONE (0) | Error correction is not applied. |
| RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_CORRECTED (1) | Error correction is applied without interpolation using the error terms from the calset. |
| RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_INTERPOLATED (2) | Error correction is applied with error terms for at least one sweep point interpolated from the calset error terms. |
| RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_SETTINGS_MODIFIED (3) | Settings during the measurment differ from those used during calibration. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_snp_data_format.html language=enus -->
## TOPIC 00111: RFMXVNA_ATTR_SPARAMS_SNP_DATA_FORMAT

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_snp_data_format.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_snp_data_format.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_SNP_DATA_FORMAT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the format in which the measured S-parameters are saved in a SnP file. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_AUTO. Get Function: RFmxVNA_SParamsGetSnPDataFormat Set Function: RFmxVNA_SParamsSetSnPDataFormat |
| Values: | RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_AUTO (0)RFmx automatically selects the appropriate SnP Data Format based on the value specified for RFMXVNA_ATTR_SPARAMS_FORMAT attribute. If you set RFMXVNA_ATTR_SPARAMS_FORMAT to Complex or SWR or Smith Impedence or Smith Admittance, S-parameters are saved in the Real-Imaginary format. If you set RFMXVNA_ATTR_SPARAMS_FORMAT to Magnitude, S-parameters are saved as either Log Magnitude-Angle or Linear Magnitude-Angle according to RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS. If you set RFMXVNA_ATTR_SPARAMS_FORMAT to Phase or Polar, S-parameters are saved as Log Magnitude-Angle by default. RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_LOG_MAGNITUDE_ANGLE (1)All available S-parameters are represented as a pair of columns - first column stores magnitude of a S-Parameter in log scale (dB) and second column stores phase of the S-Parameter in degrees. RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_REAL_IMAGINARY (2)All available S-parameters are represented as a pair of columns - first column stores real part of the complex-valued S-Parameter and second column stores imaginary part. RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_LINEAR_MAGNITUDE_ANGLE (3)All available S-parameters are represented as a pair of columns - first column stores magnitude of a S-Parameter in linear scale (V/V) and second column stores phase of the S-Parameter in degrees. |
| RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_AUTO (0) | RFmx automatically selects the appropriate SnP Data Format based on the value specified for RFMXVNA_ATTR_SPARAMS_FORMAT attribute. If you set RFMXVNA_ATTR_SPARAMS_FORMAT to Complex or SWR or Smith Impedence or Smith Admittance, S-parameters are saved in the Real-Imaginary format. If you set RFMXVNA_ATTR_SPARAMS_FORMAT to Magnitude, S-parameters are saved as either Log Magnitude-Angle or Linear Magnitude-Angle according to RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS. If you set RFMXVNA_ATTR_SPARAMS_FORMAT to Phase or Polar, S-parameters are saved as Log Magnitude-Angle by default. |
| RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_LOG_MAGNITUDE_ANGLE (1) | All available S-parameters are represented as a pair of columns - first column stores magnitude of a S-Parameter in log scale (dB) and second column stores phase of the S-Parameter in degrees. |
| RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_REAL_IMAGINARY (2) | All available S-parameters are represented as a pair of columns - first column stores real part of the complex-valued S-Parameter and second column stores imaginary part. |
| RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_LINEAR_MAGNITUDE_ANGLE (3) | All available S-parameters are represented as a pair of columns - first column stores magnitude of a S-Parameter in linear scale (V/V) and second column stores phase of the S-Parameter in degrees. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_snp_ports.html language=enus -->
## TOPIC 00112: RFMXVNA_ATTR_SPARAMS_SNP_PORTS

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_snp_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_snp_ports.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_SNP_PORTS

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies the ports for which the measured S-parameters are saved to file. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxVNA_SParamsGetSnPPorts Set Function: RFmxVNA_SParamsSetSnPPorts |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_snp_user_comment.html language=enus -->
## TOPIC 00113: RFMXVNA_ATTR_SPARAMS_SNP_USER_COMMENT

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_snp_user_comment.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_snp_user_comment.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_SNP_USER_COMMENT

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies a string that is incorporated into saved SnP file. You can specify any arbitrary string to add any meta information that you may want to store along with the measured S-Parameters data in SnP file. RFmx automatically adds a special token(!) at the start of this string such that any standard SnP file parsers would ignore this line. Additionally, multiline comments are allowed and each line is appended with the next line escape character. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxVNA_SParamsGetSnPUserComment Set Function: RFmxVNA_SParamsSetSnPUserComment |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sparams_source_port.html language=enus -->
## TOPIC 00114: RFMXVNA_ATTR_SPARAMS_SOURCE_PORT

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sparams_source_port.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sparams_source_port.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SPARAMS_SOURCE_PORT

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies the source port name of the S-Parameter. S-Parameter is denoted by 'S_(receiver port name)_(source port name)'. For example, to measure S21, set this attribute to 'port1'. Use 'sparam(n)' as the selector string to configure or read this attribute. The default value is 'port1'. Get Function: RFmxVNA_SParamsGetSourcePort Set Function: RFmxVNA_SParamsSetSourcePort |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_start_frequency.html language=enus -->
## TOPIC 00115: RFMXVNA_ATTR_START_FREQUENCY

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_start_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_start_frequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_START_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the lowest frequency at which measurements are performed. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_LINEAR. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1 GHz. Get Function: RFmxVNA_GetStartFrequency Set Function: RFmxVNA_SetStartFrequency |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_stop_frequency.html language=enus -->
## TOPIC 00116: RFMXVNA_ATTR_STOP_FREQUENCY

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_stop_frequency.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_STOP_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the highest frequency at which measurements are performed. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to RFMXVNA_VAL_SWEEP_TYPE_LINEAR. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 2 GHz. Get Function: RFmxVNA_GetStopFrequency Set Function: RFmxVNA_SetStopFrequency |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sweep_delay.html language=enus -->
## TOPIC 00117: RFMXVNA_ATTR_SWEEP_DELAY

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sweep_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sweep_delay.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SWEEP_DELAY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the time for which VNA waits before it starts acquiring data for each sweep. Total delay for acquiring the first point in each sweep is sum of this delay and RFMXVNA_ATTR_DWELL_TIME. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0 s. Get Function: RFmxVNA_GetSweepDelay Set Function: RFmxVNA_SetSweepDelay |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sweep_sequence.html language=enus -->
## TOPIC 00118: RFMXVNA_ATTR_SWEEP_SEQUENCE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sweep_sequence.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sweep_sequence.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SWEEP_SEQUENCE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the sequence of acquisitions for various frequency points and source ports. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_SWEEP_SEQUENCE_STANDARD. Get Function: RFmxVNA_GetSweepSequence Set Function: RFmxVNA_SetSweepSequence |
| Values: | RFMXVNA_VAL_SWEEP_SEQUENCE_STANDARD (0)Acquisitions for all frequency points are completed with the first source port before moving to the next source port. For example, if there are three frequency points f1, f2 and f3 and two source ports, port1 and port2, then the sweep sequence will be (f1, port1), (f2, port1), (f3, port1), (f1, port2), (f2, port2), (f3, port2). RFMXVNA_VAL_SWEEP_SEQUENCE_POINT (1)All acquisitions for a frequency point are completed with all required source ports, before moving to the next frequency point. For example, if there are three frequency points f1, f2 and f3 and two source ports, port1 and port2, then the sweep sequence will be (f1, port1), (f1, port2), (f2, port1), (f2, port2), (f3, port1), (f3, port2). |
| RFMXVNA_VAL_SWEEP_SEQUENCE_STANDARD (0) | Acquisitions for all frequency points are completed with the first source port before moving to the next source port. For example, if there are three frequency points f1, f2 and f3 and two source ports, port1 and port2, then the sweep sequence will be (f1, port1), (f2, port1), (f3, port1), (f1, port2), (f2, port2), (f3, port2). |
| RFMXVNA_VAL_SWEEP_SEQUENCE_POINT (1) | All acquisitions for a frequency point are completed with all required source ports, before moving to the next frequency point. For example, if there are three frequency points f1, f2 and f3 and two source ports, port1 and port2, then the sweep sequence will be (f1, port1), (f1, port2), (f2, port1), (f2, port2), (f3, port1), (f3, port2). |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_sweep_type.html language=enus -->
## TOPIC 00119: RFMXVNA_ATTR_SWEEP_TYPE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_sweep_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_sweep_type.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_SWEEP_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the sweep type for the measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_SWEEP_TYPE_LIST. Get Function: RFmxVNA_GetSweepType Set Function: RFmxVNA_SetSweepType |
| Values: | RFMXVNA_VAL_SWEEP_TYPE_LIST (0) The frequency is swept in arbitrary frequency steps. RFMXVNA_VAL_SWEEP_TYPE_LINEAR (1) The frequency is swept in equidistant steps over the frequency range. RFMXVNA_VAL_SWEEP_TYPE_SEGMENT (2) The frequency is swept in frequency sub-sweeps, called segments. For each segment, you can define independent values for settings like IF bandwidth, dwell time, source power level and test receiver attenuation. |
| RFMXVNA_VAL_SWEEP_TYPE_LIST (0) | The frequency is swept in arbitrary frequency steps. |
| RFMXVNA_VAL_SWEEP_TYPE_LINEAR (1) | The frequency is swept in equidistant steps over the frequency range. |
| RFMXVNA_VAL_SWEEP_TYPE_SEGMENT (2) | The frequency is swept in frequency sub-sweeps, called segments. For each segment, you can define independent values for settings like IF bandwidth, dwell time, source power level and test receiver attenuation. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_test_receiver_attenuation.html language=enus -->
## TOPIC 00120: RFMXVNA_ATTR_TEST_RECEIVER_ATTENUATION

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_test_receiver_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_test_receiver_attenuation.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_TEST_RECEIVER_ATTENUATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeF64RFmxVNA_GetAttributeF64 |
| Description: | Specifies the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. The receiver that measures the scattered waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. Use 'port::(portname)' as the selector string to configure or read this attribute for a specific VNA port. Use 'port::all' to configure same test receiver attenuation for all VNA ports. The default value is 0 dB. Get Function: RFmxVNA_GetTestReceiverAttenuation Set Function: RFmxVNA_SetTestReceiverAttenuation |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_trigger_mode.html language=enus -->
## TOPIC 00121: RFMXVNA_ATTR_TRIGGER_MODE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_trigger_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_trigger_mode.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_TRIGGER_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the trigger mode. RFMXVNA_ATTR_TRIGGER_MODE decides how many data points are acquired for each asserted trigger. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_TRIGGER_MODE_SIGNAL. Get Function: RFmxVNA_GetTriggerMode Set Function: RFmxVNA_SetTriggerMode |
| Values: | RFMXVNA_VAL_TRIGGER_MODE_SIGNAL (0)VNA waits for asserting only one instance of trigger before acquiring all data points for the configured measurements in the RFmxVNA Signal namespace. You can specify the RFmxVNA Signal name using Selector String attribute. RFMXVNA_VAL_TRIGGER_MODE_SWEEP (1)All data points that share a source port are acquired after VNA asserts one instance of the trigger. For example, when you measure S11 and S22 at 10 frequency points using a 2-port VNA, after asserting the first instance of trigger, the device completes all acquisitions that require VNA port 1 as source. Upon asserting the second trigger, the device completes all acquisitions that require VNA port 2 as source. RFMXVNA_VAL_TRIGGER_MODE_POINT (2)VNA acquires only one data point for each trigger instance that it asserts. For example, when you measure S11 and S22 at 10 frequency points using a 2-port VNA, the device will assert a total of 20 trigger instances to complete all acquisitions. |
| RFMXVNA_VAL_TRIGGER_MODE_SIGNAL (0) | VNA waits for asserting only one instance of trigger before acquiring all data points for the configured measurements in the RFmxVNA Signal namespace. You can specify the RFmxVNA Signal name using Selector String attribute. |
| RFMXVNA_VAL_TRIGGER_MODE_SWEEP (1) | All data points that share a source port are acquired after VNA asserts one instance of the trigger. For example, when you measure S11 and S22 at 10 frequency points using a 2-port VNA, after asserting the first instance of trigger, the device completes all acquisitions that require VNA port 1 as source. Upon asserting the second trigger, the device completes all acquisitions that require VNA port 2 as source. |
| RFMXVNA_VAL_TRIGGER_MODE_POINT (2) | VNA acquires only one data point for each trigger instance that it asserts. For example, when you measure S11 and S22 at 10 frequency points using a 2-port VNA, the device will assert a total of 20 trigger instances to complete all acquisitions. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_trigger_type.html language=enus -->
## TOPIC 00122: RFMXVNA_ATTR_TRIGGER_TYPE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_trigger_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_trigger_type.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_TRIGGER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the trigger type. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_TRIGGER_TYPE_NONE. Get Function: RFmxVNA_GetTriggerType Set Function: RFmxVNA_SetTriggerType |
| Values: | RFMXVNA_VAL_TRIGGER_TYPE_NONE (0)No trigger is configured. RFMXVNA_VAL_TRIGGER_TYPE_DIGITAL_EDGE (1)The trigger is asserted when a digital edge is detected. You can specify the source of the digital edge using the RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. RFMXVNA_VAL_TRIGGER_TYPE_SOFTWARE (2)The trigger is asserted when you send a software trigger. Use _RFmxVNASendSoftwareEdgeTrigger function to send a software trigger. RFmx ignores Software Edge Trigger when performing Calibration. |
| RFMXVNA_VAL_TRIGGER_TYPE_NONE (0) | No trigger is configured. |
| RFMXVNA_VAL_TRIGGER_TYPE_DIGITAL_EDGE (1) | The trigger is asserted when a digital edge is detected. You can specify the source of the digital edge using the RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. |
| RFMXVNA_VAL_TRIGGER_TYPE_SOFTWARE (2) | The trigger is asserted when you send a software trigger. Use _RFmxVNASendSoftwareEdgeTrigger function to send a software trigger. RFmx ignores Software Edge Trigger when performing Calibration. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_waves_format.html language=enus -->
## TOPIC 00123: RFMXVNA_ATTR_WAVES_FORMAT

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_waves_format.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_waves_format.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_WAVES_FORMAT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the format for wave measurement. Use 'wave(n)' as the selector string to configure or read this attribute. Use RFmxVNA Waves Fetch Y Data to fetch the waves. The default value is RFMXVNA_VAL_WAVES_FORMAT_MAGNITUDE. Get Function: RFmxVNA_WavesGetFormat Set Function: RFmxVNA_WavesSetFormat |
| Values: | RFMXVNA_VAL_WAVES_FORMAT_MAGNITUDE (0)Sets the format for the selected wave to Magnitude. You can specify Wave Magnitude Units. RFMXVNA_VAL_WAVES_FORMAT_PHASE (1)Sets the format of the selected wave to Phase. Phase values are expressed in degrees. Phase can be represented in various, mathematically equivalent ways such as phase wrapped between the range [-180, 180) degrees, or phase can be represented in an unwrapped manner. You can specify the phase representation by configuring Wave Phase Trace Type. RFMXVNA_VAL_WAVES_FORMAT_COMPLEX (2)Sets the format for the selected wave as complex numbers in cartesian co-ordinates. RFMXVNA_VAL_WAVES_FORMAT_SWR (3)Sets the format for the selected wave to Standing Wave Ratio (SWR). SWR is a unitless quantity. RFMXVNA_VAL_WAVES_FORMAT_SMITH_IMPEDANCE (4)Sets the format for the selected wave to Smith Impedance. The measured values of the wave are transformed into impedence values. Impedence values are expressed in ohms. You can use these values to plot on a Smith Chart. RFMXVNA_VAL_WAVES_FORMAT_SMITH_ADMITTANCE (5)Sets the format for the selected wave to Smith Admittance. The measured values of the wave are transformed into admittance values. Admittance values are expressed in siemens. You can use these values to plot on an Inverted Smith Chart. RFMXVNA_VAL_WAVES_FORMAT_POLAR (6)Sets the format for the selected wave as complex numbers in polar co-ordinates, where the radial axis (i.e., magnitude of the complex numbers) is always in linear scale and angular axis (phase) is represented in degrees and always wrapped between Â±180 deg. |
| RFMXVNA_VAL_WAVES_FORMAT_MAGNITUDE (0) | Sets the format for the selected wave to Magnitude. You can specify Wave Magnitude Units. |
| RFMXVNA_VAL_WAVES_FORMAT_PHASE (1) | Sets the format of the selected wave to Phase. Phase values are expressed in degrees. Phase can be represented in various, mathematically equivalent ways such as phase wrapped between the range [-180, 180) degrees, or phase can be represented in an unwrapped manner. You can specify the phase representation by configuring Wave Phase Trace Type. |
| RFMXVNA_VAL_WAVES_FORMAT_COMPLEX (2) | Sets the format for the selected wave as complex numbers in cartesian co-ordinates. |
| RFMXVNA_VAL_WAVES_FORMAT_SWR (3) | Sets the format for the selected wave to Standing Wave Ratio (SWR). SWR is a unitless quantity. |
| RFMXVNA_VAL_WAVES_FORMAT_SMITH_IMPEDANCE (4) | Sets the format for the selected wave to Smith Impedance. The measured values of the wave are transformed into impedence values. Impedence values are expressed in ohms. You can use these values to plot on a Smith Chart. |
| RFMXVNA_VAL_WAVES_FORMAT_SMITH_ADMITTANCE (5) | Sets the format for the selected wave to Smith Admittance. The measured values of the wave are transformed into admittance values. Admittance values are expressed in siemens. You can use these values to plot on an Inverted Smith Chart. |
| RFMXVNA_VAL_WAVES_FORMAT_POLAR (6) | Sets the format for the selected wave as complex numbers in polar co-ordinates, where the radial axis (i.e., magnitude of the complex numbers) is always in linear scale and angular axis (phase) is represented in degrees and always wrapped between Â±180 deg. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_waves_magnitude_units.html language=enus -->
## TOPIC 00124: RFMXVNA_ATTR_WAVES_MAGNITUDE_UNITS

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_waves_magnitude_units.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_waves_magnitude_units.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_WAVES_MAGNITUDE_UNITS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the magnitude units for all waves for which RFMXVNA_ATTR_WAVES_FORMAT attribute is set to RFMXVNA_VAL_WAVES_FORMAT_MAGNITUDE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBMV. Get Function: RFmxVNA_WavesGetMagnitudeUnits Set Function: RFmxVNA_WavesSetMagnitudeUnits |
| Values: | RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBM (0)Sets wave magnitude units to dBm. RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBMV (1)Sets wave magnitude units to dBmV. RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBUV (2)Sets wave magnitude units to dBuV. RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBMA (3)Sets wave magnitude units to dBmA. RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_W (4)Sets wave magnitude units to watts. RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_V (5)Sets wave magnitude units to volts. RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_A (6)Sets wave magnitude units to ampere. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBM (0) | Sets wave magnitude units to dBm. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBMV (1) | Sets wave magnitude units to dBmV. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBUV (2) | Sets wave magnitude units to dBuV. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBMA (3) | Sets wave magnitude units to dBmA. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_W (4) | Sets wave magnitude units to watts. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_V (5) | Sets wave magnitude units to volts. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_A (6) | Sets wave magnitude units to ampere. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_waves_measurement_enabled.html language=enus -->
## TOPIC 00125: RFMXVNA_ATTR_WAVES_MEASUREMENT_ENABLED

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_waves_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_waves_measurement_enabled.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_WAVES_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether to enable the Waves measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_FALSE. Get Function: RFmxVNA_WavesGetMeasurementEnabled Set Function: RFmxVNA_WavesSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_waves_number_of_waves.html language=enus -->
## TOPIC 00126: RFMXVNA_ATTR_WAVES_NUMBER_OF_WAVES

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_waves_number_of_waves.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_waves_number_of_waves.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_WAVES_NUMBER_OF_WAVES

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the number of waves to be measured. If you increase this attribute value from N to N+K, then existing N Waves are not affected but K new Waves are added. If you reduce number of Waves from N to N-K, then last K Waves are deleted without affecting the remaining N-K Waves.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxVNA_WavesGetNumberOfWaves Set Function: RFmxVNA_WavesSetNumberOfWaves |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_waves_phase_trace_type.html language=enus -->
## TOPIC 00127: RFMXVNA_ATTR_WAVES_PHASE_TRACE_TYPE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_waves_phase_trace_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_waves_phase_trace_type.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_WAVES_PHASE_TRACE_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies the phase type for all waves for which RFMXVNA_ATTR_WAVES_FORMAT attribute is set to RFMXVNA_VAL_WAVES_FORMAT_PHASE. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXVNA_VAL_WAVES_PHASE_TRACE_TYPE_WRAPPED. Get Function: RFmxVNA_WavesGetPhaseTraceType Set Function: RFmxVNA_WavesSetPhaseTraceType |
| Values: | RFMXVNA_VAL_WAVES_PHASE_TRACE_TYPE_WRAPPED (0)The reported wave phase is wrapped between -180 degress to +180 degrees. RFMXVNA_VAL_WAVES_PHASE_TRACE_TYPE_UNWRAPPED (1)The reported wave phase is unwrapped. |
| RFMXVNA_VAL_WAVES_PHASE_TRACE_TYPE_WRAPPED (0) | The reported wave phase is wrapped between -180 degress to +180 degrees. |
| RFMXVNA_VAL_WAVES_PHASE_TRACE_TYPE_UNWRAPPED (1) | The reported wave phase is unwrapped. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_waves_receiver.html language=enus -->
## TOPIC 00128: RFMXVNA_ATTR_WAVES_RECEIVER

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_waves_receiver.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_waves_receiver.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_WAVES_RECEIVER

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeI32RFmxVNA_GetAttributeI32 |
| Description: | Specifies whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port.Incident and scattered waves are denoted by 'a_(receiver port name)_(source port name)' and 'b_(receiver port name)_(source port name)' respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively.For example, to measure 'b21', set this attribute to Test (0), RFMXVNA_ATTR_WAVES_RECEIVER_PORT to 'port2' and RFMXVNA_ATTR_WAVES_SOURCE_PORT to 'port1'. Use 'wave(n)' as the selector string to configure or read this attribute. The default value is RFMXVNA_VAL_WAVES_RECEIVER_TEST. Get Function: RFmxVNA_WavesGetReceiver Set Function: RFmxVNA_WavesSetReceiver |
| Values: | RFMXVNA_VAL_WAVES_RECEIVER_TEST (0)Measures the wave on the test receiver. RFMXVNA_VAL_WAVES_RECEIVER_REFERENCE (1)Measures the wave on the reference receiver. |
| RFMXVNA_VAL_WAVES_RECEIVER_TEST (0) | Measures the wave on the test receiver. |
| RFMXVNA_VAL_WAVES_RECEIVER_REFERENCE (1) | Measures the wave on the reference receiver. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_waves_receiver_port.html language=enus -->
## TOPIC 00129: RFMXVNA_ATTR_WAVES_RECEIVER_PORT

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_waves_receiver_port.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_waves_receiver_port.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_WAVES_RECEIVER_PORT

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies the receiver port name for wave measurement. Incident and scattered waves are denoted by 'a_(receiver port name)_(source port name)' and 'b_(receiver port name)_(source port name)' respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure 'b21', set RFMXVNA_ATTR_WAVES_RECEIVER to Test (0), set this attribute to 'port2' and RFMXVNA_ATTR_WAVES_SOURCE_PORT to 'port1'. Use 'wave(n)' as the selector string to configure or read this attribute. The default value is 'port1'. Get Function: RFmxVNA_WavesGetReceiverPort Set Function: RFmxVNA_WavesSetReceiverPort |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_waves_results_correction_state.html language=enus -->
## TOPIC 00130: RFMXVNA_ATTR_WAVES_RESULTS_CORRECTION_STATE

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_waves_results_correction_state.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_waves_results_correction_state.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_WAVES_RESULTS_CORRECTION_STATE

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxVNA_GetAttributeI32 |
| Description: | Returns the error correction state of the VNA Waves measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxVNA_WavesGetResultsCorrectionState |
| Values: | RFMXVNA_VAL_WAVES_CORRECTION_STATE_NONE (0)Error correction is not applied. RFMXVNA_VAL_WAVES_CORRECTION_STATE_CORRECTED (1)Error correction is applied without interpolation using the error terms from the calset. RFMXVNA_VAL_WAVES_CORRECTION_STATE_INTERPOLATED (2)Error correction is applied with error terms for at least one sweep point interpolated from the calset error terms. RFMXVNA_VAL_WAVES_CORRECTION_STATE_SETTINGS_MODIFIED (3)Settings during the measurment differ from those used during calibration. |
| RFMXVNA_VAL_WAVES_CORRECTION_STATE_NONE (0) | Error correction is not applied. |
| RFMXVNA_VAL_WAVES_CORRECTION_STATE_CORRECTED (1) | Error correction is applied without interpolation using the error terms from the calset. |
| RFMXVNA_VAL_WAVES_CORRECTION_STATE_INTERPOLATED (2) | Error correction is applied with error terms for at least one sweep point interpolated from the calset error terms. |
| RFMXVNA_VAL_WAVES_CORRECTION_STATE_SETTINGS_MODIFIED (3) | Settings during the measurment differ from those used during calibration. |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_waves_source_port.html language=enus -->
## TOPIC 00131: RFMXVNA_ATTR_WAVES_SOURCE_PORT

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_waves_source_port.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_waves_source_port.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_WAVES_SOURCE_PORT

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxVNA_SetAttributeStringRFmxVNA_GetAttributeString |
| Description: | Specifies the source port name for wave measurement. Incident and scattered waves are denoted by 'a_(receiver port name)_(source port name)' and 'b_(receiver port name)_(source port name)' respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure 'b21', set RFMXVNA_ATTR_WAVES_RECEIVER to Test (0), RFMXVNA_ATTR_WAVES_RECEIVER_PORT to 'port2' and set this attribute to 'port1'. Use 'wave(n)' as the selector string to configure or read this attribute. The default value is 'port1'. Get Function: RFmxVNA_WavesGetSourcePort Set Function: RFmxVNA_WavesSetSourcePort |

<!--NI_TOPIC bundle=rfmx-vna-cvi path=rfmxvna_attr_x_axis_values.html language=enus -->
## TOPIC 00132: RFMXVNA_ATTR_X_AXIS_VALUES

- bundle_id: `rfmx-vna-cvi`
- source_path: `rfmxvna_attr_x_axis_values.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-cvi/raw/resource/enus/rfmxvna_attr_x_axis_values.html
- document_id: `rfmx-vna-cvi`
- page_type: `leaf`
- content_type: ``

RFMXVNA_ATTR_X_AXIS_VALUES

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxVNA_GetAttributeF64Array |
| Description: | Returns an array of frequency values when you perform measurements with RFMXVNA_ATTR_SWEEP_TYPE attribute set to RFMXVNA_VAL_SWEEP_TYPE_LIST or RFMXVNA_VAL_SWEEP_TYPE_LINEAR or RFMXVNA_VAL_SWEEP_TYPE_SEGMENT. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxVNA_GetXAxisValues |
