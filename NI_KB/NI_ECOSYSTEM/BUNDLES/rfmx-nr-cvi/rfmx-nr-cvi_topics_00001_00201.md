# NI DOCUMENT BUNDLE: rfmx-nr-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-nr-cvi start=1 end=201 -->
<!--NI_TOPIC bundle=rfmx-nr-cvi path=bp_help_file_title.html language=enus -->
## TOPIC 00001: RFmx NR C Reference

- bundle_id: `rfmx-nr-cvi`
- source_path: `bp_help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/bp_help_file_title.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmx NR C Reference

This help file contains information about the RFmx NR functions, attributes, and values that you can use when programming your application.

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_acpcfgmeasurementmethod.html language=enus -->
## TOPIC 00002: RFmxNR_ACPCfgMeasurementMethod

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_acpcfgmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_acpcfgmeasurementmethod.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ACPCfgMeasurementMethod

int32 __stdcall RFmxNR_ACPCfgMeasurementMethod (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 measurementMethod);

#### Purpose

Configures the method for performing the ACP measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| measurementMethod | int32 | Specifies the method for performing the ACP measurement. RFMXNR_VAL_ACP_MEASUREMENT_METHOD_NORMAL (0) The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range.RFMXNR_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE (1) The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. supportedDevices:PXIe-5665/5668RRFMXNR_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT (2) The ACP measurement acquires I/Q samples for a duration specified by the RFMXNR_ATTR_ACP_SWEEP_TIME_INTERVAL attribute.These samples are divided into smaller chunks. The size of each chunk is defined by the RFMXNR_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize the ACP Measurement speed. Accuracy of the results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following attributes have limited support when you set the RFMXNR_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXNR_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT. The RFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute will only support RFMXNR_VAL_ACP_RBW_AUTO_TRUE value. The RFMXNR_ATTR_ACP_RBW_FILTER_TYPE attribute will only support RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED value. The RFMXNR_ATTR_ACP_AVERAGING_COUNT attribute will only support a value greater than or equal to 1. The RFMXNR_ATTR_ACP_NOISE_COMPENSATION_ENABLED attribute will only support RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE value. The RFMXNR_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS attribute will only support a value of 1. The RFMXNR_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE attribute will only support a value of RFMXNR_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY. Note For multi-span FFT, the averaging count should be 1. |
| RFMXNR_VAL_ACP_MEASUREMENT_METHOD_NORMAL (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |  |
| RFMXNR_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. supportedDevices:PXIe-5665/5668R |  |
| RFMXNR_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT (2) | The ACP measurement acquires I/Q samples for a duration specified by the RFMXNR_ATTR_ACP_SWEEP_TIME_INTERVAL attribute.These samples are divided into smaller chunks. The size of each chunk is defined by the RFMXNR_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize the ACP Measurement speed. Accuracy of the results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following attributes have limited support when you set the RFMXNR_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXNR_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT. The RFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute will only support RFMXNR_VAL_ACP_RBW_AUTO_TRUE value. The RFMXNR_ATTR_ACP_RBW_FILTER_TYPE attribute will only support RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED value. The RFMXNR_ATTR_ACP_AVERAGING_COUNT attribute will only support a value greater than or equal to 1. The RFMXNR_ATTR_ACP_NOISE_COMPENSATION_ENABLED attribute will only support RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE value. The RFMXNR_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS attribute will only support a value of 1. The RFMXNR_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE attribute will only support a value of RFMXNR_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY. |  |
|  | Note For multi-span FFT, the averaging count should be 1. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_acpcfgnumberofendcoffsets.html language=enus -->
## TOPIC 00003: RFmxNR_ACPCfgNumberOfENDCOffsets

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_acpcfgnumberofendcoffsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_acpcfgnumberofendcoffsets.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ACPCfgNumberOfENDCOffsets

int32 __stdcall RFmxNR_ACPCfgNumberOfENDCOffsets (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfENDCOffsets);

#### Purpose

Configures the number of ENDC adjacent channels of the subblock.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "subblock0".Example:"subblock0""signal::sig1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| numberOfENDCOffsets | int32 | Specifies the number of ENDC adjacent channel offsets to be configured at offset positions. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_acpcfgpowerunits.html language=enus -->
## TOPIC 00004: RFmxNR_ACPCfgPowerUnits

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_acpcfgpowerunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_acpcfgpowerunits.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ACPCfgPowerUnits

int32 __stdcall RFmxNR_ACPCfgPowerUnits (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 powerUnits);

#### Purpose

Configures the unit for absolute power.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| powerUnits | int32 | Specifies the unit of absolute power. RFMXNR_VAL_ACP_POWER_UNITS_DBM (0) Indicates that the absolute power is expressed in dBm.RFMXNR_VAL_ACP_POWER_UNITS_DBM_BY_HZ (1) Indicates that the absolute power is expressed in dBm/Hz. |
| RFMXNR_VAL_ACP_POWER_UNITS_DBM (0) | Indicates that the absolute power is expressed in dBm. |  |
| RFMXNR_VAL_ACP_POWER_UNITS_DBM_BY_HZ (1) | Indicates that the absolute power is expressed in dBm/Hz. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_acpcfgrbwfilter.html language=enus -->
## TOPIC 00005: RFmxNR_ACPCfgRBWFilter

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_acpcfgrbwfilter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_acpcfgrbwfilter.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ACPCfgRBWFilter

int32 __stdcall RFmxNR_ACPCfgRBWFilter (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 RBWAuto,
 float64 RBW,
 int32 RBWFilterType);

#### Purpose

Configures the resolution bandwidth (RBW) filter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| RBWAuto | int32 | Specifies whether the measurement computes the RBW. RFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE (0) The measurement uses the RBW that you specify in the RBW parameter.RFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_TRUE (1) The measurement computes the RBW. |
| RFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE (0) | The measurement uses the RBW that you specify in the RBW parameter. |  |
| RFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_TRUE (1) | The measurement computes the RBW. |  |
| RBW | float64 | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RBWAuto parameter to RFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE. This value is expressed in Hz. |
| RBWFilterType | int32 | Specifies the shape of the RBW filter. RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED (0) No RBW filtering is performed. RFMXNR_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN (1) An RBW filter with a Gaussian response is applied.RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FLAT (2) An RBW filter with a flat response is applied. |
| RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |  |
| RFMXNR_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_acpfetchtotalaggregatedpower.html language=enus -->
## TOPIC 00006: RFmxNR_ACPFetchTotalAggregatedPower

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_acpfetchtotalaggregatedpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_acpfetchtotalaggregatedpower.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ACPFetchTotalAggregatedPower

int32 __stdcall RFmxNR_ACPFetchTotalAggregatedPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* totalAggregatedPower);

#### Purpose

Returns the sum of powers in all the subblocks.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| totalAggregatedPower | float64* | Returns the total power of all the subblocks. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. The carrier power is reported in dBm when you set the ACP Pwr Units attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_analyzeiq1waveformsplit.html language=enus -->
## TOPIC 00007: RFmxNR_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_analyzeiq1waveformsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_analyzeiq1waveformsplit.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_AnalyzeIQ1WaveformSplit

int32 __stdcall RFmxNR_AnalyzeIQ1WaveformSplit (niRFmxInstrHandle instrumentHandle,
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

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node.
 Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?topicname=rfmxinstrcvi/rfmxinstr_attr_recommended_acquisition_type.html) attribute value is either **IQ** or **IQorSpectral**. 
When using the Analysis-Only mode in RFmxNR, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| x0 | float64 | Specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | float64 | Specifies the frequency interval between data points in the spectrum. |
| IQ | NIComplexSingle[] | Specifies the array of the real part of complex-valued time domain data. This array corresponds to the in-phase (I) data. |
| IQ | NIComplexSingle[] | Specifies the array of the imaginary part of complex-valued time domain data. This array corresponds to the quadrature-phase (Q) data. |
| arraySize | int32 | Specifies the size of the array. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_buildcoresetstring.html language=enus -->
## TOPIC 00008: RFmxNR_BuildCORESETString

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_buildcoresetstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_buildcoresetstring.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_BuildCORESETString

int32 __stdcall RFmxNR_BuildCORESETString (char selectorString[],
 int32 CORESETNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the coreset string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and bandwidth part number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0""signal::sig1/subblock0/carrier0/bwp0""result::r1/subblock0/carrier0/bwp0""signal::sig1/result::r1/subblock0/carrier0/bwp0"You can use the RFmxNR_BuildBandwidthPartString function to build the selector string. |
| CORESETNumber | int32 | Specifies the CORESET number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_buildpdschclusterstring.html language=enus -->
## TOPIC 00009: RFmxNR_BuildPDSCHClusterString

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_buildpdschclusterstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_buildpdschclusterstring.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_BuildPDSCHClusterString

int32 __stdcall RFmxNR_BuildPDSCHClusterString (char selectorString[],
 int32 PDSCHClusterNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a PDSCH Cluster string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, bandwidth part number, user number, and pdsch number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0/user0/pdsch0""signal::sig1/subblock0/carrier0/bwp0/user0/pdsch0""signal::sig1/result::r1/subblock0/carrier0/bwp/user0/pdsch0""result::r1/subblock0/carrier0/bwp0/user0/pdsch0"You can use the RFmxNR_BuildPDSCHString function to build the selector string. |
| PDSCHClusterNumber | int32 | Specifies the PDSCH cluster number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_buildpdschstring.html language=enus -->
## TOPIC 00010: RFmxNR_BuildPDSCHString

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_buildpdschstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_buildpdschstring.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_BuildPDSCHString

int32 __stdcall RFmxNR_BuildPDSCHString (char selectorString[],
 int32 PDSCHNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the PDSCH string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, bandwidth part number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0/user0""signal::sig1/subblock0/carrier0/bwp0/user0""signal::sig1/result::r1/subblock0/carrier0/bwp/user0""result::r1/subblock0/carrier0/bwp0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| PDSCHNumber | int32 | Specifies the PDSCH number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_buildpuschclusterstring.html language=enus -->
## TOPIC 00011: RFmxNR_BuildPUSCHClusterString

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_buildpuschclusterstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_buildpuschclusterstring.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_BuildPUSCHClusterString

int32 __stdcall RFmxNR_BuildPUSCHClusterString (char selectorString[],
 int32 PUSCHClusterNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a PUSCH Cluster string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, bandwidth part number, user number, and pusch number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0/user0/pusch0""signal::sig1/subblock0/carrier0/bwp0/user0/pusch0""signal::sig1/result::r1/subblock0/carrier0/bwp/user0/pusch0""result::r1/subblock0/carrier0/bwp0/user0/pusch0"You can use the RFmxNR_BuildPUSCHString function to build the selector string. |
| PUSCHClusterNumber | int32 | Specifies the PUSCH cluster number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_buildpuschstring.html language=enus -->
## TOPIC 00012: RFmxNR_BuildPUSCHString

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_buildpuschstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_buildpuschstring.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_BuildPUSCHString

int32 __stdcall RFmxNR_BuildPUSCHString (char selectorString[],
 int32 PUSCHNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the PUSCH string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, bandwidth part number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0/user0""signal::sig1/subblock0/carrier0/bwp0/user0""signal::sig1/result::r1/subblock0/carrier0/bwp/user0""result::r1/subblock0/carrier0/bwp0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| PUSCHNumber | int32 | Specifies the PUSCH number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_buildsignalstring.html language=enus -->
## TOPIC 00013: RFmxNR_BuildSignalString

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_buildsignalstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_buildsignalstring.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_BuildSignalString

int32 __stdcall RFmxNR_BuildSignalString (char signalName[],
 char resultName[],
 int32 selectorStringLength,
 char selectorString[]);

#### Purpose

Creates selector string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| signalName | char[] | Specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. Example:"signal::sig1""sig1" |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| selectorStringLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | char[] | Returns the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_cfgfrequency.html language=enus -->
## TOPIC 00014: RFmxNR_CfgFrequency

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_cfgfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_cfgfrequency.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CfgFrequency

int32 __stdcall RFmxNR_CfgFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 centerFrequency);

#### Purpose

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example:"""signal::sig1""signal::sig1/subblock0"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| centerFrequency | float64 | Specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this attribute is hardware dependent. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_cfgrf.html language=enus -->
## TOPIC 00015: RFmxNR_CfgRF

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_cfgrf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_cfgrf.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CfgRF

int32 __stdcall RFmxNR_CfgRF (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 centerFrequency,
 float64 referenceLevel,
 float64 externalAttenuation);

#### Purpose

Configures the RF attributes of the signal specified by the selector string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| centerFrequency | float64 | Specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this attribute is hardware dependent. |
| referenceLevel | float64 | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |
| externalAttenuation | float64 | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_chpcfgaveraging.html language=enus -->
## TOPIC 00016: RFmxNR_CHPCfgAveraging

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_chpcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_chpcfgaveraging.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CHPCfgAveraging

int32 __stdcall RFmxNR_CHPCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount,
 int32 averagingType);

#### Purpose

Configures averaging for the CHP measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXNR_VAL_CHP_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXNR_VAL_CHP_AVERAGING_ENABLED_TRUE (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the averagingCount parameter. |
| RFMXNR_VAL_CHP_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXNR_VAL_CHP_AVERAGING_ENABLED_TRUE (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the averagingCount parameter. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXNR_VAL_CHP_AVERAGING_ENABLED_TRUE. |
| averagingType | int32 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. RFMXNR_VAL_CHP_AVERAGING_TYPE_RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. RFMXNR_VAL_CHP_AVERAGING_TYPE_LOG (1) The power spectrum is averaged in a logarithmic scale.RFMXNR_VAL_CHP_AVERAGING_TYPE_SCALAR (2) The square root of the power spectrum is averaged.RFMXNR_VAL_CHP_AVERAGING_TYPE_MAXIMUM (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXNR_VAL_CHP_AVERAGING_TYPE_MINIMUM (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXNR_VAL_CHP_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. |  |
| RFMXNR_VAL_CHP_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXNR_VAL_CHP_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |  |
| RFMXNR_VAL_CHP_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXNR_VAL_CHP_AVERAGING_TYPE_MINIMUM (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_chpfetchcomponentcarriermeasurement.html language=enus -->
## TOPIC 00017: RFmxNR_CHPFetchComponentCarrierMeasurement

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_chpfetchcomponentcarriermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_chpfetchcomponentcarriermeasurement.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CHPFetchComponentCarrierMeasurement

int32 __stdcall RFmxNR_CHPFetchComponentCarrierMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* absolutePower,
 float64* relativePower);

#### Purpose

Returns the absolute and relative powers measured in the component carriers. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| absolutePower | float64* | Returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |
| relativePower | float64* | Returns the component carrier power relative to its subblock power. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_chpfetchspectrum.html language=enus -->
## TOPIC 00018: RFmxNR_CHPFetchSpectrum

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_chpfetchspectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_chpfetchspectrum.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CHPFetchSpectrum

int32 __stdcall RFmxNR_CHPFetchSpectrum (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 spectrum[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the spectrum used for CHP measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_chpfetchsubblockpower.html language=enus -->
## TOPIC 00019: RFmxNR_CHPFetchSubblockPower

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_chpfetchsubblockpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_chpfetchsubblockpower.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CHPFetchSubblockPower

int32 __stdcall RFmxNR_CHPFetchSubblockPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* subblockPower);

#### Purpose

Returns the power of subblock. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| subblockPower | float64* | Returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. This includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_chpfetchtotalaggregatedpower.html language=enus -->
## TOPIC 00020: RFmxNR_CHPFetchTotalAggregatedPower

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_chpfetchtotalaggregatedpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_chpfetchtotalaggregatedpower.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CHPFetchTotalAggregatedPower

int32 __stdcall RFmxNR_CHPFetchTotalAggregatedPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* totalAggregatedPower);

#### Purpose

Returns the sum of powers in all the subblocks.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| totalAggregatedPower | float64* | Returns the total power of all the subblocks. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_chpvalidatenoisecalibrationdata.html language=enus -->
## TOPIC 00021: RFmxNR_CHPValidateNoiseCalibrationData

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_chpvalidatenoisecalibrationdata.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_chpvalidatenoisecalibrationdata.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CHPValidateNoiseCalibrationData

int32 __stdcall RFmxNR_CHPValidateNoiseCalibrationData (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32* noiseCalibrationDataValid);

#### Purpose

Indicates whether the CHP noise calibration data is valid for the configuration specified by the signal name in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| noiseCalibrationDataValid | int32* | Returns whether the calibration data is valid. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_clearallnamedresults.html language=enus -->
## TOPIC 00022: RFmxNR_ClearAllNamedResults

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_clearallnamedresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_clearallnamedresults.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ClearAllNamedResults

int32 __stdcall RFmxNR_ClearAllNamedResults (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears all results for the signal that you specify in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_clearnamedresult.html language=enus -->
## TOPIC 00023: RFmxNR_ClearNamedResult

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_clearnamedresult.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_clearnamedresult.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ClearNamedResult

int32 __stdcall RFmxNR_ClearNamedResult (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears a result instance specified by the result name in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_clearnoisecalibrationdatabase.html language=enus -->
## TOPIC 00024: RFmxNR_ClearNoiseCalibrationDatabase

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_clearnoisecalibrationdatabase.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_clearnoisecalibrationdatabase.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ClearNoiseCalibrationDatabase

int32 __stdcall RFmxNR_ClearNoiseCalibrationDatabase (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears the noise calibration database used for noise compensation.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_clonesignalconfiguration.html language=enus -->
## TOPIC 00025: RFmxNR_CloneSignalConfiguration

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_clonesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_clonesignalconfiguration.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CloneSignalConfiguration

int32 __stdcall RFmxNR_CloneSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char oldSignalName[],
 char newSignalName[]);

#### Purpose

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| oldSignalName | char[] | Specifies the name of the existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::OldSigName""OldSigName" |
| newSignalName | char[] | Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_close.html language=enus -->
## TOPIC 00026: RFmxNR_Close

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_close.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_close.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_Close

int32 __stdcall RFmxNR_Close (niRFmxInstrHandle instrumentHandle, int32 forceDestroy);

#### Purpose

Closes the RFmx session.

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Close](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_close.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| forceDestroy | int32 | Specifies whether to destroy the RFmx session. RFMXNR_VAL_FALSE (0) Destroys the RFmx session. Call the RFmxNR_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. RFMXNR_VAL_TRUE (1) Destroys the RFmx session. You do not have to call the RFmxNR_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |
| RFMXNR_VAL_FALSE (0) | Destroys the RFmx session. Call the RFmxNR_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. |  |
| RFMXNR_VAL_TRUE (1) | Destroys the RFmx session. You do not have to call the RFmxNR_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_createlist.html language=enus -->
## TOPIC 00027: RFmxNR_CreateList

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_createlist.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_createlist.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CreateList

int32 __stdcall RFmxNR_CreateList (niRFmxInstrHandle instrumentHandle,
 char listName[]);

#### Purpose

Creates a new list instance. Call the [RFmxNR_CreateListStep](/csh?topicname=rfmxnrcvi/cvirfmxnr_createliststep.html) function to add steps to the list. Alternatively, you can also specify the number of list steps using the [RFMXNR_ATTR_NUMBER_OF_STEPS](/csh?topicname=rfmxnrcvi/rfmxnr_attr_number_of_steps.html) attribute. 
**supported devices :**PXIe-5840/5841/5842

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| listName | char[] | Specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix.Example:"list::samplelist1""samplelist1"You can use the RFmxNR_BuildListString function to build the list name. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_createliststep.html language=enus -->
## TOPIC 00028: RFmxNR_CreateListStep

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_createliststep.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_createliststep.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CreateListStep

int32 __stdcall RFmxNR_CreateListStep (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32* createdStepIndex);

#### Purpose

Creates a new list step instance in a list. 
**supporteddevices:**PXIe-5830/5831/5832/5840/5841/5842

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix.Example:"list::samplelist1""samplelist1"You can use the RFmxNR_BuildListString function to build the selector string or use the selectorString parameter from the RFmxNR_CreateList function. |
| Output |  |  |
| Name | Type | Description |
| createdStepIndex | int32* | Returns the created list step index. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_createsignalconfiguration.html language=enus -->
## TOPIC 00029: RFmxNR_CreateSignalConfiguration

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_createsignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_createsignalconfiguration.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_CreateSignalConfiguration

int32 __stdcall RFmxNR_CreateSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char signalName[]);

#### Purpose

Creates a new instance of a signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| signalName | char[] | Specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_getattributef32.html language=enus -->
## TOPIC 00030: RFmxNR_GetAttributeF32

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_getattributef32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_getattributef32.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_GetAttributeF32

int32 __stdcall RFmxNR_GetAttributeF32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_getattributef32array.html language=enus -->
## TOPIC 00031: RFmxNR_GetAttributeF32Array

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_getattributef32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_getattributef32array.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_GetAttributeF32Array

int32 __stdcall RFmxNR_GetAttributeF32Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

 If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float32[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_getattributei32.html language=enus -->
## TOPIC 00032: RFmxNR_GetAttributeI32

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_getattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_getattributei32.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_GetAttributeI32

int32 __stdcall RFmxNR_GetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_getattributenicomplexdoublearray.html language=enus -->
## TOPIC 00033: RFmxNR_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_getattributenicomplexdoublearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_getattributenicomplexdoublearray.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_GetAttributeNIComplexDoubleArray

int32 __stdcall RFmxNR_GetAttributeNIComplexDoubleArray (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_getattributeu32.html language=enus -->
## TOPIC 00034: RFmxNR_GetAttributeU32

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_getattributeu32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_getattributeu32.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_GetAttributeU32

int32 __stdcall RFmxNR_GetAttributeU32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_getattributeu32array.html language=enus -->
## TOPIC 00035: RFmxNR_GetAttributeU32Array

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_getattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_getattributeu32array.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_GetAttributeU32Array

int32 __stdcall RFmxNR_GetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_getattributeu64array.html language=enus -->
## TOPIC 00036: RFmxNR_GetAttributeU64Array

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_getattributeu64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_getattributeu64array.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_GetAttributeU64Array

int32 __stdcall RFmxNR_GetAttributeU64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_getattributeu8.html language=enus -->
## TOPIC 00037: RFmxNR_GetAttributeU8

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_getattributeu8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_getattributeu8.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_GetAttributeU8

int32 __stdcall RFmxNR_GetAttributeU8 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_getattributeu8array.html language=enus -->
## TOPIC 00038: RFmxNR_GetAttributeU8Array

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_getattributeu8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_getattributeu8array.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_GetAttributeU8Array

int32 __stdcall RFmxNR_GetAttributeU8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_geterrorstring.html language=enus -->
## TOPIC 00039: RFmxNR_GetErrorString

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_geterrorstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_geterrorstring.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_GetErrorString

int32 __stdcall RFmxNR_GetErrorString (niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[]);

#### Purpose

Converts a status code returned by an RFmxNR function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter. 
 

 If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For **Example**, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. 
 

 If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| errorCode | int32* | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescriptionBufferSize | int32 | Passes the number of bytes in the char array you specify in the errorDescription parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize – 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string. The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_initialize.html language=enus -->
## TOPIC 00040: rfmxnr_Initialize

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_initialize.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_Initialize

int32 __stdcall RFmxNR_Initialize (char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession);

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
| optionString | char[] | Sets the initial value of certain attributes for the session. The following attributes are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about attributes used in this parameter, refer to the NI RF Vector Signal Analyzers Help. The format of this string is "AttributeName=Value", where AttributeName is the name of the attribute and Value is the value to which the attribute is set. For example, you can simulate an NI 5663E using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple attributes, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx uses yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. Note To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the NI 5665. |
|  | Note To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the NI 5665. |  |
| isNewSession | int32* | Returns RFMXNR_VAL_TRUE if the function created a new session, or RFMXNR_VAL_FALSE if the function returned a reference to an existing session. |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Identifies your instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_initializefromnirfsasession.html language=enus -->
## TOPIC 00041: RFmxNR_InitializeFromNIRFSASession

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_initializefromnirfsasession.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_initializefromnirfsasession.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_InitializeFromNIRFSASession

int32 __stdcall RFmxNR_InitializeFromNIRFSASession (uInt32 NIRFSASession, niRFmxInstrHandle *handleOut);

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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_initiate.html language=enus -->
## TOPIC 00042: RFmxNR_Initiate

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_initiate.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_Initiate

int32 __stdcall RFmxNR_Initiate (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[]);

#### Purpose

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the [RFmxNR_WaitforMeasurementComplete](/csh?topicname=rfmxnrcvi/cvirfmxnr_waitformeasurementcomplete.html) function or [RFmxNR_CheckMeasurementStatus](/csh?topicname=rfmxnrcvi/cvirfmxnr_checkmeasurementstatus.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccautolevel.html language=enus -->
## TOPIC 00043: RFmxNR_ModAccAutoLevel

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccautolevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccautolevel.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccAutoLevel

int32 __stdcall RFmxNR_ModAccAutoLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout);

#### Purpose

Performs the user-configured ModAcc measurement at multiple reference levels relative to the user-configured [RFMXNR_ATTR_REFERENCE_LEVEL](/csh?topicname=rfmxnrcvi/rfmxnr_attr_reference_level.html) attribute and configures the reference level corresponding to the lowest [RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_RMS_EVM_MEAN](/csh?topicname=rfmxnrcvi/rfmxnr_attr_modacc_results_composite_rms_evm_mean.html) result.
 
This function only measures at the reference levels that do not result in an ADC or OSP overflow when you set the [RFMXNR_ATTR_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW](/csh?topicname=rfmxnrcvi/rfmxnr_attr_modacc_auto_level_allow_overflow.html) attribute to RFMXNR_VAL_MODACC_ATUO_LEVEL_ALLOW_OVERFLOW_FALSE. If you set the RFMXNR_ATTR_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW attribute to RFMXNR_VAL_MODACC_ATUO_LEVEL_ALLOW_OVERFLOW_TRUE, this function measures at a few reference levels beyond the overflow. After calling the ModAcc Auto Level function, you need to call the ModAcc measurement.
 
This function expects: 
Auto level needs to be performed again if the input signal or RFmx configuration changes. 
For repeatable results, you must make sure that the ModAcc measurement is repeatable. 
This function measures EVM at reference levels starting at an integer at least 1 dB above the value you configure for the RFMXNR_ATTR_REFERENCE_LEVEL attribute, extending upto 12 dB lower when you set the RFMXNR_ATTR_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW attribute to RFMXNR_VAL_MODACC_ATUO_LEVEL_ALLOW_OVERFLOW_FALSE, and up to 17 dB lower when you set the RFMXNR_ATTR_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW attribute to RFMXNR_VAL_MODACC_ATUO_LEVEL_ALLOW_OVERFLOW_TRUE with a step size of 0.5 dB. 
When you use this function with the [RFMXNR_ATTR_MODACC_NOISE_COMPENSATION_ENABLED](/csh?topicname=rfmxnrcvi/rfmxnr_attr_modacc_noise_compensation_enabled.html) attribute set to RFMXNR_VAL_MODACC_NOISE_COMPENSATION_ENABLED_TRUE, you need to make sure that valid noise calibration data is available for the above measurements.

- A valid ModAcc measurement configuration
- RFMXNR_ATTR_REFERENCE_LEVEL attribute set to peak power of the signal
- Repetitive signals at the analyzer's input along with trigger settings that measure the same portion of the waveform every time the measurement is performed
- No other measurements are running in parallel

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchinbandemissiontrace.html language=enus -->
## TOPIC 00044: RFmxNR_ModAccFetchInBandEmissionTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchinbandemissiontrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchinbandemissiontrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchInBandEmissionTrace

int32 __stdcall RFmxNR_ModAccFetchInBandEmissionTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 inBandEmission[],
 float32 inBandEmissionMask[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the in-band emission trace and limits trace for the component carrier. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4.2.3 of *3GPP 38.101-1*, and section 6.4.2.3 of *3GPP 38.101-2*. The trace is not returned when there is full allocation of bandwidth, or there is clustered PUSCH or there is more than one active component carrier. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start point of the of the resource block. |
| dx | float64* | Returns the subcarrier spacing. |
| inBandEmission | float32[] | Returns an array of the in-band emission value as an array for each of the resource blocks. In-band emission is the interference falling into non-allocated resource blocks. This value is expressed in dB. |
| inBandEmissionMask | float32[] | Returns an array of the in-band emission limit value as an array for each of the resource blocks. The in-band emission limit for regions such as general, carrier leakage and IQ image, are evaluated according to the method defined in the 3GPP specification and concatenated to form a composite limit trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchiqquadratureerrorpersubcarriermeantrace.html language=enus -->
## TOPIC 00045: RFmxNR_ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchiqquadratureerrorpersubcarriermeantrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchiqquadratureerrorpersubcarriermeantrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace

int32 __stdcall RFmxNR_ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 IQQuadratureErrorPerSubcarrierMean[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the mean value of IQ Quadrature Error. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start point of the resource grid. |
| dx | float64* | Returns the sampling duration of the analyzed signal. |
| IQQuadratureErrorPerSubcarrierMean | float32[] | Returns the mean value of IQ Quadrature Error. This value is expressed in degrees. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpdsch16qamconstellationtracesplit.html language=enus -->
## TOPIC 00046: RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpdsch16qamconstellationtracesplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpdsch16qamconstellationtracesplit.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit

int32 __stdcall RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the in-phase and quadrature-phase part of PDSCH 16 QAM trace. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| I | float32[] | Returns the in-phase part of 16 QAM constellation trace. |
| Q | float32[] | Returns the quadrature-phase part of 16 QAM constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpdsch256qamconstellationtrace.html language=enus -->
## TOPIC 00047: RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpdsch256qamconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpdsch256qamconstellationtrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace

int32 __stdcall RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle QAM256Constellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches PDSCH 256 QAM trace. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| QAM256Constellation | NIComplexSingle[] | Returns the 256 QAM constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpdschdemodulatedbits.html language=enus -->
## TOPIC 00048: RFmxNR_ModAccFetchPDSCHDemodulatedBits

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpdschdemodulatedbits.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpdschdemodulatedbits.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPDSCHDemodulatedBits

int32 __stdcall RFmxNR_ModAccFetchPDSCHDemodulatedBits (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int8 bits[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the recovered bits during EVM calculation. The bits of different slots in the measurement length are concatenated. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| bits | int8[] | Returns an array of the recovered bits during EVM calculation. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpdschdmrsconstellationtrace.html language=enus -->
## TOPIC 00049: RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpdschdmrsconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpdschdmrsconstellationtrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace

int32 __stdcall RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle PDSCHDMRSConstellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches PDSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. 
Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/user0""signal::sig1/subblock0/carrier0/user0""result::r1/subblock0/carrier0/user0""signal::sig1/result::r1/subblock0/carrier0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| PDSCHDMRSConstellation | NIComplexSingle[] | Returns the PDSCH DMRS constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpdschdmrsconstellationtracesplit.html language=enus -->
## TOPIC 00050: RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpdschdmrsconstellationtracesplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpdschdmrsconstellationtracesplit.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit

int32 __stdcall RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the in-phase and quadrature-phase part of PDSCH DMRS trace. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| I | float32[] | Returns the in-phase part of PDSCH DMRS constellation trace. |
| Q | float32[] | Returns the quadrature-phase part of PDSCH DMRS constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpdschptrsconstellationtrace.html language=enus -->
## TOPIC 00051: RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpdschptrsconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpdschptrsconstellationtrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace

int32 __stdcall RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle PDSCHPTRSConstellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches PDSCH PTRS trace. 
Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/user0""signal::sig1/subblock0/carrier0/user0""result::r1/subblock0/carrier0/user0""signal::sig1/result::r1/subblock0/carrier0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| PDSCHPTRSConstellation | NIComplexSingle[] | Returns the PDSCH PTRS constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpdschptrsconstellationtracesplit.html language=enus -->
## TOPIC 00052: RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpdschptrsconstellationtracesplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpdschptrsconstellationtracesplit.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit

int32 __stdcall RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the in-phase and quadrature-phase part of PDSCH PTRS trace. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| I | float32[] | Returns the in-phase part of PDSCH PTRS constellation trace. |
| Q | float32[] | Returns the quadrature-phase part of PDSCH PTRS constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpeakevmlowpersymbolmaximumtrace.html language=enus -->
## TOPIC 00053: RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpeakevmlowpersymbolmaximumtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpeakevmlowpersymbolmaximumtrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace

int32 __stdcall RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 peakEVMLowPerSymbolMaximum[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the peak EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C-W/2. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start point of the of the resource block. |
| dx | float64* | Returns the subcarrier spacing. |
| peakEVMLowPerSymbolMaximum | float32[] | Returns an array of the peak EVM per symbol for all confgured slots. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpeakevmperslotmaximumtrace.html language=enus -->
## TOPIC 00054: RFmxNR_ModAccFetchPeakEVMPerSlotMaximumTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpeakevmperslotmaximumtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpeakevmperslotmaximumtrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPeakEVMPerSlotMaximumTrace

int32 __stdcall RFmxNR_ModAccFetchPeakEVMPerSlotMaximumTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 peakEVMPerSlotMaximum[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the peak value of EVM for each slot computed across all the symbols and all the allocated subcarriers. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start point of the of the resource block. |
| dx | float64* | Returns the subcarrier spacing. |
| peakEVMPerSlotMaximum | float32[] | Returns an array the peak value of EVM for each slot computed across all the symbols and all the allocated subcarriers. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpeakevmpersubcarriermaximumtrace.html language=enus -->
## TOPIC 00055: RFmxNR_ModAccFetchPeakEVMPerSubcarrierMaximumTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpeakevmpersubcarriermaximumtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpeakevmpersubcarriermaximumtrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPeakEVMPerSubcarrierMaximumTrace

int32 __stdcall RFmxNR_ModAccFetchPeakEVMPerSubcarrierMaximumTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 peakEVMPerSubcarrierMaximum[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the peak value of EVM for each allocated subcarrier computed across all the symbols within the measurement length. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start point of the of the resource block. |
| dx | float64* | Returns the subcarrier spacing. |
| peakEVMPerSubcarrierMaximum | float32[] | Returns an array the peak value of EVM for each allocated subcarrier computed across all the symbols within the measurement length. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpeakevmpersymbolmaximumtrace.html language=enus -->
## TOPIC 00056: RFmxNR_ModAccFetchPeakEVMPerSymbolMaximumTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpeakevmpersymbolmaximumtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpeakevmpersymbolmaximumtrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPeakEVMPerSymbolMaximumTrace

int32 __stdcall RFmxNR_ModAccFetchPeakEVMPerSymbolMaximumTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 peakEVMPerSymbolMaximum[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the peak value of EVM for each symbol computed across all the allocated subcarriers. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start point of the of the resource block. |
| dx | float64* | Returns the subcarrier spacing. |
| peakEVMPerSymbolMaximum | float32[] | Returns an array the the peak value of EVM for each symbol computed across all the allocated subcarriers. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpuschdataconstellationtrace.html language=enus -->
## TOPIC 00057: RFmxNR_ModAccFetchPUSCHDataConstellationTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpuschdataconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpuschdataconstellationtrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPUSCHDataConstellationTrace

int32 __stdcall RFmxNR_ModAccFetchPUSCHDataConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle PUSCHDataConstellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches PUSCH Data Constellation trace. The constellation points of different slots in the measurement length is concatenated. 
Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/user0""signal::sig1/subblock0/carrier0/user0""result::r1/subblock0/carrier0/user0""signal::sig1/result::r1/subblock0/carrier0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| PUSCHDataConstellation | NIComplexSingle[] | Returns the PUSCH data constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpuschdataconstellationtracesplit.html language=enus -->
## TOPIC 00058: RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpuschdataconstellationtracesplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpuschdataconstellationtracesplit.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit

int32 __stdcall RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches in-phase and quadrature-phase part of PUSCH Data Constellation trace. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| I | float32[] | Returns the in-phase part of PUSCH data constellation trace. |
| Q | float32[] | Returns the quadrature-phase part of PUSCH data constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccfetchpuschptrsconstellationtrace.html language=enus -->
## TOPIC 00059: RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccfetchpuschptrsconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccfetchpuschptrsconstellationtrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace

int32 __stdcall RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle PUSCHPTRSConstellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches PUSCH PTRS trace. The constellation points of different slots in the measurement length is concatenated. 
Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/user0""signal::sig1/subblock0/carrier0/user0""result::r1/subblock0/carrier0/user0""signal::sig1/result::r1/subblock0/carrier0/user0"You can use the RFmxNR_BuildUserString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| PUSCHPTRSConstellation | NIComplexSingle[] | Returns the PUSCH PTRS constellation trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_modaccvalidatecalibrationdata.html language=enus -->
## TOPIC 00060: RFmxNR_ModAccValidateCalibrationData

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_modaccvalidatecalibrationdata.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_modaccvalidatecalibrationdata.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ModAccValidateCalibrationData

int32 __stdcall RFmxNR_ModAccValidateCalibrationData (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32* calibrationDataValid);

#### Purpose

Specifies whether calibration data is valid for the configuration specified by the signal name in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| calibrationDataValid | int32* | Returns whether the calibration data is valid. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_obwcfgsweeptime.html language=enus -->
## TOPIC 00061: RFmxNR_OBWCfgSweepTime

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_obwcfgsweeptime.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_obwcfgsweeptime.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_OBWCfgSweepTime

int32 __stdcall RFmxNR_OBWCfgSweepTime (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 sweepTimeAuto,
 float64 sweepTimeInterval);

#### Purpose

Configures the sweep time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| sweepTimeAuto | int32 | Specifies whether the measurement sets the sweep time. RFMXNR_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) The measurement uses the sweep time that you specify in the sweepTimeInterval parameter.RFMXNR_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the RFMXNR_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute, and for UL, it uses a sweep time of 1 ms. |
| RFMXNR_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the sweepTimeInterval parameter. |  |
| RFMXNR_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) | The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the RFMXNR_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute, and for UL, it uses a sweep time of 1 ms. |  |
| sweepTimeInterval | float64 | Specifies the sweep time when you set the sweepTimeAuto parameter to RFMXNR_VAL_OBW_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_obwfetchspectrum.html language=enus -->
## TOPIC 00062: RFmxNR_OBWFetchSpectrum

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_obwfetchspectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_obwfetchspectrum.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_OBWFetchSpectrum

int32 __stdcall RFmxNR_OBWFetchSpectrum (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_pvtcfgoffpowerexclusionperiods.html language=enus -->
## TOPIC 00063: RFmxNR_PVTCfgOFFPowerExclusionPeriods

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_pvtcfgoffpowerexclusionperiods.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_pvtcfgoffpowerexclusionperiods.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_PVTCfgOFFPowerExclusionPeriods

int32 __stdcall RFmxNR_PVTCfgOFFPowerExclusionPeriods (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 OFFPowerExclusionBefore,
 float64 OFFPowerExclusionAfter);

#### Purpose

Configures the time excluded from the off region before and after the burst.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| OFFPowerExclusionBefore | float64 | Specifies the time excluded from the Off region before the burst. This value is expressed in seconds. |
| OFFPowerExclusionAfter | float64 | Specifies the time excluded from the Off region after the burst. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_pvtfetchmeasurementarray.html language=enus -->
## TOPIC 00064: RFmxNR_PVTFetchMeasurementArray

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_pvtfetchmeasurementarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_pvtfetchmeasurementarray.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_PVTFetchMeasurementArray

int32 __stdcall RFmxNR_PVTFetchMeasurementArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 measurementStatus[],
 float64 absoluteOFFPowerBefore[],
 float64 absoluteOFFPowerAfter[],
 float64 absoluteONPower[],
 float64 burstWidth[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches an array of PVT ON and OFF powers along with measurement status and burst width. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| measurementStatus | int32[] | Returns the measurement status indicating whether the off power before and after is within the standard defined limit. RFMXNR_VAL_PVT_MEASUREMENT_STATUS_FAIL (0) Indicates that the measurement has failed.RFMXNR_VAL_PVT_MEASUREMENT_STATUS_PASS (1) Indicates that the measurement has passed. |
| RFMXNR_VAL_PVT_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |  |
| RFMXNR_VAL_PVT_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |  |
| absoluteOFFPowerBefore | float64[] | Returns the OFF power in the segment before the captured burst. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. |
| absoluteOFFPowerAfter | float64[] | Returns the OFF power in the segment after the captured burst. The segment is defined as one slot after the burst and a short transient segment. This value is expressed in dBm. |
| absoluteONPower | float64[] | Returns the power of the subframes within the captured burst. This value is expressed in dBm. |
| burstWidth | float64[] | Returns the width of the captured burst. This value is expressed in seconds. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_pvtfetchwindowedsignalpowertrace.html language=enus -->
## TOPIC 00065: RFmxNR_PVTFetchWindowedSignalPowerTrace

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_pvtfetchwindowedsignalpowertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_pvtfetchwindowedsignalpowertrace.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_PVTFetchWindowedSignalPowerTrace

int32 __stdcall RFmxNR_PVTFetchWindowedSignalPowerTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 windowedSignalPower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns start time of the signal. This value is expressed in seconds. |
| dx | float64* | Returns the time bin spacing. This value is expressed in seconds. |
| windowedSignalPower | float32[] | Returns the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_resetattribute.html language=enus -->
## TOPIC 00066: RFmxNR_ResetAttribute

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_resetattribute.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_resetattribute.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_ResetAttribute

int32 __stdcall RFmxNR_ResetAttribute (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID);

#### Purpose

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being reset. Refer to the selector string topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_selectmeasurements.html language=enus -->
## TOPIC 00067: RFmxNR_SelectMeasurements

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_selectmeasurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_selectmeasurements.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SelectMeasurements

int32 __stdcall RFmxNR_SelectMeasurements (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 uInt32 measurements,
 int32 enableAllTraces);

#### Purpose

Enables all the measurements that you specify in the **measurement** parameter and disables all other measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| measurements | uInt32 | Specifies the measurements to perform. You can specify one or more of the following measurements. |
| enableAllTraces | int32 | Specifies whether to enable all traces for the selected measurement. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semcfgcomponentcarrierratedoutputpower.html language=enus -->
## TOPIC 00068: RFmxNR_SEMCfgComponentCarrierRatedOutputPower

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semcfgcomponentcarrierratedoutputpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semcfgcomponentcarrierratedoutputpower.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMCfgComponentCarrierRatedOutputPower

int32 __stdcall RFmxNR_SEMCfgComponentCarrierRatedOutputPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 componentCarrierRatedOutputPower);

#### Purpose

Configures the rated output power (Prated, x) of the component carrier. 
Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| componentCarrierRatedOutputPower | float64 | Specifies the rated output power (Prated, x), which is used only to choose the limit table for medium range base station, RFMXNR_VAL_GNODEB_CATEGORY_FR2_CATEGORY_A and RFMXNR_VAL_GNODEB_CATEGORY_FR2_CATEGORY_B. This value is expressed in dBm. This parameter will be considered when you set the RFMXNR_ATTR_LINK_DIRECTION attribute to RFMXNR_VAL_LINK_DIRECTION_DOWNLINK, RFMXNR_ATTR_SEM_DOWNLINK_MASK_TYPE attribute to RFMXNR_VAL_SEM_DOWNLINK_MASK_TYPE_STANDARD, and RFMXNR_ATTR_GNODEB_CATEGORY attribute to RFMXNR_VAL_GNODEB_CATEGORY_MEDIUM_RANGE_BASE_STATION or RFMXNR_VAL_GNODEB_CATEGORY_FR2_CATEGORY_A or RFMXNR_VAL_GNODEB_CATEGORY_FR2_CATEGORY_B. For more details please refer to section 6.6.4 and section 9.7.4 of 3GPP 38.104 specification. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semcfgnumberofoffsets.html language=enus -->
## TOPIC 00069: RFmxNR_SEMCfgNumberOfOffsets

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semcfgnumberofoffsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semcfgnumberofoffsets.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMCfgNumberOfOffsets

int32 __stdcall RFmxNR_SEMCfgNumberOfOffsets (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfOffsets);

#### Purpose

Configures the number of offset segments for the SEM measurement. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example:"""signal::sig1""signal::sig1/subblock0"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| numberOfOffsets | int32 | Specifies the number of SEM offset segments. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semcfgoffsetfrequency.html language=enus -->
## TOPIC 00070: RFmxNR_SEMCfgOffsetFrequency

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semcfgoffsetfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semcfgoffsetfrequency.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMCfgOffsetFrequency

int32 __stdcall RFmxNR_SEMCfgOffsetFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 offsetStartFrequency,
 float64 offsetStopFrequency,
 int32 offsetSideband);

#### Purpose

Configures the start and stop frequencies and the sideband of an offset segment. 
Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the selector string to configure or read this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example:"subblock0/offset0""signal::sig1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| offsetStartFrequency | float64 | Specifies the start frequency of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. |
| offsetStopFrequency | float64 | Specifies the stop frequency of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. |
| offsetSideband | int32 | Specifies whether the offset segment is present either on one side or on both sides of a carrier. RFMXNR_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE (0) Configures a lower offset segment to the left of the leftmost carrier.RFMXNR_VAL_SEM_OFFSET_SIDEBAND_POSITIVE (1) Configures an upper offset segment to the right of the rightmost carrier.RFMXNR_VAL_SEM_OFFSET_SIDEBAND_BOTH (2) Configures both the negative and the positive offset segments. |
| RFMXNR_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE (0) | Configures a lower offset segment to the left of the leftmost carrier. |  |
| RFMXNR_VAL_SEM_OFFSET_SIDEBAND_POSITIVE (1) | Configures an upper offset segment to the right of the rightmost carrier. |  |
| RFMXNR_VAL_SEM_OFFSET_SIDEBAND_BOTH (2) | Configures both the negative and the positive offset segments. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semcfguplinkmasktype.html language=enus -->
## TOPIC 00071: RFmxNR_SEMCfgUplinkMaskType

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semcfguplinkmasktype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semcfguplinkmasktype.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMCfgUplinkMaskType

int32 __stdcall RFmxNR_SEMCfgUplinkMaskType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 uplinkMaskType);

#### Purpose

Configures the standard defined mask type that has to be used in the measurement for uplink.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| uplinkMaskType | int32 | Specifies the spectrum emission mask used in the measurement for uplink. You must set the mask type to custom to configure the custom offset masks. Refer to section 6.5.2 of the 3GPP 38.101 specification for more information about standard-defined mask types. RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_GENERAL (0) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.2-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification, Table 6.5.2.1-1 and 6.5A.2.1-1 in section 6.5.2 of the 3GPP TS 38.101-2 specification and Table 6.5B.2.1.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.1.5-1, 6.6.2.1.5-2, 6.6.2.1A.1.5-1, and 6.6.2.1A.1.5-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS35 (1) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.1-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification and Table 6.5B.2.1.2.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.5-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_CUSTOM (2) You need to configure the RFMXNR_ATTR_SEM_NUMBER_OF_OFFSETS, RFMXNR_ATTR_SEM_OFFSET_START_FREQUENCY, RFMXNR_ATTR_SEM_OFFSET_STOP_FREQUENCY, RFMXNR_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START, RFMXNR_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_STOP, RFMXNR_ATTR_SEM_OFFSET_SIDEBAND, RFMXNR_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH, RFMXNR_ATTR_SEM_OFFSET_RBW_FILTER_TYPE, and RFMXNR_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL attributes for each offset. RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS03 (3) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS04 (4) The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.5.2.3.2-3 in section 6.5.2 of the 3GPP TS 38.101-1 specification. Subcarrier spacing can be configured through RFMXNR_ATTR_BANDWIDTH_PART_SUBCARRIER_SPACING attribute. Subcarrier spacing corresponding to first bandwidth part is used for computing mask. Transform precoding can be configured through RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute. Transform precoding corresponding to first bandwidth part is used for computing mask. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.2-3 in section 6.6.2 of the 3GPP TS 36.521-1 specification. RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS06 (5) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS21 (6) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS27 (7) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.8-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of intra-band contiguous CA consisting of at least one subblock with all NR carriers, for the NR subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.2A.2.3.2.1-1 in section 6.5A.2.3 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.4-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS07 (8) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and Table 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_GENERAL (0) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.2-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification, Table 6.5.2.1-1 and 6.5A.2.1-1 in section 6.5.2 of the 3GPP TS 38.101-2 specification and Table 6.5B.2.1.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.1.5-1, 6.6.2.1.5-2, 6.6.2.1A.1.5-1, and 6.6.2.1A.1.5-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |  |
| RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS35 (1) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.1-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification and Table 6.5B.2.1.2.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.5-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |  |
| RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_CUSTOM (2) | You need to configure the RFMXNR_ATTR_SEM_NUMBER_OF_OFFSETS, RFMXNR_ATTR_SEM_OFFSET_START_FREQUENCY, RFMXNR_ATTR_SEM_OFFSET_STOP_FREQUENCY, RFMXNR_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START, RFMXNR_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_STOP, RFMXNR_ATTR_SEM_OFFSET_SIDEBAND, RFMXNR_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH, RFMXNR_ATTR_SEM_OFFSET_RBW_FILTER_TYPE, and RFMXNR_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL attributes for each offset. |  |
| RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS03 (3) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |  |
| RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS04 (4) | The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.5.2.3.2-3 in section 6.5.2 of the 3GPP TS 38.101-1 specification. Subcarrier spacing can be configured through RFMXNR_ATTR_BANDWIDTH_PART_SUBCARRIER_SPACING attribute. Subcarrier spacing corresponding to first bandwidth part is used for computing mask. Transform precoding can be configured through RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute. Transform precoding corresponding to first bandwidth part is used for computing mask. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.2-3 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |  |
| RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS06 (5) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |  |
| RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS21 (6) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |  |
| RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS27 (7) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.8-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of intra-band contiguous CA consisting of at least one subblock with all NR carriers, for the NR subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.2A.2.3.2.1-1 in section 6.5A.2.3 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.4-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |  |
| RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS07 (8) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and Table 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semfetchcomponentcarriermeasurement.html language=enus -->
## TOPIC 00072: RFmxNR_SEMFetchComponentCarrierMeasurement

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semfetchcomponentcarriermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semfetchcomponentcarriermeasurement.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMFetchComponentCarrierMeasurement

int32 __stdcall RFmxNR_SEMFetchComponentCarrierMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* absolutePower,
 float64* peakAbsolutePower,
 float64* peakFrequency,
 float64* relativePower);

#### Purpose

Returns the absolute and relative powers measured in the component carriers. 
Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxNR_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| absolutePower | float64* | Returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |
| peakAbsolutePower | float64* | Returns the peak power in the component carrier. This value is expressed in dBm. |
| peakFrequency | float64* | Returns the frequency at which peak power occurs in the component carrier. This value is expressed in Hz. |
| relativePower | float64* | Returns the component carrier power relative to its subblock power. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semfetchloweroffsetpower.html language=enus -->
## TOPIC 00073: RFmxNR_SEMFetchLowerOffsetPower

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semfetchloweroffsetpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semfetchloweroffsetpower.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMFetchLowerOffsetPower

int32 __stdcall RFmxNR_SEMFetchLowerOffsetPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* totalAbsolutePower,
 float64* totalRelativePower,
 float64* peakAbsolutePower,
 float64* peakFrequency,
 float64* peakRelativePower);

#### Purpose

Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power. 
Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""signal::sig1/subblock0/offset0""signal::sig1/result::r1/subblock0/offset0""result::r1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| totalAbsolutePower | float64* | Returns the lower (negative) offset segment power. This value is expressed in dBm. |
| totalRelativePower | float64* | Returns the power in the lower offset segment relative to total aggregated power. This value is expressed in dB. |
| peakAbsolutePower | float64* | Returns the peak power in the lower offset segment. This value is expressed in dBm. |
| peakFrequency | float64* | Returns the frequency at which the peak power occurs in the lower offset segment. This value is expressed in Hz. |
| peakRelativePower | float64* | Returns the peak power in the lower offset segment relative to total aggregated power. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semfetchloweroffsetpowerarray.html language=enus -->
## TOPIC 00074: RFmxNR_SEMFetchLowerOffsetPowerArray

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semfetchloweroffsetpowerarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semfetchloweroffsetpowerarray.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMFetchLowerOffsetPowerArray

int32 __stdcall RFmxNR_SEMFetchLowerOffsetPowerArray (niRFmxInstrHandle instrumentHandle,
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

Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| totalAbsolutePower | float64[] | Returns an array of the lower (negative) segment power. This value is expressed in dBm. |
| totalRelativePower | float64[] | Returns an array of the power in the lower offset segment relative to total aggregated power. This value is expressed in dB. |
| peakAbsolutePower | float64[] | Returns an array of the peak power in the lower offset segment. This value is expressed in dBm. |
| peakFrequency | float64[] | Returns an array of the frequency at which the peak power occurs in the lower offset segment. This value is expressed in Hz. |
| peakRelativePower | float64[] | Returns an array of the peak power in the lower offset segment relative to total aggregated power. This value is expressed in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semfetchmeasurementstatus.html language=enus -->
## TOPIC 00075: RFmxNR_SEMFetchMeasurementStatus

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semfetchmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semfetchmeasurementstatus.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMFetchMeasurementStatus

int32 __stdcall RFmxNR_SEMFetchMeasurementStatus (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* measurementStatus);

#### Purpose

Returns the overall measurement status based on the standard mask type that you configure.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| measurementStatus | int32* | Returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. RFMXNR_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) Indicates that the measurement has failed.RFMXNR_VAL_SEM_MEASUREMENT_STATUS_PASS (1) Indicates that the measurement has passed. |
| RFMXNR_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |  |
| RFMXNR_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semfetchspectrum.html language=enus -->
## TOPIC 00076: RFmxNR_SEMFetchSpectrum

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semfetchspectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semfetchspectrum.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMFetchSpectrum

int32 __stdcall RFmxNR_SEMFetchSpectrum (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 spectrum[],
 float32 compositeMask[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the spectrum used for SEM measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxNR_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency of the channel. This value is expressed in Hz. |
| dx | float64* | Returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | float32[] | Returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
| compositeMask | float32[] | Returns the array of composite mask used for the channel. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semfetchsubblockmeasurement.html language=enus -->
## TOPIC 00077: RFmxNR_SEMFetchSubblockMeasurement

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semfetchsubblockmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semfetchsubblockmeasurement.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMFetchSubblockMeasurement

int32 __stdcall RFmxNR_SEMFetchSubblockMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* subblockPower,
 float64* integrationBandwidth,
 float64* frequency);

#### Purpose

Fetches the power, integration bandwidth, and center frequency of the subblock.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| subblockPower | float64* | Returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. This includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. |
| integrationBandwidth | float64* | Returns the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within a subblock. This value is expressed in Hz. |
| frequency | float64* | Returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semfetchupperoffsetmargin.html language=enus -->
## TOPIC 00078: RFmxNR_SEMFetchUpperOffsetMargin

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semfetchupperoffsetmargin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semfetchupperoffsetmargin.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMFetchUpperOffsetMargin

int32 __stdcall RFmxNR_SEMFetchUpperOffsetMargin (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* measurementStatus,
 float64* margin,
 float64* marginFrequency,
 float64* marginAbsolutePower,
 float64* marginRelativePower);

#### Purpose

Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power. 
Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""signal::sig1/subblock0/offset0""signal::sig1/result::r1/subblock0/offset0""result::r1/subblock0/offset0"You can use the RFmxNR_BuildOffsetString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| measurementStatus | int32* | Returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. RFMXNR_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) Indicates that the measurement has failed.RFMXNR_VAL_SEM_MEASUREMENT_STATUS_PASS (1) Indicates that the measurement has passed. |
| RFMXNR_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |  |
| RFMXNR_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |  |
| margin | float64* | Returns the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
| marginFrequency | float64* | Returns the frequency at which the margin occurs in the upper offset. This value is expressed in Hz. |
| marginAbsolutePower | float64* | Returns the power at which the margin occurs in the upper offset segment. This value is expressed in dBm. |
| marginRelativePower | float64* | Returns the power at which the margin occurs in the upper offset segment. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_semfetchupperoffsetmarginarray.html language=enus -->
## TOPIC 00079: RFmxNR_SEMFetchUpperOffsetMarginArray

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_semfetchupperoffsetmarginarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_semfetchupperoffsetmarginarray.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SEMFetchUpperOffsetMarginArray

int32 __stdcall RFmxNR_SEMFetchUpperOffsetMarginArray (niRFmxInstrHandle instrumentHandle,
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

Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for upper offset segments. The relative power is relative to the total aggregated power. 
Use "subblock<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxNR_BuildSubblockString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| measurementStatus | int32[] | Returns an array of the measurement status indicating whether the power before and after the burst is within the standard defined limit. RFMXNR_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) Indicates that the measurement has failed.RFMXNR_VAL_SEM_MEASUREMENT_STATUS_PASS (1) Indicates that the measurement has passed. |
| RFMXNR_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |  |
| RFMXNR_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |  |
| margin | float64[] | Returns an array of the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
| marginFrequency | float64[] | Returns an array of the frequency at which the margin occurs in the upper offset. This value is expressed in Hz. |
| marginAbsolutePower | float64[] | Returns an array of the power at which the margin occurs in the upper offset segment. This value is expressed in dBm. |
| marginRelativePower | float64[] | Returns an array of the power at which the margin occurs in the upper (positive) offset segment. This value is expressed in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_setattributef32.html language=enus -->
## TOPIC 00080: RFmxNR_SetAttributeF32

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_setattributef32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_setattributef32.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SetAttributeF32

int32 __stdcall RFmxNR_SetAttributeF32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_setattributef32array.html language=enus -->
## TOPIC 00081: RFmxNR_SetAttributeF32Array

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_setattributef32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_setattributef32array.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SetAttributeF32Array

int32 __stdcall RFmxNR_SetAttributeF32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_setattributef64.html language=enus -->
## TOPIC 00082: RFmxNR_SetAttributeF64

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_setattributef64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_setattributef64.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SetAttributeF64

int32 __stdcall RFmxNR_SetAttributeF64 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal);

#### Purpose

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float64 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_setattributei16.html language=enus -->
## TOPIC 00083: RFmxNR_SetAttributeI16

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_setattributei16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_setattributei16.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SetAttributeI16

int32 __stdcall RFmxNR_SetAttributeI16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int16 attrVal);

#### Purpose

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int16 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_setattributei32.html language=enus -->
## TOPIC 00084: RFmxNR_SetAttributeI32

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_setattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_setattributei32.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SetAttributeI32

int32 __stdcall RFmxNR_SetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_setattributei32array.html language=enus -->
## TOPIC 00085: RFmxNR_SetAttributeI32Array

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_setattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_setattributei32array.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SetAttributeI32Array

int32 __stdcall RFmxNR_SetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_setattributei64array.html language=enus -->
## TOPIC 00086: RFmxNR_SetAttributeI64Array

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_setattributei64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_setattributei64array.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SetAttributeI64Array

int32 __stdcall RFmxNR_SetAttributeI64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_setattributei8array.html language=enus -->
## TOPIC 00087: RFmxNR_SetAttributeI8Array

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_setattributei8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_setattributei8array.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SetAttributeI8Array

int32 __stdcall RFmxNR_SetAttributeI8Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int8 attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

 If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_setattributeu8.html language=enus -->
## TOPIC 00088: RFmxNR_SetAttributeU8

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_setattributeu8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_setattributeu8.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SetAttributeU8

int32 __stdcall RFmxNR_SetAttributeU8 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal);

#### Purpose

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt8 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_setattributeu8array.html language=enus -->
## TOPIC 00089: RFmxNR_SetAttributeU8Array

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_setattributeu8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_setattributeu8array.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_SetAttributeU8Array

int32 __stdcall RFmxNR_SetAttributeU8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=cvirfmxnr_waitforacquisitioncomplete.html language=enus -->
## TOPIC 00090: RFmxNR_WaitForAcquisitionComplete

- bundle_id: `rfmx-nr-cvi`
- source_path: `cvirfmxnr_waitforacquisitioncomplete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/cvirfmxnr_waitforacquisitioncomplete.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFmxNR_WaitForAcquisitionComplete

