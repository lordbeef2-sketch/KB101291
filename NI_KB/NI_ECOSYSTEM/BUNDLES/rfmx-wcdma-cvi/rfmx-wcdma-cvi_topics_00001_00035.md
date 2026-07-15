# NI DOCUMENT BUNDLE: rfmx-wcdma-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-wcdma-cvi start=1 end=35 -->
<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_acpfetchtotalcarrierpower.html language=enus -->
## TOPIC 00001: RFmxWCDMA_ACPFetchTotalCarrierPower

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_acpfetchtotalcarrierpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_acpfetchtotalcarrierpower.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_ACPFetchTotalCarrierPower

int32 __stdcall RFmxWCDMA_ACPFetchTotalCarrierPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* totalCarrierPower);

#### Purpose

Fetches the total carrier power for the ACP measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| totalCarrierPower | float64* | Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER attribute. This value is expressed in dBm. For a single-carrier measurement, total carrier power is the same as carrier absolute power. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_analyzeiq1waveform.html language=enus -->
## TOPIC 00002: RFmxWCDMA_AnalyzeIQ1Waveform

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_analyzeiq1waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_analyzeiq1waveform.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_AnalyzeIQ1Waveform

int32 __stdcall RFmxWCDMA_AnalyzeIQ1Waveform (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[],
 float64 x0,
 float64 dx,
 NIComplexSingle IQ[],
 int32 arraySize,
 int32 reset,
 int64 reserved);

#### Purpose

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes.
Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?topicname=rfmxinstrcvi/rfmxinstr_attr_recommended_acquisition_type.html) attribute value is either **IQ** or **IQorSpectral**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| x0 | float64 | Specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | float64 | Specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| IQ | NIComplexSingle[] | Specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | int32 | Specifies the size of the array. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_analyzeiq1waveformsplit.html language=enus -->
## TOPIC 00003: RFmxWCDMA_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_analyzeiq1waveformsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_analyzeiq1waveformsplit.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_AnalyzeIQ1WaveformSplit

int32 __stdcall RFmxWCDMA_AnalyzeIQ1WaveformSplit (niRFmxInstrHandle instrumentHandle,
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

Performs the enabled measurements on the I/Q complex waveform that you specify in **I** and **Q** parameters. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes.
 Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?topicname=rfmxinstrcvi/rfmxinstr_attr_recommended_acquisition_type.html) attribute value is either **IQ** or **IQorSpectral**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| x0 | float64 | Specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | float64 | Specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| I | float32[] | Specifies the real part of an array of complex-valued time domain data. The real part of this complex data array correspond to the in-phase (I) data. |
| Q | float32[] | Specifies the imaginary part of an array of complex-valued time domain data. The imaginary part of this complex data array correspond to the quadrature-phase (Q) data. |
| arraySize | int32 | Specifies the size of the array. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_autolevel.html language=enus -->
## TOPIC 00004: RFmxWCDMA_AutoLevel

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_autolevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_autolevel.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_AutoLevel

int32 __stdcall RFmxWCDMA_AutoLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 measurementInterval,
 float64* referenceLevel);

#### Purpose

Examines the input signal to calculate the peak power level and sets it as the value of the [RFMXWCDMA_ATTR_REFERENCE_LEVEL](/csh?topicname=rfmxwcdmacvi/rfmxwcdma_attr_reference_level.html) attribute. Use this function to help calculate an approximate setting for the reference level. 


 
The RFmxWCDMA Auto Level function completes the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device, based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the [RFMXWCDMA_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL](/csh?topicname=rfmxwcdmacvi/rfmxwcdma_attr_auto_level_initial_reference_level.html) attribute. 
When using PXIe-5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxWCDMA Auto Level function. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| measurementInterval | float64 | Specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| Output |  |  |
| Name | Type | Description |
| referenceLevel | float64* | Returns the reference level that represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_buildchannelstring.html language=enus -->
## TOPIC 00005: RFmxWCDMA_BuildChannelString

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_buildchannelstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_buildchannelstring.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_BuildChannelString

