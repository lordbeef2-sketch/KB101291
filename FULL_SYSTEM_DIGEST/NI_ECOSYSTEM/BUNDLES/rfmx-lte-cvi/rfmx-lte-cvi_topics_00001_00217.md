# NI DOCUMENT BUNDLE: rfmx-lte-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-lte-cvi start=1 end=217 -->
<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_acpcfgnumberofeutraoffsets.html language=enus -->
## TOPIC 00001: RFmxLTE_ACPCfgNumberOfEUTRAOffsets

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_acpcfgnumberofeutraoffsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_acpcfgnumberofeutraoffsets.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ACPCfgNumberOfEUTRAOffsets

int32 __stdcall RFmxLTE_ACPCfgNumberOfEUTRAOffsets (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfEUTRAOffsets);

#### Purpose

Configures the number of evolved universal terrestrial radio access adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled attribute to **true**. 
Use "subblock<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. Example:"subblock0""signal::sig1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| numberOfEUTRAOffsets | int32 | Specifies the number of E-UTRA adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled attribute to true. In case of non-contiguous carrier aggregation, the configured value will be used only for the outer offsets and the offset channels in the gap region are defined as per the 3GPP specification. Offset integration bandwidth and offset power reference for the outer E-UTRA offsets are set according to the value of RFMXLTE_ATTR_ACP_EUTRA_OFFSET_DEFINITION attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_acpcfgnumberofgsmoffsets.html language=enus -->
## TOPIC 00002: RFmxLTE_ACPCfgNumberOfGSMOffsets

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_acpcfgnumberofgsmoffsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_acpcfgnumberofgsmoffsets.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ACPCfgNumberOfGSMOffsets

int32 __stdcall RFmxLTE_ACPCfgNumberOfGSMOffsets (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfGSMOffsets);

#### Purpose

Configures the number of GSM adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled attribute to **true**. 
Use "subblock<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. Example:"subblock0""signal::sig1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| numberOfGSMOffsets | int32 | Specifies the number of GSM adjacent channel offsets to be configured when the channel bandwidth is 200 kHz (NB-IOT), when you set the ACP Configurable Number of Offset Enabled attribute to true.The frequency offset from the center of NB-IOT carrier to the center of the first offset is 300 kHz as defined in the 3GPP specification. The center of every other offset is placed at 200 kHz from the previous offset's center. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_acpcfgrbwfilter.html language=enus -->
## TOPIC 00003: RFmxLTE_ACPCfgRBWFilter

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_acpcfgrbwfilter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_acpcfgrbwfilter.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ACPCfgRBWFilter

int32 __stdcall RFmxLTE_ACPCfgRBWFilter (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| RBWAuto | int32 | Specifies whether the measurement computes the RBW. RFMXLTE_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE (0) The measurement uses the RBW that you specify in the RBW parameter. RFMXLTE_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_TRUE (1) The measurement computes the RBW. |
| RFMXLTE_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE (0) | The measurement uses the RBW that you specify in the RBW parameter. |  |
| RFMXLTE_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_TRUE (1) | The measurement computes the RBW. |  |
| RBW | float64 | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBWAuto parameter to RFMXLTE_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE. This value is expressed in Hz. |
| RBWFilterType | int32 | Specifies the shape of the digital RBW filter. RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED (0) No RBW filtering is performed. RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN (1) An RBW filter with a Gaussian response is applied.RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_FLAT (2) An RBW filter with a flat response is applied. |
| RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |  |
| RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_analyzeiq1waveform.html language=enus -->
## TOPIC 00004: RFmxLTE_AnalyzeIQ1Waveform

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_analyzeiq1waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_analyzeiq1waveform.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_AnalyzeIQ1Waveform

int32 __stdcall RFmxLTE_AnalyzeIQ1Waveform (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[],
 float64 x0,
 float64 dx,
 NIComplexSingle IQ[],
 int32 arraySize,
 int32 reset,
 int64 reserved);

#### Purpose

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes. Use this function only if the is function only if the is function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?topicname=rfmxinstrcvi/rfmxinstr_attr_recommended_acquisition_type.html) attribute value is either tribute value is either RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ or RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ_OR_SPECTRAL.

When using the Analysis-Only mode in RFmxLTE, the RFmx ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

|  | Note Query the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute after calling the RFmxLTE_Commit function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| x0 | float64 | Specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | float64 | Specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| IQ | NIComplexSingle[] | Specifies the array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_autolevel.html language=enus -->
## TOPIC 00005: RFmxLTE_AutoLevel

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_autolevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_autolevel.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_AutoLevel

int32 __stdcall RFmxLTE_AutoLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 measurementInterval,
 float64* referenceLevel);

#### Purpose

Examines the input signal to calculate the peak power level and sets it as the value of the [RFMXLTE_ATTR_REFERENCE_LEVEL](/csh?topicname=rfmxltecvi/rfmxlte_attr_reference_level.html) attribute. Use this function to calculate an approximate setting for the reference level. 
The RFmxLTE Auto Level function completes the following tasks: 
You can also specify the starting reference level using [RFMXLTE_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL](/csh?topicname=rfmxltecvi/rfmxlte_attr_auto_level_initial_reference_level.html) attribute. 
When using PXIe-5663/5665/5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxLTE Auto Level function. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| measurementInterval | float64 | Specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the signal analyzer. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| Output |  |  |
| Name | Type | Description |
| referenceLevel | float64* | Returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_buildcarrierstring.html language=enus -->
## TOPIC 00006: RFmxLTE_BuildCarrierString

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_buildcarrierstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_buildcarrierstring.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_BuildCarrierString

int32 __stdcall RFmxLTE_BuildCarrierString (char selectorString[],
 int32 carrierNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the carrier string to use as the selector string with the SEM and ACP carrier configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| carrierNumber | int32 | Specifies the carrier number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_buildclusterstring.html language=enus -->
## TOPIC 00007: RFmxLTE_BuildClusterString

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_buildclusterstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_buildclusterstring.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_BuildClusterString

int32 __stdcall RFmxLTE_BuildClusterString (char selectorString[],
 int32 clusterNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a cluster string to use as the selector string with the ModAcc cluster configuration or the fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| clusterNumber | int32 | Specifies the cluster number. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_buildliststring.html language=enus -->
## TOPIC 00008: RFmxLTE_BuildListString

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_buildliststring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_buildliststring.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_BuildListString

int32 __stdcall RFmxLTE_BuildListString (char listName[],
 char resultName[],
 int32 selectorStringLength,
 char selectorString[]);

#### Purpose

Creates the list string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| listName | char[] | Specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix.Example:"list::samplelist1""samplelist1" |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix.Example:"result::r1""r1" |
| selectorStringLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| selectorString | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_buildoffsetstring.html language=enus -->
## TOPIC 00009: RFmxLTE_BuildOffsetString

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_buildoffsetstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_buildoffsetstring.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_BuildOffsetString

int32 __stdcall RFmxLTE_BuildOffsetString (char selectorString[],
 int32 offsetNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the offset string to use as the selector string with SEM and ACP offset configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| offsetNumber | int32 | Specifies the offset number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_buildpdschstring.html language=enus -->
## TOPIC 00010: RFmxLTE_BuildPDSCHString

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_buildpdschstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_buildpdschstring.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_BuildPDSCHString

int32 __stdcall RFmxLTE_BuildPDSCHString (char selectorString[],
 int32 pdschNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the PDSCH string to use as the selector string with the configuration or the fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number, carrier number, and subframe number. If you do not specify the signal name, the default signal instance is used. Example:"subblock0/carrier0/subframe0""signal::sig1/subblock0/carrier0/subframe0"You can use the RFmxLTE_BuildSubframeString function to build the selector string. |
| pdschNumber | int32 | Specifies the PDSCH channel number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_buildsignalstring.html language=enus -->
## TOPIC 00011: RFmxLTE_BuildSignalString

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_buildsignalstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_buildsignalstring.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_BuildSignalString

int32 __stdcall RFmxLTE_BuildSignalString (char signalName[],
 char resultName[],
 int32 selectorStringLength,
 char selectorString[]);

#### Purpose

Creates selector string for use with configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| signalName | char[] | Specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. Example:"signal::sig1""sig1" |
| resultName | char[] | Specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| selectorStringLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | char[] | Returns the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_buildsubblockstring.html language=enus -->
## TOPIC 00012: RFmxLTE_BuildSubblockString

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_buildsubblockstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_buildsubblockstring.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_BuildSubblockString

int32 __stdcall RFmxLTE_BuildSubblockString (char selectorString[],
 int32 subblockNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the subblock string to use as the selector string with the subblock configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| subblockNumber | int32 | Specifies the number of subblocks that are configured in the intra-band noncontiguous carrier aggregation. Set this parameter to 1, which is the default, for single carrier and intra-band contiguous carrier aggregation. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_buildsubframestring.html language=enus -->
## TOPIC 00013: RFmxLTE_BuildSubframeString

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_buildsubframestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_buildsubframestring.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_BuildSubframeString

int32 __stdcall RFmxLTE_BuildSubframeString (char selectorString[],
 int32 subframeNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the subframe string to use as the selector string with the configuration or the fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| subframeNumber | int32 | Specifies the subframe number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgautonpuschchanneldetectionenabled.html language=enus -->
## TOPIC 00014: RFmxLTE_CfgAutoNPUSCHChannelDetectionEnabled

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgautonpuschchanneldetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgautonpuschchanneldetectionenabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgAutoNPUSCHChannelDetectionEnabled

int32 __stdcall RFmxLTE_CfgAutoNPUSCHChannelDetectionEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 autoNPUSCHChannelDetectionEnabled);

#### Purpose

Configures whether the values of the [RFMXLTE_ATTR_NPUSCH_TONE_OFFSET](/csh?topicname=rfmxltecvi/rfmxlte_attr_npusch_tone_offset.html), NPUSCH Num Tones, and [RFMXLTE_ATTR_NPUSCH_MODULATION_TYPE](/csh?topicname=rfmxltecvi/rfmxlte_attr_npusch_modulation_type.html) attributes for the NPUSCH channel are auto-detected by the measurement or specified by you.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| autoNPUSCHChannelDetectionEnabled | int32 | Specifies whether the values of RFMXLTE_ATTR_NPUSCH_TONE_OFFSET, NPUSCH Number of Tones, and RFMXLTE_ATTR_NPUSCH_MODULATION_TYPE attributes are auto-detected by the measurement or specified by you. RFMXLTE_VAL_AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED_FALSE (0) The measurement uses the values that you specify for the RFMXLTE_ATTR_NPUSCH_TONE_OFFSET, NPUSCH Number of Tones, and NPUSCH ModType attributes.RFMXLTE_VAL_AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED_TRUE (1) The measurement uses the values of the RFMXLTE_ATTR_NPUSCH_TONE_OFFSET, NPUSCHÂ Number of Tones, and RFMXLTE_ATTR_NPUSCH_MODULATION_TYPE attributes that are auto-detected. |
| RFMXLTE_VAL_AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED_FALSE (0) | The measurement uses the values that you specify for the RFMXLTE_ATTR_NPUSCH_TONE_OFFSET, NPUSCH Number of Tones, and NPUSCH ModType attributes. |  |
| RFMXLTE_VAL_AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED_TRUE (1) | The measurement uses the values of the RFMXLTE_ATTR_NPUSCH_TONE_OFFSET, NPUSCHÂ Number of Tones, and RFMXLTE_ATTR_NPUSCH_MODULATION_TYPE attributes that are auto-detected. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgdownlinknumberofsubframes.html language=enus -->
## TOPIC 00015: RFmxLTE_CfgDownlinkNumberOfSubframes

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgdownlinknumberofsubframes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgdownlinknumberofsubframes.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgDownlinkNumberOfSubframes

int32 __stdcall RFmxLTE_CfgDownlinkNumberOfSubframes (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfSubframes);

#### Purpose

Configures the number of unique subframes that are transmitted from the DUT. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| numberOfSubframes | int32 | Specifies the number of subframes to be configured. If you set the RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE attribute to RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL, this parameter will be set to 10 for FDD and 20 for TDD by default. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgdownlinksynchronizationsignal.html language=enus -->
## TOPIC 00016: RFmxLTE_CfgDownlinkSynchronizationSignal

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgdownlinksynchronizationsignal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgdownlinksynchronizationsignal.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgDownlinkSynchronizationSignal

int32 __stdcall RFmxLTE_CfgDownlinkSynchronizationSignal (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 PSSPower,
 float64 SSSPower);

#### Purpose

Configures the synchronization signal power relative to the cell-specific reference signal. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| PSSPower | float64 | Specifies the power of the primary synchronization signal (PSS) relative to the power of the cell-specific reference signal. This value is expressed in dB. |
| SSSPower | float64 | Specifies the power of the secondary synchronization signal (SSS) relative to the power of the cell-specific reference signal. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgduplexscheme.html language=enus -->
## TOPIC 00017: RFmxLTE_CfgDuplexScheme

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgduplexscheme.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgduplexscheme.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgDuplexScheme

int32 __stdcall RFmxLTE_CfgDuplexScheme (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 duplexScheme,
 int32 uplinkDownlinkConfiguration);

#### Purpose

Configures the duplexing technique of the signal being measured.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| duplexScheme | int32 | Specifies the duplexing technique of the signal being measured. RFMXLTE_VAL_DUPLEX_SCHEME_FDD (0) Specifies that the duplexing technique is frequency-division duplexing. RFMXLTE_VAL_DUPLEX_SCHEME_TDD (1) Specifies that the duplexing technique is time-division duplexing. RFMXLTE_VAL_DUPLEX_SCHEME_LAA (2) Specifies that the duplexing technique is license assisted access. |
| RFMXLTE_VAL_DUPLEX_SCHEME_FDD (0) | Specifies that the duplexing technique is frequency-division duplexing. |  |
| RFMXLTE_VAL_DUPLEX_SCHEME_TDD (1) | Specifies that the duplexing technique is time-division duplexing. |  |
| RFMXLTE_VAL_DUPLEX_SCHEME_LAA (2) | Specifies that the duplexing technique is license assisted access. |  |
| uplinkDownlinkConfiguration | int32 | Specifies the configuration of the LTE frame structure in the time division duplex (TDD) mode. To configure the LTE frame, refer to table 4.2-2 of the 3GPP TS 36.211 specification.RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_0 (0) The configuration of the LTE frame structure in the TDD duplex mode is 0.RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_1 (1) The configuration of the LTE frame structure in the TDD duplex mode is 1.RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_2 (2) The configuration of the LTE frame structure in the TDD duplex mode is 2.RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_3 (3) The configuration of the LTE frame structure in the TDD duplex mode is 3.RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_4 (4) The configuration of the LTE frame structure in the TDD duplex mode is 4.RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_5 (5) The configuration of the LTE frame structure in the TDD duplex mode is 5.RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_6 (6) The configuration of the LTE frame structure in the TDD duplex mode is 6. |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_0 (0) | The configuration of the LTE frame structure in the TDD duplex mode is 0. |  |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_1 (1) | The configuration of the LTE frame structure in the TDD duplex mode is 1. |  |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_2 (2) | The configuration of the LTE frame structure in the TDD duplex mode is 2. |  |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_3 (3) | The configuration of the LTE frame structure in the TDD duplex mode is 3. |  |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_4 (4) | The configuration of the LTE frame structure in the TDD duplex mode is 4. |  |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_5 (5) | The configuration of the LTE frame structure in the TDD duplex mode is 5. |  |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_6 (6) | The configuration of the LTE frame structure in the TDD duplex mode is 6. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgemtcanalysisenabled.html language=enus -->
## TOPIC 00018: RFmxLTE_CfgEMTCAnalysisEnabled

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgemtcanalysisenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgemtcanalysisenabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgEMTCAnalysisEnabled

int32 __stdcall RFmxLTE_CfgEMTCAnalysisEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 EMTCAnalysisEnabled);

#### Purpose

Configures whether the component carrier contains an enhanced machine type communications (Cat-M1 or Cat-M2) transmission. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| EMTCAnalysisEnabled | int32 | Specifies whether the component carrier contains an eMTC transmission. RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_FALSE (0) The measurement considers the signal as LTE FDD/TDD transmission. RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_TRUE (1) Detects the eMTC half duplex pattern, narrow band hopping, and eMTC guard symbols present in the uplink transmission. |
| RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_FALSE (0) | The measurement considers the signal as LTE FDD/TDD transmission. |  |
| RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_TRUE (1) | Detects the eMTC half duplex pattern, narrow band hopping, and eMTC guard symbols present in the uplink transmission. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgenodebcategory.html language=enus -->
## TOPIC 00019: RFmxLTE_CfgeNodeBCategory

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgenodebcategory.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgenodebcategory.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgeNodeBCategory

int32 __stdcall RFmxLTE_CfgeNodeBCategory (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 eNodeBCategory);

#### Purpose

Configures the eNodeB category of the signal being measured.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| eNodeBCategory | int32 | Specifies the downlink eNodeB (Base Station) category. RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_A (0) Specifies the eNodeB is Wide Area Base Station - Category A.RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION1 (1) Specifies the eNodeB is Wide Area Base Station - Category B Option1.RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION2 (2) Specifies the eNodeB is Wide Area Base Station - Category B Option2.RFMXLTE_VAL_ENODEB_LOCAL_AREA_BASE_STATION (3) Specifies the eNodeB is Local Area Base Station.RFMXLTE_VAL_ENODEB_HOME_BASE_STATION (4) Specifies the eNodeB is Home Base Station.RFMXLTE_VAL_ENODEB_MEDIUM_RANGE_BASE_STATION (5) Specifies the eNodeB is Medium Range Base Station. |
| RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_A (0) | Specifies the eNodeB is Wide Area Base Station - Category A. |  |
| RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION1 (1) | Specifies the eNodeB is Wide Area Base Station - Category B Option1. |  |
| RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION2 (2) | Specifies the eNodeB is Wide Area Base Station - Category B Option2. |  |
| RFMXLTE_VAL_ENODEB_LOCAL_AREA_BASE_STATION (3) | Specifies the eNodeB is Local Area Base Station. |  |
| RFMXLTE_VAL_ENODEB_HOME_BASE_STATION (4) | Specifies the eNodeB is Home Base Station. |  |
| RFMXLTE_VAL_ENODEB_MEDIUM_RANGE_BASE_STATION (5) | Specifies the eNodeB is Medium Range Base Station. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgexternalattenuation.html language=enus -->
## TOPIC 00020: RFmxLTE_CfgExternalAttenuation

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgexternalattenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgexternalattenuation.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgExternalAttenuation

int32 __stdcall RFmxLTE_CfgExternalAttenuation (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 externalAttenuation);

#### Purpose

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| externalAttenuation | float64 | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgfrequencyearfcn.html language=enus -->
## TOPIC 00021: RFmxLTE_CfgFrequencyEARFCN

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgfrequencyearfcn.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgfrequencyearfcn.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgFrequencyEARFCN

int32 __stdcall RFmxLTE_CfgFrequencyEARFCN (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 linkDirection,
 int32 band,
 int32 EARFCN);

#### Purpose

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to the E-UTRA absolute radio frequency channel number (EARFCN) frequency. 
Use "subblock<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. Example:"subblock0""signal::sig1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| linkDirection | int32 | Specifies the link direction of the received signal. RFMXLTE_VAL_LINK_DIRECTION_DOWNLINK (0) The measurement uses 3GPP LTE downlink specification to measure the received signal.RFMXLTE_VAL_LINK_DIRECTION_UPLINK (1) The measurement uses 3GPP LTE uplink specification to measure the received signal. |
| RFMXLTE_VAL_LINK_DIRECTION_DOWNLINK (0) | The measurement uses 3GPP LTE downlink specification to measure the received signal. |  |
| RFMXLTE_VAL_LINK_DIRECTION_UPLINK (1) | The measurement uses 3GPP LTE uplink specification to measure the received signal. |  |
| band | int32 | Specifies the E-UTRA operating frequency band of a subblock as defined in section 5.2 of the 3GPP TS 36.521 specification. Valid values are from 1 to 256, inclusive. |
| EARFCN | int32 | Specifies the evolved universal terrestrial radio access (E-UTRA) absolute radio frequency channel number. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgnpuschformat.html language=enus -->
## TOPIC 00022: RFmxLTE_CfgNPUSCHFormat

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgnpuschformat.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgnpuschformat.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgNPUSCHFormat

int32 __stdcall RFmxLTE_CfgNPUSCHFormat (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 format);

#### Purpose

Configures the format of the narrowband physical uplink shared channel (NPUSCH). 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| format | int32 | Specifies the NPUSCH format. A value of 1 indicates that NPUSCH carries user data (UL-SCH) and a value of 2 indicates, NPUSCH carries uplink control information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgnumberofpdschchannels.html language=enus -->
## TOPIC 00023: RFmxLTE_CfgNumberOfPDSCHChannels

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgnumberofpdschchannels.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgnumberofpdschchannels.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgNumberOfPDSCHChannels

int32 __stdcall RFmxLTE_CfgNumberOfPDSCHChannels (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfPDSCHChannels);

#### Purpose

Configures the number of different physical downlink shared channel (PDSCH) allocations in a subframe. 
Use "subframe<*l*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/subframe<*l*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number, carrier number, and subframe number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0/subframe0""signal::sig1/subblock0/carrier0/subframe0"You can use the RFmxLTE_BuildSubframeString function to build the selector string. |
| numberOfPDSCHChannels | int32 | Specifies the number of PDSCH allocations in a subframe. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgnumberofpuschresourceblockclusters.html language=enus -->
## TOPIC 00024: RFmxLTE_CfgNumberOfPUSCHResourceBlockClusters

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgnumberofpuschresourceblockclusters.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgnumberofpuschresourceblockclusters.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgNumberOfPUSCHResourceBlockClusters

int32 __stdcall RFmxLTE_CfgNumberOfPUSCHResourceBlockClusters (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfResourceBlockClusters);

#### Purpose

Configures the number of clusters of resource allocations. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| numberOfResourceBlockClusters | int32 | Specifies the number resource allocation clusters, with each cluster including one or more consecutive resource blocks. For more information about the physical uplink shared channel (PUSCH) number of clusters, refer to 5.5.2.1.1 of the 3GPP TS 36.213 specification. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgnumberofsubblocks.html language=enus -->
## TOPIC 00025: RFmxLTE_CfgNumberOfSubblocks

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgnumberofsubblocks.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgnumberofsubblocks.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgNumberOfSubblocks

int32 __stdcall RFmxLTE_CfgNumberOfSubblocks (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfSubblocks);

#### Purpose

Configures the number of subblocks.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| numberOfSubblocks | int32 | Specifies the number of subblocks that are configured in the intra-band noncontiguous carrier aggregation. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgpcfich.html language=enus -->
## TOPIC 00026: RFmxLTE_CfgPCFICH

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgpcfich.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgpcfich.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgPCFICH

int32 __stdcall RFmxLTE_CfgPCFICH (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 CFI,
 float64 power);

#### Purpose

Configures the **CFI** and **power** parameters of the physical control format indicator channel (PCFICH). 
Use "subframe<*l*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/subframe<*l*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number, carrier number, and subframe number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0/subframe0""signal::sig1/subblock0/carrier0/subframe0"You can use the RFmxLTE_BuildSubframeString function to build the selector string. |
| CFI | int32 | Specifies the control format indicator (CFI) carried by PCFICH. CFI is used to compute the number of OFDM symbols which will determine the size of physical downlink control channel (PDCCH) within a subframe. |
| power | float64 | Specifies the power of the PCFICH relative to the power of the cell-specific reference signal. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_cfgreferencelevel.html language=enus -->
## TOPIC 00027: RFmxLTE_CfgReferenceLevel

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_cfgreferencelevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_cfgreferencelevel.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CfgReferenceLevel

int32 __stdcall RFmxLTE_CfgReferenceLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 referenceLevel);

#### Purpose

Configures the reference level, which represents the maximum expected power of an RF input signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| referenceLevel | float64 | Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_chpcfgsweeptime.html language=enus -->
## TOPIC 00028: RFmxLTE_CHPCfgSweepTime

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_chpcfgsweeptime.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_chpcfgsweeptime.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CHPCfgSweepTime

int32 __stdcall RFmxLTE_CHPCfgSweepTime (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 sweepTimeAuto,
 float64 sweepTimeInterval);

#### Purpose

Configures the sweep time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| sweepTimeAuto | int32 | Specifies whether the measurement computes the sweep time. RFMXLTE_VAL_CHP_SWEEP_TIME_AUTO_FALSE (0) The measurement uses the sweep time that you specify in the sweepTimeInterval parameter.RFMXLTE_VAL_CHP_SWEEP_TIME_AUTO_TRUE (1) The measurement uses a sweep time of 1 ms. |
| RFMXLTE_VAL_CHP_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the sweepTimeInterval parameter. |  |
| RFMXLTE_VAL_CHP_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses a sweep time of 1 ms. |  |
| sweepTimeInterval | float64 | Specifies the sweep time when you set the sweepTimeAuto parameter to RFMXLTE_VAL_CHP_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_chpfetchcomponentcarriermeasurementarray.html language=enus -->
## TOPIC 00029: RFmxLTE_CHPFetchComponentCarrierMeasurementArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_chpfetchcomponentcarriermeasurementarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_chpfetchcomponentcarriermeasurementarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CHPFetchComponentCarrierMeasurementArray

int32 __stdcall RFmxLTE_CHPFetchComponentCarrierMeasurementArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 absolutePower[],
 float64 relativePower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns an array of the absolute and relative powers measured in the component carriers. The relative power is relative to subblock power. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| absolutePower | float64[] | Returns the array of powers measured over the integration bandwidths of the component carriers in a subblock. |
| relativePower | float64[] | Returns the array of component carrier powers relative to their subblock powers measured over the integration bandwidths of the component carriers in the subblock. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_clonesignalconfiguration.html language=enus -->
## TOPIC 00030: RFmxLTE_CloneSignalConfiguration

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_clonesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_clonesignalconfiguration.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CloneSignalConfiguration

int32 __stdcall RFmxLTE_CloneSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char oldSignalName[],
 char newSignalName[]);

#### Purpose

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| oldSignalName | char[] | Specifies the name of the existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::OldSigName""OldSigName" |
| newSignalName | char[] | Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_createsignalconfiguration.html language=enus -->
## TOPIC 00031: RFmxLTE_CreateSignalConfiguration

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_createsignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_createsignalconfiguration.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_CreateSignalConfiguration

int32 __stdcall RFmxLTE_CreateSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char signalName[]);

#### Purpose

Creates a new instance of a signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| signalName | char[] | Specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_getattributei8.html language=enus -->
## TOPIC 00032: RFmxLTE_GetAttributeI8

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_getattributei8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_getattributei8.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_GetAttributeI8

int32 __stdcall RFmxLTE_GetAttributeI8 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_getattributei8array.html language=enus -->
## TOPIC 00033: RFmxLTE_GetAttributeI8Array

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_getattributei8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_getattributei8array.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_GetAttributeI8Array

int32 __stdcall RFmxLTE_GetAttributeI8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_initialize.html language=enus -->
## TOPIC 00034: rfmxlte_Initialize

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_initialize.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_Initialize

int32 __stdcall RFmxLTE_Initialize (char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession);

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
| optionString | char[] | Sets the initial value of certain attributes for the session. The following attributes are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about attributes used in this parameter, refer to the NI RF Vector Signal Analyzers Help. The format of this string is "AttributeName=Value", where AttributeName is the name of the attribute and Value is the value to which the attribute is set. For example, you can simulate an PXIe-5663E using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple attributes, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx uses yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |
|  | Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |  |
| isNewSession | int32* | Returns RFMXLTE_VAL_TRUE if the function created a new session, or RFMXLTE_VAL_FALSE if the function returned a reference to an existing session. |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Identifies your instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modacccfgaveraging.html language=enus -->
## TOPIC 00035: RFmxLTE_ModAccCfgAveraging

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modacccfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modacccfgaveraging.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccCfgAveraging

int32 __stdcall RFmxLTE_ModAccCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount);