int32 __stdcall RFmxNR_WaitForAcquisitionComplete (niRFmxInstrHandle instrumentHandle, float64 timeout);

#### Purpose

Waits and blocks the data flow until the acquisition is complete. This function is typically called after a specific initiate function. 
 


 This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_waitforacquisitioncomplete.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxNR_Initialize function. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxNR_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_all_traces_enabled.html language=enus -->
## TOPIC 00091: RFMXNR_ATTR_ACP_ALL_TRACES_ENABLED

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_all_traces_enabled.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_FALSE. Get Function: RFmxNR_ACPGetAllTracesEnabled Set Function: RFmxNR_ACPSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_amplitude_correction_type.html language=enus -->
## TOPIC 00092: RFMXNR_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_amplitude_correction_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_amplitude_correction_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY. Get Function: RFmxNR_ACPGetAmplitudeCorrectionType Set Function: RFmxNR_ACPSetAmplitudeCorrectionType |
| Values: | RFMXNR_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY (0)All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. RFMXNR_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN (1)An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |
| RFMXNR_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY (0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXNR_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN (1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_component_carrier_integration_bandwidth.html language=enus -->
## TOPIC 00093: RFMXNR_ATTR_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_component_carrier_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_component_carrier_integration_bandwidth.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the integration bandwidth of the component carrier (CC). This value is expressed in Hz. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. The default value is 9 MHz. Get Function: RFmxNR_ACPGetComponentCarrierIntegrationBandwidth Set Function: RFmxNR_ACPSetComponentCarrierIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_fft_window.html language=enus -->
## TOPIC 00094: RFMXNR_ATTR_ACP_FFT_WINDOW

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_fft_window.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_fft_window.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_FFT_WINDOW

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the FFT window type to be used to reduce spectral leakage. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_ACP_FFT_WINDOW_FLAT_TOP. Get Function: RFmxNR_ACPGetFFTWindow Set Function: RFmxNR_ACPSetFFTWindow |
| Values: | RFMXNR_VAL_ACP_FFT_WINDOW_NONE (0)No spectral leakage. RFMXNR_VAL_ACP_FFT_WINDOW_FLAT_TOP (1)Spectral leakage is reduced using flat top window type. RFMXNR_VAL_ACP_FFT_WINDOW_HANNING (2)Spectral leakage is reduced using Hanning window type. RFMXNR_VAL_ACP_FFT_WINDOW_HAMMING (3)Spectral leakage is reduced using Hamming window type. RFMXNR_VAL_ACP_FFT_WINDOW_GAUSSIAN (4)Spectral leakage is reduced using Gaussian window type. RFMXNR_VAL_ACP_FFT_WINDOW_BLACKMAN (5)Spectral leakage is reduced using Blackman window type. RFMXNR_VAL_ACP_FFT_WINDOW_BLACKMAN_HARRIS (6)Spectral leakage is reduced using Blackman-Harris window type. RFMXNR_VAL_ACP_FFT_WINDOW_KAISER_BESSEL (7)Spectral leakage is reduced using Kaiser-Bessel window type. |
| RFMXNR_VAL_ACP_FFT_WINDOW_NONE (0) | No spectral leakage. |
| RFMXNR_VAL_ACP_FFT_WINDOW_FLAT_TOP (1) | Spectral leakage is reduced using flat top window type. |
| RFMXNR_VAL_ACP_FFT_WINDOW_HANNING (2) | Spectral leakage is reduced using Hanning window type. |
| RFMXNR_VAL_ACP_FFT_WINDOW_HAMMING (3) | Spectral leakage is reduced using Hamming window type. |
| RFMXNR_VAL_ACP_FFT_WINDOW_GAUSSIAN (4) | Spectral leakage is reduced using Gaussian window type. |
| RFMXNR_VAL_ACP_FFT_WINDOW_BLACKMAN (5) | Spectral leakage is reduced using Blackman window type. |
| RFMXNR_VAL_ACP_FFT_WINDOW_BLACKMAN_HARRIS (6) | Spectral leakage is reduced using Blackman-Harris window type. |
| RFMXNR_VAL_ACP_FFT_WINDOW_KAISER_BESSEL (7) | Spectral leakage is reduced using Kaiser-Bessel window type. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_noise_compensation_enabled.html language=enus -->
## TOPIC 00095: RFMXNR_ATTR_ACP_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_noise_compensation_enabled.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_NOISE_COMPENSATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether RFmx compensates for the instrument noise when performing the measurement when you set RFMXNR_ATTR_ACP_NOISE_CALIBRATION_MODE attribute to RFMXNR_VAL_ACP_NOISE_CALIBRATION_MODE_AUTO, or when you set RFMXNR_ATTR_ACP_NOISE_CALIBRATION_MODE to RFMXNR_VAL_ACP_NOISE_CALIBRATION_MODE_MANUAL and RFMXNR_ATTR_ACP_MEASUREMENT_MODE attribute to RFMXNR_VAL_ACP_MEASUREMENT_MODE_MEASURERefer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE. Get Function: RFmxNR_ACPGetNoiseCompensationEnabled Set Function: RFmxNR_ACPSetNoiseCompensationEnabled |
| Values: | RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE (0)Disables noise compensation. RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE (1)Enables noise compensation. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |
| RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE (0) | Disables noise compensation. |
| RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE (1) | Enables noise compensation. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_offset_sideband.html language=enus -->
## TOPIC 00096: RFMXNR_ATTR_ACP_OFFSET_SIDEBAND

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_offset_sideband.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_offset_sideband.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_OFFSET_SIDEBAND

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the sideband measured for the offset channel. Use 'offset(k)' or 'subblock(n)' or 'subblock(n)/offset(k)' as the Selector Strings to read this result. The default value is RFMXNR_VAL_ACP_OFFSET_SIDEBAND_BOTH. Get Function: RFmxNR_ACPGetOffsetSideband Set Function: RFmxNR_ACPSetOffsetSideband |
| Values: | RFMXNR_VAL_ACP_OFFSET_SIDEBAND_NEGATIVE (0)Configures a lower offset segment to the left of the leftmost carrier. RFMXNR_VAL_ACP_OFFSET_SIDEBAND_POSITIVE (1)Configures an upper offset segment to the right of the rightmost carrier. RFMXNR_VAL_ACP_OFFSET_SIDEBAND_BOTH (2)Configures both the negative and the positive offset segments. |
| RFMXNR_VAL_ACP_OFFSET_SIDEBAND_NEGATIVE (0) | Configures a lower offset segment to the left of the leftmost carrier. |
| RFMXNR_VAL_ACP_OFFSET_SIDEBAND_POSITIVE (1) | Configures an upper offset segment to the right of the rightmost carrier. |
| RFMXNR_VAL_ACP_OFFSET_SIDEBAND_BOTH (2) | Configures both the negative and the positive offset segments. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_power_units.html language=enus -->
## TOPIC 00097: RFMXNR_ATTR_ACP_POWER_UNITS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_power_units.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_power_units.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_POWER_UNITS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the unit for absolute power. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_ACP_POWER_UNITS_DBM. Get Function: RFmxNR_ACPGetPowerUnits Set Function: RFmxNR_ACPSetPowerUnits |
| Values: | RFMXNR_VAL_ACP_POWER_UNITS_DBM (0)Indicates that the absolute power is expressed in dBm. RFMXNR_VAL_ACP_POWER_UNITS_DBM_BY_HZ (1)Indicates that the absolute power is expressed in dBm/Hz. |
| RFMXNR_VAL_ACP_POWER_UNITS_DBM (0) | Indicates that the absolute power is expressed in dBm. |
| RFMXNR_VAL_ACP_POWER_UNITS_DBM_BY_HZ (1) | Indicates that the absolute power is expressed in dBm/Hz. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_rbw_filter_type.html language=enus -->
## TOPIC 00098: RFMXNR_ATTR_ACP_RBW_FILTER_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_rbw_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_rbw_filter_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_RBW_FILTER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the shape of the RBW filter. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED. Get Function: RFmxNR_ACPGetRBWFilterType Set Function: RFmxNR_ACPSetRBWFilterType |
| Values: | RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED (0)No RBW filtering is performed. RFMXNR_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN (1)An RBW filter with a Gaussian response is applied. RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FLAT (2)An RBW filter with a flat response is applied. |
| RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |
| RFMXNR_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |
| RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_results_component_carrier_relative_power.html language=enus -->
## TOPIC 00099: RFMXNR_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_results_component_carrier_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_results_component_carrier_relative_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the component carrier power relative to its subblock power. This value is expressed in dB. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. Get Function: RFmxNR_ACPGetResultsComponentCarrierRelativePower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_results_lower_offset_absolute_power.html language=enus -->
## TOPIC 00100: RFMXNR_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_results_lower_offset_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_results_lower_offset_absolute_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the lower (negative) offset channel power. The carrier power is reported in dBm when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to RFMXNR_VAL_ACP_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXNR_ATTR_ACP_POWER_UNITS attribute to RFMXNR_VAL_ACP_POWER_UNITS_DBM_BY_HZ. Use 'offset(k)' or 'subblock(n)' or 'subblock(n)/offset(k)' as the Selector Strings to read this result. Get Function: RFmxNR_ACPGetResultsLowerOffsetAbsolutePower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_acp_results_lower_offset_relative_power.html language=enus -->
## TOPIC 00101: RFMXNR_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_acp_results_lower_offset_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_acp_results_lower_offset_relative_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. Use 'offset(k)' or 'subblock(n)' or 'subblock(n)/offset(k)' as the Selector Strings to read this result. Get Function: RFmxNR_ACPGetResultsLowerOffsetRelativePower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_bandwidth_part_resource_block_offset.html language=enus -->
## TOPIC 00102: RFMXNR_ATTR_BANDWIDTH_PART_RESOURCE_BLOCK_OFFSET

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_bandwidth_part_resource_block_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_bandwidth_part_resource_block_offset.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_BANDWIDTH_PART_RESOURCE_BLOCK_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the resource block offset of a bandwidth part relative to the resource RFMXNR_ATTR_GRID_START attribute. Use 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetBandwidthPartResourceBlockOffset Set Function: RFmxNR_SetBandwidthPartResourceBlockOffset |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_bandwidth_part_subcarrier_spacing.html language=enus -->
## TOPIC 00103: RFMXNR_ATTR_BANDWIDTH_PART_SUBCARRIER_SPACING

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_bandwidth_part_subcarrier_spacing.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_bandwidth_part_subcarrier_spacing.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_BANDWIDTH_PART_SUBCARRIER_SPACING

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the subcarrier spacing of the bandwidth part used in the component carrier. Use 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)' as the Selector Strings to configure or read this attribute. The default value is 30kHz.Valid values for frequency range 1 are 15kHz, 30kHz, and 60kHz.Valid values for frequency range 2-1 are 60kHz and 120kHz.Valid values for frequency range 2-2 are 120kHz, 480kHz, and 960kHz. Get Function: RFmxNR_GetBandwidthPartSubcarrierSpacing Set Function: RFmxNR_SetBandwidthPartSubcarrierSpacing |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_cell_id.html language=enus -->
## TOPIC 00104: RFMXNR_ATTR_CELL_ID

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_cell_id.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_cell_id.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CELL_ID

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies a physical layer cell identity. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to configure or read this attribute. The default value is 0. Valid values are 0 to 1007, inclusive. Get Function: RFmxNR_GetCellID Set Function: RFmxNR_SetCellID |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_integration_bandwidth_type.html language=enus -->
## TOPIC 00105: RFMXNR_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_integration_bandwidth_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_integration_bandwidth_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_SIGNAL_BANDWIDTH. Get Function: RFmxNR_CHPGetIntegrationBandwidthType Set Function: RFmxNR_CHPSetIntegrationBandwidthType |
| Values: | RFMXNR_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_SIGNAL_BANDWIDTH (0)The IBW excludes the guard bands at the edges of the carrier or subblock. RFMXNR_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_CHANNEL_BANDWIDTH (1)The IBW includes the guard bands at the edges of the carrier or subblock. |
| RFMXNR_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_SIGNAL_BANDWIDTH (0) | The IBW excludes the guard bands at the edges of the carrier or subblock. |
| RFMXNR_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_CHANNEL_BANDWIDTH (1) | The IBW includes the guard bands at the edges of the carrier or subblock. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_noise_calibration_averaging_auto.html language=enus -->
## TOPIC 00106: RFMXNR_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_AUTO

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_noise_calibration_averaging_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_noise_calibration_averaging_auto.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE. Get Function: RFmxNR_CHPGetNoiseCalibrationAveragingAuto Set Function: RFmxNR_CHPSetNoiseCalibrationAveragingAuto |
| Values: | RFMXNR_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE (0)RFmx uses the averages that you set for RFMXNR_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_COUNT attribute. RFMXNR_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE (1)RFmx uses a noise calibration averaging count of 32. |
| RFMXNR_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE (0) | RFmx uses the averages that you set for RFMXNR_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_COUNT attribute. |
| RFMXNR_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE (1) | RFmx uses a noise calibration averaging count of 32. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_noise_calibration_averaging_count.html language=enus -->
## TOPIC 00107: RFMXNR_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_COUNT

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_noise_calibration_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_noise_calibration_averaging_count.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the averaging count used for noise calibration when you set the RFMXNR_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_AUTO attribute to RFMXNR_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 32. Get Function: RFmxNR_CHPGetNoiseCalibrationAveragingCount Set Function: RFmxNR_CHPSetNoiseCalibrationAveragingCount |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_noise_calibration_mode.html language=enus -->
## TOPIC 00108: RFMXNR_ATTR_CHP_NOISE_CALIBRATION_MODE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_noise_calibration_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_noise_calibration_mode.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_NOISE_CALIBRATION_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_CHP_NOISE_CALIBRATION_MODE_AUTO. Get Function: RFmxNR_CHPGetNoiseCalibrationMode Set Function: RFmxNR_CHPSetNoiseCalibrationMode |
| Values: | RFMXNR_VAL_CHP_NOISE_CALIBRATION_MODE_MANUAL (0)When you set RFMXNR_ATTR_CHP_MEASUREMENT_MODE attribute to RFMXNR_VAL_CHP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR, you can initiate the instrument noise calibration for CHP manually. When you set the RFMXNR_ATTR_CHP_MEASUREMENT_MODE attribute to RFMXNR_VAL_CHP_MEASUREMENT_MODE_MEASURE, you can initiate the CHP measurement manually. RFMXNR_VAL_CHP_NOISE_CALIBRATION_MODE_AUTO (1)When you set the RFMXNR_ATTR_CHP_NOISE_COMPENSATION_ENABLED attribute to RFMXNR_VAL_CHP_NOISE_COMPENSATION_ENABLED_TRUE, RFmx sets the RFMXINSTR_ATTR_INPUT_ISOLATION_ENABLED attribute to Enabled and calibrates the instrument noise in the current state of the instrument. Next, RFmx resets the RFMXINSTR_ATTR_INPUT_ISOLATION_ENABLED attribute and performs the CHP measurement including compensation for the noise contribution of the instrument. RFmx skips noise calibration in this mode if valid noise calibration data is already cached. When you set the RFMXNR_ATTR_CHP_NOISE_COMPENSATION_ENABLED to RFMXNR_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE, RFmx does not calibrate instrument noise and performs the CHP measurement without compensating for the noise contribution of the instrument. |
| RFMXNR_VAL_CHP_NOISE_CALIBRATION_MODE_MANUAL (0) | When you set RFMXNR_ATTR_CHP_MEASUREMENT_MODE attribute to RFMXNR_VAL_CHP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR, you can initiate the instrument noise calibration for CHP manually. When you set the RFMXNR_ATTR_CHP_MEASUREMENT_MODE attribute to RFMXNR_VAL_CHP_MEASUREMENT_MODE_MEASURE, you can initiate the CHP measurement manually. |
| RFMXNR_VAL_CHP_NOISE_CALIBRATION_MODE_AUTO (1) | When you set the RFMXNR_ATTR_CHP_NOISE_COMPENSATION_ENABLED attribute to RFMXNR_VAL_CHP_NOISE_COMPENSATION_ENABLED_TRUE, RFmx sets the RFMXINSTR_ATTR_INPUT_ISOLATION_ENABLED attribute to Enabled and calibrates the instrument noise in the current state of the instrument. Next, RFmx resets the RFMXINSTR_ATTR_INPUT_ISOLATION_ENABLED attribute and performs the CHP measurement including compensation for the noise contribution of the instrument. RFmx skips noise calibration in this mode if valid noise calibration data is already cached. When you set the RFMXNR_ATTR_CHP_NOISE_COMPENSATION_ENABLED to RFMXNR_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE, RFmx does not calibrate instrument noise and performs the CHP measurement without compensating for the noise contribution of the instrument. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_rbw_filter_bandwidth.html language=enus -->
## TOPIC 00109: RFMXNR_ATTR_CHP_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_rbw_filter_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_rbw_filter_bandwidth.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_RBW_FILTER_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RFMXNR_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH attribute to RFMXNR_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_FALSE. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 30 kHz. Get Function: RFmxNR_CHPGetRBWFilterBandwidth Set Function: RFmxNR_CHPSetRBWFilterBandwidth |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_rbw_filter_type.html language=enus -->
## TOPIC 00110: RFMXNR_ATTR_CHP_RBW_FILTER_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_rbw_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_rbw_filter_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_RBW_FILTER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the shape of the digital RBW filter. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED. Get Function: RFmxNR_CHPGetRBWFilterType Set Function: RFmxNR_CHPSetRBWFilterType |
| Values: | RFMXNR_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED (0)No RBW filtering is performed. RFMXNR_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN (1)An RBW filter with a Gaussian response is applied. RFMXNR_VAL_CHP_RBW_FILTER_TYPE_FLAT (2)An RBW filter with a flat response is applied. |
| RFMXNR_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |
| RFMXNR_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |
| RFMXNR_VAL_CHP_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_results_component_carrier_absolute_power.html language=enus -->
## TOPIC 00111: RFMXNR_ATTR_CHP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_results_component_carrier_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_results_component_carrier_absolute_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. Get Function: RFmxNR_CHPGetResultsComponentCarrierAbsolutePower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_results_component_carrier_relative_power.html language=enus -->
## TOPIC 00112: RFMXNR_ATTR_CHP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_results_component_carrier_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_results_component_carrier_relative_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the component carrier power relative to its subblock power. This value is expressed in dB. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. Get Function: RFmxNR_CHPGetResultsComponentCarrierRelativePower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_results_subblock_power.html language=enus -->
## TOPIC 00113: RFMXNR_ATTR_CHP_RESULTS_SUBBLOCK_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_results_subblock_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_results_subblock_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_RESULTS_SUBBLOCK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. This includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. Use 'subblock(n)' as the Selector Strings to read this result. Get Function: RFmxNR_CHPGetResultsSubblockPower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_results_total_aggregated_power.html language=enus -->
## TOPIC 00114: RFMXNR_ATTR_CHP_RESULTS_TOTAL_AGGREGATED_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_results_total_aggregated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_results_total_aggregated_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_RESULTS_TOTAL_AGGREGATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxNR_CHPGetResultsTotalAggregatedPower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_subblock_integration_bandwidth.html language=enus -->
## TOPIC 00115: RFMXNR_ATTR_CHP_SUBBLOCK_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_subblock_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_subblock_integration_bandwidth.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_SUBBLOCK_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Specifies the integration bandwidth of the subblock. This value is expressed in Hz. It is the span from left edge of the integration bandwidth of the leftmost carrier to the right edge of the integration bandwidth of the rightmost carrier within a subblock. Use 'subblock(n)' as the Selector Strings to read this attribute. The default value is 0. Get Function: RFmxNR_CHPGetSubblockIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_sweep_time_auto.html language=enus -->
## TOPIC 00116: RFMXNR_ATTR_CHP_SWEEP_TIME_AUTO

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_sweep_time_auto.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether the measurement sets the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxNR_CHPGetSweepTimeAuto Set Function: RFmxNR_CHPSetSweepTimeAuto |
| Values: | RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the sweep time that you specify in the Sweep Time Interval attribute. RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_TRUE (1)The measurement uses the sweep time based on the resolution bandwidth. |
| RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval attribute. |
| RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the sweep time based on the resolution bandwidth. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_chp_sweep_time_interval.html language=enus -->
## TOPIC 00117: RFMXNR_ATTR_CHP_SWEEP_TIME_INTERVAL

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_chp_sweep_time_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_chp_sweep_time_interval.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_CHP_SWEEP_TIME_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the sweep time when you set the RFMXNR_ATTR_CHP_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1 ms. Get Function: RFmxNR_CHPGetSweepTimeInterval Set Function: RFmxNR_CHPSetSweepTimeInterval |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_component_carrier_allocated.html language=enus -->
## TOPIC 00118: RFMXNR_ATTR_COMPONENT_CARRIER_ALLOCATED

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_component_carrier_allocated.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_component_carrier_allocated.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_COMPONENT_CARRIER_ALLOCATED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether a component carrier has one or more resource elements allocated. While performing IBE measurement on a subblock, you set this attribute to False for all secondary component carriers as specified in section 6.4A.2.3 of 3GPP 38.521-1 and 3GPP 38.521-2 specifications. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to configure or read this attribute. The default value is RFMXNR_VAL_COMPONENT_CARRIER_ALLOCATED_TRUE. Get Function: RFmxNR_GetComponentCarrierAllocated Set Function: RFmxNR_SetComponentCarrierAllocated |
| Values: | RFMXNR_VAL_COMPONENT_CARRIER_ALLOCATED_FALSE (0)No resource elements are allocated for the component carrier. Only subblock IBE is computed. RFMXNR_VAL_COMPONENT_CARRIER_ALLOCATED_TRUE (1)One or more resource elements are allocated for the component carrier. |
| RFMXNR_VAL_COMPONENT_CARRIER_ALLOCATED_FALSE (0) | No resource elements are allocated for the component carrier. Only subblock IBE is computed. |
| RFMXNR_VAL_COMPONENT_CARRIER_ALLOCATED_TRUE (1) | One or more resource elements are allocated for the component carrier. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_component_carrier_radio_access_type.html language=enus -->
## TOPIC 00119: RFMXNR_ATTR_COMPONENT_CARRIER_RADIO_ACCESS_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_component_carrier_radio_access_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_component_carrier_radio_access_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_COMPONENT_CARRIER_RADIO_ACCESS_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies if a carrier is a NR or an E-UTRA carrier while using dual connectivity (EN-DC) signal. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to configure or read this attribute. The default value is RFMXNR_VAL_COMPONENT_CARRIER_RADIO_ACCESS_TYPE_NR. Get Function: RFmxNR_GetComponentCarrierRadioAccessType Set Function: RFmxNR_SetComponentCarrierRadioAccessType |
| Values: | RFMXNR_VAL_COMPONENT_CARRIER_RADIO_ACCESS_TYPE_NR (0)Specifies that the carrier is NR. RFMXNR_VAL_COMPONENT_CARRIER_RADIO_ACCESS_TYPE_EUTRA (1)Specifies that the carrier is E-UTRA. |
| RFMXNR_VAL_COMPONENT_CARRIER_RADIO_ACCESS_TYPE_NR (0) | Specifies that the carrier is NR. |
| RFMXNR_VAL_COMPONENT_CARRIER_RADIO_ACCESS_TYPE_EUTRA (1) | Specifies that the carrier is E-UTRA. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_digital_edge_trigger_edge.html language=enus -->
## TOPIC 00120: RFMXNR_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_digital_edge_trigger_edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_digital_edge_trigger_edge.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the active edge for the trigger. This attribute is used only when you set the RFMXNR_ATTR_TRIGGER_TYPE attribute to RFMXNR_VAL_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_DIGITAL_EDGE_RISING_EDGE. Get Function: RFmxNR_GetDigitalEdgeTriggerEdge Set Function: RFmxNR_SetDigitalEdgeTriggerEdge |
| Values: | RFMXNR_VAL_DIGITAL_EDGE_RISING_EDGE (0)The trigger asserts on the rising edge of the signal. RFMXNR_VAL_DIGITAL_EDGE_FALLING_EDGE (1)The trigger asserts on the falling edge of the signal. |
| RFMXNR_VAL_DIGITAL_EDGE_RISING_EDGE (0) | The trigger asserts on the rising edge of the signal. |
| RFMXNR_VAL_DIGITAL_EDGE_FALLING_EDGE (1) | The trigger asserts on the falling edge of the signal. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_gnodeb_type.html language=enus -->
## TOPIC 00121: RFMXNR_ATTR_GNODEB_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_gnodeb_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_gnodeb_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_GNODEB_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the downlink gNodeB (Base Station) type. Refer to the 3GPP 38.104 specification for more information about RFMXNR_ATTR_GNODEB_TYPE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Type 1-C. Get Function: RFmxNR_GetgNodeBType Set Function: RFmxNR_SetgNodeBType |
| Values: | RFMXNR_VAL_GNODEB_TYPE_1C (0)Type 1-C NR base station operating at FR1 and conducted requirements apply. RFMXNR_VAL_GNODEB_TYPE_1H (1)Type 1-H base station operating at FR1 and conducted and OTA requirements apply. RFMXNR_VAL_GNODEB_TYPE_1O (2)Type 1-O base station operating at FR1 and OTA requirements apply. RFMXNR_VAL_GNODEB_TYPE_2O (3)Type 2-O base station operating at FR2 and OTA requirements apply. |
| RFMXNR_VAL_GNODEB_TYPE_1C (0) | Type 1-C NR base station operating at FR1 and conducted requirements apply. |
| RFMXNR_VAL_GNODEB_TYPE_1H (1) | Type 1-H base station operating at FR1 and conducted and OTA requirements apply. |
| RFMXNR_VAL_GNODEB_TYPE_1O (2) | Type 1-O base station operating at FR1 and OTA requirements apply. |
| RFMXNR_VAL_GNODEB_TYPE_2O (3) | Type 2-O base station operating at FR2 and OTA requirements apply. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_grid_size.html language=enus -->
## TOPIC 00122: RFMXNR_ATTR_GRID_SIZE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_grid_size.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_grid_size.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_GRID_SIZE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the reference resource grid size when you set the RFMXNR_ATTR_GRID_SIZE_MODE attribute to RFMXNR_VAL_GRID_SIZE_MODE_MANUAL. Use 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)' as the Selector Strings to configure or read this attribute. Get Function: RFmxNR_GetGridSize Set Function: RFmxNR_SetGridSize |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_grid_start.html language=enus -->
## TOPIC 00123: RFMXNR_ATTR_GRID_START

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_grid_start.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_grid_start.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_GRID_START

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode attribute to Manual. Use 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetGridStart Set Function: RFmxNR_SetGridStart |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_iq_power_edge_trigger_level.html language=enus -->
## TOPIC 00124: RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_iq_power_edge_trigger_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_iq_power_edge_trigger_level.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXNR_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE; and in dBm when you set the RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXNR_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the RFMXNR_ATTR_TRIGGER_TYPE attribute to RFMXNR_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value of this attribute is hardware dependent. Get Function: RFmxNR_GetIQPowerEdgeTriggerLevel Set Function: RFmxNR_SetIQPowerEdgeTriggerLevel |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_list_step_timer_duration.html language=enus -->
## TOPIC 00125: RFMXNR_ATTR_LIST_STEP_TIMER_DURATION

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_list_step_timer_duration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_list_step_timer_duration.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_LIST_STEP_TIMER_DURATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the duration of a given list step in units specified by RFMXNR_ATTR_LIST_STEP_TIMER_UNIT. You need to use a selector string to configure or read this attribute for the list step instance. The default value is 0. Get Function: RFmxNR_GetListStepTimerDuration Set Function: RFmxNR_SetListStepTimerDuration |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_iq_impairments_per_subcarrier_enabled.html language=enus -->
## TOPIC 00126: RFMXNR_ATTR_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_iq_impairments_per_subcarrier_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_iq_impairments_per_subcarrier_enabled.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether to return I/Q impairments independently for each subcarrier. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_FALSE. Get Function: RFmxNR_ModAccGetIQImpairmentsPerSubcarrierEnabled Set Function: RFmxNR_ModAccSetIQImpairmentsPerSubcarrierEnabled |
| Values: | RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_FALSE (0)Indicates that the independent estimation of I/Q impairments for each subcarrier is disabled. RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_TRUE (1)Indicates that the independent estimation of I/Q impairments for each subcarrier is enabled. |
| RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_FALSE (0) | Indicates that the independent estimation of I/Q impairments for each subcarrier is disabled. |
| RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_TRUE (1) | Indicates that the independent estimation of I/Q impairments for each subcarrier is enabled. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_iq_mismatch_estimation_enabled.html language=enus -->
## TOPIC 00127: RFMXNR_ATTR_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_iq_mismatch_estimation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_iq_mismatch_estimation_enabled.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether to estimate the IQ impairments such as IQ gain imbalance and quadrature skew. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_TRUE. Get Function: RFmxNR_ModAccGetIQMismatchEstimationEnabled Set Function: RFmxNR_ModAccSetIQMismatchEstimationEnabled |
| Values: | RFMXNR_VAL_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_FALSE (0)IQ Impairments estimation is disabled. RFMXNR_VAL_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_TRUE (1)IQ Impairments estimation is enabled. |
| RFMXNR_VAL_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_FALSE (0) | IQ Impairments estimation is disabled. |
| RFMXNR_VAL_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_TRUE (1) | IQ Impairments estimation is enabled. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_measurement_length_unit.html language=enus -->
## TOPIC 00128: RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_measurement_length_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_measurement_length_unit.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the units in which measurement offset and measurement length are specified. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT. Get Function: RFmxNR_ModAccGetMeasurementLengthUnit Set Function: RFmxNR_ModAccSetMeasurementLengthUnit |
| Values: | RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT (1)Measurement offset and measurement length are specified in units of slots. RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_SUBFRAME (3)Measurement offset and measurement length are specified in units of subframes. RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_TIME (6)Measurement offset and measurement length are specified in seconds. Specify the measurement offset and length in multiples of 1 ms * (15 kHz/minimum subcarrier spacing of all carriers). All slots within this notional time duration are analysed. |
| RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT (1) | Measurement offset and measurement length are specified in units of slots. |
| RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_SUBFRAME (3) | Measurement offset and measurement length are specified in units of subframes. |
| RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_TIME (6) | Measurement offset and measurement length are specified in seconds. Specify the measurement offset and length in multiples of 1 ms * (15 kHz/minimum subcarrier spacing of all carriers). All slots within this notional time duration are analysed. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_measurement_mode.html language=enus -->
## TOPIC 00129: RFMXNR_ATTR_MODACC_MEASUREMENT_MODE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_measurement_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_measurement_mode.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_MEASUREMENT_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_MODACC_MEASUREMENT_MODE_MEASURE. Get Function: RFmxNR_ModAccGetMeasurementMode Set Function: RFmxNR_ModAccSetMeasurementMode |
| Values: | RFMXNR_VAL_MODACC_MEASUREMENT_MODE_MEASURE (0)The ModAcc measurement is performed on the acquired signal. RFMXNR_VAL_MODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR (1)The ModAcc measurement measures the noise floor of the instrument across the frequency determined by the carrier frequency and the channel bandwidth. In this mode, the measurement expects the signal generator to be turned off and checks if there is any signal power detected at RFIn port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is already calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |
| RFMXNR_VAL_MODACC_MEASUREMENT_MODE_MEASURE (0) | The ModAcc measurement is performed on the acquired signal. |
| RFMXNR_VAL_MODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR (1) | The ModAcc measurement measures the noise floor of the instrument across the frequency determined by the carrier frequency and the channel bandwidth. In this mode, the measurement expects the signal generator to be turned off and checks if there is any signal power detected at RFIn port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is already calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_multicarrier_filter_enabled.html language=enus -->
## TOPIC 00130: RFMXNR_ATTR_MODACC_MULTICARRIER_FILTER_ENABLED

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_multicarrier_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_multicarrier_filter_enabled.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_MULTICARRIER_FILTER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this attribute, if number of carriers is set to more than 1 or if you set the RFMXNR_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED attribute to RFMXNR_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_FALSE, where in the multi carrier filter will always be used. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_FALSE. Get Function: RFmxNR_ModAccGetMulticarrierFilterEnabled Set Function: RFmxNR_ModAccSetMulticarrierFilterEnabled |
| Values: | RFMXNR_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_FALSE (0)Measurement doesn't use the filter. RFMXNR_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_TRUE (1)Measurement filters out unwanted emissions. |
| RFMXNR_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_FALSE (0) | Measurement doesn't use the filter. |
| RFMXNR_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_TRUE (1) | Measurement filters out unwanted emissions. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_component_carrier_iq_timing_skew_mean.html language=enus -->
## TOPIC 00131: RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_IQ_TIMING_SKEW_MEAN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_component_carrier_iq_timing_skew_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_component_carrier_iq_timing_skew_mean.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_IQ_TIMING_SKEW_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the estimated IQ Timing Skew averaged over Meas Length. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. IQ Timing skew is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds. Get Function: RFmxNR_ModAccGetResultsComponentCarrierIQTimingSkewMean |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_component_carrier_quadrature_error_mean.html language=enus -->
## TOPIC 00132: RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_QUADRATURE_ERROR_MEAN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_component_carrier_quadrature_error_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_component_carrier_quadrature_error_mean.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_QUADRATURE_ERROR_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the estimated quadrature error averaged over measurement length. This value is expressed in degrees. Quadrature error is the measure of skewness in degree of the I component with respect to the Q component of the IQ signal being measured. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsComponentCarrierQuadratureErrorMean |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_component_carrier_slot_frequency_error_maximum.html language=enus -->
## TOPIC 00133: RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_SLOT_FREQUENCY_ERROR_MAXIMUM

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_component_carrier_slot_frequency_error_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_component_carrier_slot_frequency_error_maximum.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_SLOT_FREQUENCY_ERROR_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the estimated maximum per slot carrier frequency offset over the Measurement Length. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. The default value is 0. Get Function: RFmxNR_ModAccGetResultsComponentCarrierSlotFrequencyErrorMaximum |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_composite_peak_evm_slot_index.html language=enus -->
## TOPIC 00134: RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SLOT_INDEX

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_composite_peak_evm_slot_index.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_composite_peak_evm_slot_index.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SLOT_INDEX

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeI32 |
| Description: | Returns the slot index where ModAcc Results Max Pk Composite EVM occurs. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsCompositePeakEVMSlotIndex |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pdsch_data_re_power_mean.html language=enus -->
## TOPIC 00135: RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DATA_RE_POWER_MEAN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pdsch_data_re_power_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pdsch_data_re_power_mean.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DATA_RE_POWER_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the mean value (over Meas Length) of power calculated on PDSCH data REs. Use 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPDSCHDataREPowerMean |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pdsch_qpsk_rms_evm_mean.html language=enus -->
## TOPIC 00136: RFMXNR_ATTR_MODACC_RESULTS_PDSCH_QPSK_RMS_EVM_MEAN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pdsch_qpsk_rms_evm_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pdsch_qpsk_rms_evm_mean.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PDSCH_QPSK_RMS_EVM_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calculated over measurement length on all QPSK modulated PDSCH data symbols. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB. Use 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPDSCHQPSKRMSEVMMean |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pusch_data_peak_evm_maximum.html language=enus -->
## TOPIC 00137: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_PEAK_EVM_MAXIMUM

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pusch_data_peak_evm_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pusch_data_peak_evm_maximum.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_PEAK_EVM_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the maximum value of peak EVMs calculated over measurement length on PUSCH data symbols. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB.Use 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPUSCHDataPeakEVMMaximum |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pusch_data_re_power_mean.html language=enus -->
## TOPIC 00138: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEAN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pusch_data_re_power_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pusch_data_re_power_mean.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the mean value (over Meas Length) of power calculated on PUSCH data REs. Use 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPUSCHDataREPowerMean |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pusch_data_rms_evm_mean.html language=enus -->
## TOPIC 00139: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEAN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pusch_data_rms_evm_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pusch_data_rms_evm_mean.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calculated over measurement length on PUSCH data symbols. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB.Use 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPUSCHDataRMSEVMMean |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pusch_data_transient_rms_evm_mean.html language=enus -->
## TOPIC 00140: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_TRANSIENT_RMS_EVM_MEAN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pusch_data_transient_rms_evm_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pusch_data_transient_rms_evm_mean.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_TRANSIENT_RMS_EVM_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calulated over measurement interval for the PUSCH symbols where the transient occurs. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB. Use 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPUSCHDataTransientRMSEVMMean |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pusch_dmrs_peak_evm_maximum.html language=enus -->
## TOPIC 00141: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUM

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pusch_dmrs_peak_evm_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pusch_dmrs_peak_evm_maximum.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the maximum value of peak EVMs calculated over measurement length on PUSCH DMRS. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB.Use 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPUSCHDMRSPeakEVMMaximum |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pusch_dmrs_re_power_mean.html language=enus -->
## TOPIC 00142: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RE_POWER_MEAN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pusch_dmrs_re_power_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pusch_dmrs_re_power_mean.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RE_POWER_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the mean value (over Meas Length) of power calculated on PUSCH DMRS REs. Use 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPUSCHDMRSREPowerMean |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pusch_dmrs_rms_evm_mean.html language=enus -->
## TOPIC 00143: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEAN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pusch_dmrs_rms_evm_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pusch_dmrs_rms_evm_mean.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the mean value of RMS EVMs calculated over measurement length on PUSCH DMRS. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXNR_ATTR_MODACC_EVM_UNIT attribute to RFMXNR_VAL_MODACC_EVM_UNIT_DB, the measurement returns this result in dB.Use 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPUSCHDMRSRMSEVMMean |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pusch_peak_phase_offset_maximum.html language=enus -->
## TOPIC 00144: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_MAXIMUM

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pusch_peak_phase_offset_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pusch_peak_phase_offset_maximum.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the maximum value over Meas Length of peak phase offsets between the reference and measurement slots. Use 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPUSCHPeakPhaseOffsetMaximum |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_pusch_peak_phase_offset_slot_index.html language=enus -->
## TOPIC 00145: RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_SLOT_INDEX

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_pusch_peak_phase_offset_slot_index.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_pusch_peak_phase_offset_slot_index.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_SLOT_INDEX

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeI32 |
| Description: | Returns the slot index where ModAcc Results PUSCH Pk Phase Offset Max occurs. Use 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsPUSCHPeakPhaseOffsetSlotIndex |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_spectral_flatness_range2_maximum_to_range1_minimum.html language=enus -->
## TOPIC 00146: RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE1_MINIMUM

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_spectral_flatness_range2_maximum_to_range1_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_spectral_flatness_range2_maximum_to_range1_minimum.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE1_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the peak-to-peak ripple of the EVM equalizer coefficients from maximum in Range2 to minimum in Range1 for the Measurement unit that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsSpectralFlatnessRange2MaximumToRange1Minimum |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_spectral_flatness_range2_maximum_to_range2_minimum.html language=enus -->
## TOPIC 00147: RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE2_MINIMUM

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_spectral_flatness_range2_maximum_to_range2_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_spectral_flatness_range2_maximum_to_range2_minimum.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE2_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the peak-to-peak ripple of the magnitude of EVM equalizer coefficients within Range2 for the Measurement unit, that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsSpectralFlatnessRange2MaximumToRange2Minimum |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_subblock_in_band_emission_margin.html language=enus -->
## TOPIC 00148: RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_IN_BAND_EMISSION_MARGIN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_subblock_in_band_emission_margin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_subblock_in_band_emission_margin.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_IN_BAND_EMISSION_MARGIN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns In-Band Emission Margin of the subblock's aggregated bandwidth. This value is expressed in dB. Margin is the smallest difference between In-Band Emission measurement trace and the limit trace. The limit is defined in section 6.4A.2.2.2 of 3GPP 38.101-1 specification and section 6.4A.2.3 of 3GPP 38.101-2 specification. In-Band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The margin is not returned in case of clustered PUSCH allocation, or when there is more than one active carrier, or when there is full allocation of resource blocks, or when carriers with different sub-carrier spacing are aggregated or when the number of carriers is greater than 2.Use 'subblock(n)' as the Selector Strings to read this attribute. Get Function: RFmxNR_ModAccGetResultsSubblockInBandEmissionMargin |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_results_subblock_lo_component_carrier_index.html language=enus -->
## TOPIC 00149: RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_LO_COMPONENT_CARRIER_INDEX

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_results_subblock_lo_component_carrier_index.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_results_subblock_lo_component_carrier_index.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_LO_COMPONENT_CARRIER_INDEX

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeI32 |
| Description: | Returns the index of the component carrier that includes the LO of the transmitter according to the RFMXNR_ATTR_SUBBLOCK_FREQUENCY and RFMXNR_ATTR_SUBBLOCK_TRANSMIT_LO_FREQUENCY attributes. If the LO of the transmitter doesn't fall into any component carrier of the subblock, the attribute returns -1. This result is valid only when you set the RFMXNR_ATTR_TRANSMITTER_ARCHITECTURE attribute to RFMXNR_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_SUBBLOCK. Use 'subblock(n)' as the Selector Strings to read this result. Get Function: RFmxNR_ModAccGetResultsSubblockLOComponentCarrierIndex |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_short_frame_enabled.html language=enus -->
## TOPIC 00150: RFMXNR_ATTR_MODACC_SHORT_FRAME_ENABLED

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_short_frame_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_short_frame_enabled.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_SHORT_FRAME_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether the input signal has a periodicity shorter than the NR frame duration. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_MODACC_SHORT_FRAME_ENABLED_FALSE. Get Function: RFmxNR_ModAccGetShortFrameEnabled Set Function: RFmxNR_ModAccSetShortFrameEnabled |
| Values: | RFMXNR_VAL_MODACC_SHORT_FRAME_ENABLED_FALSE (0)When you set the attribute to False or the RFMXNR_ATTR_TRIGGER_TYPE attribute is set to a value other than RFMXNR_VAL_TRIGGER_TYPE_NONE, a signal periodicity equal to the maximum of 1 frame duration and the configured SSB periodicity, if SSB is active, is assumed. RFMXNR_VAL_MODACC_SHORT_FRAME_ENABLED_TRUE (1)When you set the attribute to False or the RFMXNR_ATTR_TRIGGER_TYPE attribute is set to None, the measurement uses RFMXNR_ATTR_MODACC_SHORT_FRAME_LENGTH as signal periodicity. |
| RFMXNR_VAL_MODACC_SHORT_FRAME_ENABLED_FALSE (0) | When you set the attribute to False or the RFMXNR_ATTR_TRIGGER_TYPE attribute is set to a value other than RFMXNR_VAL_TRIGGER_TYPE_NONE, a signal periodicity equal to the maximum of 1 frame duration and the configured SSB periodicity, if SSB is active, is assumed. |
| RFMXNR_VAL_MODACC_SHORT_FRAME_ENABLED_TRUE (1) | When you set the attribute to False or the RFMXNR_ATTR_TRIGGER_TYPE attribute is set to None, the measurement uses RFMXNR_ATTR_MODACC_SHORT_FRAME_LENGTH as signal periodicity. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_short_frame_length.html language=enus -->
## TOPIC 00151: RFMXNR_ATTR_MODACC_SHORT_FRAME_LENGTH

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_short_frame_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_short_frame_length.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_SHORT_FRAME_LENGTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the short frame periodicity in unit specified by Short Frame Length Unit. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.01. Get Function: RFmxNR_ModAccGetShortFrameLength Set Function: RFmxNR_ModAccSetShortFrameLength |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_modacc_transient_period_evm_mode.html language=enus -->
## TOPIC 00152: RFMXNR_ATTR_MODACC_TRANSIENT_PERIOD_EVM_MODE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_modacc_transient_period_evm_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_modacc_transient_period_evm_mode.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_MODACC_TRANSIENT_PERIOD_EVM_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Configures the EVM measurement behavior for symbols affected by power transients. According to 3GPP 38.101-1 Rel. 17.6 transient EVM measurement (i.e. Transient Period EVM Mode set to Include) is applicable when RFMXNR_ATTR_LINK_DIRECTION is set to RFMXNR_VAL_LINK_DIRECTION_UPLINK, RFMXNR_ATTR_FREQUENCY_RANGE is set to RFMXNR_VAL_FREQUENCY_RANGE_RANGE1, RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED is set to RFMXNR_VAL_PUSCH_TRANSFORM_PRECODING_ENABLED_FALSE, and RFMXNR_ATTR_BANDWIDTH_PART_SUBCARRIER_SPACING is set to 15kHz or 30kHz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_MODACC_TRANSIENT_PERIOD_EVM_MODE_DISABLED. Get Function: RFmxNR_ModAccGetTransientPeriodEVMMode Set Function: RFmxNR_ModAccSetTransientPeriodEVMMode |
| Values: | RFMXNR_VAL_MODACC_TRANSIENT_PERIOD_EVM_MODE_DISABLED (0)No special treatment of transient symbols (old behavior). RFMXNR_VAL_MODACC_TRANSIENT_PERIOD_EVM_MODE_EXCLUDE (1)Transient symbols are not considered for EVM computation. RFMXNR_VAL_MODACC_TRANSIENT_PERIOD_EVM_MODE_INCLUDE (2)Transient EVM measurement definition is applied to transient symbols and returned as a separate Transient RMS EVM result. |
| RFMXNR_VAL_MODACC_TRANSIENT_PERIOD_EVM_MODE_DISABLED (0) | No special treatment of transient symbols (old behavior). |
| RFMXNR_VAL_MODACC_TRANSIENT_PERIOD_EVM_MODE_EXCLUDE (1) | Transient symbols are not considered for EVM computation. |
| RFMXNR_VAL_MODACC_TRANSIENT_PERIOD_EVM_MODE_INCLUDE (2) | Transient EVM measurement definition is applied to transient symbols and returned as a separate Transient RMS EVM result. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_number_of_steps.html language=enus -->
## TOPIC 00153: RFMXNR_ATTR_NUMBER_OF_STEPS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_number_of_steps.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_number_of_steps.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_NUMBER_OF_STEPS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the number of active steps in the list. You need to use a selector string to configure or read this attribute for the list instance. The default value is 0. Get Function: RFmxNR_GetNumberOfSteps Set Function: RFmxNR_SetNumberOfSteps |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_number_of_subblocks.html language=enus -->
## TOPIC 00154: RFMXNR_ATTR_NUMBER_OF_SUBBLOCKS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_number_of_subblocks.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_number_of_subblocks.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_NUMBER_OF_SUBBLOCKS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the number of subblocks configured in intraband non-contiguous carrier aggregation scenarios. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Set this attribute to 1 for single carrier and intra-band contiguous carrier aggregation. Get Function: RFmxNR_GetNumberOfSubblocks Set Function: RFmxNR_SetNumberOfSubblocks |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_number_of_users.html language=enus -->
## TOPIC 00155: RFMXNR_ATTR_NUMBER_OF_USERS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_number_of_users.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_number_of_users.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_NUMBER_OF_USERS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the number of users present in the bandwidth part. Use 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)' as the Selector Strings to configure or read this attribute. The default value is 1. Get Function: RFmxNR_GetNumberOfUsers Set Function: RFmxNR_SetNumberOfUsers |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_obw_averaging_type.html language=enus -->
## TOPIC 00156: RFMXNR_ATTR_OBW_AVERAGING_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_obw_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_obw_averaging_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_OBW_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_OBW_AVERAGING_TYPE_RMS. Get Function: RFmxNR_OBWGetAveragingType Set Function: RFmxNR_OBWSetAveragingType |
| Values: | RFMXNR_VAL_OBW_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXNR_VAL_OBW_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. RFMXNR_VAL_OBW_AVERAGING_TYPE_SCALAR (2)The square root of the power spectrum is averaged. RFMXNR_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXNR_VAL_OBW_AVERAGING_TYPE_MINIMUM (4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXNR_VAL_OBW_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXNR_VAL_OBW_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXNR_VAL_OBW_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |
| RFMXNR_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXNR_VAL_OBW_AVERAGING_TYPE_MINIMUM (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_obw_rbw_filter_auto_bandwidth.html language=enus -->
## TOPIC 00157: RFMXNR_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_obw_rbw_filter_auto_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_obw_rbw_filter_auto_bandwidth.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the RBW. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_TRUE. Get Function: RFmxNR_OBWGetRBWFilterAutoBandwidth Set Function: RFmxNR_OBWSetRBWFilterAutoBandwidth |
| Values: | RFMXNR_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_FALSE (0)The measurement uses the RBW that you specify in the RFMXNR_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. RFMXNR_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_TRUE (1)The measurement computes the RBW. |
| RFMXNR_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_FALSE (0) | The measurement uses the RBW that you specify in the RFMXNR_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |
| RFMXNR_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_TRUE (1) | The measurement computes the RBW. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_obw_rbw_filter_bandwidth.html language=enus -->
## TOPIC 00158: RFMXNR_ATTR_OBW_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_obw_rbw_filter_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_obw_rbw_filter_bandwidth.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_OBW_RBW_FILTER_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RFMXNR_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH attribute to RFMXNR_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_FALSE. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10 kHz. Get Function: RFmxNR_OBWGetRBWFilterBandwidth Set Function: RFmxNR_OBWSetRBWFilterBandwidth |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pbch_power.html language=enus -->
## TOPIC 00159: RFMXNR_ATTR_PBCH_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pbch_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pbch_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PBCH_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the power scaling value for the PBCH REs in the SS/PBCH block. This value is expressed in dB. Use 'carrier(k)' or 'subblock(n)carrier(k)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetPBCHPower Set Function: RFmxNR_SetPBCHPower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pdsch_dmrs_additional_positions.html language=enus -->
## TOPIC 00160: RFMXNR_ATTR_PDSCH_DMRS_ADDITIONAL_POSITIONS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pdsch_dmrs_additional_positions.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pdsch_dmrs_additional_positions.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PDSCH_DMRS_ADDITIONAL_POSITIONS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the number of additional sets of consecutive DMRS symbols in a slot. Use 'pdsch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pdsch(r)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetPDSCHDMRSAdditionalPositions Set Function: RFmxNR_SetPDSCHDMRSAdditionalPositions |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pdsch_mapping_type.html language=enus -->
## TOPIC 00161: RFMXNR_ATTR_PDSCH_MAPPING_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pdsch_mapping_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pdsch_mapping_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PDSCH_MAPPING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the mapping type of DMRS. Use 'pdsch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pdsch(r)' as the Selector Strings to configure or read this attribute. The default value is RFMXNR_VAL_PDSCH_MAPPING_TYPE_TYPE_A. Get Function: RFmxNR_GetPDSCHMappingType Set Function: RFmxNR_SetPDSCHMappingType |
| Values: | RFMXNR_VAL_PDSCH_MAPPING_TYPE_TYPE_A (0)The first DMRS symbol index in a slot is either 2 or 3. RFMXNR_VAL_PDSCH_MAPPING_TYPE_TYPE_B (1)The first DMRS symbol index in a slot is 0. |
| RFMXNR_VAL_PDSCH_MAPPING_TYPE_TYPE_A (0) | The first DMRS symbol index in a slot is either 2 or 3. |
| RFMXNR_VAL_PDSCH_MAPPING_TYPE_TYPE_B (1) | The first DMRS symbol index in a slot is 0. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pdsch_number_of_resource_block_clusters.html language=enus -->
## TOPIC 00162: RFMXNR_ATTR_PDSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pdsch_number_of_resource_block_clusters.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pdsch_number_of_resource_block_clusters.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PDSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. Use 'pdsch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pdsch(r)' as the Selector Strings to configure or read this attribute. The default value is 1. Get Function: RFmxNR_GetPDSCHNumberOfResourceBlockClusters Set Function: RFmxNR_SetPDSCHNumberOfResourceBlockClusters |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pdsch_ptrs_antenna_ports.html language=enus -->
## TOPIC 00163: RFMXNR_ATTR_PDSCH_PTRS_ANTENNA_PORTS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pdsch_ptrs_antenna_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pdsch_ptrs_antenna_ports.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PDSCH_PTRS_ANTENNA_PORTS

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeStringRFmxNR_GetAttributeString |
| Description: | Specifies the DMRS Antenna Ports associated with PTRS transmission. Use 'pdsch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pdsch(r)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetPDSCHPTRSAntennaPorts Set Function: RFmxNR_SetPDSCHPTRSAntennaPorts |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pdsch_ptrs_re_offset.html language=enus -->
## TOPIC 00164: RFMXNR_ATTR_PDSCH_PTRS_RE_OFFSET

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pdsch_ptrs_re_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pdsch_ptrs_re_offset.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PDSCH_PTRS_RE_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the RE Offset to be used for transmission of PTRS as defined in Table 7.4.1.2.2-1 of 3GPP 38.211 specification. Use 'pdsch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pdsch(r)' as the Selector Strings to configure or read this attribute. The default value is 00. Get Function: RFmxNR_GetPDSCHPTRSREOffset Set Function: RFmxNR_SetPDSCHPTRSREOffset |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pdsch_slot_allocation.html language=enus -->
## TOPIC 00165: RFMXNR_ATTR_PDSCH_SLOT_ALLOCATION

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pdsch_slot_allocation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pdsch_slot_allocation.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PDSCH_SLOT_ALLOCATION

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeStringRFmxNR_GetAttributeString |
| Description: | Specifies the slot allocation in NR Frame. This defines the indices of the allocated slots. The format is defined by range format specifiers. The range format specifier is a comma separated list of entries in the following format:Single unsigned integer values or lastA range of single unsigned integer values given as i0:i1, where i0 represents the first and i1 the last value in the range, with i0 (= i1. The keyword last expands to the largest allowed value, depending on the context of the range specification.Examples: 2,5 will expand to {2,5}1:3,7 will expand to {1,2,3,7}.Use 'pdsch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pdsch(r)' as the Selector Strings to configure or read this attribute. The default value is 0-Last. Valid values are from 0 to (Maximum number of slots in frame - 1), inclusive. Get Function: RFmxNR_GetPDSCHSlotAllocation Set Function: RFmxNR_SetPDSCHSlotAllocation |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_piby2bpsk_power_boost_enabled.html language=enus -->
## TOPIC 00166: RFMXNR_ATTR_PIBY2BPSK_POWER_BOOST_ENABLED

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_piby2bpsk_power_boost_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_piby2bpsk_power_boost_enabled.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PIBY2BPSK_POWER_BOOST_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the power boost for PI/2 BPSK signal when you set the RFMXNR_ATTR_FREQUENCY_RANGE attribute to RFMXNR_VAL_FREQUENCY_RANGE_RANGE1. This attribute is valid only for uplink direction. For PI/2 BPSK modulation, if this attribute is set to True, Power Class attribute to 3,RFMXNR_ATTR_BAND attribute to 40, 41, 77, 78, or 79, and the RFMXNR_ATTR_PUSCH_SLOT_ALLOCATION attribute is set such that, at most 40% of the radio frame is active, then the EVM Equalizer spectral flatness mask specified in section 6.4.2.4.1 of 3GPP 38.101-1 is used. Otherwise the EVM Equalizer spectral flatness mask specified in section 6.4.2.4 of 3GPP 38.101-1 is used.When you set the RFMXNR_ATTR_FREQUENCY_RANGE attribute to Range 2, the measurement ignores the RFMXNR_ATTR_PIBY2BPSK_POWER_BOOST_ENABLED attribute. In this case, when you set the RFMXNR_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION attribute to RFMXNR_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_NORMAL, the equalizer spectral flatness mask as specified in section 6.4.2.5 of 3GPP TS 38.101-2 is used for the PI/2 BPSK signal. Otherwise, the equalizer spectral flatness mask as specified in section 6.4.2.4 of 3GPP 38.101-2 is used.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_PIBY2BPSK_POWER_BOOST_ENABLED_FALSE. Get Function: RFmxNR_GetPiBy2BPSKPowerBoostEnabled Set Function: RFmxNR_SetPiBy2BPSKPowerBoostEnabled |
| Values: | RFMXNR_VAL_PIBY2BPSK_POWER_BOOST_ENABLED_FALSE (0)Power boost for PI/2 BPSK modulation is not enabled. RFMXNR_VAL_PIBY2BPSK_POWER_BOOST_ENABLED_TRUE (1)Power boost for PI/2 BPSK modulation is enabled. |
| RFMXNR_VAL_PIBY2BPSK_POWER_BOOST_ENABLED_FALSE (0) | Power boost for PI/2 BPSK modulation is not enabled. |
| RFMXNR_VAL_PIBY2BPSK_POWER_BOOST_ENABLED_TRUE (1) | Power boost for PI/2 BPSK modulation is enabled. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_dmrs_additional_positions.html language=enus -->
## TOPIC 00167: RFMXNR_ATTR_PUSCH_DMRS_ADDITIONAL_POSITIONS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_dmrs_additional_positions.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_dmrs_additional_positions.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_DMRS_ADDITIONAL_POSITIONS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the number of additional sets of consecutive DMRS symbols in a slot. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetPUSCHDMRSAdditionalPositions Set Function: RFmxNR_SetPUSCHDMRSAdditionalPositions |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_dmrs_antenna_ports.html language=enus -->
## TOPIC 00168: RFMXNR_ATTR_PUSCH_DMRS_ANTENNA_PORTS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_dmrs_antenna_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_dmrs_antenna_ports.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_DMRS_ANTENNA_PORTS

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeStringRFmxNR_GetAttributeString |
| Description: | Specifies the antenna ports used for DMRS transmission. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is 0. Valid values depend on RFMXNR_ATTR_PUSCH_MAPPING_TYPE and RFMXNR_ATTR_PUSCH_DMRS_NUMBER_OF_CDM_GROUPS attributes. Get Function: RFmxNR_GetPUSCHDMRSAntennaPorts Set Function: RFmxNR_SetPUSCHDMRSAntennaPorts |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_dmrs_number_of_cdm_groups.html language=enus -->
## TOPIC 00169: RFMXNR_ATTR_PUSCH_DMRS_NUMBER_OF_CDM_GROUPS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_dmrs_number_of_cdm_groups.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_dmrs_number_of_cdm_groups.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_DMRS_NUMBER_OF_CDM_GROUPS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the number of CDM groups, when you set the RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to RFMXNR_VAL_PUSCH_TRANSFORM_PRECODING_ENABLED_FALSE, otherwise it is coerced to 2. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is 1. Get Function: RFmxNR_GetPUSCHDMRSNumberOfCDMGroups Set Function: RFmxNR_SetPUSCHDMRSNumberOfCDMGroups |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_dmrs_power.html language=enus -->
## TOPIC 00170: RFMXNR_ATTR_PUSCH_DMRS_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_dmrs_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_dmrs_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_DMRS_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the factor which boosts the PUSCH DMRS REs. This value is expressed in dB. This attribute is ignored if you set the RFMXNR_ATTR_PUSCH_DMRS_POWER_MODE attribute to RFMXNR_VAL_PUSCH_DMRS_POWER_MODE_CDM_GROUPS. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetPUSCHDMRSPower Set Function: RFmxNR_SetPUSCHDMRSPower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_dmrs_pusch_id.html language=enus -->
## TOPIC 00171: RFMXNR_ATTR_PUSCH_DMRS_PUSCH_ID

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_dmrs_pusch_id.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_dmrs_pusch_id.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_DMRS_PUSCH_ID

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the value of RFMXNR_ATTR_PUSCH_DMRS_PUSCH_ID used for reference signal generation. This attribute is valid only when you set the RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to RFMXNR_VAL_PUSCH_TRANSFORM_PRECODING_ENABLED_TRUE and RFMXNR_ATTR_PUSCH_DMRS_PUSCH_ID_MODE attribute to RFMXNR_VAL_PUSCH_DMRS_PUSCH_ID_MODE_USER_DEFINED. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is 0. Valid values are from 0 to 1007, inclusive. Get Function: RFmxNR_GetPUSCHDMRSPUSCHID Set Function: RFmxNR_SetPUSCHDMRSPUSCHID |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_dmrs_pusch_id_mode.html language=enus -->
## TOPIC 00172: RFMXNR_ATTR_PUSCH_DMRS_PUSCH_ID_MODE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_dmrs_pusch_id_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_dmrs_pusch_id_mode.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_DMRS_PUSCH_ID_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether PUSCH DMRS PUSCH ID is based on RFMXNR_ATTR_CELL_ID or specified by you. This attribute is valid only when you set the RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to RFMXNR_VAL_PUSCH_TRANSFORM_PRECODING_ENABLED_TRUE. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is RFMXNR_VAL_PUSCH_DMRS_PUSCH_ID_MODE_CELL_ID. Get Function: RFmxNR_GetPUSCHDMRSPUSCHIDMode Set Function: RFmxNR_SetPUSCHDMRSPUSCHIDMode |
| Values: | RFMXNR_VAL_PUSCH_DMRS_PUSCH_ID_MODE_CELL_ID (0)The value of PUSCH DMRS PUSCH ID is based on Cell ID attribute. RFMXNR_VAL_PUSCH_DMRS_PUSCH_ID_MODE_USER_DEFINED (1)The value of PUSCH DMRS PUSCH ID is specified by you. |
| RFMXNR_VAL_PUSCH_DMRS_PUSCH_ID_MODE_CELL_ID (0) | The value of PUSCH DMRS PUSCH ID is based on Cell ID attribute. |
| RFMXNR_VAL_PUSCH_DMRS_PUSCH_ID_MODE_USER_DEFINED (1) | The value of PUSCH DMRS PUSCH ID is specified by you. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_dmrs_type_a_position.html language=enus -->
## TOPIC 00173: RFMXNR_ATTR_PUSCH_DMRS_TYPE_A_POSITION

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_dmrs_type_a_position.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_dmrs_type_a_position.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_DMRS_TYPE_A_POSITION

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the position of first DMRS symbol in a slot when you set the RFMXNR_ATTR_PUSCH_MAPPING_TYPE attribute to RFMXNR_VAL_PUSCH_MAPPING_TYPE_TYPE_A. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is 2. Get Function: RFmxNR_GetPUSCHDMRSTypeAPosition Set Function: RFmxNR_SetPUSCHDMRSTypeAPosition |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_mapping_type.html language=enus -->
## TOPIC 00174: RFMXNR_ATTR_PUSCH_MAPPING_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_mapping_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_mapping_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_MAPPING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the mapping type of DMRS. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is RFMXNR_VAL_PUSCH_MAPPING_TYPE_TYPE_A. Get Function: RFmxNR_GetPUSCHMappingType Set Function: RFmxNR_SetPUSCHMappingType |
| Values: | RFMXNR_VAL_PUSCH_MAPPING_TYPE_TYPE_A (0)The first DMRS symbol index in a slot is either 2 or 3 based on RFMXNR_ATTR_PUSCH_DMRS_TYPE_A_POSITION attribute. RFMXNR_VAL_PUSCH_MAPPING_TYPE_TYPE_B (1)The first DMRS symbol index in a slot is the first active PUSCH symbol. |
| RFMXNR_VAL_PUSCH_MAPPING_TYPE_TYPE_A (0) | The first DMRS symbol index in a slot is either 2 or 3 based on RFMXNR_ATTR_PUSCH_DMRS_TYPE_A_POSITION attribute. |
| RFMXNR_VAL_PUSCH_MAPPING_TYPE_TYPE_B (1) | The first DMRS symbol index in a slot is the first active PUSCH symbol. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_number_of_resource_blocks.html language=enus -->
## TOPIC 00175: RFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_number_of_resource_blocks.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_number_of_resource_blocks.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This attribute is ignored if you set the RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED attribute to RFMXNR_VAL_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_TRUE. Use 'puschcluster(s)' or 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)/puschcluster(s)' as the Selector Strings to configure or read this attribute. The default value is -1. If you set this attribute to -1, all available resource blocks for the specified bandwidth are configured. Get Function: RFmxNR_GetPUSCHNumberOfResourceBlocks Set Function: RFmxNR_SetPUSCHNumberOfResourceBlocks |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_ptrs_antenna_ports.html language=enus -->
## TOPIC 00176: RFMXNR_ATTR_PUSCH_PTRS_ANTENNA_PORTS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_ptrs_antenna_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_ptrs_antenna_ports.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_PTRS_ANTENNA_PORTS

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeStringRFmxNR_GetAttributeString |
| Description: | Specifies the DMRS antenna ports associated with PTRS transmission. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to RFMXNR_VAL_PUSCH_PTRS_ENABLED_TRUE. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetPUSCHPTRSAntennaPorts Set Function: RFmxNR_SetPUSCHPTRSAntennaPorts |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_ptrs_enabled.html language=enus -->
## TOPIC 00177: RFMXNR_ATTR_PUSCH_PTRS_ENABLED

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_ptrs_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_ptrs_enabled.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_PTRS_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether the PUSCH transmission contains PTRS signals. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is RFMXNR_VAL_PUSCH_PTRS_ENABLED_FALSE. Get Function: RFmxNR_GetPUSCHPTRSEnabled Set Function: RFmxNR_SetPUSCHPTRSEnabled |
| Values: | RFMXNR_VAL_PUSCH_PTRS_ENABLED_FALSE (0)The PUSCH Transmission does not contain PTRS signals. RFMXNR_VAL_PUSCH_PTRS_ENABLED_TRUE (1)The PUSCH PTRS contains PTRS signals. |
| RFMXNR_VAL_PUSCH_PTRS_ENABLED_FALSE (0) | The PUSCH Transmission does not contain PTRS signals. |
| RFMXNR_VAL_PUSCH_PTRS_ENABLED_TRUE (1) | The PUSCH PTRS contains PTRS signals. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_ptrs_frequency_density.html language=enus -->
## TOPIC 00178: RFMXNR_ATTR_PUSCH_PTRS_FREQUENCY_DENSITY

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_ptrs_frequency_density.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_ptrs_frequency_density.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_PTRS_FREQUENCY_DENSITY

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the density of PTRS in frequency domain. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to RFMXNR_VAL_PUSCH_PTRS_ENABLED_TRUE and RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED attribute to RFMXNR_VAL_PUSCH_PTRS_ENABLED_FALSE. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is 2. Get Function: RFmxNR_GetPUSCHPTRSFrequencyDensity Set Function: RFmxNR_SetPUSCHPTRSFrequencyDensity |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pusch_ptrs_power.html language=enus -->
## TOPIC 00179: RFMXNR_ATTR_PUSCH_PTRS_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pusch_ptrs_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pusch_ptrs_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PUSCH_PTRS_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the factor by which the PUSCH PTRS REs are boosted. This value is expressed in dB. This attribute is valid only if you set the RFMXNR_ATTR_PUSCH_PTRS_ENABLED attribute to RFMXNR_VAL_PUSCH_PTRS_ENABLED_TRUE. Use 'pusch(r)' or 'user(l)' or 'bwp(m)' or 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)/bwp(m)/user(l)/pusch(r)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetPUSCHPTRSPower Set Function: RFmxNR_SetPUSCHPTRSPower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pvt_averaging_type.html language=enus -->
## TOPIC 00180: RFMXNR_ATTR_PVT_AVERAGING_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pvt_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pvt_averaging_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PVT_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the measurement averaging type. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_PVT_AVERAGING_TYPE_RMS. Get Function: RFmxNR_PVTGetAveragingType Set Function: RFmxNR_PVTSetAveragingType |
| Values: | RFMXNR_VAL_PVT_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RFMXNR_VAL_PVT_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. |
| RFMXNR_VAL_PVT_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. |
| RFMXNR_VAL_PVT_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pvt_measurement_enabled.html language=enus -->
## TOPIC 00181: RFMXNR_ATTR_PVT_MEASUREMENT_ENABLED

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pvt_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pvt_measurement_enabled.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PVT_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether to enable the PVT measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_FALSE. Get Function: RFmxNR_PVTGetMeasurementEnabled Set Function: RFmxNR_PVTSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pvt_off_power_exclusion_before.html language=enus -->
## TOPIC 00182: RFMXNR_ATTR_PVT_OFF_POWER_EXCLUSION_BEFORE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pvt_off_power_exclusion_before.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pvt_off_power_exclusion_before.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PVT_OFF_POWER_EXCLUSION_BEFORE

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the time excluded from the OFF region before the burst and at the beginning for uplink and downlink, respectively. The value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Refer to measurement guidelines details in the NR Power Vs Time concept help for more information. Get Function: RFmxNR_PVTGetOFFPowerExclusionBefore Set Function: RFmxNR_PVTSetOFFPowerExclusionBefore |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pvt_results_absolute_off_power_after.html language=enus -->
## TOPIC 00183: RFMXNR_ATTR_PVT_RESULTS_ABSOLUTE_OFF_POWER_AFTER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pvt_results_absolute_off_power_after.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pvt_results_absolute_off_power_after.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PVT_RESULTS_ABSOLUTE_OFF_POWER_AFTER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the OFF power in the segment after the captured burst for the uplink direction, while it returns NaN in the segment after the captured burst for the downlink direction. The segment is defined as one slot after the burst and a short transient segment. This value is expressed in dBm. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. The default value is 0. Get Function: RFmxNR_PVTGetResultsAbsoluteOFFPowerAfter |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pvt_results_absolute_off_power_before.html language=enus -->
## TOPIC 00184: RFMXNR_ATTR_PVT_RESULTS_ABSOLUTE_OFF_POWER_BEFORE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pvt_results_absolute_off_power_before.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pvt_results_absolute_off_power_before.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PVT_RESULTS_ABSOLUTE_OFF_POWER_BEFORE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the OFF power in the segment before the captured burst for the uplink direction, while it returns NaN in the segment after the captured burst for the downlink direction. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. The default value is 0. Get Function: RFmxNR_PVTGetResultsAbsoluteOFFPowerBefore |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pvt_results_absolute_on_power.html language=enus -->
## TOPIC 00185: RFMXNR_ATTR_PVT_RESULTS_ABSOLUTE_ON_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pvt_results_absolute_on_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pvt_results_absolute_on_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PVT_RESULTS_ABSOLUTE_ON_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the average ON power within the measurement interval. This value is expressed in dBm. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. The default value is 0. Get Function: RFmxNR_PVTGetResultsAbsoluteONPower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pvt_results_burst_width.html language=enus -->
## TOPIC 00186: RFMXNR_ATTR_PVT_RESULTS_BURST_WIDTH

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pvt_results_burst_width.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pvt_results_burst_width.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PVT_RESULTS_BURST_WIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the width of the captured burst for the uplink direction, while it returns NaN of the captured burst for the downlink direction. This value is expressed in seconds. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this result. The default value is 0. Get Function: RFmxNR_PVTGetResultsBurstWidth |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_pvt_results_measurement_status.html language=enus -->
## TOPIC 00187: RFMXNR_ATTR_PVT_RESULTS_MEASUREMENT_STATUS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_pvt_results_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_pvt_results_measurement_status.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_PVT_RESULTS_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeI32 |
| Description: | Returns the measurement status indicating whether the off power before and after is within the standard defined limit. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to read this attribute. The default value is 0. Get Function: RFmxNR_PVTGetResultsMeasurementStatus |
| Values: | RFMXNR_VAL_PVT_MEASUREMENT_STATUS_FAIL (0)Indicates that the measurement has failed. RFMXNR_VAL_PVT_MEASUREMENT_STATUS_PASS (1)Indicates that the measurement has passed. |
| RFMXNR_VAL_PVT_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |
| RFMXNR_VAL_PVT_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_rated_trp.html language=enus -->
## TOPIC 00188: RFMXNR_ATTR_RATED_TRP

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_rated_trp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_rated_trp.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_RATED_TRP

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the rated carrier TRP output power. This value is expressed in dBm. Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetRatedTRP Set Function: RFmxNR_SetRatedTRP |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_reference_grid_alignment_mode.html language=enus -->
## TOPIC 00189: RFMXNR_ATTR_REFERENCE_GRID_ALIGNMENT_MODE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_reference_grid_alignment_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_reference_grid_alignment_mode.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_REFERENCE_GRID_ALIGNMENT_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether to align the bandwidthparts and the SSB in a component carrier to a reference resource grid automatically or manually. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for the named signals. The default value is RFMXNR_VAL_REFERENCE_GRID_ALIGNMENT_MODE_AUTO. Get Function: RFmxNR_GetReferenceGridAlignmentMode Set Function: RFmxNR_SetReferenceGridAlignmentMode |
| Values: | RFMXNR_VAL_REFERENCE_GRID_ALIGNMENT_MODE_MANUAL (0)The subcarrier spacing of the reference resource grid and the grid start of each bandwidthpart is user specified. Center of subcarrier 0 in common resource block 0 of the reference resource grid is considered as Reference Point A. RFMXNR_VAL_REFERENCE_GRID_ALIGNMENT_MODE_AUTO (1)The subcarrier spacing of the reference resource grid is determined by the largest subcarrier spacing among the configured bandwidthparts and the SSB. The grid start of each bandwidthpart and the SSB is computed by minimizing k0 to {0, +6} subcarriers. |
| RFMXNR_VAL_REFERENCE_GRID_ALIGNMENT_MODE_MANUAL (0) | The subcarrier spacing of the reference resource grid and the grid start of each bandwidthpart is user specified. Center of subcarrier 0 in common resource block 0 of the reference resource grid is considered as Reference Point A. |
| RFMXNR_VAL_REFERENCE_GRID_ALIGNMENT_MODE_AUTO (1) | The subcarrier spacing of the reference resource grid is determined by the largest subcarrier spacing among the configured bandwidthparts and the SSB. The grid start of each bandwidthpart and the SSB is computed by minimizing k0 to {0, +6} subcarriers. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_sem_subblock_aggregated_channel_bandwidth.html language=enus -->
## TOPIC 00190: RFMXNR_ATTR_SEM_SUBBLOCK_AGGREGATED_CHANNEL_BANDWIDTH

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_sem_subblock_aggregated_channel_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_sem_subblock_aggregated_channel_bandwidth.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_SEM_SUBBLOCK_AGGREGATED_CHANNEL_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth. Use 'subblock(n)' as the Selector Strings to read this result. The default value is 0. Get Function: RFmxNR_SEMGetSubblockAggregatedChannelBandwidth |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_sem_subblock_integration_bandwidth.html language=enus -->
## TOPIC 00191: RFMXNR_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_sem_subblock_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_sem_subblock_integration_bandwidth.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. Use 'subblock(n)' as the Selector Strings to read this result. The default value is 0. Get Function: RFmxNR_SEMGetSubblockIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_sem_sweep_time_auto.html language=enus -->
## TOPIC 00192: RFMXNR_ATTR_SEM_SWEEP_TIME_AUTO

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_sem_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_sem_sweep_time_auto.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_SEM_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies whether the measurement sets the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_SEM_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxNR_SEMGetSweepTimeAuto Set Function: RFmxNR_SEMSetSweepTimeAuto |
| Values: | RFMXNR_VAL_SEM_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the sweep time that you specify in the RFMXNR_ATTR_SEM_SWEEP_TIME_INTERVAL attribute. RFMXNR_VAL_SEM_SWEEP_TIME_AUTO_TRUE (1)The measurement uses a sweep time of 1 ms. |
| RFMXNR_VAL_SEM_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the RFMXNR_ATTR_SEM_SWEEP_TIME_INTERVAL attribute. |
| RFMXNR_VAL_SEM_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses a sweep time of 1 ms. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_ssb_subcarrier_offset.html language=enus -->
## TOPIC 00193: RFMXNR_ATTR_SSB_SUBCARRIER_OFFSET

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_ssb_subcarrier_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_ssb_subcarrier_offset.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_SSB_SUBCARRIER_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies an additional subcarrier offset for the SS/PBCH block in units of resource blocks of 15 kHz or subcarrier spacing given by SSB Subcarrier Common attribute for frequency range 1 and frequency range 2 respectively. Use 'carrier(k)' or 'subblock(n)carrier(k)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetSSBSubcarrierOffset Set Function: RFmxNR_SetSSBSubcarrierOffset |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_sss_power.html language=enus -->
## TOPIC 00194: RFMXNR_ATTR_SSS_POWER

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_sss_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_sss_power.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_SSS_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB. Use 'carrier(k)' or 'subblock(n)carrier(k)' as the Selector Strings to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetSSSPower Set Function: RFmxNR_SetSSSPower |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_sub_band_allocation.html language=enus -->
## TOPIC 00195: RFMXNR_ATTR_SUB_BAND_ALLOCATION

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_sub_band_allocation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_sub_band_allocation.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_SUB_BAND_ALLOCATION

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeStringRFmxNR_GetAttributeString |
| Description: | Specifies the sub-band allocation in the NR-U wideband channel. Sub-band is the set of RBs with approximately 20 MHz bandwidth, where the wideband channel is uniformly divided into an integer number of 20 MHz sub-bands.This attribute is valid only for the bands n46, n96, n102 as defined in the 3GPP TS 37.213 for the shared spectrum channel access.The format is defined by range format specifiers. The range format specifier is a comma separated list of entries in the following format:Single unsigned integer values or lastA range of single unsigned integer values given as i0:i1, where i0 represents the first and i1 the last value in the range, with i0 (= i1. The keyword last expands to the largest allowed value, depending on the context of the range specification.Examples: 0,2 will expand to {0,2}0:2,3 will expand to {0,1,2,3}.Use 'carrier(k)' or 'subblock(n)' or 'subblock(n)/carrier(k)' as the Selector Strings to configure or read this attribute. The default value is 0-Last, whereLast = 0 for 20 MHz 1 for 40 MHz 2 for 60 MHz 3 for 80 MHz 4 for 100 MHz Get Function: RFmxNR_GetSubBandAllocation Set Function: RFmxNR_SetSubBandAllocation |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_subblock_transmit_lo_frequency.html language=enus -->
## TOPIC 00196: RFMXNR_ATTR_SUBBLOCK_TRANSMIT_LO_FREQUENCY

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_subblock_transmit_lo_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_subblock_transmit_lo_frequency.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_SUBBLOCK_TRANSMIT_LO_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the frequency of the transmitters local oscillator. This value is expressed in Hz. The frequency is defined per subblock and relative to the respective subblock center frequency. Use 'subblock(n)' as the Selector String to configure or read this attribute. The default value is 0. Get Function: RFmxNR_GetSubblockTransmitLOFrequency Set Function: RFmxNR_SetSubblockTransmitLOFrequency |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_subcarrier_spacing_common.html language=enus -->
## TOPIC 00197: RFMXNR_ATTR_SUBCARRIER_SPACING_COMMON

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_subcarrier_spacing_common.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_subcarrier_spacing_common.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_SUBCARRIER_SPACING_COMMON

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeF64RFmxNR_GetAttributeF64 |
| Description: | Specifies the basic unit of RFMXNR_ATTR_SSB_SUBCARRIER_OFFSET attribute for frequency range 2. The attribute refers to the MIB control element subCarrierSpacingCommon in 3GPP TS 38.331. Use 'carrier(k)' or 'subblock(n)carrier(k)' as the Selector Strings to configure or read this attribute. The default value is 60kHz. Get Function: RFmxNR_GetSubcarrierSpacingCommon Set Function: RFmxNR_SetSubcarrierSpacingCommon |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_trigger_type.html language=enus -->
## TOPIC 00198: RFMXNR_ATTR_TRIGGER_TYPE

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_trigger_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_trigger_type.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_TRIGGER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the type of trigger to be used for signal acquisition. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXNR_VAL_TRIGGER_TYPE_NONE. Get Function: RFmxNR_GetTriggerType Set Function: RFmxNR_SetTriggerType |
| Values: | RFMXNR_VAL_TRIGGER_TYPE_NONE (0)No Reference Trigger is configured. RFMXNR_VAL_TRIGGER_TYPE_DIGITAL_EDGE (1)The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXNR_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. RFMXNR_VAL_TRIGGER_TYPE_IQ_POWER_EDGE (2)The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. RFMXNR_VAL_TRIGGER_TYPE_SOFTWARE (3)The Reference Trigger is not asserted until a software trigger occurs. |
| RFMXNR_VAL_TRIGGER_TYPE_NONE (0) | No Reference Trigger is configured. |
| RFMXNR_VAL_TRIGGER_TYPE_DIGITAL_EDGE (1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXNR_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. |
| RFMXNR_VAL_TRIGGER_TYPE_IQ_POWER_EDGE (2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. |
| RFMXNR_VAL_TRIGGER_TYPE_SOFTWARE (3) | The Reference Trigger is not asserted until a software trigger occurs. |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_txp_number_of_analysis_threads.html language=enus -->
## TOPIC 00199: RFMXNR_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_txp_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_txp_number_of_analysis_threads.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxNR_SetAttributeI32RFmxNR_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism inside TXP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The number of threads must range from 1 to the number of physical cores. The default value is 1. The number of threads set used in calculations is not guaranteed. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Get Function: RFmxNR_TXPGetNumberOfAnalysisThreads Set Function: RFmxNR_TXPSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_txp_results_average_power_mean.html language=enus -->
## TOPIC 00200: RFMXNR_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_txp_results_average_power_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_txp_results_average_power_mean.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the average power of the acquired signal. When you set the RFMXNR_ATTR_TXP_AVERAGING_ENABLED to RFMXNR_VAL_TXP_AVERAGING_ENABLED_TRUE, it returns the max of the peak power computed for each averaging count. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is dBm. Get Function: RFmxNR_TXPGetResultsAveragePowerMean |

<!--NI_TOPIC bundle=rfmx-nr-cvi path=rfmxnr_attr_txp_results_peak_power_maximum.html language=enus -->
## TOPIC 00201: RFMXNR_ATTR_TXP_RESULTS_PEAK_POWER_MAXIMUM

- bundle_id: `rfmx-nr-cvi`
- source_path: `rfmxnr_attr_txp_results_peak_power_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-cvi/raw/resource/enus/rfmxnr_attr_txp_results_peak_power_maximum.html
- document_id: `rfmx-nr-cvi`
- page_type: `leaf`
- content_type: ``

RFMXNR_ATTR_TXP_RESULTS_PEAK_POWER_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxNR_GetAttributeF64 |
| Description: | Returns the peak power of the acquired signal. When you set the RFMXNR_ATTR_TXP_AVERAGING_ENABLED to RFMXNR_VAL_TXP_AVERAGING_ENABLED_TRUE, it returns the mean of the average power computed for each averaging count. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is dBm. Get Function: RFmxNR_TXPGetResultsPeakPowerMaximum |