int32 __stdcall RFmxWCDMA_BuildChannelString (char selectorString[],
 int32 channelNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the channel string to use as the selector string with the channel configuration and results.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| channelNumber | int32 | Specifies the channel number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string that can be passed to the selectorString parameter of Fetch functions. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_buildoffsetstring.html language=enus -->
## TOPIC 00006: RFmxWCDMA_BuildOffsetString

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_buildoffsetstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_buildoffsetstring.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_BuildOffsetString

int32 __stdcall RFmxWCDMA_BuildOffsetString (char selectorString[],
 int32 offsetNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the offset string to use as the selector string with the SEM and ACP offset configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| offsetNumber | int32 | Specifies the offset number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string that can be passed to the selectorString parameter of Fetch functions. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_buildsignalstring.html language=enus -->
## TOPIC 00007: RFmxWCDMA_BuildSignalString

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_buildsignalstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_buildsignalstring.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_BuildSignalString

int32 __stdcall RFmxWCDMA_BuildSignalString (char signalName[],
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
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_cdacfgmeasurementchannel.html language=enus -->
## TOPIC 00008: RFmxWCDMA_CDACfgMeasurementChannel

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_cdacfgmeasurementchannel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_cdacfgmeasurementchannel.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_CDACfgMeasurementChannel

int32 __stdcall RFmxWCDMA_CDACfgMeasurementChannel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 spreadingFactor,
 int32 spreadingCode,
 int32 modulationType,
 int32 branch);

#### Purpose

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| spreadingFactor | int32 | Specifies the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| spreadingCode | int32 | Specifies the spreading code of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| modulationType | int32 | Specifies the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |
| branch | int32 | Specifies the branch of the measurement channel. This value is used to compute the symbol results of the CDA measurement. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_cdacfgpowerunit.html language=enus -->
## TOPIC 00009: RFmxWCDMA_CDACfgPowerUnit

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_cdacfgpowerunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_cdacfgpowerunit.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_CDACfgPowerUnit

int32 __stdcall RFmxWCDMA_CDACfgPowerUnit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 powerUnit);

#### Purpose

Configures the power unit for all code domain power results, except Total Power (dBm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| powerUnit | int32 | Specifies the measurement unit of all power results, except, RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER. RFMXWCDMA_VAL_CDA_POWER_UNIT_DB (0) Specifies the power relative to the total power.RFMXWCDMA_VAL_CDA_POWER_UNIT_DBM (1) Specifies the absolute power measured. |
| RFMXWCDMA_VAL_CDA_POWER_UNIT_DB (0) | Specifies the power relative to the total power. |  |
| RFMXWCDMA_VAL_CDA_POWER_UNIT_DBM (1) | Specifies the absolute power measured. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_cdafetchsymbolmagnitudeerrortrace.html language=enus -->
## TOPIC 00010: RFmxWCDMA_CDAFetchSymbolMagnitudeErrorTrace

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_cdafetchsymbolmagnitudeerrortrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_cdafetchsymbolmagnitudeerrortrace.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_CDAFetchSymbolMagnitudeErrorTrace

int32 __stdcall RFmxWCDMA_CDAFetchSymbolMagnitudeErrorTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 symbolMagnitudeError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the magnitude error trace of the measurement channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| symbolMagnitudeError | float32[] | Returns an array of magnitude errors of the symbols of the measurement channel. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_cdafetchsymbolphaseerrortrace.html language=enus -->
## TOPIC 00011: RFmxWCDMA_CDAFetchSymbolPhaseErrorTrace

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_cdafetchsymbolphaseerrortrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_cdafetchsymbolphaseerrortrace.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_CDAFetchSymbolPhaseErrorTrace

int32 __stdcall RFmxWCDMA_CDAFetchSymbolPhaseErrorTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 symbolPhaseError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the phase error trace of the measurement channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| symbolPhaseError | float32[] | Returns an array of phase errors of the symbols of the measurement channel. This value is expressed in degrees. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_cdafetchsymbolpowertrace.html language=enus -->
## TOPIC 00012: RFmxWCDMA_CDAFetchSymbolPowerTrace

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_cdafetchsymbolpowertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_cdafetchsymbolpowertrace.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_CDAFetchSymbolPowerTrace

int32 __stdcall RFmxWCDMA_CDAFetchSymbolPowerTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 symbolPowers[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the power versus time trace of the symbol corresponding to the measurement channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| symbolPowers | float32[] | Returns the array of symbol powers of the measurement channel. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_modacccfgreferencewaveform.html language=enus -->
## TOPIC 00013: RFmxWCDMA_ModAccCfgReferenceWaveform

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_modacccfgreferencewaveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_modacccfgreferencewaveform.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_ModAccCfgReferenceWaveform

int32 __stdcall RFmxWCDMA_ModAccCfgReferenceWaveform (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 x0,
 float64 dx,
 NIComplexSingle referenceWaveform[],
 int32 arraySize);

#### Purpose

Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster
ModAcc measurements. 
This function is used only when you set the [RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE](/csh?topicname=rfmxwcdmacvi/rfmxwcdma_attr_modacc_synchronization_mode.html) attribute to RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_MARKER.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| x0 | float64 | Specifies the start time. This value is expressed in seconds. |
| dx | float64 | Specifies the sample duration. This value is expressed in seconds. |
| referenceWaveform | NIComplexSingle[] | Specifies an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_modacccfgreferencewaveformsplit.html language=enus -->
## TOPIC 00014: RFmxWCDMA_ModAccCfgReferenceWaveformSplit

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_modacccfgreferencewaveformsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_modacccfgreferencewaveformsplit.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_ModAccCfgReferenceWaveformSplit

int32 __stdcall RFmxWCDMA_ModAccCfgReferenceWaveformSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 x0,
 float64 dx,
 float32 I[],
 float32 Q[],
 int32 arraySize);

#### Purpose

Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster
 ModAcc measurements. 
This function is used only when you set the [RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE](/csh?topicname=rfmxwcdmacvi/rfmxwcdma_attr_modacc_synchronization_mode.html) attribute to RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_MARKER.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| x0 | float64 | Specifies the start time. This value is expressed in seconds. |
| dx | float64 | Specifies the sample duration. This value is expressed in seconds. |
| I | float32[] | Specifies the real part of an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
| Q | float32[] | Specifies the imaginary part of an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_modacccfgsynchronizationmodeandinterval.html language=enus -->
## TOPIC 00015: RFmxWCDMA_ModAccCfgSynchronizationModeAndInterval

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_modacccfgsynchronizationmodeandinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_modacccfgsynchronizationmodeandinterval.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_ModAccCfgSynchronizationModeAndInterval

int32 __stdcall RFmxWCDMA_ModAccCfgSynchronizationModeAndInterval (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 synchronizationMode,
 int32 measurementOffset,
 int32 measurementLength);

#### Purpose

Configures the synchronization mode, measurement offset, and measurement length of the ModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| synchronizationMode | int32 | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME (0) The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the frame boundary. RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT (1) The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the slot boundary. RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY (2) The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the symbol boundary. RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_MARKER (3) The measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the Trigger. This is the fastest way to do a ModAcc measurement. This mode requires the RFMXWCDMA_ATTR_TRIGGER_TYPE attribute to be set to digital and the trigger must occur at the start of the frame. For more information about Marker mode, refer to Marker Mode. |
| RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the frame boundary. |  |
| RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the slot boundary. |  |
| RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY (2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the symbol boundary. |  |
| RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_MARKER (3) | The measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the Trigger. This is the fastest way to do a ModAcc measurement. This mode requires the RFMXWCDMA_ATTR_TRIGGER_TYPE attribute to be set to digital and the trigger must occur at the start of the frame. For more information about Marker mode, refer to Marker Mode. |  |
| measurementOffset | int32 | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the synchronizationMode parameter. Valid values are [0, (15 - ModAcc Measurement Length)]. The sum of the ModAcc measurement offset and ModAcc measurement length must be less than or equal to 15. |
| measurementLength | int32 | Specifies the duration for the modulation accuracy measurement. This value is expressed in slots. Valid values are [1,(15 - ModAcc Measurement Offset)]. The sum of the ModAcc measurement offset and ModAcc measurement length must be less than or equal to 15. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_modaccfetchconstellationtrace.html language=enus -->
## TOPIC 00016: RFmxWCDMA_ModAccFetchConstellationTrace

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_modaccfetchconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_modaccfetchconstellationtrace.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_ModAccFetchConstellationTrace

int32 __stdcall RFmxWCDMA_ModAccFetchConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle constellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement. 
Use "carrier<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| constellation | NIComplexSingle[] | Returns an array of complex chips of the corrected signal of a carrier on which the ModAcc measurements are done. You can use these chips to obtain the constellation diagram. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_modaccfetchmulticarrieriqimpairments.html language=enus -->
## TOPIC 00017: RFmxWCDMA_ModAccFetchMulticarrierIQImpairments

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_modaccfetchmulticarrieriqimpairments.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_modaccfetchmulticarrieriqimpairments.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_ModAccFetchMulticarrierIQImpairments

int32 __stdcall RFmxWCDMA_ModAccFetchMulticarrierIQImpairments (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* multicarrierIQOriginOffset,
 float64* multicarrierIQGainImbalance,
 float64* multicarrierIQQuadratureError);

#### Purpose

Fetches the I/Q impairments for a multicarrier signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| multicarrierIQOriginOffset | float64* | Returns the estimated I/Q origin offset of the multicarrier signal when the RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE attribute is set to RFMXWCDMA_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_BAND. This value is expressed in dB. This result is useful when the LO is at the center of the multicarrier signal. |
| multicarrierIQGainImbalance | float64* | Returns NaN. This parameter has been added for future use. |
| multicarrierIQQuadratureError | float64* | Returns NaN. This parameter has been added for future use. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_modaccfetchnumberofdetectedchannels.html language=enus -->
## TOPIC 00018: RFmxWCDMA_ModAccFetchNumberOfDetectedChannels

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_modaccfetchnumberofdetectedchannels.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_modaccfetchnumberofdetectedchannels.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_ModAccFetchNumberOfDetectedChannels

int32 __stdcall RFmxWCDMA_ModAccFetchNumberOfDetectedChannels (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* numberOfDetectedChannels);

#### Purpose

Fetches the number of detected channels in a carrier for the ModAcc measurement. 
Use "carrier<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| numberOfDetectedChannels | int32* | Returns the number of detected channels when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT. If you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED or RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_TEST_MODEL, this parameter returns the number of configured channels. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_modaccfetchnumberofdetectedchannelsarray.html language=enus -->
## TOPIC 00019: RFmxWCDMA_ModAccFetchNumberOfDetectedChannelsArray

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_modaccfetchnumberofdetectedchannelsarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_modaccfetchnumberofdetectedchannelsarray.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_ModAccFetchNumberOfDetectedChannelsArray

int32 __stdcall RFmxWCDMA_ModAccFetchNumberOfDetectedChannelsArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 numberofDetectedChannels[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches an array of number of detected channels of all the carriers in the ModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| numberofDetectedChannels | int32[] | Returns the array of the number of detected channels when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to Auto Detect. If you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED or RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_TEST_MODEL, this parameter returns the array of the number of configured channels. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_modaccfetchpeakactivecde.html language=enus -->
## TOPIC 00020: RFmxWCDMA_ModAccFetchPeakActiveCDE

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_modaccfetchpeakactivecde.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_modaccfetchpeakactivecde.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_ModAccFetchPeakActiveCDE

int32 __stdcall RFmxWCDMA_ModAccFetchPeakActiveCDE (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* peakActiveCDE,
 int32* peakActiveCDESpreadingFactor,
 int32* peakActiveCDECode,
 int32* peakActiveCDEBranch);

#### Purpose

Fetches the peak value among the code domain errors (CDEs) of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement. 
Use "carrier<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| peakActiveCDE | float64* | Returns the maximum value among the active code domain errors for a carrier. This value is expressed in dB. The active CDEs are computed by despreading the descrambled error vectors corresponding to each active channel with the appropriate active channel codes. The active CDE is defined as the ratio of the mean power of this despread error vector to the mean power of the composite reference waveform. |
| peakActiveCDESpreadingFactor | int32* | Returns the spreading factor of the channel corresponding to the value of the peakActiveCDE parameter for a carrier. |
| peakActiveCDECode | int32* | Returns the spreading code of the channel corresponding to the value of the peakActiveCDE parameter for a carrier. |
| peakActiveCDEBranch | int32* | Returns the branch of the channel corresponding to the value of the peakActiveCDE parameter for a carrier. RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I (0) Signal is modulated on the in-phase branch. RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q (1) Signal is modulated on the quadrature branch. |
| RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I (0) | Signal is modulated on the in-phase branch. |  |
| RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q (1) | Signal is modulated on the quadrature branch. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=cvirfmxwcdma_modaccfetchpeakactivecdearray.html language=enus -->
## TOPIC 00021: RFmxWCDMA_ModAccFetchPeakActiveCDEArray

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `cvirfmxwcdma_modaccfetchpeakactivecdearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/cvirfmxwcdma_modaccfetchpeakactivecdearray.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA_ModAccFetchPeakActiveCDEArray

int32 __stdcall RFmxWCDMA_ModAccFetchPeakActiveCDEArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 peakActiveCDE[],
 int32 peakActiveCDESpreadingFactor[],
 int32 peakActiveCDECode[],
 int32 peakActiveCDEBranch[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches arrays of peak CDE values among all the active channels of a carrier, and the corresponding code numbers, spreading factors, and branches of the carriers. Each element in these arrays corresponds to the peak value among the code domain errors of all the active channels in each carrier.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| peakActiveCDE | float64[] | Returns array of maximum values among the active code domain errors. This value is expressed in dB. The active CDEs are computed by despreading the descrambled error vectors corresponding to each active channel with the appropriate active channel codes. The active CDE is defined as the ratio of the mean power of this despread error vector to the mean power of the composite reference waveform. |
| peakActiveCDESpreadingFactor | int32[] | Returns the array of spreading factors of the channel corresponding to the value of the peakActiveCDE parameter. |
| peakActiveCDECode | int32[] | Returns the array of spreading codes of the channel corresponding to the value of the peakActiveCDE parameter. |
| peakActiveCDEBranch | int32[] | Returns the array of branch values of the channel corresponding to the value of the peakActiveCDE parameter. RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I (0) Signal is modulated on the in-phase branch. RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q (1) Signal is modulated on the quadrature branch. |
| RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I (0) | Signal is modulated on the in-phase branch. |  |
| RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q (1) | Signal is modulated on the quadrature branch. |  |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_cda_synchronization_mode.html language=enus -->
## TOPIC 00022: RFMXWCDMA_ATTR_CDA_SYNCHRONIZATION_MODE

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_cda_synchronization_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_cda_synchronization_mode.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_CDA_SYNCHRONIZATION_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWCDMA_SetAttributeI32RFmxWCDMA_GetAttributeI32 |
| Description: | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_SLOT. Get Function: RFmxWCDMA_CDAGetSynchronizationMode Set Function: RFmxWCDMA_CDASetSynchronizationMode |
| Values: | RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_FRAME (0)The frame boundary is detected and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH attribute, starting at RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET slots from the frame boundary. RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_SLOT (1)The slot boundary is detected and the measurement is performed over the number of slots expressed by RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH attribute, starting at RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET slots from the slot boundary. RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY (2)The symbol boundary is detected and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH attribute, starting at RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET slots from the symbol boundary. |
| RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary is detected and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH attribute, starting at RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET slots from the frame boundary. |
| RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH attribute, starting at RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET slots from the slot boundary. |
| RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY (2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH attribute, starting at RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET slots from the symbol boundary. |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_channel_configuration_mode.html language=enus -->
## TOPIC 00023: RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_channel_configuration_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_channel_configuration_mode.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWCDMA_SetAttributeI32RFmxWCDMA_GetAttributeI32 |
| Description: | Specifies the channel configuration mode. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT. Get Function: RFmxWCDMA_GetChannelConfigurationMode Set Function: RFmxWCDMA_SetChannelConfigurationMode |
| Values: | RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT (0)The measurement detects the channels. RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED (1)Configure the channels using the RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS attribute and the RFmxWCDMA_CfgUserDefinedChannelArray function. RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_TEST_MODEL (2)Choose from the standard-defined channel configurations using the RFMXWCDMA_ATTR_UPLINK_TEST_MODEL attribute. |
| RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT (0) | The measurement detects the channels. |
| RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED (1) | Configure the channels using the RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS attribute and the RFmxWCDMA_CfgUserDefinedChannelArray function. |
| RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_TEST_MODEL (2) | Choose from the standard-defined channel configurations using the RFMXWCDMA_ATTR_UPLINK_TEST_MODEL attribute. |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_chp_results_total_carrier_power.html language=enus -->
## TOPIC 00024: RFMXWCDMA_ATTR_CHP_RESULTS_TOTAL_CARRIER_POWER

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_chp_results_total_carrier_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_chp_results_total_carrier_power.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_CHP_RESULTS_TOTAL_CARRIER_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWCDMA_GetAttributeF64 |
| Description: | Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the RFMXWCDMA_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER attribute. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxWCDMA_CHPGetResultsTotalCarrierPower |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_chp_sweep_time_auto.html language=enus -->
## TOPIC 00025: RFMXWCDMA_ATTR_CHP_SWEEP_TIME_AUTO

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_chp_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_chp_sweep_time_auto.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_CHP_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWCDMA_SetAttributeI32RFmxWCDMA_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxWCDMA_CHPGetSweepTimeAuto Set Function: RFmxWCDMA_CHPSetSweepTimeAuto |
| Values: | RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the sweep time that you specify in the RFMXWCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL attribute. RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_TRUE (1)The measurement uses a sweep time value of one slot duration. |
| RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the RFMXWCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL attribute. |
| RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses a sweep time value of one slot duration. |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_modacc_results_chip_rate_error.html language=enus -->
## TOPIC 00026: RFMXWCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_modacc_results_chip_rate_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_modacc_results_chip_rate_error.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWCDMA_GetAttributeF64 |
| Description: | Returns the chip rate error of the composite signal. This value is expressed in ppm. Use 'carrier(n)' as the selector string to read this attribute. Get Function: RFmxWCDMA_ModAccGetResultsChipRateError |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_modacc_results_detected_branch.html language=enus -->
## TOPIC 00027: RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_BRANCH

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_modacc_results_detected_branch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_modacc_results_detected_branch.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_BRANCH

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWCDMA_GetAttributeI32 |
| Description: | Returns the branch of the detected channel. If the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute is set to RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED or RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_TEST_MODEL, the RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_BRANCH attribute returns the branch of the configured channel of a carrier. Use 'carrier(n)/channel(k)' as the selector string to read this result. Get Function: RFmxWCDMA_ModAccGetResultsDetectedBranch |
| Values: | RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_I (0)The signal is modulated on the in-phase branch. RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_Q (1)The signal is modulated on the quadrature-phase branch. |
| RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_I (0) | The signal is modulated on the in-phase branch. |
| RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_Q (1) | The signal is modulated on the quadrature-phase branch. |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_modacc_results_detected_modulation_type.html language=enus -->
## TOPIC 00028: RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_MODULATION_TYPE

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_modacc_results_detected_modulation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_modacc_results_detected_modulation_type.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_MODULATION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWCDMA_GetAttributeI32 |
| Description: | Returns the modulation type of the detected channel. If the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute is set to RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED or RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_TEST_MODEL, the RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_MODULATION_TYPE attribute returns the modulation type of the configured channel of a carrier. Use 'carrier(n)/channel(k)' as the selector string to read this result. Get Function: RFmxWCDMA_ModAccGetResultsDetectedModulationType |
| Values: | RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_BPSK_QPSK (0)The modulation type is BPSK. RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_4PAM_16QAM (1)The modulation type is 4-PAM. |
| RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_BPSK_QPSK (0) | The modulation type is BPSK. |
| RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_4PAM_16QAM (1) | The modulation type is 4-PAM. |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_qevm_results_mean_rms_evm.html language=enus -->
## TOPIC 00029: RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_RMS_EVM

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_qevm_results_mean_rms_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_qevm_results_mean_rms_evm.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_RMS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWCDMA_GetAttributeF64 |
| Description: | Returns the mean of the RMS EVM values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWCDMA_QEVMGetResultsMeanRMSEVM |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_qevm_rrc_filter_enabled.html language=enus -->
## TOPIC 00030: RFMXWCDMA_ATTR_QEVM_RRC_FILTER_ENABLED

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_qevm_rrc_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_qevm_rrc_filter_enabled.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_QEVM_RRC_FILTER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWCDMA_SetAttributeI32RFmxWCDMA_GetAttributeI32 |
| Description: | Specifies whether to enable the RRC filter. Use this attribute to disable the filter if the received signal is already RRC-filtered. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWCDMA_VAL_QEVM_RRC_FILTER_ENABLED_TRUE. Get Function: RFmxWCDMA_QEVMGetRRCFilterEnabled Set Function: RFmxWCDMA_QEVMSetRRCFilterEnabled |
| Values: | RFMXWCDMA_VAL_QEVM_RRC_FILTER_ENABLED_FALSE (0)Disables the RRC filter in the measurement. RFMXWCDMA_VAL_QEVM_RRC_FILTER_ENABLED_TRUE (1)Enables the RRC filter in the measurement. |
| RFMXWCDMA_VAL_QEVM_RRC_FILTER_ENABLED_FALSE (0) | Disables the RRC filter in the measurement. |
| RFMXWCDMA_VAL_QEVM_RRC_FILTER_ENABLED_TRUE (1) | Enables the RRC filter in the measurement. |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_qevm_spectrum_inverted.html language=enus -->
## TOPIC 00031: RFMXWCDMA_ATTR_QEVM_SPECTRUM_INVERTED

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_qevm_spectrum_inverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_qevm_spectrum_inverted.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_QEVM_SPECTRUM_INVERTED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWCDMA_SetAttributeI32RFmxWCDMA_GetAttributeI32 |
| Description: | Specifies whether the spectrum of the signal is inverted. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWCDMA_VAL_QEVM_SPECTRUM_INVERTED_FALSE. Get Function: RFmxWCDMA_QEVMGetSpectrumInverted Set Function: RFmxWCDMA_QEVMSetSpectrumInverted |
| Values: | RFMXWCDMA_VAL_QEVM_SPECTRUM_INVERTED_FALSE (0)The spectrum is not inverted. RFMXWCDMA_VAL_QEVM_SPECTRUM_INVERTED_TRUE (1)The spectrum is inverted. |
| RFMXWCDMA_VAL_QEVM_SPECTRUM_INVERTED_FALSE (0) | The spectrum is not inverted. |
| RFMXWCDMA_VAL_QEVM_SPECTRUM_INVERTED_TRUE (1) | The spectrum is inverted. |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_result_fetch_timeout.html language=enus -->
## TOPIC 00032: RFMXWCDMA_ATTR_RESULT_FETCH_TIMEOUT

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_result_fetch_timeout.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_result_fetch_timeout.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_RESULT_FETCH_TIMEOUT

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWCDMA_SetAttributeF64RFmxWCDMA_GetAttributeF64 |
| Description: | Specifies the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxWCDMA_GetFetchTimeout Set Function: RFmxWCDMA_SetFetchTimeout |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_sem_offset_bandwidth_integral.html language=enus -->
## TOPIC 00033: RFMXWCDMA_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_sem_offset_bandwidth_integral.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_sem_offset_bandwidth_integral.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWCDMA_GetAttributeI32 |
| Description: | Returns the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW. Use 'offset(n)' as the selector string to read this attribute. If this attribute returns a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of the bandwidth integral and the RBW. Get Function: RFmxWCDMA_SEMGetOffsetBandwidthIntegral |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_sem_results_lower_offset_measurement_status.html language=enus -->
## TOPIC 00034: RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_sem_results_lower_offset_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_sem_results_lower_offset_measurement_status.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWCDMA_GetAttributeI32 |
| Description: | Indicates the measurement status based on the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxWCDMA_SEMGetResultsLowerOffsetMeasurementStatus |
| Values: | RFMXWCDMA_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL (0)Indicates that the value of the SEM Results Lower Offset Margin attribute is positive. RFMXWCDMA_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS (1)Indicates that the value of the SEM Results Lower Offset Margin attribute is zero or negative. |
| RFMXWCDMA_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL (0) | Indicates that the value of the SEM Results Lower Offset Margin attribute is positive. |
| RFMXWCDMA_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS (1) | Indicates that the value of the SEM Results Lower Offset Margin attribute is zero or negative. |

<!--NI_TOPIC bundle=rfmx-wcdma-cvi path=rfmxwcdma_attr_sem_results_lower_offset_peak_frequency.html language=enus -->
## TOPIC 00035: RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmx-wcdma-cvi`
- source_path: `rfmxwcdma_attr_sem_results_lower_offset_peak_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-cvi/raw/resource/enus/rfmxwcdma_attr_sem_results_lower_offset_peak_frequency.html
- document_id: `rfmx-wcdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWCDMA_GetAttributeF64 |
| Description: | Returns the frequency at which the peak power is observed in the lower offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxWCDMA_SEMGetResultsLowerOffsetPeakFrequency |