#### Purpose

Configures averaging for the ModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_TRUE (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the averagingCount parameter. |
| RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_TRUE (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the averagingCount parameter. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_TRUE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modacccfgcommonclocksourceenabled.html language=enus -->
## TOPIC 00036: RFmxLTE_ModAccCfgCommonClockSourceEnabled

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modacccfgcommonclocksourceenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modacccfgcommonclocksourceenabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccCfgCommonClockSourceEnabled

int32 __stdcall RFmxLTE_ModAccCfgCommonClockSourceEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 commonClockSourceEnabled);

#### Purpose

Configures the Reference Clock and specifies whether same Reference Clock is used for local oscillator and D/A converter. 
The modacc measurement ignores this function, when you set the [RFMXLTE_ATTR_LINK_DIRECTION](/csh?topicname=rfmxltecvi/rfmxlte_attr_link_direction.html) attribute to RFMXLTE_VAL_LINK_DIRECTION_DOWNLINK.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| commonClockSourceEnabled | int32 | Specifies whether the same Reference Clock is used for the local oscillator and the D/A converter. When the same Reference Clock is used, the carrier frequency offset is proportional to the Sample Clock error. RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE (0) The Sample Clock error is estimated independently.RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE (1) The Sample Clock error is estimated from carrier frequency offset. |
| RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE (0) | The Sample Clock error is estimated independently. |  |
| RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE (1) | The Sample Clock error is estimated from carrier frequency offset. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modacccfgevmunit.html language=enus -->
## TOPIC 00037: RFmxLTE_ModAccCfgEVMUnit

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modacccfgevmunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modacccfgevmunit.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccCfgEVMUnit

int32 __stdcall RFmxLTE_ModAccCfgEVMUnit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 EVMUnit);

#### Purpose

Configures the units of the EVM results.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| EVMUnit | int32 | Specifies the units of the EVM results. RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE (0) The EVM is reported in percentage.RFMXLTE_VAL_MODACC_EVM_UNIT_DB (1) The EVM is reported in dB. |
| RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE (0) | The EVM is reported in percentage. |  |
| RFMXLTE_VAL_MODACC_EVM_UNIT_DB (1) | The EVM is reported in dB. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modacccfgfftwindowoffset.html language=enus -->
## TOPIC 00038: RFmxLTE_ModAccCfgFFTWindowOffset

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modacccfgfftwindowoffset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modacccfgfftwindowoffset.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccCfgFFTWindowOffset

int32 __stdcall RFmxLTE_ModAccCfgFFTWindowOffset (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 FFTWindowOffset);

#### Purpose

Configures the position of the FFT window that is used to calculate the EVM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| FFTWindowOffset | float64 | Specifies the position of the FFT window that is used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this parameter to 0, the EVM window starts from the end of cyclic prefix. If you set this parameter to 100, the EVM window starts from the beginning of cyclic prefix. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modacccfgfftwindowposition.html language=enus -->
## TOPIC 00039: RFmxLTE_ModAccCfgFFTWindowPosition

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modacccfgfftwindowposition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modacccfgfftwindowposition.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccCfgFFTWindowPosition

int32 __stdcall RFmxLTE_ModAccCfgFFTWindowPosition (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 FFTWindowType,
 float64 FFTWindowOffset,
 float64 FFTWindowLength);

#### Purpose

Configures the FFT window position used for an EVM calculation. 
Refer to the LTE Modulation Accuracy (ModAcc) topic for more information about FFT window position.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| FFTWindowType | int32 | Specifies the FFT window type used for an EVM calculation. RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_3GPP (0) The maximum EVM between the start window position and the end window position is returned according to the 3GPP specification. The window positions are specified by the FFTWindowLength parameter. For more information about the FFT window specification, refer to the 3GPP TS 36.521 specification, Annexe E.3.2. RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_CUSTOM (1) Only one FFT window position is used for the EVM calculation. The FFT window position is specified by the FFTWindowOffset parameter. |
| RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_3GPP (0) | The maximum EVM between the start window position and the end window position is returned according to the 3GPP specification. The window positions are specified by the FFTWindowLength parameter. For more information about the FFT window specification, refer to the 3GPP TS 36.521 specification, Annexe E.3.2. |  |
| RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_CUSTOM (1) | Only one FFT window position is used for the EVM calculation. The FFT window position is specified by the FFTWindowOffset parameter. |  |
| FFTWindowOffset | float64 | Specifies the position of the FFT window used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this parameter to 0, the EVM window starts from the end of cyclic prefix. If you set this parameter to 100, the EVM window starts from the beginning of cyclic prefix. |
| FFTWindowLength | float64 | Specifies the FFT window length. This value is expressed in a percentage of the cyclic prefix length. This parameter is used when you set the FFTWindowType parameter to RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_3GPP, where you need to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modacccfginbandemissionmasktype.html language=enus -->
## TOPIC 00040: RFmxLTE_ModAccCfgInBandEmissionMaskType

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modacccfginbandemissionmasktype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modacccfginbandemissionmasktype.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccCfgInBandEmissionMaskType

int32 __stdcall RFmxLTE_ModAccCfgInBandEmissionMaskType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 inBandEmissionMaskType);

#### Purpose

Configures the **inBandEmissionMaskType** parameter to be used.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| inBandEmissionMaskType | int32 | Specifies the in-band emissions mask type to be used for measuring in-band emission margin (dB) and subblock in-Band emission margin (dB) results. Refer to section 6.5.2.3.5 of the 3GPP 36.521-1 specification for more information.RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_8_10 (0) Specifies the mask type to be used for UE, supporting 3GPP Release 8 to 3GPP Release 10 specification.RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_11_ONWARDS (1) Specifies the mask type to be used for UE, supporting 3GPP Release 11 and higher specification. |
| RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_8_10 (0) | Specifies the mask type to be used for UE, supporting 3GPP Release 8 to 3GPP Release 10 specification. |  |
| RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_11_ONWARDS (1) | Specifies the mask type to be used for UE, supporting 3GPP Release 11 and higher specification. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchcsrsevm.html language=enus -->
## TOPIC 00041: RFmxLTE_ModAccFetchCSRSEVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchcsrsevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchcsrsevm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchCSRSEVM

int32 __stdcall RFmxLTE_ModAccFetchCSRSEVM (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* meanRMSCSRSEVM);

#### Purpose

Fetches the cell-specific reference signal EVM. 
Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanRMSCSRSEVM | float64* | Returns the mean value of RMS EVMs calculated on Reference Signal (RS) resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement is returned in percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement is returned in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchdownlinkdetectedcellid.html language=enus -->
## TOPIC 00042: RFmxLTE_ModAccFetchDownlinkDetectedCellID

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchdownlinkdetectedcellid.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchdownlinkdetectedcellid.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchDownlinkDetectedCellID

int32 __stdcall RFmxLTE_ModAccFetchDownlinkDetectedCellID (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* detectedCellID);

#### Purpose

Fetches the detected cell ID. This function is valid only when the measured signal contains primary synchronization signal (PSS) and secondary synchronization signal (SSS). 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| detectedCellID | int32* | Returns the detected cell ID value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchdownlinkdetectedcellidarray.html language=enus -->
## TOPIC 00043: RFmxLTE_ModAccFetchDownlinkDetectedCellIDArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchdownlinkdetectedcellidarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchdownlinkdetectedcellidarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchDownlinkDetectedCellIDArray

int32 __stdcall RFmxLTE_ModAccFetchDownlinkDetectedCellIDArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 detectedCellID[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the array of detected cell IDs for all the component carriers within the subblock. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| detectedCellID | int32[] | Returns the array of the detected cell ID values. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchdownlinkpbchconstellation.html language=enus -->
## TOPIC 00044: RFmxLTE_ModAccFetchDownlinkPBCHConstellation

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchdownlinkpbchconstellation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchdownlinkpbchconstellation.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchDownlinkPBCHConstellation

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPBCHConstellation (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle PBCHConstellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the PBCH constellation trace for the control channels. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| PBCHConstellation | NIComplexSingle[] | Returns the PBCH constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchdownlinkpdcchconstellation.html language=enus -->
## TOPIC 00045: RFmxLTE_ModAccFetchDownlinkPDCCHConstellation

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchdownlinkpdcchconstellation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchdownlinkpdcchconstellation.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchDownlinkPDCCHConstellation

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPDCCHConstellation (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle PDCCHConstellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the PDCCH constellation trace for the control channels. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| PDCCHConstellation | NIComplexSingle[] | Returns the PDCCH constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchdownlinkpdcchconstellationsplit.html language=enus -->
## TOPIC 00046: RFmxLTE_ModAccFetchDownlinkPDCCHConstellationSplit

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchdownlinkpdcchconstellationsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchdownlinkpdcchconstellationsplit.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchDownlinkPDCCHConstellationSplit

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPDCCHConstellationSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the in-phase and quadrature-phase part of PDCCH constellation trace for the control channels. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result:r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| I | float32[] | Returns the in-phase part of PDCCH constellation trace. |
| Q | float32[] | Returns the quadrature-phase part of PDCCH constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchdownlinkphichconstellation.html language=enus -->
## TOPIC 00047: RFmxLTE_ModAccFetchDownlinkPHICHConstellation

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchdownlinkphichconstellation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchdownlinkphichconstellation.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchDownlinkPHICHConstellation

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPHICHConstellation (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle PHICHConstellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the PHICH constellation trace for the control channels. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| PHICHConstellation | NIComplexSingle[] | Returns the PHICH constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchdownlinkphichconstellationsplit.html language=enus -->
## TOPIC 00048: RFmxLTE_ModAccFetchDownlinkPHICHConstellationSplit

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchdownlinkphichconstellationsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchdownlinkphichconstellationsplit.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchDownlinkPHICHConstellationSplit

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPHICHConstellationSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the in-phase and quadrature-phase part of PHICH constellation trace for the control channels. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result:r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| I | float32[] | Returns the in-phase part of PHICH constellation trace. |
| Q | float32[] | Returns the quadrature-phase part of PHICH constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchevmhighpersymboltrace.html language=enus -->
## TOPIC 00049: RFmxLTE_ModAccFetchEVMHighPerSymbolTrace

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchevmhighpersymboltrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchevmhighpersymboltrace.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchEVMHighPerSymbolTrace

int32 __stdcall RFmxLTE_ModAccFetchEVMHighPerSymbolTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 EVMHighPerSymbol[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the EVM per symbol trace for all the configured slots. The EVM is obtained by using the FFT window position, Delta_C+W/2. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM symbol position corresponding to the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | float64* | Returns 1 as the value. |
| EVMHighPerSymbol | float32[] | Returns the array of the EVM per symbol trace for all the configured slots. The EVM is obtained by using FFT window position, Delta_C+W/2. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchinbandemissionmarginarray.html language=enus -->
## TOPIC 00050: RFmxLTE_ModAccFetchInBandEmissionMarginArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchinbandemissionmarginarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchinbandemissionmarginarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchInBandEmissionMarginArray

int32 __stdcall RFmxLTE_ModAccFetchInBandEmissionMarginArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 inBandEmissionMargin[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns an array of margins on non allocated resource blocks (RBs) in the uplink signal for all component carriers within the subblock. 
The function result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](/csh?topicname=rfmxltecvi/rfmxlte_attr_link_direction.html) attribute to RFMXLTE_VAL_LINK_DIRECTION_UPLINK. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| inBandEmissionMargin | float64[] | Returns the array of the in-band emission margins. The margin is the least difference between the in-band emission measurement trace and limit trace. The limit is defined in section 6.5.2.3.5 of the 3GPP TS 36.521 specification. The in-band emissions are a measure of the interference falling into the non-allocated resources blocks. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchmaximumfrequencyerrorperslottrace.html language=enus -->
## TOPIC 00051: RFmxLTE_ModAccFetchMaximumFrequencyErrorPerSlotTrace

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchmaximumfrequencyerrorperslottrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchmaximumfrequencyerrorperslottrace.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchMaximumFrequencyErrorPerSlotTrace

int32 __stdcall RFmxLTE_ModAccFetchMaximumFrequencyErrorPerSlotTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 maximumFrequencyErrorPerSlot[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the <strong>arraySize</strong> parameter to 0 to get the size of all the arrays in the <strong>actualArraySize</strong> parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM slot position corresponding to the ModAcc Meas Offset property. |
| dx | float64* | Returns 1 as the value. |
| maximumFrequencyErrorPerSlot | float32[] | Returns an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the <strong>arraySize</strong> parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchmaximummagnitudeerrorpersymboltrace.html language=enus -->
## TOPIC 00052: RFmxLTE_ModAccFetchMaximumMagnitudeErrorPerSymbolTrace

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchmaximummagnitudeerrorpersymboltrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchmaximummagnitudeerrorpersymboltrace.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchMaximumMagnitudeErrorPerSymbolTrace

int32 __stdcall RFmxLTE_ModAccFetchMaximumMagnitudeErrorPerSymbolTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 maximumMagnitudeErrorPerSymbol[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the peak value of the magnitude error for each symbol computed across all the allocated subcarriers. 
The function result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](/csh?topicname=rfmxltecvi/rfmxlte_attr_link_direction.html) attribute to RFMXLTE_VAL_LINK_DIRECTION_UPLINK. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM symbol position corresponding to the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | float64* | Returns 1 as the value. |
| maximumMagnitudeErrorPerSymbol | float32[] | Returns the array of the peak value of the magnitude error for each symbol computed across all the allocated subcarriers. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchnpuschconstellationtrace.html language=enus -->
## TOPIC 00053: RFmxLTE_ModAccFetchNPUSCHConstellationTrace

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchnpuschconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchnpuschconstellationtrace.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchNPUSCHConstellationTrace

int32 __stdcall RFmxLTE_ModAccFetchNPUSCHConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle dataConstellation[],
 int32 dataConstellationArraySize,
 int32* dataConstellationActualArraySize,
 NIComplexSingle DMRSConstellation[],
 int32 DMRSConstellationArraySize,
 int32* DMRSConstellationActualArraySize);

#### Purpose

Returns the recovered narrowband physical uplink shared channel (NPUSCH) constellation points. The constellation points of different slots in the measurement length are concatenated. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| dataConstellationArraySize | int32 | Specifies the size of dataConstellationI and dataConstellationQ array. Set the dataConstellationArraySize parameter to 0 to get the size of dataConstellationI and dataConstellationQ array in the dataConstellationActualArraySize parameter. |
| DMRSConstellationArraySize | int32 | Specifies the size of DMRSConstellationI and DMRSConstellationQ array. Set the DMRSConstellationArraySize parameter to 0 to get the size of DMRSConstellationI and DMRSConstellationQ array in the DMRSConstellationActualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| dataConstellation | NIComplexSingle[] | Returns the data constellation trace. |
| dataConstellationActualArraySize | int32* | Returns the actual size of dataConstellationI and dataConstellationQ array, if you pass NULL to all output array parameters, and set the dataConstellationArraySize parameter to 0. |
| DMRSConstellation | NIComplexSingle[] | Returns the demodulation reference signal (DMRS) constellation trace. |
| DMRSConstellationActualArraySize | int32* | Returns the actual size of DMRSConstellationI and DMRSConstellationQ array, if you pass NULL to all output array parameters, and set the DMRSConstellationArraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchpdschevmarray.html language=enus -->
## TOPIC 00054: RFmxLTE_ModAccFetchPDSCHEVMArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchpdschevmarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchpdschevmarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchPDSCHEVMArray

int32 __stdcall RFmxLTE_ModAccFetchPDSCHEVMArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 meanRMSEVM[],
 float64 meanRMSQPSKEVM[],
 float64 meanRMS16QAMEVM[],
 float64 meanRMS64QAMEVM[],
 float64 meanRMS256QAMEVM[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the array of physical downlink shared channel (PDSCH) EVM for all the component carriers within the subblock. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| meanRMSEVM | float64[] | Returns the array of mean values of RMS EVMs calculated on the PDSCH data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement is returned in percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement is returned in dB. |
| meanRMSQPSKEVM | float64[] | Returns the array of mean values of RMS EVMs calculated on all QPSK modulated PDSCH resource blocks over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement is returned in percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement is returned in dB. |
| meanRMS16QAMEVM | float64[] | Returns the array of mean values of RMS EVMs calculated on all 16 QAM modulated PDSCH resource blocks over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement is returned in percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement is returned in dB. |
| meanRMS64QAMEVM | float64[] | Returns the array of mean values of RMS EVMs calculated on all 64 QAM modulated PDSCH resource blocks over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement is returned in percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement is returned in dB. |
| meanRMS256QAMEVM | float64[] | Returns the array of mean values of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement is returned in percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement is returned in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchpuschdataevmarray.html language=enus -->
## TOPIC 00055: RFmxLTE_ModAccFetchPUSCHDataEVMArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchpuschdataevmarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchpuschdataevmarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchPUSCHDataEVMArray

int32 __stdcall RFmxLTE_ModAccFetchPUSCHDataEVMArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 meanRMSDataEVM[],
 float64 maximumPeakDataEVM[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns an array of the Mean RMS PUSCH data EVM and the maximum peak PUSCH data EVM. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| meanRMSDataEVM | float64[] | Returns the array of the mean value of the RMS EVMs calculated on PUSCH data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| maximumPeakDataEVM | float64[] | Returns the array of the maximum value of the peak EVMs calculated on PUSCH data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchpuschdmrsevm.html language=enus -->
## TOPIC 00056: RFmxLTE_ModAccFetchPUSCHDMRSEVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchpuschdmrsevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchpuschdmrsevm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchPUSCHDMRSEVM

int32 __stdcall RFmxLTE_ModAccFetchPUSCHDMRSEVM (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* meanRMSDMRSEVM,
 float64* maximumPeakDMRSEVM);

#### Purpose

Fetches the EVM values calculated on PUSCH DMRS calculated over the length of the measurement. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanRMSDMRSEVM | float64* | Returns the mean value of RMS EVMs calculated on PUSCH DMRS over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dB or in percentage. |
| maximumPeakDMRSEVM | float64* | Returns the maximum value of peak EVMs calculated on PUSCH DMRS over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dB or in percentage. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchpuschdmrsevmarray.html language=enus -->
## TOPIC 00057: RFmxLTE_ModAccFetchPUSCHDMRSEVMArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchpuschdmrsevmarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchpuschdmrsevmarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchPUSCHDMRSEVMArray

int32 __stdcall RFmxLTE_ModAccFetchPUSCHDMRSEVMArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 meanRMSDMRSEVM[],
 float64 maximumPeakDMRSEVM[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns an array of the PUSCH mean RMS DMRS EVM and the PUSCH maximum peak DMRS EVM of all the component carriers within the subblock. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| meanRMSDMRSEVM | float64[] | Returns the array of the mean value of RMS EVMs calculated on PUSCH DMRS over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| maximumPeakDMRSEVM | float64[] | Returns the array of the maximum value of peak EVMs calculated on PUSCH DMRS over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dB or in percentage. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchpuschsymbolpower.html language=enus -->
## TOPIC 00058: RFmxLTE_ModAccFetchPUSCHSymbolPower

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchpuschsymbolpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchpuschsymbolpower.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchPUSCHSymbolPower

int32 __stdcall RFmxLTE_ModAccFetchPUSCHSymbolPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* PUSCHMeanDataPower,
 float64* PUSCHMeanDMRSPower);

#### Purpose

Fetches the physical uplink shared channel (PUSCH) symbol power measurement. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| PUSCHMeanDataPower | float64* | Returns the mean value of the power calculated on PUSCH data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| PUSCHMeanDMRSPower | float64* | Returns the mean value of the power calculated on PUSCH DMRS over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchrmsmagnitudeerrorpersymboltrace.html language=enus -->
## TOPIC 00059: RFmxLTE_ModAccFetchRMSMagnitudeErrorPerSymbolTrace

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchrmsmagnitudeerrorpersymboltrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchrmsmagnitudeerrorpersymboltrace.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchRMSMagnitudeErrorPerSymbolTrace

int32 __stdcall RFmxLTE_ModAccFetchRMSMagnitudeErrorPerSymbolTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 RMSMagnitudeErrorPerSymbol[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the RMS mean value of the magnitude error for each symbol computed over all the allocated subcarriers and within the measurement length. 
The function result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](/csh?topicname=rfmxltecvi/rfmxlte_attr_link_direction.html) attribute to RFMXLTE_VAL_LINK_DIRECTION_UPLINK. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM symbol position corresponding to the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | float64* | Returns 1 as the value. |
| RMSMagnitudeErrorPerSymbol | float32[] | Returns the RMS mean value of the magnitude error for each symbol computed over all the allocated subcarriers and within the measurement length. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchsrsconstellationsplit.html language=enus -->
## TOPIC 00060: RFmxLTE_ModAccFetchSRSConstellationSplit

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchsrsconstellationsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchsrsconstellationsplit.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchSRSConstellationSplit

int32 __stdcall RFmxLTE_ModAccFetchSRSConstellationSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the in-phase and quadrature-phase part of constellation trace for the SRS channel. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result:r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| I | float32[] | Returns the in-phase part of SRS constellation trace. |
| Q | float32[] | Returns the quadrature-phase part of SRS constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchsynchronizationsignalconstellation.html language=enus -->
## TOPIC 00061: RFmxLTE_ModAccFetchSynchronizationSignalConstellation

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchsynchronizationsignalconstellation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchsynchronizationsignalconstellation.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchSynchronizationSignalConstellation

int32 __stdcall RFmxLTE_ModAccFetchSynchronizationSignalConstellation (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle SSSConstellation[],
 NIComplexSingle PSSConstellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the constellations traces for PSS and SSS. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| SSSConstellation | NIComplexSingle[] | Returns SSS constellation trace. |
| PSSConstellation | NIComplexSingle[] | Returns PSS constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchsynchronizationsignalconstellationsplit.html language=enus -->
## TOPIC 00062: RFmxLTE_ModAccFetchSynchronizationSignalConstellationSplit

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchsynchronizationsignalconstellationsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchsynchronizationsignalconstellationsplit.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchSynchronizationSignalConstellationSplit

int32 __stdcall RFmxLTE_ModAccFetchSynchronizationSignalConstellationSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 SSSConstellationI[],
 float32 SSSConstellationQ[],
 float32 PSSConstellationI[],
 float32 PSSConstellationQ[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the in-phase and quadrature-phase part of constellations traces for PSS and SSS. 

 Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result:r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of SSSConstellationI, SSSConstellationQ, PSSConstellationI and PSSConstellationQ array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| SSSConstellationI | float32[] | Returns the in-phase part of SSS constellation trace. |
| SSSConstellationQ | float32[] | Returns the quadrature-phase part of SSS constellation trace. |
| PSSConstellationI | float32[] | Returns the in-phase part of PSS constellation trace. |
| PSSConstellationQ | float32[] | Returns the quadrature-phase part of PSS constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_modaccfetchsynchronizationsignalevmarray.html language=enus -->
## TOPIC 00063: RFmxLTE_ModAccFetchSynchronizationSignalEVMArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_modaccfetchsynchronizationsignalevmarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_modaccfetchsynchronizationsignalevmarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ModAccFetchSynchronizationSignalEVMArray

int32 __stdcall RFmxLTE_ModAccFetchSynchronizationSignalEVMArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 meanRMSPSSEVM[],
 float64 meanRMSSSSEVM[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the array of primary synchronization signal (PSS) EVMs and secondary synchronization signal (SSS) EVMS for all the component carriers within a subblock. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| meanRMSPSSEVM | float64[] | Returns the array of mean values of RMS EVMs calculated on PSS channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement is returned in percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement is returned in dB. |
| meanRMSSSSEVM | float64[] | Returns the array of mean values of RMS EVMs calculated on SSS channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement is returned in percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement is returned in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_obwcfgrbwfilter.html language=enus -->
## TOPIC 00064: RFmxLTE_OBWCfgRBWFilter

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_obwcfgrbwfilter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_obwcfgrbwfilter.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_OBWCfgRBWFilter

int32 __stdcall RFmxLTE_OBWCfgRBWFilter (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| RBWAuto | int32 | Specifies whether the measurement computes the RBW. RFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_FALSE (0) The measurement uses the RBW that you specify in the RBW parameter.RFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_TRUE (1) The measurement computes the RBW. |
| RFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_FALSE (0) | The measurement uses the RBW that you specify in the RBW parameter. |  |
| RFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_TRUE (1) | The measurement computes the RBW. |  |
| RBW | float64 | Specifies the bandwidth of the resolution bandwidth (RBW) filter, used to sweep the acquired signal, when you set the RBWAuto parameter to RFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_FALSE. This value is expressed in Hz. |
| RBWFilterType | int32 | Specifies the shape of the digital RBW filter. RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED (0) No RBW filtering is performed. RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN (1) An RBW filter with a Gaussian response is applied.RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_FLAT (2) An RBW filter with a flat response is applied. |
| RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |  |
| RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_obwfetchmeasurement.html language=enus -->
## TOPIC 00065: RFmxLTE_OBWFetchMeasurement

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_obwfetchmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_obwfetchmeasurement.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_OBWFetchMeasurement

int32 __stdcall RFmxLTE_OBWFetchMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* occupiedBandwidth,
 float64* absolutePower,
 float64* startFrequency,
 float64* stopFrequency);

#### Purpose

Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock. 
Use "subblock<*n*>" as the selector string to read results from this function. 
Refer to the LTE Occupied Bandwidth topic for more information about OBW measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| occupiedBandwidth | float64* | Returns the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. |
| absolutePower | float64* | Returns the power measured over the integration bandwidth of the carrier/subblock. |
| startFrequency | float64* | Returns the start frequency of the subblock. The occupied bandwidth of a carrier/subblock is calculated using the following equation: Stop frequency - Start frequency = Occupied bandwidth. |
| stopFrequency | float64* | Returns the stop frequency of the subblock. The occupied bandwidth of a carrier/subblock is calculated using the following equation: Stop frequency - Start frequency = Occupied bandwidth. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_obwfetchspectrum.html language=enus -->
## TOPIC 00066: RFmxLTE_OBWFetchSpectrum

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_obwfetchspectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_obwfetchspectrum.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_OBWFetchSpectrum

int32 __stdcall RFmxLTE_OBWFetchSpectrum (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 spectrum[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the spectrum used for OBW measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency of the channel. This value is expressed in Hz. |
| dx | float64* | Returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | float32[] | Returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_pvtfetchsignalpowertrace.html language=enus -->
## TOPIC 00067: RFmxLTE_PVTFetchSignalPowerTrace

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_pvtfetchsignalpowertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_pvtfetchsignalpowertrace.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_PVTFetchSignalPowerTrace

int32 __stdcall RFmxLTE_PVTFetchSignalPowerTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 signalPower[],
 float32 absoluteLimit[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the instantaneous signal power trace along with absolute limit for each segment in the trace as specified by section 6.5.2.4.5 of the *3GPP 36.521*. This value is expressed in dBm. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns start time of the signal. This value is expressed in seconds. |
| dx | float64* | Returns the time bin spacing. This value is expressed in seconds. |
| signalPower | float32[] | Returns the instantaneous signal power trace. This value is expressed in dBm. |
| absoluteLimit | float32[] | Returns absolute limit for each segment in the trace as specified by section 6.5.2.4.5 of the 3GPP 36.521 specification. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_resetattribute.html language=enus -->
## TOPIC 00068: RFmxLTE_ResetAttribute

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_resetattribute.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_resetattribute.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ResetAttribute

int32 __stdcall RFmxLTE_ResetAttribute (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID);

#### Purpose

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being reset. Refer to the selector string topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_resettodefault.html language=enus -->
## TOPIC 00069: RFmxLTE_ResetToDefault

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_resettodefault.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_resettodefault.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_ResetToDefault

int32 __stdcall RFmxLTE_ResetToDefault (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Resets a signal to the default values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_semcfgoffsetabsolutelimit.html language=enus -->
## TOPIC 00070: RFmxLTE_SEMCfgOffsetAbsoluteLimit

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_semcfgoffsetabsolutelimit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_semcfgoffsetabsolutelimit.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SEMCfgOffsetAbsoluteLimit

int32 __stdcall RFmxLTE_SEMCfgOffsetAbsoluteLimit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 offsetAbsoluteLimitStart,
 float64 offsetAbsoluteLimitStop);

#### Purpose

Configures the start and the stop limit of an offset segment. 
Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example:"subblock0/offset0""signal::sig1/subblock0/offset0"You can use the RFmxLTE_BuildOffsetString function to build the selector string. |
| offsetAbsoluteLimitStart | float64 | Specifies the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. |
| offsetAbsoluteLimitStop | float64 | Specifies the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_semcfgoffsetfrequency.html language=enus -->
## TOPIC 00071: RFmxLTE_SEMCfgOffsetFrequency

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_semcfgoffsetfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_semcfgoffsetfrequency.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SEMCfgOffsetFrequency

int32 __stdcall RFmxLTE_SEMCfgOffsetFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 offsetStartFrequency,
 float64 offsetStopFrequency,
 int32 offsetSideband);

#### Purpose

Configures the start and stop frequencies and the sideband of an offset segment. 
Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to configure from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example:"subblock0/offset0""signal::sig1/subblock0/offset0"You can use the RFmxLTE_BuildOffsetString function to build the selector string. |
| offsetStartFrequency | float64 | Specifies the start frequency of an offset segment relative to the carrier channel bandwidth edge (single-carrier) or the subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. |
| offsetStopFrequency | float64 | Specifies the stop frequency of an offset segment relative to the carrier channel bandwidth edge (single-carrier) or the subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. |
| offsetSideband | int32 | Specifies whether the offset segment is present on one side, or on both sides of the carrier. RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE (0) Configures a lower offset segment to the left of the leftmost carrier.RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_POSITIVE (1) Configures an upper offset segment to the right of the rightmost carrier.RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_BOTH (2) Configures both the negative and the positive offset segments. |
| RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE (0) | Configures a lower offset segment to the left of the leftmost carrier. |  |
| RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_POSITIVE (1) | Configures an upper offset segment to the right of the rightmost carrier. |  |
| RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_BOTH (2) | Configures both the negative and the positive offset segments. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_semcfgoffsetfrequencyarray.html language=enus -->
## TOPIC 00072: RFmxLTE_SEMCfgOffsetFrequencyArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_semcfgoffsetfrequencyarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_semcfgoffsetfrequencyarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SEMCfgOffsetFrequencyArray

int32 __stdcall RFmxLTE_SEMCfgOffsetFrequencyArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 offsetStartFrequency[],
 float64 offsetStopFrequency[],
 int32 offsetSideband[],
 int32 numberOfElements);

#### Purpose

Configures the arrays of the start and stop frequencies and the sideband of an offset segment. 
Use "subblock<*n*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| offsetStartFrequency | float64[] | Specifies the array of the start frequency values of the offset segment relative to the carrier channel bandwidth edge (single-carrier) or the subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. |
| offsetStopFrequency | float64[] | Specifies the array of the stop frequency values of the offset segment relative to the carrier channel bandwidth edge (single-carrier) or the subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. |
| offsetSideband | int32[] | Specifies whether the offset segment is present on one side, or on both sides of the carrier for each offset. RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE (0) Configures a lower offset segment to the left of the leftmost carrier.RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_POSITIVE (1) Configures an upper offset segment to the right of the rightmost carrier.RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_BOTH (2) Configures both the negative and the positive offset segments. |
| RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE (0) | Configures a lower offset segment to the left of the leftmost carrier. |  |
| RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_POSITIVE (1) | Configures an upper offset segment to the right of the rightmost carrier. |  |
| RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_BOTH (2) | Configures both the negative and the positive offset segments. |  |
| numberOfElements | int32 | Specifies the number of elements in each array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_semcfgoffsetlimitfailmaskarray.html language=enus -->
## TOPIC 00073: RFmxLTE_SEMCfgOffsetLimitFailMaskArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_semcfgoffsetlimitfailmaskarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_semcfgoffsetlimitfailmaskarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SEMCfgOffsetLimitFailMaskArray

int32 __stdcall RFmxLTE_SEMCfgOffsetLimitFailMaskArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 limitFailMask[],
 int32 numberOfElements);

#### Purpose

Configures the array of limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| limitFailMask | int32[] | Specifies the array of criterion to determine the measurement fail status. |
| numberOfElements | int32 | Specifies the number of elements in each array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_semcfgoffsetrelativelimitarray.html language=enus -->
## TOPIC 00074: RFmxLTE_SEMCfgOffsetRelativeLimitArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_semcfgoffsetrelativelimitarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_semcfgoffsetrelativelimitarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SEMCfgOffsetRelativeLimitArray

int32 __stdcall RFmxLTE_SEMCfgOffsetRelativeLimitArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 relativeLimitStart[],
 float64 relativeLimitStop[],
 int32 numberOfElements);

#### Purpose

Configures the array of start and stop relative limits of the offset segments. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| relativeLimitStart | float64[] | Specifies the array of relative power limits corresponding to the beginning of the offset segment. This value is expressed in dB. |
| relativeLimitStop | float64[] | Specifies the array of relative power limits corresponding to the end of the offset segment. This value is expressed in dB. |
| numberOfElements | int32 | Specifies the number of elements in each array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_semfetchcomponentcarriermeasurement.html language=enus -->
## TOPIC 00075: RFmxLTE_SEMFetchComponentCarrierMeasurement

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_semfetchcomponentcarriermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_semfetchcomponentcarriermeasurement.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SEMFetchComponentCarrierMeasurement

int32 __stdcall RFmxLTE_SEMFetchComponentCarrierMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* absoluteIntegratedPower,
 float64* relativeIntegratedPower);

#### Purpose

Returns the absolute power and relative power measured in the component carrier. The relative power is relative to subblock power. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| absoluteIntegratedPower | float64* | Returns the power measured over the integration bandwidth of the carrier. |
| relativeIntegratedPower | float64* | Returns the component carrier power relative to its subblock power. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_semfetchcomponentcarriermeasurementarray.html language=enus -->
## TOPIC 00076: RFmxLTE_SEMFetchComponentCarrierMeasurementArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_semfetchcomponentcarriermeasurementarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_semfetchcomponentcarriermeasurementarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SEMFetchComponentCarrierMeasurementArray

int32 __stdcall RFmxLTE_SEMFetchComponentCarrierMeasurementArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 absoluteIntegratedPower[],
 float64 relativeIntegratedPower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns an array of the absolute powers and relative powers measured in the component carriers. The relative power is relative to subblock power. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| absoluteIntegratedPower | float64[] | Returns the array of power measured in the subblock. |
| relativeIntegratedPower | float64[] | Returns the array of the sum of powers of all the frequency bins over the integration bandwidth of the component carrier power relative to its subblock power. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_semfetchloweroffsetmarginarray.html language=enus -->
## TOPIC 00077: RFmxLTE_SEMFetchLowerOffsetMarginArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_semfetchloweroffsetmarginarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_semfetchloweroffsetmarginarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SEMFetchLowerOffsetMarginArray

int32 __stdcall RFmxLTE_SEMFetchLowerOffsetMarginArray (niRFmxInstrHandle instrumentHandle,
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

Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for lower offset segments. The relative power is relative to the total aggregated power. 
Use "subblock<*n*>" as the selector string to read results from this function. 
Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| measurementStatus | int32[] | Returns the array of the measurement status indicating whether the power before and after the burst is within the standard defined limit. RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) Indicates that the measurement has failed.RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_PASS (1) Indicates that the measurement has passed. |
| RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |  |
| RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |  |
| margin | float64[] | Returns the array of margins from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginFrequency | float64[] | Returns the array of frequency at which the margin occurs in the lower (negative) offset. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginAbsolutePower | float64[] | Returns the array of power at which the margin occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginRelativePower | float64[] | Returns the array of powers at which the margin occurs in the upper (positive) offset segment relative to the value returned by the RFMXLTE_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_semfetchspectrum.html language=enus -->
## TOPIC 00078: RFmxLTE_SEMFetchSpectrum

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_semfetchspectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_semfetchspectrum.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SEMFetchSpectrum

int32 __stdcall RFmxLTE_SEMFetchSpectrum (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 spectrum[],
 float32 compositeMask[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the spectrum used for the SEM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency of the channel. This value is expressed in Hz. |
| dx | float64* | Returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | float32[] | Returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
| compositeMask | float32[] | Returns the array of composite mask used for the channel. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_semfetchupperoffsetmargin.html language=enus -->
## TOPIC 00079: RFmxLTE_SEMFetchUpperOffsetMargin

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_semfetchupperoffsetmargin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_semfetchupperoffsetmargin.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SEMFetchUpperOffsetMargin

int32 __stdcall RFmxLTE_SEMFetchUpperOffsetMargin (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* measurementStatus,
 float64* margin,
 float64* marginFrequency,
 float64* marginAbsolutePower,
 float64* marginRelativePower);

#### Purpose

Returns the measurement status, margin, frequency at margin, and absolute and relative powers at margin for upper offset segments. The relative power is relative to total aggregated power. 
Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this function. 
Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""signal::sig1/subblock0/offset0""signal::sig1/result::r1/subblock0/offset0""result::r1/subblock0/offset0"You can use the RFmxLTE_BuildOffsetString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| measurementStatus | int32* | Returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) Indicates that the measurement has failed.RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_PASS (1) Indicates that the measurement has passed. |
| RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |  |
| RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |  |
| margin | float64* | Returns the margin from the standard defined absolute limit mask for upper offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginFrequency | float64* | Returns the frequency at which the margin occurs in the upper offset. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginAbsolutePower | float64* | Returns the power at which the margin occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginRelativePower | float64* | Returns the power at which the margin occurs in the upper (positive) offset segment relative to the value returned by the RFMXLTE_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_setattributef32.html language=enus -->
## TOPIC 00080: RFmxLTE_SetAttributeF32

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_setattributef32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_setattributef32.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SetAttributeF32

int32 __stdcall RFmxLTE_SetAttributeF32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_setattributei32.html language=enus -->
## TOPIC 00081: RFmxLTE_SetAttributeI32

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_setattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_setattributei32.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SetAttributeI32

int32 __stdcall RFmxLTE_SetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_setattributei32array.html language=enus -->
## TOPIC 00082: RFmxLTE_SetAttributeI32Array

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_setattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_setattributei32array.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SetAttributeI32Array

int32 __stdcall RFmxLTE_SetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_setattributei64.html language=enus -->
## TOPIC 00083: RFmxLTE_SetAttributeI64

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_setattributei64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_setattributei64.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SetAttributeI64

int32 __stdcall RFmxLTE_SetAttributeI64 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 attrVal);

#### Purpose

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int64 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_setattributei64array.html language=enus -->
## TOPIC 00084: RFmxLTE_SetAttributeI64Array

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_setattributei64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_setattributei64array.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SetAttributeI64Array

int32 __stdcall RFmxLTE_SetAttributeI64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_setattributestring.html language=enus -->
## TOPIC 00085: RFmxLTE_SetAttributeString

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_setattributestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_setattributestring.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SetAttributeString

int32 __stdcall RFmxLTE_SetAttributeString (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, char attrVal[]);

#### Purpose

Sets the value of an RFmx string attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | char[] | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_setattributeu16.html language=enus -->
## TOPIC 00086: RFmxLTE_SetAttributeU16

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_setattributeu16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_setattributeu16.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SetAttributeU16

int32 __stdcall RFmxLTE_SetAttributeU16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt16 attrVal);

#### Purpose

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt16 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_setattributeu32array.html language=enus -->
## TOPIC 00087: RFmxLTE_SetAttributeU32Array

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_setattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_setattributeu32array.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SetAttributeU32Array

int32 __stdcall RFmxLTE_SetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_setattributeu64array.html language=enus -->
## TOPIC 00088: RFmxLTE_SetAttributeU64Array

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_setattributeu64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_setattributeu64array.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SetAttributeU64Array

int32 __stdcall RFmxLTE_SetAttributeU64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt64[] | Pass the value to which you want to set the attribute. Note Some of the values might not be valid depending on the current state of the instrument session. |
|  | Note Some of the values might not be valid depending on the current state of the instrument session. |  |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_slotphasecfgsynchronizationmodeandinterval.html language=enus -->
## TOPIC 00089: RFmxLTE_SlotPhaseCfgSynchronizationModeAndInterval

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_slotphasecfgsynchronizationmodeandinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_slotphasecfgsynchronizationmodeandinterval.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SlotPhaseCfgSynchronizationModeAndInterval

int32 __stdcall RFmxLTE_SlotPhaseCfgSynchronizationModeAndInterval (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 synchronizationMode,
 int32 measurementOffset,
 int32 measurementLength);

#### Purpose

Configures the **synchronizationMode**, **measurementOffset**, and **measurementLength** parameters of SlotPhase measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| synchronizationMode | int32 | Specifies whether the measurement is performed from the frame or the slot boundary. RFMXLTE_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME (0) The frame boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the measurementLength parameter, starting at the offset from the boundary specified by the measurementOffset parameter. When you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to RFMXLTE_VAL_TRIGGER_TYPE_DIGITAL_EDGE, the measurement expects a trigger at the frame boundary. RFMXLTE_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT (1) The slot boundary the acquired signal is detected, and the measurement is performed over the number of slots specified by the measurementLength parameter, starting at the offset from the boundary specified by the measurementOffset parameter. When you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to RFMXLTE_VAL_TRIGGER_TYPE_DIGITAL_EDGE, the measurement expects a trigger at any slot boundary. |
| RFMXLTE_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the measurementLength parameter, starting at the offset from the boundary specified by the measurementOffset parameter. When you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to RFMXLTE_VAL_TRIGGER_TYPE_DIGITAL_EDGE, the measurement expects a trigger at the frame boundary. |  |
| RFMXLTE_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary the acquired signal is detected, and the measurement is performed over the number of slots specified by the measurementLength parameter, starting at the offset from the boundary specified by the measurementOffset parameter. When you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to RFMXLTE_VAL_TRIGGER_TYPE_DIGITAL_EDGE, the measurement expects a trigger at any slot boundary. |  |
| measurementOffset | int32 | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the Synchronization Mode parameter. This value is expressed in slots. |
| measurementLength | int32 | Specifies the number of slots to be measured. This value is expressed in slots. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_slotphasefetchmaximumphasediscontinuityarray.html language=enus -->
## TOPIC 00090: RFmxLTE_SlotPhaseFetchMaximumPhaseDiscontinuityArray

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_slotphasefetchmaximumphasediscontinuityarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_slotphasefetchmaximumphasediscontinuityarray.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SlotPhaseFetchMaximumPhaseDiscontinuityArray

int32 __stdcall RFmxLTE_SlotPhaseFetchMaximumPhaseDiscontinuityArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 maximumPhaseDiscontinuity[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the array of maximum values of phase differences at slot boundaries within the measurement interval. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| maximumPhaseDiscontinuity | float64[] | Returns the array of maximum values of phase difference at the slot boundaries within the RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_LENGTH. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_slotphasefetchphasediscontinuities.html language=enus -->
## TOPIC 00091: RFmxLTE_SlotPhaseFetchPhaseDiscontinuities

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_slotphasefetchphasediscontinuities.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_slotphasefetchphasediscontinuities.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SlotPhaseFetchPhaseDiscontinuities

int32 __stdcall RFmxLTE_SlotPhaseFetchPhaseDiscontinuities (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 slotPhaseDiscontinuity[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the array of phase differences at slot boundaries within measurement interval.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| slotPhaseDiscontinuity | float64[] | Returns the array of phase differences at the slot boundaries within the RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_LENGTH. This value is expressed in degrees. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_slotphasefetchsamplephaseerror.html language=enus -->
## TOPIC 00092: RFmxLTE_SlotPhaseFetchSamplePhaseError

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_slotphasefetchsamplephaseerror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_slotphasefetchsamplephaseerror.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SlotPhaseFetchSamplePhaseError

int32 __stdcall RFmxLTE_SlotPhaseFetchSamplePhaseError (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 samplePhaseError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the sample phase error trace for the SlotPhase measurement. At each sample, this is the phase difference between received signal and locally generated reference signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start sample phase error linear fit trace value. |
| dx | float64* | Returns the spacing between the sample phase error linear fit trace values. |
| samplePhaseError | float32[] | Returns the array of sample phase error traces. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_slotphasefetchsamplephaseerrorlinearfittrace.html language=enus -->
## TOPIC 00093: RFmxLTE_SlotPhaseFetchSamplePhaseErrorLinearFitTrace

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_slotphasefetchsamplephaseerrorlinearfittrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_slotphasefetchsamplephaseerrorlinearfittrace.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SlotPhaseFetchSamplePhaseErrorLinearFitTrace

int32 __stdcall RFmxLTE_SlotPhaseFetchSamplePhaseErrorLinearFitTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 samplePhaseErrorLinearFit[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the sample phase error linear fit trace for the SlotPhase measurement. The linear fit is over the array of phase differences at each sample between the received signal and the locally generated reference signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start sample phase error linear fit trace value. This value is expressed in degrees. |
| dx | float64* | Returns the spacing between the sample phase error linear fit trace values. |
| samplePhaseErrorLinearFit | float32[] | Returns the array of sample phase error linear fit traces. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_slotpowercfgmeasurementinterval.html language=enus -->
## TOPIC 00094: RFmxLTE_SlotPowerCfgMeasurementInterval

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_slotpowercfgmeasurementinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_slotpowercfgmeasurementinterval.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SlotPowerCfgMeasurementInterval

int32 __stdcall RFmxLTE_SlotPowerCfgMeasurementInterval (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 measurementOffset,
 int32 measurementLength);

#### Purpose

Configures the **measurementOffset** and **measurementLength** parameters of SlotPower measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| measurementOffset | int32 | Specifies the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframes. |
| measurementLength | int32 | Specifies the number of subframes to be measured. This value is expressed in subframes. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=cvirfmxlte_slotpowerfetchpowers.html language=enus -->
## TOPIC 00095: RFmxLTE_SlotPowerFetchPowers

- bundle_id: `rfmx-lte-cvi`
- source_path: `cvirfmxlte_slotpowerfetchpowers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/cvirfmxlte_slotpowerfetchpowers.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFmxLTE_SlotPowerFetchPowers

int32 __stdcall RFmxLTE_SlotPowerFetchPowers (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 subframePower[],
 float64 subframePowerDelta[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the array of Subframe Power and the Subframe Power Delta parameters over the measurement interval. A NaN is returned as subframe power delta, when the preceding slot is not occupied.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx obtains this parameter from the RFmxLTE_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| subframePower | float64[] | Returns the array of subframe power values over the measurement interval. The values are expressed in dBm. |
| subframePowerDelta | float64[] | Returns the array of subframe power delta values over the measurement interval. Subframe power delta values are the power difference between the two consecutive subframes. The values are expressed in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxLTE_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_averaging_type.html language=enus -->
## TOPIC 00096: RFMXLTE_ATTR_ACP_AVERAGING_TYPE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_averaging_type.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Default value is RMS. Get Function: RFmxLTE_ACPGetAveragingType Set Function: RFmxLTE_ACPSetAveragingType |
| Values: | RFMXLTE_VAL_ACP_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. RFMXLTE_VAL_ACP_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. RFMXLTE_VAL_ACP_AVERAGING_TYPE_SCALAR (2)The square root of the power spectrum is averaged. RFMXLTE_VAL_ACP_AVERAGING_TYPE_MAXIMUM (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXLTE_VAL_ACP_AVERAGING_TYPE_MINIMUM (4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXLTE_VAL_ACP_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. |
| RFMXLTE_VAL_ACP_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXLTE_VAL_ACP_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |
| RFMXLTE_VAL_ACP_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXLTE_VAL_ACP_AVERAGING_TYPE_MINIMUM (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_far_if_output_power_offset.html language=enus -->
## TOPIC 00097: RFMXLTE_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_far_if_output_power_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_far_if_output_power_offset.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is valid only when you set the RFMXLTE_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to RFMXLTE_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE and RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 20. Get Function: RFmxLTE_ACPGetFarIFOutputPowerOffset Set Function: RFmxLTE_ACPSetFarIFOutputPowerOffset |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_fft_overlap_mode.html language=enus -->
## TOPIC 00098: RFMXLTE_ATTR_ACP_FFT_OVERLAP_MODE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_fft_overlap_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_fft_overlap_mode.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_FFT_OVERLAP_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the overlap mode when you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT. In Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. Then the FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_ACP_FFT_OVERLAP_MODE_DISABLED. Get Function: RFmxLTE_ACPGetFFTOverlapMode Set Function: RFmxLTE_ACPSetFFTOverlapMode |
| Values: | RFMXLTE_VAL_ACP_FFT_OVERLAP_MODE_DISABLED (0)Disables the overlap between the FFT chunks. RFMXLTE_VAL_ACP_FFT_OVERLAP_MODE_AUTOMATIC (1)Measurement sets the number of overlapped samples between consecutive FFT chunks to 50% of the RFMXLTE_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute value. RFMXLTE_VAL_ACP_FFT_OVERLAP_MODE_USER_DEFINED (2)Measurement uses the overlap that you specify in the RFMXLTE_ATTR_ACP_FFT_OVERLAP attribute. |
| RFMXLTE_VAL_ACP_FFT_OVERLAP_MODE_DISABLED (0) | Disables the overlap between the FFT chunks. |
| RFMXLTE_VAL_ACP_FFT_OVERLAP_MODE_AUTOMATIC (1) | Measurement sets the number of overlapped samples between consecutive FFT chunks to 50% of the RFMXLTE_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute value. |
| RFMXLTE_VAL_ACP_FFT_OVERLAP_MODE_USER_DEFINED (2) | Measurement uses the overlap that you specify in the RFMXLTE_ATTR_ACP_FFT_OVERLAP attribute. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_if_output_power_offset_auto.html language=enus -->
## TOPIC 00099: RFMXLTE_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_if_output_power_offset_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_if_output_power_offset_auto.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This attribute is valid only when you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE. Get Function: RFmxLTE_ACPGetIFOutputPowerOffsetAuto Set Function: RFmxLTE_ACPSetIFOutputPowerOffsetAuto |
| Values: | RFMXLTE_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE (0)The measurement sets the IF output power level offset using the values of the RFMXLTE_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET and RFMXLTE_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET attributes. RFMXLTE_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE (1)The measurement automatically computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. |
| RFMXLTE_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE (0) | The measurement sets the IF output power level offset using the values of the RFMXLTE_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET and RFMXLTE_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET attributes. |
| RFMXLTE_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE (1) | The measurement automatically computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_measurement_enabled.html language=enus -->
## TOPIC 00100: RFMXLTE_ATTR_ACP_MEASUREMENT_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_measurement_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether to enable the ACP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_FALSE. Get Function: RFmxLTE_ACPGetMeasurementEnabled Set Function: RFmxLTE_ACPSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_measurement_method.html language=enus -->
## TOPIC 00101: RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_measurement_method.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the method for performing the ACP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_NORMAL. Get Function: RFmxLTE_ACPGetMeasurementMethod Set Function: RFmxLTE_ACPSetMeasurementMethod |
| Values: | RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_NORMAL (0)The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE (1)The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668 RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT (2)The ACP measurement acquires all the samples specified by the RFMXLTE_ATTR_ACP_SWEEP_TIME_INTERVAL attribute and divides them in to smaller chunks of equal size defined by the RFMXLTE_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute. FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Sequential FFT method should be used for the following scenarios. 1. While performing fast ACP measurements by utilizing smaller FFT sizes. However, accuracy of the results may be reduced. 2. When measuring signals with time-varying spectral characteristics, sequential FFT with overlap mode set to Automatic should be used. 3. For accurate power measurements when the power characteristics of the signal vary over time averaging is allowed. Not: For Mmlti-span FFT, the averaging count should be 1. |
| RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_NORMAL (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668 |
| RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT (2) | The ACP measurement acquires all the samples specified by the RFMXLTE_ATTR_ACP_SWEEP_TIME_INTERVAL attribute and divides them in to smaller chunks of equal size defined by the RFMXLTE_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute. FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Sequential FFT method should be used for the following scenarios. 1. While performing fast ACP measurements by utilizing smaller FFT sizes. However, accuracy of the results may be reduced. 2. When measuring signals with time-varying spectral characteristics, sequential FFT with overlap mode set to Automatic should be used. 3. For accurate power measurements when the power characteristics of the signal vary over time averaging is allowed. Not: For Mmlti-span FFT, the averaging count should be 1. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_measurement_mode.html language=enus -->
## TOPIC 00102: RFMXLTE_ATTR_ACP_MEASUREMENT_MODE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_measurement_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_measurement_mode.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_MEASUREMENT_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_ACP_MEASUREMENT_MODE_MEASURE. Get Function: RFmxLTE_ACPGetMeasurementMode Set Function: RFmxLTE_ACPSetMeasurementMode |
| Values: | RFMXLTE_VAL_ACP_MEASUREMENT_MODE_MEASURE (0)ACP measurement is performed on the acquired signal. RFMXLTE_VAL_ACP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR (1)Manual noise calibration of the signal analyzer is performed for the ACP measurement. |
| RFMXLTE_VAL_ACP_MEASUREMENT_MODE_MEASURE (0) | ACP measurement is performed on the acquired signal. |
| RFMXLTE_VAL_ACP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR (1) | Manual noise calibration of the signal analyzer is performed for the ACP measurement. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_noise_calibration_averaging_auto.html language=enus -->
## TOPIC 00103: RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_noise_calibration_averaging_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_noise_calibration_averaging_auto.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE. Get Function: RFmxLTE_ACPGetNoiseCalibrationAveragingAuto Set Function: RFmxLTE_ACPSetNoiseCalibrationAveragingAuto |
| Values: | RFMXLTE_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE (0)RFmx uses the averages that you set for RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT attribute. RFMXLTE_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE (1)RFmx uses the following averaging counts: When you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_NORMAL or RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL, RFmx uses a noise calibration averaging count of 32. When you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE and sweep time is less than 5 ms, RFmx uses a noise calibration averaging count of 15. When you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE and sweep time is greater than or equal to 5 ms, RFmx uses a noise calibration averaging count of 5. |
| RFMXLTE_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE (0) | RFmx uses the averages that you set for RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT attribute. |
| RFMXLTE_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE (1) | RFmx uses the following averaging counts: When you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_NORMAL or RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL, RFmx uses a noise calibration averaging count of 32. When you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE and sweep time is less than 5 ms, RFmx uses a noise calibration averaging count of 15. When you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE and sweep time is greater than or equal to 5 ms, RFmx uses a noise calibration averaging count of 5. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_noise_compensation_enabled.html language=enus -->
## TOPIC 00104: RFMXLTE_ATTR_ACP_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_noise_compensation_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_NOISE_COMPENSATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether RFmx compensates for the instrument noise while performing the measurement when you set the RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_MODE attribute to RFMXLTE_VAL_ACP_NOISE_CALIBRATION_MODE_AUTO, or when you set the RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_MODE attribute to RFMXLTE_VAL_ACP_NOISE_CALIBRATION_MODE_MANUAL and the RFMXLTE_ATTR_ACP_MEASUREMENT_MODE attribute to RFMXLTE_VAL_ACP_MEASUREMENT_MODE_MEASURE. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE. Get Function: RFmxLTE_ACPGetNoiseCompensationEnabled Set Function: RFmxLTE_ACPSetNoiseCompensationEnabled |
| Values: | RFMXLTE_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE (0)Disables compensation of the channel powers for the noise floor of the signal analyzer. RFMXLTE_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE (1)Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If the signal analyzer or the measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668, PXIe-5830/5831/5832/5842/5860 |
| RFMXLTE_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE (0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| RFMXLTE_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If the signal analyzer or the measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668, PXIe-5830/5831/5832/5842/5860 |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_noise_compensation_type.html language=enus -->
## TOPIC 00105: RFMXLTE_ATTR_ACP_NOISE_COMPENSATION_TYPE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_noise_compensation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_noise_compensation_type.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_NOISE_COMPENSATION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_AND_TERMINATION. Get Function: RFmxLTE_ACPGetNoiseCompensationType Set Function: RFmxLTE_ACPSetNoiseCompensationType |
| Values: | RFMXLTE_VAL_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_AND_TERMINATION (0)Compensates for noise from the analyzer and the 50 ohm termination. The measured power values are in excess of the thermal noise floor. RFMXLTE_VAL_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_ONLY (1)Compensates for analyzer noise only. |
| RFMXLTE_VAL_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_AND_TERMINATION (0) | Compensates for noise from the analyzer and the 50 ohm termination. The measured power values are in excess of the thermal noise floor. |
| RFMXLTE_VAL_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_ONLY (1) | Compensates for analyzer noise only. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_number_of_analysis_threads.html language=enus -->
## TOPIC 00106: RFMXLTE_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_number_of_analysis_threads.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the ACP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxLTE_ACPGetNumberOfAnalysisThreads Set Function: RFmxLTE_ACPSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_offset_frequency.html language=enus -->
## TOPIC 00107: RFMXLTE_ATTR_ACP_OFFSET_FREQUENCY

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_offset_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_offset_frequency.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_OFFSET_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Specifies the offset frequency of an offset channel. This value is expressed in Hz. When you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_UPLINK, the offset frequency is computed from the center of a reference component carrier/subblock to the center of the nearest RBW filter of the offset channel. When you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_DOWNLINK, the offset frequency is computed from the center of the closest component carrier to the center of the nearest RBW filter of the offset channel. Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. The default value is 10 MHz. Get Function: RFmxLTE_ACPGetOffsetFrequency |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_power_units.html language=enus -->
## TOPIC 00108: RFMXLTE_ATTR_ACP_POWER_UNITS

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_power_units.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_power_units.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_POWER_UNITS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the units for absolute power. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_ACP_POWER_UNITS_DBM_BY_HZ. Get Function: RFmxLTE_ACPGetPowerUnits Set Function: RFmxLTE_ACPSetPowerUnits |
| Values: | RFMXLTE_VAL_ACP_POWER_UNITS_DBM (0)The absolute powers are reported in dBm. RFMXLTE_VAL_ACP_POWER_UNITS_DBM_BY_HZ (1)The absolute powers are reported in dBm/Hz. |
| RFMXLTE_VAL_ACP_POWER_UNITS_DBM (0) | The absolute powers are reported in dBm. |
| RFMXLTE_VAL_ACP_POWER_UNITS_DBM_BY_HZ (1) | The absolute powers are reported in dBm/Hz. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_results_component_carrier_absolute_power.html language=enus -->
## TOPIC 00109: RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_results_component_carrier_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_results_component_carrier_absolute_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the power measured over the integration bandwidth of the carrier. The carrier power is reported in dBm when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to RFMXLTE_VAL_ACP_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to RFMXLTE_VAL_ACP_POWER_UNITS_DBM_BY_HZ. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ACPGetResultsComponentCarrierAbsolutePower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_results_component_carrier_relative_power.html language=enus -->
## TOPIC 00110: RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_results_component_carrier_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_results_component_carrier_relative_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the component carrier power relative to its subblock power. This value is expressed in dB. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ACPGetResultsComponentCarrierRelativePower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_results_lower_offset_absolute_power.html language=enus -->
## TOPIC 00111: RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_results_lower_offset_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_results_lower_offset_absolute_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the lower (negative) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to RFMXLTE_VAL_ACP_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to RFMXLTE_VAL_ACP_POWER_UNITS_DBM_BY_HZ. Refer to the 3GPP 36.521 specification for more information about the applicability of an offset channel. Refer to the LTE Uplink Adjacent Channel Power and LTE Downlink Adjacent Channel Power topics for more information.Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. Get Function: RFmxLTE_ACPGetResultsLowerOffsetAbsolutePower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_results_lower_offset_relative_power.html language=enus -->
## TOPIC 00112: RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_results_lower_offset_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_results_lower_offset_relative_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. Refer to the 3GPP TS 36.521 specification for more information about the applicability of the offset channel. Refer to the LTE Uplink Adjacent Channel Power and LTE Downlink Adjacent Channel Power topics for more information.Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. Get Function: RFmxLTE_ACPGetResultsLowerOffsetRelativePower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_results_upper_offset_absolute_power.html language=enus -->
## TOPIC 00113: RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_results_upper_offset_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_results_upper_offset_absolute_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the upper (positive) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to RFMXLTE_VAL_ACP_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to RFMXLTE_VAL_ACP_POWER_UNITS_DBM_BY_HZ. Refer to the 3GPP TS 36.521 specification for more information about the applicability of offset channel. Refer to the LTE Uplink Adjacent Channel Power and LTE Downlink Adjacent Channel Power topics for more information about ACP offsets.Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. Get Function: RFmxLTE_ACPGetResultsUpperOffsetAbsolutePower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acp_subblock_integration_bandwidth.html language=enus -->
## TOPIC 00114: RFMXLTE_ATTR_ACP_SUBBLOCK_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acp_subblock_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acp_subblock_integration_bandwidth.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACP_SUBBLOCK_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Specifies the integration bandwidth of the subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. Use 'subblock(n)' as the selector string to read this result. The default value is 0. Get Function: RFmxLTE_ACPGetSubblockIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_acquisition_bandwidth_optimization_enabled.html language=enus -->
## TOPIC 00115: RFMXLTE_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_acquisition_bandwidth_optimization_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_acquisition_bandwidth_optimization_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.Refer to the Acquisition Bandwidth Optimization Enabled topic for more information. The default value is RFMXLTE_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_TRUE. Get Function: RFmxLTE_GetAcquisitionBandwidthOptimizationEnabled Set Function: RFmxLTE_SetAcquisitionBandwidthOptimizationEnabled |
| Values: | RFMXLTE_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_FALSE (0)RFmx does not optimize acquisition bandwidth and will be based on the Nyquist criterion. The value of the acquisition center frequency is the same as the value of the Center Frequency that you configure. RFMXLTE_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_TRUE (1)RFmx positions the acquisition center frequency to acquire the least bandwidth based on the configuration and span needed for the measurement. This helps in reducing the amount of data to process for the measurement, thus improving the speed. However this might cause the LO to be positioned at a non-dc subcarrier position, hence the measurement sensitive to it should have this attribute disabled. |
| RFMXLTE_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_FALSE (0) | RFmx does not optimize acquisition bandwidth and will be based on the Nyquist criterion. The value of the acquisition center frequency is the same as the value of the Center Frequency that you configure. |
| RFMXLTE_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_TRUE (1) | RFmx positions the acquisition center frequency to acquire the least bandwidth based on the configuration and span needed for the measurement. This helps in reducing the amount of data to process for the measurement, thus improving the speed. However this might cause the LO to be positioned at a non-dc subcarrier position, hence the measurement sensitive to it should have this attribute disabled. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_auto_control_channel_power_detection_enabled.html language=enus -->
## TOPIC 00116: RFMXLTE_ATTR_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_auto_control_channel_power_detection_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_auto_control_channel_power_detection_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power attributes are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power attribute is not supported. This attribute is not valid, when you set the RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE attribute to RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL. The measurement ignores this attribute, when you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_UPLINK.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_TRUE. Get Function: RFmxLTE_GetAutoControlChannelPowerDetectionEnabled Set Function: RFmxLTE_SetAutoControlChannelPowerDetectionEnabled |
| Values: | RFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_FALSE (0)The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, PHICH Power, and PCFICH Power attributes that you specify are used for the measurement. RFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_TRUE (1)The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, and PCFICH Power attributes are auto-detected and used for the measurement. |
| RFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_FALSE (0) | The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, PHICH Power, and PCFICH Power attributes that you specify are used for the measurement. |
| RFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_TRUE (1) | The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, and PCFICH Power attributes are auto-detected and used for the measurement. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_auto_level_initial_reference_level.html language=enus -->
## TOPIC 00117: RFMXLTE_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_auto_level_initial_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_auto_level_initial_reference_level.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the initial reference level that the RFmxLTE_AutoLevel function uses to estimate the peak power of the input signal. This value is expressed in dBm. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 30. Get Function: RFmxLTE_GetAutoLevelInitialReferenceLevel Set Function: RFmxLTE_SetAutoLevelInitialReferenceLevel |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_auto_pcfich_cfi_detection_enabled.html language=enus -->
## TOPIC 00118: RFMXLTE_ATTR_AUTO_PCFICH_CFI_DETECTION_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_auto_pcfich_cfi_detection_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_auto_pcfich_cfi_detection_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_AUTO_PCFICH_CFI_DETECTION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the value of RFMXLTE_ATTR_PCFICH_CFI attribute is auto-detected by the measurement or user-specified. This attribute is not valid, when you set the RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE attribute to RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL. The measurement ignores this attribute, when you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_UPLINK.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_TRUE. Get Function: RFmxLTE_GetAutoPCFICHCFIDetectionEnabled Set Function: RFmxLTE_SetAutoPCFICHCFIDetectionEnabled |
| Values: | RFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_FALSE (0)The value of PCFICH CFI attribute used for the measurement is specified by you. RFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_TRUE (1)The value of PCFICH CFI attribute used for the measurement is auto-detected. This value is obtained by decoding the PCFICH channel. |
| RFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_FALSE (0) | The value of PCFICH CFI attribute used for the measurement is specified by you. |
| RFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_TRUE (1) | The value of PCFICH CFI attribute used for the measurement is auto-detected. This value is obtained by decoding the PCFICH channel. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_cell_id.html language=enus -->
## TOPIC 00119: RFMXLTE_ATTR_CELL_ID

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_cell_id.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_cell_id.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_CELL_ID

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies a physical layer cell identity. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is 0. Valid values are 0 to 503, inclusive. Get Function: RFmxLTE_GetCellID Set Function: RFmxLTE_SetCellID |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_center_frequency_for_limits.html language=enus -->
## TOPIC 00120: RFMXLTE_ATTR_CENTER_FREQUENCY_FOR_LIMITS

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_center_frequency_for_limits.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_center_frequency_for_limits.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_CENTER_FREQUENCY_FOR_LIMITS

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. If you do not set a value for this attribute, the measurement internally uses RFMXLTE_ATTR_CENTER_FREQUENCY for determining SEM mask, IBE limits, and spectral flatness ranges. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxLTE_GetCenterFrequencyForLimits Set Function: RFmxLTE_SetCenterFrequencyForLimits |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_chp_noise_compensation_enabled.html language=enus -->
## TOPIC 00121: RFMXLTE_ATTR_CHP_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_chp_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_chp_noise_compensation_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_CHP_NOISE_COMPENSATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the RFMXLTE_ATTR_CHP_NOISE_CALIBRATION_MODE attribute to RFMXLTE_VAL_CHP_NOISE_CALIBRATION_MODE_AUTO, or set the RFMXLTE_ATTR_CHP_NOISE_CALIBRATION_MODE attribute to RFMXLTE_VAL_CHP_NOISE_CALIBRATION_MODE_MANUAL and the RFMXLTE_ATTR_CHP_MEASUREMENT_MODE attribute to RFMXLTE_VAL_CHP_MEASUREMENT_MODE_MEASURE. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE. Get Function: RFmxLTE_CHPGetNoiseCompensationEnabled Set Function: RFmxLTE_CHPSetNoiseCompensationEnabled |
| Values: | RFMXLTE_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE (0)Disables noise compensation. RFMXLTE_VAL_CHP_NOISE_COMPENSATION_ENABLED_TRUE (1)Enables noise compensation. |
| RFMXLTE_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE (0) | Disables noise compensation. |
| RFMXLTE_VAL_CHP_NOISE_COMPENSATION_ENABLED_TRUE (1) | Enables noise compensation. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_chp_number_of_analysis_threads.html language=enus -->
## TOPIC 00122: RFMXLTE_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_chp_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_chp_number_of_analysis_threads.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxLTE_CHPGetNumberOfAnalysisThreads Set Function: RFmxLTE_CHPSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_chp_rbw_filter_auto_bandwidth.html language=enus -->
## TOPIC 00123: RFMXLTE_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_chp_rbw_filter_auto_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_chp_rbw_filter_auto_bandwidth.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the CHP measurement computes the RBW. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_TRUE. Get Function: RFmxLTE_CHPGetRBWFilterAutoBandwidth Set Function: RFmxLTE_CHPSetRBWFilterAutoBandwidth |
| Values: | RFMXLTE_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_FALSE (0)The measurement uses the RBW that you specify in the RFMXLTE_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. RFMXLTE_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_TRUE (1)The measurement computes the RBW. |
| RFMXLTE_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_FALSE (0) | The measurement uses the RBW that you specify in the RFMXLTE_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXLTE_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_TRUE (1) | The measurement computes the RBW. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_chp_results_component_carrier_absolute_power.html language=enus -->
## TOPIC 00124: RFMXLTE_ATTR_CHP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_chp_results_component_carrier_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_chp_results_component_carrier_absolute_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_CHP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_CHPGetResultsComponentCarrierAbsolutePower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_chp_results_subblock_power.html language=enus -->
## TOPIC 00125: RFMXLTE_ATTR_CHP_RESULTS_SUBBLOCK_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_chp_results_subblock_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_chp_results_subblock_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_CHP_RESULTS_SUBBLOCK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the sum of total power of all the frequency bins over the integration bandwidth of the subblock. This value includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. Use 'subblock(n)' as the selector string to read this result. Get Function: RFmxLTE_CHPGetResultsSubblockPower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_component_carrier_frequency.html language=enus -->
## TOPIC 00126: RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_component_carrier_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_component_carrier_frequency.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency attribute. This value is expressed in Hz.This attribute is applicable only if you set the RFMXLTE_ATTR_COMPONENT_CARRIER_SPACING_TYPE attribute to RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_USER. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is 0. Get Function: RFmxLTE_GetComponentCarrierFrequency Set Function: RFmxLTE_SetComponentCarrierFrequency |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_component_carrier_spacing_type.html language=enus -->
## TOPIC 00127: RFMXLTE_ATTR_COMPONENT_CARRIER_SPACING_TYPE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_component_carrier_spacing_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_component_carrier_spacing_type.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_COMPONENT_CARRIER_SPACING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the spacing between two adjacent component carriers within a subblock. Refer to the Channel Spacing and Carrier Frequency Offset Definition and Reference Frequency topics for more information about component carrier spacing. Use 'subblock(n)' as the selector string to configure or read this attribute. The default value is RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL. Get Function: RFmxLTE_GetComponentCarrierSpacingType Set Function: RFmxLTE_SetComponentCarrierSpacingType |
| Values: | RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL (0)Calculates the frequency spacing between component carriers, as defined in section 5.4.1A in the 3GPP TS 36.521 specification, and sets the RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY attribute. RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_MINIMUM (1)Calculates the frequency spacing between component carriers, as defined in section 5.4.1A of the 3GPP TS 36.521 specification, and sets the RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY attribute. RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_USER (2)The CC frequency that you configure in the RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY attribute is used. |
| RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL (0) | Calculates the frequency spacing between component carriers, as defined in section 5.4.1A in the 3GPP TS 36.521 specification, and sets the RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY attribute. |
| RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_MINIMUM (1) | Calculates the frequency spacing between component carriers, as defined in section 5.4.1A of the 3GPP TS 36.521 specification, and sets the RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY attribute. |
| RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_USER (2) | The CC frequency that you configure in the RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY attribute is used. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_cyclic_prefix_mode.html language=enus -->
## TOPIC 00128: RFMXLTE_ATTR_CYCLIC_PREFIX_MODE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_cyclic_prefix_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_cyclic_prefix_mode.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_CYCLIC_PREFIX_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_CYCLIC_PREFIX_MODE_NORMAL. Get Function: RFmxLTE_GetCyclicPrefixMode Set Function: RFmxLTE_SetCyclicPrefixMode |
| Values: | RFMXLTE_VAL_CYCLIC_PREFIX_MODE_NORMAL (0)The CP duration is 4.67 microseconds, and the number of symbols in a slot is 7. RFMXLTE_VAL_CYCLIC_PREFIX_MODE_EXTENDED (1)The CP duration is 16.67 microseconds, and the number of symbols in a slot is 6. |
| RFMXLTE_VAL_CYCLIC_PREFIX_MODE_NORMAL (0) | The CP duration is 4.67 microseconds, and the number of symbols in a slot is 7. |
| RFMXLTE_VAL_CYCLIC_PREFIX_MODE_EXTENDED (1) | The CP duration is 16.67 microseconds, and the number of symbols in a slot is 6. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_digital_edge_trigger_edge.html language=enus -->
## TOPIC 00129: RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_digital_edge_trigger_edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_digital_edge_trigger_edge.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the active edge for the trigger. This attribute is used only when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to RFMXLTE_VAL_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_DIGITAL_EDGE_RISING_EDGE. Get Function: RFmxLTE_GetDigitalEdgeTriggerEdge Set Function: RFmxLTE_SetDigitalEdgeTriggerEdge |
| Values: | RFMXLTE_VAL_DIGITAL_EDGE_RISING_EDGE (0)The trigger asserts on the rising edge of the signal. RFMXLTE_VAL_DIGITAL_EDGE_FALLING_EDGE (1)The trigger asserts on the falling edge of the signal. |
| RFMXLTE_VAL_DIGITAL_EDGE_RISING_EDGE (0) | The trigger asserts on the rising edge of the signal. |
| RFMXLTE_VAL_DIGITAL_EDGE_FALLING_EDGE (1) | The trigger asserts on the falling edge of the signal. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_digital_edge_trigger_source.html language=enus -->
## TOPIC 00130: RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_digital_edge_trigger_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_digital_edge_trigger_source.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeStringRFmxLTE_GetAttributeString |
| Description: | Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to RFMXLTE_VAL_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value of this attribute is hardware dependent. Get Function: RFmxLTE_GetDigitalEdgeTriggerSource Set Function: RFmxLTE_SetDigitalEdgeTriggerSource |
| Values: | RFMXLTE_VAL_PFI0_STR (PFI0)The trigger is received on PFI 0. RFMXLTE_VAL_PFI1_STR (PFI1)The trigger is received on PFI 1. RFMXLTE_VAL_PXI_TRIG0_STR (PXI_Trig0)The trigger is received on PXI trigger line 0. RFMXLTE_VAL_PXI_TRIG1_STR (PXI_Trig1)The trigger is received on PXI trigger line 1. RFMXLTE_VAL_PXI_TRIG2_STR (PXI_Trig2)The trigger is received on PXI trigger line 2. RFMXLTE_VAL_PXI_TRIG3_STR (PXI_Trig3)The trigger is received on PXI trigger line 3. RFMXLTE_VAL_PXI_TRIG4_STR (PXI_Trig4)The trigger is received on PXI trigger line 4. RFMXLTE_VAL_PXI_TRIG5_STR (PXI_Trig5)The trigger is received on PXI trigger line 5. RFMXLTE_VAL_PXI_TRIG6_STR (PXI_Trig6)The trigger is received on PXI trigger line 6. RFMXLTE_VAL_PXI_TRIG7_STR (PXI_Trig7)The trigger is received on PXI trigger line 7. RFMXLTE_VAL_PXI_STAR_STR (PXI_STAR)The trigger is received on the PXI star trigger line. RFMXLTE_VAL_PXIE_DSTARB_STR (PXIe_DStarB)The trigger is received on the PXIe DStar B trigger line. RFMXLTE_VAL_TIMER_EVENT_STR (TimerEvent)The trigger is received from the Timer Event. |
| RFMXLTE_VAL_PFI0_STR (PFI0) | The trigger is received on PFI 0. |
| RFMXLTE_VAL_PFI1_STR (PFI1) | The trigger is received on PFI 1. |
| RFMXLTE_VAL_PXI_TRIG0_STR (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| RFMXLTE_VAL_PXI_TRIG1_STR (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| RFMXLTE_VAL_PXI_TRIG2_STR (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| RFMXLTE_VAL_PXI_TRIG3_STR (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| RFMXLTE_VAL_PXI_TRIG4_STR (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| RFMXLTE_VAL_PXI_TRIG5_STR (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| RFMXLTE_VAL_PXI_TRIG6_STR (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| RFMXLTE_VAL_PXI_TRIG7_STR (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| RFMXLTE_VAL_PXI_STAR_STR (PXI_STAR) | The trigger is received on the PXI star trigger line. |
| RFMXLTE_VAL_PXIE_DSTARB_STR (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |
| RFMXLTE_VAL_TIMER_EVENT_STR (TimerEvent) | The trigger is received from the Timer Event. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_dmrs_occ_enabled.html language=enus -->
## TOPIC 00131: RFMXLTE_ATTR_DMRS_OCC_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_dmrs_occ_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_dmrs_occ_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_DMRS_OCC_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this attribute to TRUE for multi antenna cases. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is RFMXLTE_VAL_DMRS_OCC_ENABLED_FALSE. Get Function: RFmxLTE_GetDMRSOCCEnabled Set Function: RFmxLTE_SetDMRSOCCEnabled |
| Values: | RFMXLTE_VAL_DMRS_OCC_ENABLED_FALSE (0)The measurement ignores the RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD and uses the RFMXLTE_ATTR_PUSCH_N_DMRS_2 field for DMRS calculations. RFMXLTE_VAL_DMRS_OCC_ENABLED_TRUE (1)The measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the value of RFMXLTE_ATTR_PUSCH_N_DMRS_2 and [w(0) w(1)] for DMRS signal based on the values you set for the RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD and RFMXLTE_ATTR_TRANSMIT_ANTENNA_TO_ANALYZE. |
| RFMXLTE_VAL_DMRS_OCC_ENABLED_FALSE (0) | The measurement ignores the RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD and uses the RFMXLTE_ATTR_PUSCH_N_DMRS_2 field for DMRS calculations. |
| RFMXLTE_VAL_DMRS_OCC_ENABLED_TRUE (1) | The measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the value of RFMXLTE_ATTR_PUSCH_N_DMRS_2 and [w(0) w(1)] for DMRS signal based on the values you set for the RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD and RFMXLTE_ATTR_TRANSMIT_ANTENNA_TO_ANALYZE. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_downlink_auto_cell_id_detection_enabled.html language=enus -->
## TOPIC 00132: RFMXLTE_ATTR_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_downlink_auto_cell_id_detection_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_downlink_auto_cell_id_detection_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether to enable autodetection of the cell ID. If the signal being measured does not contain primary and secondary sync signal (PSS/SSS), autodetection of cell ID is not possible. Detected cell ID can be fetched using RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_DETECTED_CELL_ID attribute. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_TRUE. Get Function: RFmxLTE_GetDownlinkAutoCellIDDetectionEnabled Set Function: RFmxLTE_SetDownlinkAutoCellIDDetectionEnabled |
| Values: | RFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_FALSE (0)The measurement uses the cell ID you configure. RFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_TRUE (1)The measurement auto detects the cell ID. |
| RFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_FALSE (0) | The measurement uses the cell ID you configure. |
| RFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_TRUE (1) | The measurement auto detects the cell ID. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_downlink_channel_configuration_mode.html language=enus -->
## TOPIC 00133: RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_downlink_channel_configuration_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_downlink_channel_configuration_mode.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the channel configuration mode. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL. Get Function: RFmxLTE_GetDownlinkChannelConfigurationMode Set Function: RFmxLTE_SetDownlinkChannelConfigurationMode |
| Values: | RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_USER_DEFINED (1)You have to manually set all the signals and channels. RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL (2)You need to select a test model using the RFMXLTE_ATTR_DOWNLINK_TEST_MODEL attribute, which will configure all the signals and channels automatically according to the 3GPP specification. |
| RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_USER_DEFINED (1) | You have to manually set all the signals and channels. |
| RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL (2) | You need to select a test model using the RFMXLTE_ATTR_DOWNLINK_TEST_MODEL attribute, which will configure all the signals and channels automatically according to the 3GPP specification. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_downlink_number_of_subframes.html language=enus -->
## TOPIC 00134: RFMXLTE_ATTR_DOWNLINK_NUMBER_OF_SUBFRAMES

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_downlink_number_of_subframes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_downlink_number_of_subframes.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_DOWNLINK_NUMBER_OF_SUBFRAMES

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the number of unique subframes transmitted by the DUT. If you set the RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE attribute to RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL, this attribute will be set to 10 for FDD and 20 for TDD by default. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is 10. Valid values are 10 and 20. Get Function: RFmxLTE_GetDownlinkNumberOfSubframes Set Function: RFmxLTE_SetDownlinkNumberOfSubframes |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_downlink_test_model.html language=enus -->
## TOPIC 00135: RFMXLTE_ATTR_DOWNLINK_TEST_MODEL

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_downlink_test_model.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_downlink_test_model.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_DOWNLINK_TEST_MODEL

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the E-UTRA Test Model type when you set the RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE attribute to RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_1.1. Get Function: RFmxLTE_GetDownlinkTestModel Set Function: RFmxLTE_SetDownlinkTestModel |
| Values: | RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_1 (0)Specifies an E-UTRA Test Model 1. RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_2 (1)Specifies an E-UTRA Test Model 1.2. RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2 (2)Specifies an E-UTRA Test Model 2. RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2A (3)Specifies an E-UTRA Test Model 2a. RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2B (8)Specifies an E-UTRA Test Model 2b. RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1 (4)Specifies an E-UTRA Test Model 3.1. RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1A (7)Specifies an E-UTRA Test Model 3.1a. RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1B (9)Specifies an E-UTRA Test Model 3.1b. RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_2 (5)Specifies an E-UTRA Test Model 3.2. RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_3 (6)Specifies an E-UTRA Test Model 3.3. |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_1 (0) | Specifies an E-UTRA Test Model 1. |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_2 (1) | Specifies an E-UTRA Test Model 1.2. |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2 (2) | Specifies an E-UTRA Test Model 2. |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2A (3) | Specifies an E-UTRA Test Model 2a. |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2B (8) | Specifies an E-UTRA Test Model 2b. |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1 (4) | Specifies an E-UTRA Test Model 3.1. |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1A (7) | Specifies an E-UTRA Test Model 3.1a. |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1B (9) | Specifies an E-UTRA Test Model 3.1b. |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_2 (5) | Specifies an E-UTRA Test Model 3.2. |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_3 (6) | Specifies an E-UTRA Test Model 3.3. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_downlink_user_defined_cell_specific_ratio.html language=enus -->
## TOPIC 00136: RFMXLTE_ATTR_DOWNLINK_USER_DEFINED_CELL_SPECIFIC_RATIO

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_downlink_user_defined_cell_specific_ratio.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_downlink_user_defined_cell_specific_ratio.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_DOWNLINK_USER_DEFINED_CELL_SPECIFIC_RATIO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the ratio Rhob/Rhoa for the cell-specific ratio of one, two, or four cell-specific antenna ports as described in Table 5.2-1 in section 5.2 of the 3GPP TS 36.213 specification. This attribute determines the power of the channel resource element (RE) in the symbols that do not contain the reference symbols. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is P_B=0. Get Function: RFmxLTE_GetDownlinkUserDefinedCellSpecificRatio Set Function: RFmxLTE_SetDownlinkUserDefinedCellSpecificRatio |
| Values: | RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B0 (0)Specifies a ratio of 1 for one antenna port and 5/4 for two or four antenna ports. RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B1 (1)Specifies a ratio of 4/5 for one antenna port and 1 for two or four antenna ports. RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B2 (2)Specifies a ratio of 3/5 for one antenna port and 3/4 for two or four antenna ports. RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B3 (3)Specifies a ratio of 2/5 for one antenna port and 1/2 for two or four antenna ports. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B0 (0) | Specifies a ratio of 1 for one antenna port and 5/4 for two or four antenna ports. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B1 (1) | Specifies a ratio of 4/5 for one antenna port and 1 for two or four antenna ports. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B2 (2) | Specifies a ratio of 3/5 for one antenna port and 3/4 for two or four antenna ports. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B3 (3) | Specifies a ratio of 2/5 for one antenna port and 1/2 for two or four antenna ports. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_duplex_scheme.html language=enus -->
## TOPIC 00137: RFMXLTE_ATTR_DUPLEX_SCHEME

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_duplex_scheme.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_duplex_scheme.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_DUPLEX_SCHEME

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the duplexing technique of the signal being measured. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_DUPLEX_SCHEME_FDD. Get Function: RFmxLTE_GetDuplexScheme Set Function: RFmxLTE_SetDuplexScheme |
| Values: | RFMXLTE_VAL_DUPLEX_SCHEME_FDD (0)Specifies that the duplexing technique is frequency-division duplexing. RFMXLTE_VAL_DUPLEX_SCHEME_TDD (1)Specifies that the duplexing technique is time-division duplexing. RFMXLTE_VAL_DUPLEX_SCHEME_LAA (2)Specifies that the duplexing technique is license assisted access. |
| RFMXLTE_VAL_DUPLEX_SCHEME_FDD (0) | Specifies that the duplexing technique is frequency-division duplexing. |
| RFMXLTE_VAL_DUPLEX_SCHEME_TDD (1) | Specifies that the duplexing technique is time-division duplexing. |
| RFMXLTE_VAL_DUPLEX_SCHEME_LAA (2) | Specifies that the duplexing technique is license assisted access. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_emtc_analysis_enabled.html language=enus -->
## TOPIC 00138: RFMXLTE_ATTR_EMTC_ANALYSIS_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_emtc_analysis_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_emtc_analysis_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_EMTC_ANALYSIS_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_FALSE. Get Function: RFmxLTE_GetEMTCAnalysisEnabled Set Function: RFmxLTE_SetEMTCAnalysisEnabled |
| Values: | RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_FALSE (0)The measurement considers the signal as LTE FDD/TDD transmission. RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_TRUE (1)Detects the eMTC half duplex pattern, narrow band hopping, and eMTC guard symbols present in the uplink transmission. |
| RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_FALSE (0) | The measurement considers the signal as LTE FDD/TDD transmission. |
| RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_TRUE (1) | Detects the eMTC half duplex pattern, narrow band hopping, and eMTC guard symbols present in the uplink transmission. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_enodeb_category.html language=enus -->
## TOPIC 00139: RFMXLTE_ATTR_ENODEB_CATEGORY

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_enodeb_category.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_enodeb_category.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_ENODEB_CATEGORY

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the downlink eNodeB (Base station) category. Refer to the 3GPP 36.141 specification for more details. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Wide Area Base Station - Category A. Get Function: RFmxLTE_GeteNodeBCategory Set Function: RFmxLTE_SeteNodeBCategory |
| Values: | RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_A (0)Specifies eNodeB is Wide Area Base Station - Category A. RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION1 (1)Specifies eNodeB is Wide Area Base Station - Category B Option1. RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION2 (2)Specifies eNodeB is Wide Area Base Station - Category B Option2. RFMXLTE_VAL_ENODEB_LOCAL_AREA_BASE_STATION (3)Specifies eNodeB is Local Area Base Station. RFMXLTE_VAL_ENODEB_HOME_BASE_STATION (4)Specifies eNodeB is Home Base Station. RFMXLTE_VAL_ENODEB_MEDIUM_RANGE_BASE_STATION (5)Specifies eNodeB is Medium Range Base Station. |
| RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_A (0) | Specifies eNodeB is Wide Area Base Station - Category A. |
| RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION1 (1) | Specifies eNodeB is Wide Area Base Station - Category B Option1. |
| RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION2 (2) | Specifies eNodeB is Wide Area Base Station - Category B Option2. |
| RFMXLTE_VAL_ENODEB_LOCAL_AREA_BASE_STATION (3) | Specifies eNodeB is Local Area Base Station. |
| RFMXLTE_VAL_ENODEB_HOME_BASE_STATION (4) | Specifies eNodeB is Home Base Station. |
| RFMXLTE_VAL_ENODEB_MEDIUM_RANGE_BASE_STATION (5) | Specifies eNodeB is Medium Range Base Station. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_external_attenuation.html language=enus -->
## TOPIC 00140: RFMXLTE_ATTR_EXTERNAL_ATTENUATION

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_external_attenuation.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_EXTERNAL_ATTENUATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. Refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help for more information about attenuation. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxLTE_GetExternalAttenuation Set Function: RFmxLTE_SetExternalAttenuation |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_iq_power_edge_trigger_level.html language=enus -->
## TOPIC 00141: RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_iq_power_edge_trigger_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_iq_power_edge_trigger_level.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE and in dBm when you set the RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to RFMXLTE_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value of this attribute is hardware dependent. Get Function: RFmxLTE_GetIQPowerEdgeTriggerLevel Set Function: RFmxLTE_SetIQPowerEdgeTriggerLevel |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_iq_power_edge_trigger_level_type.html language=enus -->
## TOPIC 00142: RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_iq_power_edge_trigger_level_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_iq_power_edge_trigger_level_type.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the reference for the RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute is used only when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to RFMXLTE_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE. Get Function: RFmxLTE_GetIQPowerEdgeTriggerLevelType Set Function: RFmxLTE_SetIQPowerEdgeTriggerLevelType |
| Values: | RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0)The IQ Power Edge Level attribute is relative to the value of the RFMXLTE_ATTR_REFERENCE_LEVEL attribute. RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1)The IQ Power Edge Level attribute specifies the absolute power. |
| RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0) | The IQ Power Edge Level attribute is relative to the value of the RFMXLTE_ATTR_REFERENCE_LEVEL attribute. |
| RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1) | The IQ Power Edge Level attribute specifies the absolute power. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_iq_power_edge_trigger_slope.html language=enus -->
## TOPIC 00143: RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_iq_power_edge_trigger_slope.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_iq_power_edge_trigger_slope.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This attribute is used only when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to RFMXLTE_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_IQ_POWER_EDGE_RISING_SLOPE. Get Function: RFmxLTE_GetIQPowerEdgeTriggerSlope Set Function: RFmxLTE_SetIQPowerEdgeTriggerSlope |
| Values: | RFMXLTE_VAL_IQ_POWER_EDGE_RISING_SLOPE (0)The trigger asserts when the signal power is rising. RFMXLTE_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1)The trigger asserts when the signal power is falling. |
| RFMXLTE_VAL_IQ_POWER_EDGE_RISING_SLOPE (0) | The trigger asserts when the signal power is rising. |
| RFMXLTE_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1) | The trigger asserts when the signal power is falling. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_laa_number_of_subframes.html language=enus -->
## TOPIC 00144: RFMXLTE_ATTR_LAA_NUMBER_OF_SUBFRAMES

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_laa_number_of_subframes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_laa_number_of_subframes.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_LAA_NUMBER_OF_SUBFRAMES

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the number of subframes in an LAA burst including the starting subframe. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is 1. Get Function: RFmxLTE_GetLAANumberOfSubframes Set Function: RFmxLTE_SetLAANumberOfSubframes |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_laa_starting_subframe.html language=enus -->
## TOPIC 00145: RFMXLTE_ATTR_LAA_STARTING_SUBFRAME

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_laa_starting_subframe.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_laa_starting_subframe.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_LAA_STARTING_SUBFRAME

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the starting subframe of an LAA burst. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is 0. Get Function: RFmxLTE_GetLAAStartingSubframe Set Function: RFmxLTE_SetLAAStartingSubframe |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_list_step_timer_unit.html language=enus -->
## TOPIC 00146: RFMXLTE_ATTR_LIST_STEP_TIMER_UNIT

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_list_step_timer_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_list_step_timer_unit.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_LIST_STEP_TIMER_UNIT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the units in which RFMXLTE_ATTR_LIST_STEP_TIMER_DURATION and RFMXLTE_ATTR_LIST_STEP_TIMER_OFFSET are specified. You need to use a selector string to configure or read this attribute for the list step instance. The default value is RFMXLTE_VAL_LIST_STEP_TIMER_UNIT_SLOT. Get Function: RFmxLTE_GetListStepTimerUnit Set Function: RFmxLTE_SetListStepTimerUnit |
| Values: | RFMXLTE_VAL_LIST_STEP_TIMER_UNIT_SLOT (1)List Step Timer Duration and List Step Timer Offset are specified in units of slots. RFMXLTE_VAL_LIST_STEP_TIMER_UNIT_TIME (6)List Step Timer Duration and List Step Timer Offset are specified in seconds. |
| RFMXLTE_VAL_LIST_STEP_TIMER_UNIT_SLOT (1) | List Step Timer Duration and List Step Timer Offset are specified in units of slots. |
| RFMXLTE_VAL_LIST_STEP_TIMER_UNIT_TIME (6) | List Step Timer Duration and List Step Timer Offset are specified in seconds. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_mi_configuration.html language=enus -->
## TOPIC 00147: RFMXLTE_ATTR_MI_CONFIGURATION

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_mi_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_mi_configuration.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MI_CONFIGURATION

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the Mi parameter is specified by section 6.1.2.6 of 3GPP TS 36.141 specification for testing E-TMs or in the Table 6.9-1 of 3GPP TS 36.211 specification. The Mi parameter determines the number of PHICH groups in each downlink subframe, when you set the RFMXLTE_ATTR_DUPLEX_SCHEME attribute to RFMXLTE_VAL_DUPLEX_SCHEME_TDD. This attribute is not valid, when you set the RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE attribute to RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL. The measurement ignores this attribute, when you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_UPLINK.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_MI_CONFIGURATION_STANDARD. Get Function: RFmxLTE_GetMiConfiguration Set Function: RFmxLTE_SetMiConfiguration |
| Values: | RFMXLTE_VAL_MI_CONFIGURATION_TEST_MODEL (0)Mi parameter is set to 1 as specified in section 6.1.2.6 of 3GPP TS 36.141 specification. RFMXLTE_VAL_MI_CONFIGURATION_STANDARD (1)Mi parameter is specified by the Table 6.9-1 of 3GPP TS 36.211 specification. |
| RFMXLTE_VAL_MI_CONFIGURATION_TEST_MODEL (0) | Mi parameter is set to 1 as specified in section 6.1.2.6 of 3GPP TS 36.141 specification. |
| RFMXLTE_VAL_MI_CONFIGURATION_STANDARD (1) | Mi parameter is specified by the Table 6.9-1 of 3GPP TS 36.211 specification. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_all_traces_enabled.html language=enus -->
## TOPIC 00148: RFMXLTE_ATTR_MODACC_ALL_TRACES_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_all_traces_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_FALSE. Get Function: RFmxLTE_ModAccGetAllTracesEnabled Set Function: RFmxLTE_ModAccSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_averaging_count.html language=enus -->
## TOPIC 00149: RFMXLTE_ATTR_MODACC_AVERAGING_COUNT

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_averaging_count.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXLTE_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxLTE_ModAccGetAveragingCount Set Function: RFmxLTE_ModAccSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_averaging_enabled.html language=enus -->
## TOPIC 00150: RFMXLTE_ATTR_MODACC_AVERAGING_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_averaging_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the ModAcc measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_FALSE. Get Function: RFmxLTE_ModAccGetAveragingEnabled Set Function: RFmxLTE_ModAccSetAveragingEnabled |
| Values: | RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_TRUE (1)The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the RFMXLTE_ATTR_MODACC_AVERAGING_COUNT attribute. |
| RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_TRUE (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the RFMXLTE_ATTR_MODACC_AVERAGING_COUNT attribute. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_channel_estimation_type.html language=enus -->
## TOPIC 00151: RFMXLTE_ATTR_MODACC_CHANNEL_ESTIMATION_TYPE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_channel_estimation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_channel_estimation_type.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_CHANNEL_ESTIMATION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the method used for the channel estimation for the ModAcc measurement. The measurement ignores this attribute, when you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_DOWNLINK.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Reference+Data. Get Function: RFmxLTE_ModAccGetChannelEstimationType Set Function: RFmxLTE_ModAccSetChannelEstimationType |
| Values: | RFMXLTE_VAL_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE (0)Only the demodulation reference signal (DMRS) symbol is used to calculate the channel coefficients. RFMXLTE_VAL_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE_AND_DATA (1)Both the DMRS symbol and the data symbol are used to calculate the channel coefficients, as specified by the 3GPP 36.521 specification, Annexe E. |
| RFMXLTE_VAL_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE (0) | Only the demodulation reference signal (DMRS) symbol is used to calculate the channel coefficients. |
| RFMXLTE_VAL_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE_AND_DATA (1) | Both the DMRS symbol and the data symbol are used to calculate the channel coefficients, as specified by the 3GPP 36.521 specification, Annexe E. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_common_clock_source_enabled.html language=enus -->
## TOPIC 00152: RFMXLTE_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_common_clock_source_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_common_clock_source_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. The ModAcc measurement ignores this attribute, when you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_DOWNLINK.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE. Get Function: RFmxLTE_ModAccGetCommonClockSourceEnabled Set Function: RFmxLTE_ModAccSetCommonClockSourceEnabled |
| Values: | RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE (0)The Sample Clock error is estimated independently. RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE (1)The Sample Clock error is estimated from carrier frequency offset. |
| RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE (0) | The Sample Clock error is estimated independently. |
| RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE (1) | The Sample Clock error is estimated from carrier frequency offset. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_evm_unit.html language=enus -->
## TOPIC 00153: RFMXLTE_ATTR_MODACC_EVM_UNIT

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_evm_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_evm_unit.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_EVM_UNIT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the units of the EVM results. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE. Get Function: RFmxLTE_ModAccGetEVMUnit Set Function: RFmxLTE_ModAccSetEVMUnit |
| Values: | RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE (0)The EVM is reported as a percentage. RFMXLTE_VAL_MODACC_EVM_UNIT_DB (1)The EVM is reported in dB. |
| RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE (0) | The EVM is reported as a percentage. |
| RFMXLTE_VAL_MODACC_EVM_UNIT_DB (1) | The EVM is reported in dB. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_evm_with_exclusion_period_enabled.html language=enus -->
## TOPIC 00154: RFMXLTE_ATTR_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_evm_with_exclusion_period_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_evm_with_exclusion_period_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether to exclude some portion of the slots when calculating the EVM. This attribute is valid only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP TS 36.521-1 specification for more information about exclusion. The measurement ignores this attribute, when you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_DOWNLINK.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED_FALSE. Get Function: RFmxLTE_ModAccGetEVMWithExclusionPeriodEnabled Set Function: RFmxLTE_ModAccSetEVMWithExclusionPeriodEnabled |
| Values: | RFMXLTE_VAL_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED_FALSE (0)EVM is calculated on complete slots. RFMXLTE_VAL_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED_TRUE (1)EVM is calculated on truncated slots. The power changes at the slot boundaries are detected by the measurement, and the defined 3GPP specification period is excluded from the slots being measured. |
| RFMXLTE_VAL_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED_FALSE (0) | EVM is calculated on complete slots. |
| RFMXLTE_VAL_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED_TRUE (1) | EVM is calculated on truncated slots. The power changes at the slot boundaries are detected by the measurement, and the defined 3GPP specification period is excluded from the slots being measured. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_fft_window_length.html language=enus -->
## TOPIC 00155: RFMXLTE_ATTR_MODACC_FFT_WINDOW_LENGTH

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_fft_window_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_fft_window_length.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_FFT_WINDOW_LENGTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This attribute is used when you set the RFMXLTE_ATTR_MODACC_FFT_WINDOW_TYPE attribute to RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. Refer to the Annexe E.3.2 of 3GPP 36.521 specification for more information. Refer to the LTE Modulation Accuracy (ModAcc) topic for more information about FFT Window Length. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is as given in the 3GPP specification. The default value is 91.7 %CP for 10M bandwidth. Valid values range from -1 to 100, inclusive.When this attribute is set to -1, RFmx populates the FFT Window Length based on carrier bandwidth automatically, as given in the Annexe E.5.1 of 3GPP 36.104 specification. Get Function: RFmxLTE_ModAccGetFFTWindowLength Set Function: RFmxLTE_ModAccSetFFTWindowLength |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_fft_window_offset.html language=enus -->
## TOPIC 00156: RFMXLTE_ATTR_MODACC_FFT_WINDOW_OFFSET

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_fft_window_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_fft_window_offset.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_FFT_WINDOW_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the position of the FFT window used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this attribute to 0, the EVM window starts at the end of cyclic prefix. If you set this attribute to 100, the EVM window starts at the beginning of cyclic prefix. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 50. Valid values are 0 to 100, inclusive. Get Function: RFmxLTE_ModAccGetFFTWindowOffset Set Function: RFmxLTE_ModAccSetFFTWindowOffset |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_frequency_error_estimation.html language=enus -->
## TOPIC 00157: RFMXLTE_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_frequency_error_estimation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_frequency_error_estimation.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the operation mode of frequency error estimation. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_NORMAL. Get Function: RFmxLTE_ModAccGetFrequencyErrorEstimation Set Function: RFmxLTE_ModAccSetFrequencyErrorEstimation |
| Values: | RFMXLTE_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_NORMAL (1)Estimate and correct frequency error of range +/- half subcarrier spacing. RFMXLTE_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_WIDE (2)Estimate and correct frequency error of range +/- half resource block when RFMXLTE_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED is RFMXLTE_VAL_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_TRUE. |
| RFMXLTE_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_NORMAL (1) | Estimate and correct frequency error of range +/- half subcarrier spacing. |
| RFMXLTE_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_WIDE (2) | Estimate and correct frequency error of range +/- half resource block when RFMXLTE_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED is RFMXLTE_VAL_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_TRUE. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_in_band_emission_mask_type.html language=enus -->
## TOPIC 00158: RFMXLTE_ATTR_MODACC_IN_BAND_EMISSION_MASK_TYPE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_in_band_emission_mask_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_in_band_emission_mask_type.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_IN_BAND_EMISSION_MASK_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the in-band emissions mask type to be used for measuring in-band emission margin (dB) and subblock in-Band emission margin (dB) results. Refer to section 6.5.2.3.5 of the 3GPP 36.521-1 specification for more information.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Release 8-10 for bandwidths other than 200 KHz and RFMXLTE_ATTR_EMTC_ANALYSIS_ENABLED is False. It is Release 11 Onwards, otherwise. Get Function: RFmxLTE_ModAccGetInBandEmissionMaskType Set Function: RFmxLTE_ModAccSetInBandEmissionMaskType |
| Values: | RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_8_10 (0)Specifies the mask type to be used for UE, supporting 3GPP Release 8 to 3GPP Release 10 specification. RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_11_ONWARDS (1)Specifies the mask type to be used for UE, supporting 3GPP Release 11 and higher specification. |
| RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_8_10 (0) | Specifies the mask type to be used for UE, supporting 3GPP Release 8 to 3GPP Release 10 specification. |
| RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_11_ONWARDS (1) | Specifies the mask type to be used for UE, supporting 3GPP Release 11 and higher specification. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_iq_gain_imbalance_correction_enabled.html language=enus -->
## TOPIC 00159: RFMXLTE_ATTR_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_iq_gain_imbalance_correction_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_iq_gain_imbalance_correction_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether to enable IQ gain imbalance correction. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_FALSE. Get Function: RFmxLTE_ModAccGetIQGainImbalanceCorrectionEnabled Set Function: RFmxLTE_ModAccSetIQGainImbalanceCorrectionEnabled |
| Values: | RFMXLTE_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_FALSE (0)IQ gain imbalance correction is disabled. RFMXLTE_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_TRUE (1)IQ gain imbalance correction is enabled. |
| RFMXLTE_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_FALSE (0) | IQ gain imbalance correction is disabled. |
| RFMXLTE_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_TRUE (1) | IQ gain imbalance correction is enabled. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_iq_origin_offset_estimation_enabled.html language=enus -->
## TOPIC 00160: RFMXLTE_ATTR_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_iq_origin_offset_estimation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_iq_origin_offset_estimation_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether to estimate IQ origin offset. Note: IQ origin offset estimation is supported only when you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_UPLINK or RFMXLTE_VAL_LINK_DIRECTION_SIDELINK. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_TRUE. Get Function: RFmxLTE_ModAccGetIQOriginOffsetEstimationEnabled Set Function: RFmxLTE_ModAccSetIQOriginOffsetEstimationEnabled |
| Values: | RFMXLTE_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_FALSE (0)IQ origin offset estimation and correction is disabled. RFMXLTE_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_TRUE (1)IQ origin offset estimation and correction is enabled. |
| RFMXLTE_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_FALSE (0) | IQ origin offset estimation and correction is disabled. |
| RFMXLTE_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_TRUE (1) | IQ origin offset estimation and correction is enabled. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_multicarrier_time_synchronization_mode.html language=enus -->
## TOPIC 00161: RFMXLTE_ATTR_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_multicarrier_time_synchronization_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_multicarrier_time_synchronization_mode.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the time synchronization mode used in uplink in the case of carrier aggregation. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE_COMMON. Get Function: RFmxLTE_ModAccGetMulticarrierTimeSynchronizationMode Set Function: RFmxLTE_ModAccSetMulticarrierTimeSynchronizationMode |
| Values: | RFMXLTE_VAL_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE_COMMON (0)Specifies that a common time synchronization value is used for synchronization of all the component carriers and time synchronization value is obtained from the synchronization of the first active component carrier of the first subblock. RFMXLTE_VAL_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE_PER_CARRIER (1)Specifies that time synchronization is performed on each component carrier. |
| RFMXLTE_VAL_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE_COMMON (0) | Specifies that a common time synchronization value is used for synchronization of all the component carriers and time synchronization value is obtained from the synchronization of the first active component carrier of the first subblock. |
| RFMXLTE_VAL_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE_PER_CARRIER (1) | Specifies that time synchronization is performed on each component carrier. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_downlink_detected_cell_id.html language=enus -->
## TOPIC 00162: RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_DETECTED_CELL_ID

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_downlink_detected_cell_id.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_downlink_detected_cell_id.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_DETECTED_CELL_ID

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeI32 |
| Description: | Returns the detected cell ID value. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsDownlinkDetectedCellID |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_downlink_ofdm_symbol_transmit_power.html language=enus -->
## TOPIC 00163: RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_OFDM_SYMBOL_TRANSMIT_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_downlink_ofdm_symbol_transmit_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_downlink_ofdm_symbol_transmit_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_OFDM_SYMBOL_TRANSMIT_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of power calculated in one OFDM symbol over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsDownlinkOFDMSymbolTransmitPower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_downlink_rs_transmit_power.html language=enus -->
## TOPIC 00164: RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_RS_TRANSMIT_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_downlink_rs_transmit_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_downlink_rs_transmit_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_RS_TRANSMIT_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsDownlinkRSTransmitPower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_mean_quadrature_error.html language=enus -->
## TOPIC 00165: RFMXLTE_ATTR_MODACC_RESULTS_MEAN_QUADRATURE_ERROR

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_mean_quadrature_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_mean_quadrature_error.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_MEAN_QUADRATURE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the estimated quadrature error averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured.When you set the RFMXLTE_ATTR_COMPONENT_CARRIER_BANDWIDTH attribute to 200.0 k and the RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES attribute to 12, this result is available. For other values of RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES, this result will be reported as NaN.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsMeanQuadratureError |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_mean_rms_csrs_evm.html language=enus -->
## TOPIC 00166: RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_CSRS_EVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_mean_rms_csrs_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_mean_rms_csrs_evm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_CSRS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calculated on RS resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsMeanRMSCSRSEVM |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_mean_rms_pss_evm.html language=enus -->
## TOPIC 00167: RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PSS_EVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_mean_rms_pss_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_mean_rms_pss_evm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PSS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calculated on primary synchronization signal (PSS) channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsMeanRMSPSSEVM |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_mean_rms_srs_evm.html language=enus -->
## TOPIC 00168: RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_SRS_EVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_mean_rms_srs_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_mean_rms_srs_evm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_SRS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calculated on the SRS symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsMeanRMSSRSEVM |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_mean_rms_sss_evm.html language=enus -->
## TOPIC 00169: RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_SSS_EVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_mean_rms_sss_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_mean_rms_sss_evm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_SSS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calculated on secondary synchronization signal (SSS) channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsMeanRMSSSSEVM |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_mean_srs_power.html language=enus -->
## TOPIC 00170: RFMXLTE_ATTR_MODACC_RESULTS_MEAN_SRS_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_mean_srs_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_mean_srs_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_MEAN_SRS_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of power calculated on SRS over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This values is expressed in dBm. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsMeanSRSPower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_mean_symbol_clock_error.html language=enus -->
## TOPIC 00171: RFMXLTE_ATTR_MODACC_RESULTS_MEAN_SYMBOL_CLOCK_ERROR

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_mean_symbol_clock_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_mean_symbol_clock_error.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_MEAN_SYMBOL_CLOCK_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the estimated symbol clock error averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in ppm. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsMeanSymbolClockError |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_npusch_maximum_peak_data_evm.html language=enus -->
## TOPIC 00172: RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MAXIMUM_PEAK_DATA_EVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_npusch_maximum_peak_data_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_npusch_maximum_peak_data_evm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MAXIMUM_PEAK_DATA_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the maximum value of peak EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to percentage, the result is returned as a percentage, and when you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the result is returned in dB. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. The default value is 0. Get Function: RFmxLTE_ModAccGetResultsNPUSCHMaximumPeakDataEVM |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_npusch_maximum_peak_dmrs_evm.html language=enus -->
## TOPIC 00173: RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MAXIMUM_PEAK_DMRS_EVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_npusch_maximum_peak_dmrs_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_npusch_maximum_peak_dmrs_evm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MAXIMUM_PEAK_DMRS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the maximum value of peak EVMs calculated on NPUSCH DMRS over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the result is returned as a percentage, and when you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the result is returned in dB. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. The default value is 0. Get Function: RFmxLTE_ModAccGetResultsNPUSCHMaximumPeakDMRSEVM |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_npusch_mean_dmrs_power.html language=enus -->
## TOPIC 00174: RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MEAN_DMRS_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_npusch_mean_dmrs_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_npusch_mean_dmrs_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MEAN_DMRS_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute.This value is expressed in dBm. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is 0. Get Function: RFmxLTE_ModAccGetResultsNPUSCHMeanDMRSPower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_npusch_mean_rms_data_evm.html language=enus -->
## TOPIC 00175: RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MEAN_RMS_DATA_EVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_npusch_mean_rms_data_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_npusch_mean_rms_data_evm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MEAN_RMS_DATA_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to percentage, the result is returned as a percentage, and when you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the result is returned in dB.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsNPUSCHMeanRMSDataEVM |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_pdsch_mean_rms_256qam_evm.html language=enus -->
## TOPIC 00176: RFMXLTE_ATTR_MODACC_RESULTS_PDSCH_MEAN_RMS_256QAM_EVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_pdsch_mean_rms_256qam_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_pdsch_mean_rms_256qam_evm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_PDSCH_MEAN_RMS_256QAM_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsPDSCHMeanRMS256QAMEVM |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_pdsch_mean_rms_evm.html language=enus -->
## TOPIC 00177: RFMXLTE_ATTR_MODACC_RESULTS_PDSCH_MEAN_RMS_EVM

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_pdsch_mean_rms_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_pdsch_mean_rms_evm.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_PDSCH_MEAN_RMS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calculated on PDSCH data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to RFMXLTE_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsPDSCHMeanRMSEVM |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_peak_composite_evm_slot_index.html language=enus -->
## TOPIC 00178: RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SLOT_INDEX

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_peak_composite_evm_slot_index.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_peak_composite_evm_slot_index.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SLOT_INDEX

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeI32 |
| Description: | Returns the slot index where the ModAcc maximum peak composite EVM occurs.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsPeakCompositeEVMSlotIndex |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_peak_composite_evm_subcarrier_index.html language=enus -->
## TOPIC 00179: RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SUBCARRIER_INDEX

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_peak_composite_evm_subcarrier_index.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_peak_composite_evm_subcarrier_index.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SUBCARRIER_INDEX

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeI32 |
| Description: | Returns the subcarrier index where the maximum peak composite EVM for ModAcc occurs.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsPeakCompositeEVMSubcarrierIndex |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_spectral_flatness_range1_maximum_to_range2_minimum.html language=enus -->
## TOPIC 00180: RFMXLTE_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE2_MINIMUM

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_spectral_flatness_range1_maximum_to_range2_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_spectral_flatness_range1_maximum_to_range2_minimum.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE2_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Measurement Offset parameter. The frequency Range1 and frequency Measurement Offset parameter are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. This value is expressed in dB.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsSpectralFlatnessRange1MaximumToRange2Minimum |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_results_subblock_mean_quadrature_error.html language=enus -->
## TOPIC 00181: RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_QUADRATURE_ERROR

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_results_subblock_mean_quadrature_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_results_subblock_mean_quadrature_error.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_QUADRATURE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the estimated quadrature error averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock. This result is valid only when you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_UPLINK and the RFMXLTE_ATTR_TRANSMITTER_ARCHITECTURE attribute to RFMXLTE_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_SUBBLOCK. Otherwise, this parameter returns NaN, as measurement of this result is currently not supported.Use 'subblock(n)' as the selector string to read this result. Get Function: RFmxLTE_ModAccGetResultsSubblockMeanQuadratureError |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_modacc_spectral_flatness_condition.html language=enus -->
## TOPIC 00182: RFMXLTE_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_modacc_spectral_flatness_condition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_modacc_spectral_flatness_condition.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the frequency ranges at which to measure spectral flatness. The measurement ignores this attribute, when you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to RFMXLTE_VAL_LINK_DIRECTION_DOWNLINK.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_NORMAL. Get Function: RFmxLTE_ModAccGetSpectralFlatnessCondition Set Function: RFmxLTE_ModAccSetSpectralFlatnessCondition |
| Values: | RFMXLTE_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_NORMAL (0)Uses the frequency range defined in the section 6.5.2.4.5, and table 6.5.2.4.3-1 of 3GPP 36.521 specification. RFMXLTE_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_EXTREME (1)Uses the frequency range defined in the section 6.5.2.4.5, and table 6.5.2.4.3-2 of 3GPP 36.521 specification. |
| RFMXLTE_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_NORMAL (0) | Uses the frequency range defined in the section 6.5.2.4.5, and table 6.5.2.4.3-1 of 3GPP 36.521 specification. |
| RFMXLTE_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_EXTREME (1) | Uses the frequency range defined in the section 6.5.2.4.5, and table 6.5.2.4.3-2 of 3GPP 36.521 specification. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_npusch_dmrs_base_sequence_index.html language=enus -->
## TOPIC 00183: RFMXLTE_ATTR_NPUSCH_DMRS_BASE_SEQUENCE_INDEX

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_npusch_dmrs_base_sequence_index.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_npusch_dmrs_base_sequence_index.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_NPUSCH_DMRS_BASE_SEQUENCE_INDEX

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the base sequence index of the Narrowband Physical Uplink Shared Channel (NPUSCH) DMRS as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. This attribute is valid when you set the NPUSCH Group Hopping Enabled attribute to False, the RFMXLTE_ATTR_NPUSCH_DMRS_BASE_SEQUENCE_MODE attribute to RFMXLTE_VAL_NPUSCH_DMRS_BASE_SEQUENCE_MODE_MANUAL, and the RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES attribute to 3, 6, or 12.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is 0. For 3 tones, valid values are 0 to 11, inclusive. For 6 tones, valid values are 0 to 13, inclusive. For 12 tones, valid values are 0 to 29, inclusive. Get Function: RFmxLTE_GetNPUSCHDMRSBaseSequenceIndex Set Function: RFmxLTE_SetNPUSCHDMRSBaseSequenceIndex |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_npusch_dmrs_base_sequence_mode.html language=enus -->
## TOPIC 00184: RFMXLTE_ATTR_NPUSCH_DMRS_BASE_SEQUENCE_MODE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_npusch_dmrs_base_sequence_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_npusch_dmrs_base_sequence_mode.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_NPUSCH_DMRS_BASE_SEQUENCE_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the RFMXLTE_ATTR_NPUSCH_DMRS_BASE_SEQUENCE_INDEX attribute is computed by the measurement or specified by you. This attribute is valid when you set the NPUSCH Group Hopping Enabled attribute to False, the RFMXLTE_ATTR_NPUSCH_FORMAT attribute to 1, and the RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES attribute to 3, 6, or 12.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is RFMXLTE_VAL_NPUSCH_DMRS_BASE_SEQUENCE_MODE_AUTO. Get Function: RFmxLTE_GetNPUSCHDMRSBaseSequenceMode Set Function: RFmxLTE_SetNPUSCHDMRSBaseSequenceMode |
| Values: | RFMXLTE_VAL_NPUSCH_DMRS_BASE_SEQUENCE_MODE_MANUAL (0)The measurement uses the value that you specify for the NPUSCH DMRS Base Sequence Index attribute. RFMXLTE_VAL_NPUSCH_DMRS_BASE_SEQUENCE_MODE_AUTO (1)The measurement uses the value of RFMXLTE_ATTR_NCELL_ID attribute to compute the NPUSCH DMRS Base Sequence Index as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. |
| RFMXLTE_VAL_NPUSCH_DMRS_BASE_SEQUENCE_MODE_MANUAL (0) | The measurement uses the value that you specify for the NPUSCH DMRS Base Sequence Index attribute. |
| RFMXLTE_VAL_NPUSCH_DMRS_BASE_SEQUENCE_MODE_AUTO (1) | The measurement uses the value of RFMXLTE_ATTR_NCELL_ID attribute to compute the NPUSCH DMRS Base Sequence Index as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_npusch_dmrs_cyclic_shift.html language=enus -->
## TOPIC 00185: RFMXLTE_ATTR_NPUSCH_DMRS_CYCLIC_SHIFT

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_npusch_dmrs_cyclic_shift.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_npusch_dmrs_cyclic_shift.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_NPUSCH_DMRS_CYCLIC_SHIFT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the cyclic shift of the narrowband physical uplink shared channel (NPUSCH) DMRS as defined in Table 10.1.4.1.2-3 of the 3GPP TS 36.211 specification. This attribute is valid when you set the RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES attribute to 3 or 6. If the value of RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES attribute is 12, the RFMXLTE_ATTR_NPUSCH_DMRS_CYCLIC_SHIFT attribute has a fixed value of 0.Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is 0. For 3 tones, valid values are 0 to 2, inclusive. For 6 tones, valid values are 0 to 3, inclusive. Get Function: RFmxLTE_GetNPUSCHDMRSCyclicShift Set Function: RFmxLTE_SetNPUSCHDMRSCyclicShift |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_npusch_dmrs_delta_sequence_shift.html language=enus -->
## TOPIC 00186: RFMXLTE_ATTR_NPUSCH_DMRS_DELTA_SEQUENCE_SHIFT

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_npusch_dmrs_delta_sequence_shift.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_npusch_dmrs_delta_sequence_shift.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_NPUSCH_DMRS_DELTA_SEQUENCE_SHIFT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS, which is used to calculate the sequence shift pattern. This value is used to compute the sequence group number as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. This attribute is valid when you set the RFMXLTE_ATTR_NPUSCH_DMRS_GROUP_HOPPING_ENABLED attribute to RFMXLTE_VAL_NPUSCH_DMRS_GROUP_HOPPING_ENABLED_TRUE. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is 0. Valid values are 0 to 29, inclusive. Get Function: RFmxLTE_GetNPUSCHDMRSDeltaSequenceShift Set Function: RFmxLTE_SetNPUSCHDMRSDeltaSequenceShift |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_npusch_dmrs_group_hopping_enabled.html language=enus -->
## TOPIC 00187: RFMXLTE_ATTR_NPUSCH_DMRS_GROUP_HOPPING_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_npusch_dmrs_group_hopping_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_npusch_dmrs_group_hopping_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_NPUSCH_DMRS_GROUP_HOPPING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the group hopping is enabled for narrowband physical uplink shared channel (NPUSCH) DMRS. This attribute is valid only when the RFMXLTE_ATTR_NPUSCH_FORMAT is 1. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is RFMXLTE_VAL_NPUSCH_DMRS_GROUP_HOPPING_ENABLED_FALSE. Get Function: RFmxLTE_GetNPUSCHDMRSGroupHoppingEnabled Set Function: RFmxLTE_SetNPUSCHDMRSGroupHoppingEnabled |
| Values: | RFMXLTE_VAL_NPUSCH_DMRS_GROUP_HOPPING_ENABLED_FALSE (0)Group hopping is disabled. RFMXLTE_VAL_NPUSCH_DMRS_GROUP_HOPPING_ENABLED_TRUE (1)Group hopping is enabled. The sequence group number is calculated as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. |
| RFMXLTE_VAL_NPUSCH_DMRS_GROUP_HOPPING_ENABLED_FALSE (0) | Group hopping is disabled. |
| RFMXLTE_VAL_NPUSCH_DMRS_GROUP_HOPPING_ENABLED_TRUE (1) | Group hopping is enabled. The sequence group number is calculated as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_number_of_steps.html language=enus -->
## TOPIC 00188: RFMXLTE_ATTR_NUMBER_OF_STEPS

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_number_of_steps.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_number_of_steps.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_NUMBER_OF_STEPS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the number of active steps in a list. You need to use a selector string to configure or read this attribute for the list instance. The default value is 0. Get Function: RFmxLTE_GetNumberOfSteps Set Function: RFmxLTE_SetNumberOfSteps |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_number_of_subblocks.html language=enus -->
## TOPIC 00189: RFMXLTE_ATTR_NUMBER_OF_SUBBLOCKS

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_number_of_subblocks.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_number_of_subblocks.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_NUMBER_OF_SUBBLOCKS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the number of subblocks that are configured in intra-band noncontiguous carrier aggregation. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Set this attribute to 1 for single carrier and intra-band contiguous carrier aggregation. Get Function: RFmxLTE_GetNumberOfSubblocks Set Function: RFmxLTE_SetNumberOfSubblocks |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_obw_all_traces_enabled.html language=enus -->
## TOPIC 00190: RFMXLTE_ATTR_OBW_ALL_TRACES_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_obw_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_obw_all_traces_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_OBW_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_FALSE. Get Function: RFmxLTE_OBWGetAllTracesEnabled Set Function: RFmxLTE_OBWSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_obw_amplitude_correction_type.html language=enus -->
## TOPIC 00191: RFMXLTE_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_obw_amplitude_correction_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_obw_amplitude_correction_type.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY. Get Function: RFmxLTE_OBWGetAmplitudeCorrectionType Set Function: RFmxLTE_OBWSetAmplitudeCorrectionType |
| Values: | RFMXLTE_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY (0)All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. RFMXLTE_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN (1)An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |
| RFMXLTE_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY (0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXLTE_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN (1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_obw_averaging_count.html language=enus -->
## TOPIC 00192: RFMXLTE_ATTR_OBW_AVERAGING_COUNT

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_obw_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_obw_averaging_count.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_OBW_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXLTE_ATTR_OBW_AVERAGING_ENABLED attribute to RFMXLTE_VAL_OBW_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxLTE_OBWGetAveragingCount Set Function: RFmxLTE_OBWSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_obw_averaging_enabled.html language=enus -->
## TOPIC 00193: RFMXLTE_ATTR_OBW_AVERAGING_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_obw_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_obw_averaging_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_OBW_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the OBW measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_OBW_AVERAGING_ENABLED_FALSE. Get Function: RFmxLTE_OBWGetAveragingEnabled Set Function: RFmxLTE_OBWSetAveragingEnabled |
| Values: | RFMXLTE_VAL_OBW_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXLTE_VAL_OBW_AVERAGING_ENABLED_TRUE (1)The OBW measurement uses the value of the RFMXLTE_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |
| RFMXLTE_VAL_OBW_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXLTE_VAL_OBW_AVERAGING_ENABLED_TRUE (1) | The OBW measurement uses the value of the RFMXLTE_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_obw_averaging_type.html language=enus -->
## TOPIC 00194: RFMXLTE_ATTR_OBW_AVERAGING_TYPE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_obw_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_obw_averaging_type.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_OBW_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_OBW_AVERAGING_TYPE_RMS. Get Function: RFmxLTE_OBWGetAveragingType Set Function: RFmxLTE_OBWSetAveragingType |
| Values: | RFMXLTE_VAL_OBW_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXLTE_VAL_OBW_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. RFMXLTE_VAL_OBW_AVERAGING_TYPE_SCALAR (2)The square root of the power spectrum is averaged. RFMXLTE_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXLTE_VAL_OBW_AVERAGING_TYPE_MINIMUM (4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXLTE_VAL_OBW_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXLTE_VAL_OBW_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXLTE_VAL_OBW_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |
| RFMXLTE_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXLTE_VAL_OBW_AVERAGING_TYPE_MINIMUM (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_pcfich_cfi.html language=enus -->
## TOPIC 00195: RFMXLTE_ATTR_PCFICH_CFI

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_pcfich_cfi.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_pcfich_cfi.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_PCFICH_CFI

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the control format indicator (CFI) carried by physical control format indicator channel (PCFICH). CFI is used to compute the number of OFDM symbols which will determine the size of physical downlink control channel (PDCCH) within a subframe. Use 'subframe(l)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/subframe(l)' as the selector string to configure or read this attribute. The default value is 1. Get Function: RFmxLTE_GetPCFICHCFI Set Function: RFmxLTE_SetPCFICHCFI |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_pcfich_power.html language=enus -->
## TOPIC 00196: RFMXLTE_ATTR_PCFICH_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_pcfich_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_pcfich_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_PCFICH_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the power of physical control format indicator channel (PCFICH) relative to the power of cell-specific reference signal. This value is expressed in dB. Use 'subframe(l)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/subframe(l)' as the selector string to configure or read this attribute. The default value is 0. Get Function: RFmxLTE_GetDownlinkUserDefinedPCFICHPower Set Function: RFmxLTE_SetDownlinkUserDefinedPCFICHPower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_pdsch_resource_block_allocation.html language=enus -->
## TOPIC 00197: RFMXLTE_ATTR_PDSCH_RESOURCE_BLOCK_ALLOCATION

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_pdsch_resource_block_allocation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_pdsch_resource_block_allocation.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_PDSCH_RESOURCE_BLOCK_ALLOCATION

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeStringRFmxLTE_GetAttributeString |
| Description: | Specifies the resource blocks of the physical downlink shared channel (PDSCH) allocation. The following string formats are supported for this attribute: 1) RBStartValue1-RBStopValue1,RBStartValue2-RBStopValue22) RB1,RB23) RBStartValue1-RBStopValue1, RB1,RBStartValue2-RBStopValue2,RB2For example: If the RB allocation is 0-5,7,8,10-15, the RB allocation string specifies contiguous resource blocks from 0 to 5, resource block 7, resource block 8, and contiguous resource blocks from 10 to 15.Use 'PDSCH(m)' or 'subframe(l)' or 'carrier(k)' or 'subblock(n)/carrier(k)/subframe(l)/PDSCH(m)' as the selector string to configure or read this attribute. The default value is 0-49. Get Function: RFmxLTE_GetPDSCHResourceBlockAllocation Set Function: RFmxLTE_SetPDSCHResourceBlockAllocation |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_phich_duration.html language=enus -->
## TOPIC 00198: RFMXLTE_ATTR_PHICH_DURATION

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_phich_duration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_phich_duration.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_PHICH_DURATION

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the physical hybrid-ARQ indicator channel (PHICH) duration. Use 'subframe(l)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/subframe(l)' as the selector string to configure or read this attribute. The default value is RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_DURATION_NORMAL. Get Function: RFmxLTE_GetPHICHDuration Set Function: RFmxLTE_SetPHICHDuration |
| Values: | RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_DURATION_NORMAL (0)Orthogonal sequences of length 4 is used to extract PHICH. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_DURATION_NORMAL (0) | Orthogonal sequences of length 4 is used to extract PHICH. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_phich_resource.html language=enus -->
## TOPIC 00199: RFMXLTE_ATTR_PHICH_RESOURCE

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_phich_resource.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_phich_resource.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_PHICH_RESOURCE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the physical channel hybridARQ indicator channel (PHICH) resource value. This value is expressed in Ng. This attribute is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH. Use 'subframe(l)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/subframe(l)' as the selector string to configure or read this attribute. The default value is 1/6. Get Function: RFmxLTE_GetPHICHResource Set Function: RFmxLTE_SetPHICHResource |
| Values: | RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE_SIXTH (0)Specifies the PHICH resource value is 1/6. RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_HALF (1)Specifies the PHICH resource value is 1/2. RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE (2)Specifies the PHICH resource value is 1. RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_TWO (3)Specifies the PHICH resource value is 2. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE_SIXTH (0) | Specifies the PHICH resource value is 1/6. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_HALF (1) | Specifies the PHICH resource value is 1/2. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE (2) | Specifies the PHICH resource value is 1. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_TWO (3) | Specifies the PHICH resource value is 2. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_pssch_resource_block_offset.html language=enus -->
## TOPIC 00200: RFMXLTE_ATTR_PSSCH_RESOURCE_BLOCK_OFFSET

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_pssch_resource_block_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_pssch_resource_block_offset.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_PSSCH_RESOURCE_BLOCK_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the starting resource block number of a physical sidelink shared channel (PSSCH) allocation. Use 'carrier(k)' or 'subblock(n)/carrier(k)' as the selector string to configure or read this attribute. The default value is 0. Get Function: RFmxLTE_GetPSSCHResourceBlockOffset Set Function: RFmxLTE_SetPSSCHResourceBlockOffset |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_pusch_resource_block_offset.html language=enus -->
## TOPIC 00201: RFMXLTE_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_pusch_resource_block_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_pusch_resource_block_offset.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the starting resource block number of a physical uplink shared channel (PUSCH) cluster.Use 'cluster(l)' or 'carrier(k)' or 'subblock(n)/carrier(k)'/cluster(l)' as the selector string to configure or read this attribute. The default value is 0. Get Function: RFmxLTE_GetPUSCHResourceBlockOffset Set Function: RFmxLTE_SetPUSCHResourceBlockOffset |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_aggregated_maximum_power.html language=enus -->
## TOPIC 00202: RFMXLTE_ATTR_SEM_AGGREGATED_MAXIMUM_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_aggregated_maximum_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_aggregated_maximum_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_AGGREGATED_MAXIMUM_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the aggregated maximum output power of all transmit antenna connectors. This value is expressed in dBm. Refer to the Section 6.6.3 of 3GPP 36.141 specification for more details. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Valid values are within 20, inclusive. This attribute is considered only when you set the Link Direction attribute to Downlink, eNodeB Category attribute to Home Base Station, and SEM DL Mask Type attribute to eNodeB Category Based. Get Function: RFmxLTE_SEMGetAggregatedMaximumPower Set Function: RFmxLTE_SEMSetAggregatedMaximumPower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_averaging_count.html language=enus -->
## TOPIC 00203: RFMXLTE_ATTR_SEM_AVERAGING_COUNT

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_averaging_count.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXLTE_ATTR_SEM_AVERAGING_ENABLED attribute to RFMXLTE_VAL_SEM_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxLTE_SEMGetAveragingCount Set Function: RFmxLTE_SEMSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_lower_offset_margin_absolute_power.html language=enus -->
## TOPIC 00204: RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_lower_offset_margin_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_lower_offset_margin_absolute_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the power at which the margin occurs in the lower (negative) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm.Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information about SEM offsets. Get Function: RFmxLTE_SEMGetResultsLowerOffsetMarginAbsolutePower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_lower_offset_margin_frequency.html language=enus -->
## TOPIC 00205: RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_lower_offset_margin_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_lower_offset_margin_frequency.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the frequency at which the margin occurs in the lower (negative) offset. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz.Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information about SEM offsets. Get Function: RFmxLTE_SEMGetResultsLowerOffsetMarginFrequency |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_measurement_status.html language=enus -->
## TOPIC 00206: RFMXLTE_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_measurement_status.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeI32 |
| Description: | Returns the overall measurement status based on the standard mask type that you configure in the SEM Standard Mask Type attribute. You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxLTE_SEMGetResultsMeasurementStatus |
| Values: | RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_FAIL (0)Indicates that the measurement has failed. RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_PASS (1)Indicates that the measurement has passed. |
| RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |
| RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_subblock_integration_bandwidth.html language=enus -->
## TOPIC 00207: RFMXLTE_ATTR_SEM_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_subblock_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_subblock_integration_bandwidth.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the integration bandwidth of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use 'subblock(n)' as the selector string to read this result. Get Function: RFmxLTE_SEMGetResultsSubblockIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_subblock_power.html language=enus -->
## TOPIC 00208: RFMXLTE_ATTR_SEM_RESULTS_SUBBLOCK_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_subblock_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_subblock_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_SUBBLOCK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the power measured over the integration bandwidth of the subblock. This value is expressed in dBm. Use 'subblock(n)' as the selector string to read this result. Get Function: RFmxLTE_SEMGetResultsSubblockPower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_total_aggregated_power.html language=enus -->
## TOPIC 00209: RFMXLTE_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_total_aggregated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_total_aggregated_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm. You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxLTE_SEMGetResultsTotalAggregatedPower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_upper_offset_absolute_peak_power.html language=enus -->
## TOPIC 00210: RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_upper_offset_absolute_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_upper_offset_absolute_peak_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the power in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm.Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information about SEM offsets. Get Function: RFmxLTE_SEMGetResultsUpperOffsetAbsolutePeakPower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_upper_offset_margin.html language=enus -->
## TOPIC 00211: RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_upper_offset_margin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_upper_offset_margin.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the margin from the absolute limit mask for the upper (positive) offset. The Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz.Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information about SEM offsets. Get Function: RFmxLTE_SEMGetResultsUpperOffsetMargin |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_upper_offset_margin_absolute_power.html language=enus -->
## TOPIC 00212: RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_upper_offset_margin_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_upper_offset_margin_absolute_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the power at which the margin occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm.Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information about SEM offsets. Get Function: RFmxLTE_SEMGetResultsUpperOffsetMarginAbsolutePower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_upper_offset_margin_relative_power.html language=enus -->
## TOPIC 00213: RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_upper_offset_margin_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_upper_offset_margin_relative_power.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeF64 |
| Description: | Returns the power at which the margin occurs in the upper (positive) offset segment relative to the total aggregated power. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB.Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information about SEM offsets. Get Function: RFmxLTE_SEMGetResultsUpperOffsetMarginRelativePower |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_results_upper_offset_measurement_status.html language=enus -->
## TOPIC 00214: RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_results_upper_offset_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_results_upper_offset_measurement_status.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxLTE_GetAttributeI32 |
| Description: | Returns the measurement status based on the user-configured standard measurement limits and the failure criteria specified by Limit Fail Mask for the upper (positive) offset. For intra-band noncontiguous case, the offset segment may be truncated or discarded based on offset overlap rules defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. Use 'offset(k)' or 'subblock(n)/offset(k)' as the selector string to read this result. Refer to the LTE Uplink Spectral Emission Mask and LTE Downlink Spectral Emission Mask topics for more information about SEM offsets. Get Function: RFmxLTE_SEMGetResultsUpperOffsetMeasurementStatus |
| Values: | RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL (0)Indicates that the measurement has failed. RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS (1)Indicates that the measurement has passed. |
| RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |
| RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_sweep_time_auto.html language=enus -->
## TOPIC 00215: RFMXLTE_ATTR_SEM_SWEEP_TIME_AUTO

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_sweep_time_auto.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_SEM_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxLTE_SEMGetSweepTimeAuto Set Function: RFmxLTE_SEMSetSweepTimeAuto |
| Values: | RFMXLTE_VAL_SEM_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the sweep time that you specify in the RFMXLTE_ATTR_SEM_SWEEP_TIME_INTERVAL attribute. RFMXLTE_VAL_SEM_SWEEP_TIME_AUTO_TRUE (1)The measurement uses a sweep time of 1 ms. |
| RFMXLTE_VAL_SEM_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the RFMXLTE_ATTR_SEM_SWEEP_TIME_INTERVAL attribute. |
| RFMXLTE_VAL_SEM_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses a sweep time of 1 ms. |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_sem_sweep_time_interval.html language=enus -->
## TOPIC 00216: RFMXLTE_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_sem_sweep_time_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_sem_sweep_time_interval.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SEM_SWEEP_TIME_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeF64RFmxLTE_GetAttributeF64 |
| Description: | Specifies the sweep time when you set the RFMXLTE_ATTR_SEM_SWEEP_TIME_AUTO attribute to RFMXLTE_VAL_SEM_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1 ms. Get Function: RFmxLTE_SEMGetSweepTimeInterval Set Function: RFmxLTE_SEMSetSweepTimeInterval |

<!--NI_TOPIC bundle=rfmx-lte-cvi path=rfmxlte_attr_slotphase_common_clock_source_enabled.html language=enus -->
## TOPIC 00217: RFMXLTE_ATTR_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED

- bundle_id: `rfmx-lte-cvi`
- source_path: `rfmxlte_attr_slotphase_common_clock_source_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-cvi/raw/resource/enus/rfmxlte_attr_slotphase_common_clock_source_enabled.html
- document_id: `rfmx-lte-cvi`
- page_type: `leaf`
- content_type: ``

RFMXLTE_ATTR_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxLTE_SetAttributeI32RFmxLTE_GetAttributeI32 |
| Description: | Specifies whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXLTE_VAL_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED_TRUE. Get Function: RFmxLTE_SlotPhaseGetCommonClockSourceEnabled Set Function: RFmxLTE_SlotPhaseSetCommonClockSourceEnabled |
| Values: | RFMXLTE_VAL_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED_FALSE (0)The Sample Clock error is estimated independently. RFMXLTE_VAL_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED_TRUE (1)The Sample Clock error is estimated from carrier frequency offset. |
| RFMXLTE_VAL_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED_FALSE (0) | The Sample Clock error is estimated independently. |
| RFMXLTE_VAL_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED_TRUE (1) | The Sample Clock error is estimated from carrier frequency offset. |
