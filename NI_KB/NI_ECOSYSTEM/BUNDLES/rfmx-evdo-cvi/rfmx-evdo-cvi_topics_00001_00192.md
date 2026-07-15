# NI DOCUMENT BUNDLE: rfmx-evdo-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-evdo-cvi start=1 end=192 -->
<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_acpcfgoffsetpowerreference.html language=enus -->
## TOPIC 00001: RFmxEVDO_ACPCfgOffsetPowerReference

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_acpcfgoffsetpowerreference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_acpcfgoffsetpowerreference.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_ACPCfgOffsetPowerReference

int32 __stdcall RFmxEVDO_ACPCfgOffsetPowerReference (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 offsetPowerReferenceCarrier,
 int32 offsetPowerReferenceSpecific);

#### Purpose

Configures the power reference of the offset channels in multi-carrier setups.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| offsetPowerReferenceCarrier | int32 | Specifies how the reference power is selected.RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_CLOSEST (0) The measurement uses the carrier power closest to the center frequency of the offset channel as the power reference. RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_HIGHEST (1) The measurement uses the highest measured active carrier power as the power reference.RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_COMPOSITE (2) The measurement uses total measured active carrier power as the power reference. RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_SPECIFIC (3) The measurement uses the power measured in the carrier with index specified by the offsetPowerReferenceSpecific attribute as the power reference. |
| RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_CLOSEST (0) | The measurement uses the carrier power closest to the center frequency of the offset channel as the power reference. |  |
| RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_HIGHEST (1) | The measurement uses the highest measured active carrier power as the power reference. |  |
| RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_COMPOSITE (2) | The measurement uses total measured active carrier power as the power reference. |  |
| RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_SPECIFIC (3) | The measurement uses the power measured in the carrier with index specified by the offsetPowerReferenceSpecific attribute as the power reference. |  |
| offsetPowerReferenceSpecific | int32 | Specifies the carrier number that is used as power reference. This parameter only applies if you set the offsetPowerReferenceCarrier parameter to offsetPowerReferenceSpecific. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_acpcfgsweeptime.html language=enus -->
## TOPIC 00002: RFmxEVDO_ACPCfgSweepTime

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_acpcfgsweeptime.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_acpcfgsweeptime.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_ACPCfgSweepTime

int32 __stdcall RFmxEVDO_ACPCfgSweepTime (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 sweepTimeAuto,
 float64 sweepTimeInterval);

#### Purpose

Configures the sweep time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| sweepTimeAuto | int32 | Specifies whether the measurement calculates the sweep time. RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_FALSE (0) The measurement uses the sweep time that you specify using the sweepTimeInterval parameter.RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_TRUE (1) The measurement uses the default sweep time of 1.67 ms. |
| RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify using the sweepTimeInterval parameter. |  |
| RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the default sweep time of 1.67 ms. |  |
| sweepTimeInterval | float64 | Specifies the sweep time when you set the sweepTimeAuto parameter to RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_analyzespectrum1waveform.html language=enus -->
## TOPIC 00003: RFmxEVDO_AnalyzeSpectrum1Waveform

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_analyzespectrum1waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_analyzespectrum1waveform.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_AnalyzeSpectrum1Waveform

int32 __stdcall RFmxEVDO_AnalyzeSpectrum1Waveform (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[],
 float64 x0,
 float64 dx,
 float32 spectrum[],
 int32 arraySize,
 int32 reset,
 int64 reserved);

#### Purpose

Performs the enabled measurements on the spectrum waveform that you specify in the **spectrum** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes.
Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?topicname=rfmxinstrcvi/rfmxinstr_attr_recommended_acquisition_type.html) attribute value is either **spectral** or **IQorSpectral**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: """result::r1""r1" |
| x0 | float64 | Specifies the start frequency of the spectrum. This value is expressed in Hz. |
| dx | float64 | Specifies the frequency interval between data points in the spectrum. |
| spectrum | float32[] | Contains the real-value power spectrum. |
| arraySize | int32 | Specifies the size of the array. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| Reserved | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_autolevel.html language=enus -->
## TOPIC 00004: RFmxEVDO_AutoLevel

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_autolevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_autolevel.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_AutoLevel

int32 __stdcall RFmxEVDO_AutoLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 measurementInterval,
 float64* referenceLevel);

#### Purpose

Examines the input signal to calculate the peak power level and sets it as the value of the [RFMXEVDO_ATTR_REFERENCE_LEVEL](/csh?topicname=rfmxevdocvi/rfmxevdo_attr_reference_level.html) attribute. Use this function to help calculate an approximate setting for the reference level. 


 
The RFmxEVDO Auto Level function completes the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device, based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

RFMXEVDO_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| measurementInterval | float64 | Specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the RF signal analyzer. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | float64* | Returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_buildchannelstring.html language=enus -->
## TOPIC 00005: RFmxEVDO_BuildChannelString

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_buildchannelstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_buildchannelstring.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_BuildChannelString

int32 __stdcall RFmxEVDO_BuildChannelString (char selectorString[],
 int32 channelNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the channel string to use as the selector string with the modulation accuracy (ModAcc) channel configuration or fetch attributes and functions. 
Refer to the [Selector String](/csh?topicname=rfmxspecan/selector_string_cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| channelNumber | int32 | Specifies the channel number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | char[] | Returns the selector string you can use in the selectorString input parameter for Configuration functions, Fetch functions, or the RFmxEVDO_Initiate function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_buildoffsetstring.html language=enus -->
## TOPIC 00006: RFmxEVDO_BuildOffsetString

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_buildoffsetstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_buildoffsetstring.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_BuildOffsetString

int32 __stdcall RFmxEVDO_BuildOffsetString (char selectorString[],
 int32 offsetNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates the offset string to use as the selector string with adjacent channel power (ACP) and spectral emission mask (SEM) offset configuration or fetch attributes and functions. 
Refer to the [Selector String](/csh?topicname=rfmxspecan/selector_string_cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| offsetNumber | int32 | Specifies the offset number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | char[] | Returns the selector string you can use in the selectorString input parameter for Configuration functions, Fetch functions, or the RFmxEVDO_Initiate function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_buildsignalstring.html language=enus -->
## TOPIC 00007: RFmxEVDO_BuildSignalString

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_buildsignalstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_buildsignalstring.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_BuildSignalString

int32 __stdcall RFmxEVDO_BuildSignalString (char signalName[],
 char resultName[],
 int32 selectorStringLength,
 char selectorString[]);

#### Purpose

Creates a selector string for use with configuration or fetch attributes and functions. 
Refer to the [Selector String](/csh?topicname=rfmxspecan/selector_string_cvi.html) topic for information about the string syntax for named signals.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| signalName | char[] | Specifies the name of the signal when using named signal configurations. This input accepts the signal name with or without the "signal::" prefix. Examples: """signal::sig1""sig1" |
| resultName | char[] | Specifies the name of the result when performing overlapped measurements. This input accepts the result name with or without the "result::" prefix. Examples:"""result::r1""r1" |
| selectorStringLength | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | char[] | Returns the selector string you can use in the selectorString input parameter for Configuration functions, Fetch functions, or other functions that build selector strings. This string contains the signal and/or result names with their appropriate prefixes.Examples:"""signal::sig1""result::r1""signal::sig1/result::r1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_cdacfgsynchronizationmodeandinterval.html language=enus -->
## TOPIC 00008: RFmxEVDO_CDACfgSynchronizationModeAndInterval

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_cdacfgsynchronizationmodeandinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_cdacfgsynchronizationmodeandinterval.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_CDACfgSynchronizationModeAndInterval

int32 __stdcall RFmxEVDO_CDACfgSynchronizationModeAndInterval (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 synchronizationMode,
 int32 measurementOffset,
 int32 measurementLength);

#### Purpose

Configures the synchronization mode, measurement offset, and measurement length.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| synchronizationMode | int32 | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_FRAME (0) The frame boundary is detected, and the measurement is performed over the number of slots specified by the CDA Meas Length attribute starting at CDA Meas Offset slots from the frame boundary. RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_SLOT (1) The slot boundary is detected and the measurement is performed over the number of slots specified by CDA Meas Length number of slots, starting at CDA Meas Offset slots from the slot boundary. RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY (2) The symbol boundary is detected and the measurement is performed over the number of slots specified by the CDA Meas Length attribute, starting at CDA Meas Offset slots from the symbol boundary. |
| RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the CDA Meas Length attribute starting at CDA Meas Offset slots from the frame boundary. |  |
| RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by CDA Meas Length number of slots, starting at CDA Meas Offset slots from the slot boundary. |  |
| RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY (2) | The symbol boundary is detected and the measurement is performed over the number of slots specified by the CDA Meas Length attribute, starting at CDA Meas Offset slots from the symbol boundary. |  |
| measurementOffset | int32 | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the synchronizationMode parameter. |
| measurementLength | int32 | Specifies the duration of the CDA measurement. This value is expressed in slots. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_cdacfguplinkmeasurementchannel.html language=enus -->
## TOPIC 00009: RFmxEVDO_CDACfgUplinkMeasurementChannel

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_cdacfguplinkmeasurementchannel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_cdacfguplinkmeasurementchannel.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_CDACfgUplinkMeasurementChannel

int32 __stdcall RFmxEVDO_CDACfgUplinkMeasurementChannel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 walshCodeLength,
 int32 walshCodeNumber,
 int32 branch);

#### Purpose

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| walshCodeLength | int32 | Specifies the Walsh code length of the channel, subject to channel-specific analysis. |
| walshCodeNumber | int32 | Specifies the Walsh code number of the channel, subject to channel-specific analysis. |
| branch | int32 | Specifies the Walsh branch of the channel, subject to channel-specific analysis. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_cdafetchiqimpairments.html language=enus -->
## TOPIC 00010: RFmxEVDO_CDAFetchIQImpairments

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_cdafetchiqimpairments.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_cdafetchiqimpairments.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_CDAFetchIQImpairments

int32 __stdcall RFmxEVDO_CDAFetchIQImpairments (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* IQOriginOffset,
 float64* IQGainImbalance,
 float64* IQQuadratureError);

#### Purpose

Fetches the measured I/Q impairments.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| IQOriginOffset | float64* | Returns the I/Q origin offset. This value is expressed in dB. |
| IQGainImbalance | float64* | Returns the I/Q gain imbalance. This value is expressed in dB. |
| IQQuadratureError | float64* | Returns the I/Q quadrature error. This value is expressed in degrees. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_cdafetchuplinksymbolevmtrace.html language=enus -->
## TOPIC 00011: RFmxEVDO_CDAFetchUplinkSymbolEVMTrace

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_cdafetchuplinksymbolevmtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_cdafetchuplinksymbolevmtrace.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_CDAFetchUplinkSymbolEVMTrace

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolEVMTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 symbolEVM[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the symbol EVM trace of the configured measurement channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| symbolEVM | float32[] | Returns the real signal values stored in an array. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_cdafetchuplinksymbolmagnitudeerrortrace.html language=enus -->
## TOPIC 00012: RFmxEVDO_CDAFetchUplinkSymbolMagnitudeErrorTrace

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_cdafetchuplinksymbolmagnitudeerrortrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_cdafetchuplinksymbolmagnitudeerrortrace.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_CDAFetchUplinkSymbolMagnitudeErrorTrace

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolMagnitudeErrorTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 symbolMagnitudeError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the symbol magnitude error trace of the configured measurement channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| symbolMagnitudeError | float32[] | Returns the real signal values stored in an array. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_cfgcarrierfrequency.html language=enus -->
## TOPIC 00013: RFmxEVDO_CfgCarrierFrequency

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_cfgcarrierfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_cfgcarrierfrequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_CfgCarrierFrequency

int32 __stdcall RFmxEVDO_CfgCarrierFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 carrierFrequency);

#### Purpose

Configures the carrier frequency of the selected carrier as an offset frequency relative to the center frequency. Use "carrier<n>" as the selector string to configure this function. 
Configure the center frequency by using the [RFmxEVDO_CfgFrequency](/csh?topicname=rfmxevdocvi/cvirfmxevdo_cfgfrequency.html) function. If the number of carriers is greater than 1, configure the number of carriers using the [RFmxEVDO_CfgNumberOfCarriers](/csh?topicname=rfmxevdocvi/cvirfmxevdo_cfgnumberofcarriers.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. Examples: "carrier0""signal::sig1/carrier0"You can use the RFmxEVDO_BuildCarrierString function to build the selector string. |
| carrierFrequency | float64 | Specifies the carrier frequency. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_cfgexternalattenuation.html language=enus -->
## TOPIC 00014: RFmxEVDO_CfgExternalAttenuation

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_cfgexternalattenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_cfgexternalattenuation.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_CfgExternalAttenuation

int32 __stdcall RFmxEVDO_CfgExternalAttenuation (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 externalAttenuation);

#### Purpose

Specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| externalAttenuation | float64 | Specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the RF signal analyzer RF IN connector. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_cfgfrequencychannelnumber.html language=enus -->
## TOPIC 00015: RFmxEVDO_CfgFrequencyChannelNumber

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_cfgfrequencychannelnumber.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_cfgfrequencychannelnumber.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_CfgFrequencyChannelNumber

int32 __stdcall RFmxEVDO_CfgFrequencyChannelNumber (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 linkDirection,
 int32 bandClass,
 int32 channelNumber);

#### Purpose

Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| linkDirection | int32 | Specifies which direction the frequency is calculated. Currently, only uplink is supported. |
| bandClass | int32 | Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. Valid values range between 0 and 15, inclusive. |
| channelNumber | int32 | Is the absolute RF channel number. The valid range for this parameter depends on the value you specify for the band parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_initialize.html language=enus -->
## TOPIC 00016: rfmxevdo_Initialize

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_initialize.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_Initialize

int32 __stdcall RFmxEVDO_Initialize (char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession);

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
| optionString | char[] | Sets the initial value of certain attributes for the session. The following attributes are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about attributes used in this parameter, refer to the NI RF Vector Signal Analyzers Help. The format of this string is "AttributeName=Value", where AttributeName is the name of the attribute and Value is the value to which the attribute is set. For example, you can simulate an PXIe-5663E using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple attributes, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx uses yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |
|  | Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |  |
| isNewSession | int32* | Returns RFMXEVDO_VAL_TRUE if the function created a new session, or RFMXEVDO_VAL_FALSE if the function returned a reference to an existing session. |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Identifies your instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_initiate.html language=enus -->
## TOPIC 00017: RFmxEVDO_Initiate

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_initiate.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_Initiate

int32 __stdcall RFmxEVDO_Initiate (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[]);

#### Purpose

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes. To get the status of measurements, use the [RFmxEVDO_WaitforMeasurementComplete](/csh?topicname=rfmxevdocvi/cvirfmxevdo_waitformeasurementcomplete.html) function or [RFmxEVDO_CheckMeasurementStatus](/csh?topicname=rfmxevdocvi/cvirfmxevdo_checkmeasurementstatus.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: """result::r1""r1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_modacccfgsynchronizationmodeandinterval.html language=enus -->
## TOPIC 00018: RFmxEVDO_ModAccCfgSynchronizationModeAndInterval

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_modacccfgsynchronizationmodeandinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_modacccfgsynchronizationmodeandinterval.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_ModAccCfgSynchronizationModeAndInterval

int32 __stdcall RFmxEVDO_ModAccCfgSynchronizationModeAndInterval (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 synchronizationMode,
 int32 measurementOffset,
 int32 measurementLength);

#### Purpose

Configures how the modulation accuracy (ModAcc) measurement synchronizes to the signal and the synchronization interval length.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| synchronizationMode | int32 | Specifies whether the measurement is performed from frame, slot, or symbol boundary.RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME (0) The frame boundary is detected and measurement is performed over the measurementLength parameter value, starting at the offset from the frame boundary specified in the measurementOffset parameter.RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT (1) The slot boundary is detected and measurement is performed over the measurementLength parameter value, starting at the offset from the frame boundary specified in the measurementOffset parameter.RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY (2) The symbol boundary is detected and measurement is performed over the measurementLength parameter value, starting at the offset from the frame boundary specified in the measurementOffset parameter. |
| RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary is detected and measurement is performed over the measurementLength parameter value, starting at the offset from the frame boundary specified in the measurementOffset parameter. |  |
| RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary is detected and measurement is performed over the measurementLength parameter value, starting at the offset from the frame boundary specified in the measurementOffset parameter. |  |
| RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY (2) | The symbol boundary is detected and measurement is performed over the measurementLength parameter value, starting at the offset from the frame boundary specified in the measurementOffset parameter. |  |
| measurementOffset | int32 | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the synchronizationMode parameter. For example, if the synchronizationMode is set to RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME, ModAcc synchronizes to the first frame it finds. The measurement offset in slots is added after the boundary of this frame. The analysis is then started. |
| measurementLength | int32 | Specifies the duration of the ModAcc measurement. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_modaccfetchconstellationtrace.html language=enus -->
## TOPIC 00019: RFmxEVDO_ModAccFetchConstellationTrace

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_modaccfetchconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_modaccfetchconstellationtrace.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_ModAccFetchConstellationTrace

int32 __stdcall RFmxEVDO_ModAccFetchConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle constellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the constellation trace of the EV-DO measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| constellation | NIComplexSingle[] | Returns an array of complex chips of the corrected signal on which the ModAcc measurements are done. These chips can be used to obtain the constellation diagram. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_modaccfetchconstellationtracesplit.html language=enus -->
## TOPIC 00020: RFmxEVDO_ModAccFetchConstellationTraceSplit

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_modaccfetchconstellationtracesplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_modaccfetchconstellationtracesplit.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_ModAccFetchConstellationTraceSplit

int32 __stdcall RFmxEVDO_ModAccFetchConstellationTraceSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the constellation trace of the EV-DO measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| I | float32[] | Returns the real part of an array of complex chips of the corrected signal on which the ModAcc measurements are done. These chips can be used to obtain the constellation diagram. |
| Q | float32[] | Returns the imaginary part of an array of complex chips of the corrected signal on which the ModAcc measurements are done. These chips can be used to obtain the constellation diagram. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_modaccfetchphaseerrortrace.html language=enus -->
## TOPIC 00021: RFmxEVDO_ModAccFetchPhaseErrorTrace

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_modaccfetchphaseerrortrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_modaccfetchphaseerrortrace.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_ModAccFetchPhaseErrorTrace

int32 __stdcall RFmxEVDO_ModAccFetchPhaseErrorTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 phaseError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the phase error trace of the ModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| x0 | float64* | Is the start parameter. |
| dx | float64* | Is the delta parameter. |
| phaseError | float32[] | Returns the real signal values stored in an array. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_modaccfetchuplinkdetecteddatamodulationtype.html language=enus -->
## TOPIC 00022: RFmxEVDO_ModAccFetchUplinkDetectedDataModulationType

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_modaccfetchuplinkdetecteddatamodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_modaccfetchuplinkdetecteddatamodulationtype.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_ModAccFetchUplinkDetectedDataModulationType

int32 __stdcall RFmxEVDO_ModAccFetchUplinkDetectedDataModulationType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* uplinkDetectedDataModulationType);

#### Purpose

Returns the modulation type of the uplink data channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| uplinkDetectedDataModulationType | int32* | Returns the detected modulation type of the uplink data channel.RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_DATA_CHANNEL_ABSENT (1) The uplink data channel is absent. RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_B4 (2) The uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q4 (3) The uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q2 (4) The uplink data channel uses QPSK with the Walsh function W(2,1). RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q4Q2 (5) The uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_E4E2 (6) The uplink data channel uses 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_DATA_CHANNEL_ABSENT (1) | The uplink data channel is absent. |  |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_B4 (2) | The uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). |  |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q4 (3) | The uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). |  |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q2 (4) | The uplink data channel uses QPSK with the Walsh function W(2,1). |  |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q4Q2 (5) | The uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). |  |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_E4E2 (6) | The uplink data channel uses 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_modaccfetchuplinkevm.html language=enus -->
## TOPIC 00023: RFmxEVDO_ModAccFetchUplinkEVM

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_modaccfetchuplinkevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_modaccfetchuplinkevm.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_ModAccFetchUplinkEVM

int32 __stdcall RFmxEVDO_ModAccFetchUplinkEVM (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* uplinkRMSEVM,
 float64* uplinkPeakEVM,
 float64* uplinkRho,
 float64* frequencyError,
 float64* chipRateError,
 float64* uplinkRMSMagnitudeError,
 float64* uplinkRMSPhaseError);

#### Purpose

Returns the EVM and related values of the EV-DO uplink.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| uplinkRMSEVM | float64* | Returns the RMS of the EVM, as a percentage. |
| uplinkPeakEVM | float64* | Returns the peak value of the uplink EVM, as a percentage. |
| uplinkRho | float64* | Returns the Rho value. |
| frequencyError | float64* | Returns the detected frequency error in Hz. |
| chipRateError | float64* | Returns the chip rate error in parts per million (ppm). |
| uplinkRMSMagnitudeError | float64* | Returns the RMS of the magnitude error, as a percentage. |
| uplinkRMSPhaseError | float64* | Returns the RMS of the phase error in degrees. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_obwcfgaveraging.html language=enus -->
## TOPIC 00024: RFmxEVDO_OBWCfgAveraging

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_obwcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_obwcfgaveraging.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_OBWCfgAveraging

int32 __stdcall RFmxEVDO_OBWCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount,
 int32 averagingType);

#### Purpose

Configures averaging for the occupied bandwidth (OBW) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_FALSE (0) Averaging is not enabled.RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_TRUE (1) Averaging is enabled. |
| RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_FALSE (0) | Averaging is not enabled. |  |
| RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_TRUE (1) | Averaging is enabled. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_TRUE. |
| averagingType | int32 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. RFMXEVDO_VAL_OBW_AVERAGING_TYPE_RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.RFMXEVDO_VAL_OBW_AVERAGING_TYPE_LOG (1) The power spectrum is averaged in a logarithmic scale.RFMXEVDO_VAL_OBW_AVERAGING_TYPE_SCALAR (2) The square root of the power spectrum is averaged.RFMXEVDO_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXEVDO_VAL_OBW_AVERAGING_TYPE_MINIMUM (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXEVDO_VAL_OBW_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXEVDO_VAL_OBW_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXEVDO_VAL_OBW_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |  |
| RFMXEVDO_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXEVDO_VAL_OBW_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_obwcfgrbwfilter.html language=enus -->
## TOPIC 00025: RFmxEVDO_OBWCfgRBWFilter

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_obwcfgrbwfilter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_obwcfgrbwfilter.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_OBWCfgRBWFilter

int32 __stdcall RFmxEVDO_OBWCfgRBWFilter (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| RBWAuto | int32 | Specifies whether the measurement calculates the RBW. RFMXEVDO_VAL_OBW_RBW_AUTO_FALSE (0) RFmx EV-DO automatically computes the RBW.RFMXEVDO_VAL_OBW_RBW_AUTO_TRUE (1) The measurement uses the RBW you specify. |
| RFMXEVDO_VAL_OBW_RBW_AUTO_FALSE (0) | RFmx EV-DO automatically computes the RBW. |  |
| RFMXEVDO_VAL_OBW_RBW_AUTO_TRUE (1) | The measurement uses the RBW you specify. |  |
| RBW | float64 | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBWAuto parameter to RFMXEVDO_VAL_OBW_RBW_AUTO_FALSE. This value is expressed in Hz. |
| RBWFilterType | int32 | Specifies the shape of the digital RBW filter. RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED (0) No RBW filtering is performed.RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN (1) An RBW filter with a Gaussian response is applied.RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_FLAT (2) An RBW filter with a flat response is applied. |
| RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED (0) | No RBW filtering is performed. |  |
| RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_obwcfgsweeptime.html language=enus -->
## TOPIC 00026: RFmxEVDO_OBWCfgSweepTime

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_obwcfgsweeptime.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_obwcfgsweeptime.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_OBWCfgSweepTime

int32 __stdcall RFmxEVDO_OBWCfgSweepTime (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 sweepTimeAuto,
 float64 sweepTimeInterval);

#### Purpose

Configures sweep time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| sweepTimeAuto | int32 | Specifies whether the measurement calculates the sweep time. RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) The measurement uses the sweep time that you specify using the sweepTimeInterval parameter.RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) The measurement uses the default sweep time of 1.67 ms. |
| RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify using the sweepTimeInterval parameter. |  |
| RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the default sweep time of 1.67 ms. |  |
| sweepTimeInterval | float64 | Specifies the sweep time when you set the sweepTimeAuto parameter to RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_obwfetchmeasurement.html language=enus -->
## TOPIC 00027: RFmxEVDO_OBWFetchMeasurement

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_obwfetchmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_obwfetchmeasurement.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_OBWFetchMeasurement

int32 __stdcall RFmxEVDO_OBWFetchMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* occupiedBandwidth,
 float64* absolutePower,
 float64* startFrequency,
 float64* stopFrequency);

#### Purpose

Returns the occupied bandwidth (OBW) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| occupiedBandwidth | float64* | Returns the occupied bandwidth. This value is expressed in Hz. |
| absolutePower | float64* | Returns the total integrated power of the averaged spectrum acquired by the OBW measurement. This value is expressed in dBm. |
| startFrequency | float64* | Returns the start frequency of the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = stop frequency - start frequency |
| stopFrequency | float64* | Returns the stop frequency of the OBW. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_semcfgsweeptime.html language=enus -->
## TOPIC 00028: RFmxEVDO_SEMCfgSweepTime

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_semcfgsweeptime.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_semcfgsweeptime.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SEMCfgSweepTime

int32 __stdcall RFmxEVDO_SEMCfgSweepTime (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 sweepTimeAuto,
 float64 sweepTimeInterval);

#### Purpose

Configures the sweep time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| sweepTimeAuto | int32 | Specifies whether the measurement calculates the sweep time. RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_FALSE (0) The measurement uses the sweep time that you specify using the sweepTimeInterval parameter.RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_TRUE (1) The measurement uses the default sweep time of 1.67 ms. |
| RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify using the sweepTimeInterval parameter. |  |
| RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the default sweep time of 1.67 ms. |  |
| sweepTimeInterval | float64 | Specifies the sweep time when you set the sweepTimeAuto parameter to RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_semfetchcarriermeasurement.html language=enus -->
## TOPIC 00029: RFmxEVDO_SEMFetchCarrierMeasurement

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_semfetchcarriermeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_semfetchcarriermeasurement.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SEMFetchCarrierMeasurement

int32 __stdcall RFmxEVDO_SEMFetchCarrierMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* absoluteIntegratedPower,
 float64* relativeIntegratedPower);

#### Purpose

Returns the carrier measurements for the carrier selected by the selector string. Use "carrier<n>" as the selector string to read parameters from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxEVDO_BuildCarrierString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| absoluteIntegratedPower | float64* | Returns absolute power of the selected carrier. This value is expressed in dBm. |
| relativeIntegratedPower | float64* | Returns the relative power of the selected carrier. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_semfetchcarriermeasurementarray.html language=enus -->
## TOPIC 00030: RFmxEVDO_SEMFetchCarrierMeasurementArray

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_semfetchcarriermeasurementarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_semfetchcarriermeasurementarray.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SEMFetchCarrierMeasurementArray

int32 __stdcall RFmxEVDO_SEMFetchCarrierMeasurementArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 absoluteIntegratedPower[],
 float64 relativeIntegratedPower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the array of carrier measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| absoluteIntegratedPower | float64[] | Returns the array of absolute carrier powers. This value is expressed in dBm. |
| relativeIntegratedPower | float64[] | Returns the array of relative carrier powers. This value is expressed in dB. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_semfetchloweroffsetmarginarray.html language=enus -->
## TOPIC 00031: RFmxEVDO_SEMFetchLowerOffsetMarginArray

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_semfetchloweroffsetmarginarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_semfetchloweroffsetmarginarray.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SEMFetchLowerOffsetMarginArray

int32 __stdcall RFmxEVDO_SEMFetchLowerOffsetMarginArray (niRFmxInstrHandle instrumentHandle,
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

Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| measurementStatus | int32[] | Returns the array of lower offset measurement statuses. |
| margin | float64[] | Returns the array of margins. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginFrequency | float64[] | Returns the array of frequencies at which the margin occurred in each lower (negative) offset segment. This value is expressed in Hz. |
| marginAbsolutePower | float64[] | Returns the array of powers at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. |
| marginRelativePower | float64[] | Returns the array of powers at which the margin occurred in each lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_semfetchmeasurementstatus.html language=enus -->
## TOPIC 00032: RFmxEVDO_SEMFetchMeasurementStatus

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_semfetchmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_semfetchmeasurementstatus.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SEMFetchMeasurementStatus

int32 __stdcall RFmxEVDO_SEMFetchMeasurementStatus (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* measurementStatus);

#### Purpose

Fetches the SEM measurement status.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| measurementStatus | int32* | Returns the status of the measurement. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_semfetchtotalcarrierpower.html language=enus -->
## TOPIC 00033: RFmxEVDO_SEMFetchTotalCarrierPower

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_semfetchtotalcarrierpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_semfetchtotalcarrierpower.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SEMFetchTotalCarrierPower

int32 __stdcall RFmxEVDO_SEMFetchTotalCarrierPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* totalCarrierPower);

#### Purpose

Returns the total carrier power of the selected carrier.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| totalCarrierPower | float64* | Returns the total carrier power of the selected carrier. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_semfetchupperoffsetmarginarray.html language=enus -->
## TOPIC 00034: RFmxEVDO_SEMFetchUpperOffsetMarginArray

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_semfetchupperoffsetmarginarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_semfetchupperoffsetmarginarray.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SEMFetchUpperOffsetMarginArray

int32 __stdcall RFmxEVDO_SEMFetchUpperOffsetMarginArray (niRFmxInstrHandle instrumentHandle,
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

Returns the measurement status and margin from the limit line measured in the upper offset segments.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| measurementStatus | int32[] | Returns the array of upper offset measurement statuses. |
| margin | float64[] | Returns the array of margins. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
| marginFrequency | float64[] | Returns the array of frequencies at which the margin occurred in each upper (positive) offset. This value is expressed in Hz. |
| marginAbsolutePower | float64[] | Returns the array of powers at which the margin occurred in each upper (positive) offset segment. This value is expressed in dBm. |
| marginRelativePower | float64[] | Returns the array of powers at which the margin occurred in each upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributef64.html language=enus -->
## TOPIC 00035: RFmxEVDO_SetAttributeF64

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributef64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributef64.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeF64

int32 __stdcall RFmxEVDO_SetAttributeF64 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal);

#### Purpose

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float64 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributef64array.html language=enus -->
## TOPIC 00036: RFmxEVDO_SetAttributeF64Array

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributef64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributef64array.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeF64Array

int32 __stdcall RFmxEVDO_SetAttributeF64Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float64 attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributei16.html language=enus -->
## TOPIC 00037: RFmxEVDO_SetAttributeI16

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributei16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributei16.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeI16

int32 __stdcall RFmxEVDO_SetAttributeI16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int16 attrVal);

#### Purpose

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int16 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributei32.html language=enus -->
## TOPIC 00038: RFmxEVDO_SetAttributeI32

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributei32.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeI32

int32 __stdcall RFmxEVDO_SetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributei32array.html language=enus -->
## TOPIC 00039: RFmxEVDO_SetAttributeI32Array

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributei32array.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeI32Array

int32 __stdcall RFmxEVDO_SetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributei64.html language=enus -->
## TOPIC 00040: RFmxEVDO_SetAttributeI64

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributei64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributei64.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeI64

int32 __stdcall RFmxEVDO_SetAttributeI64 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 attrVal);

#### Purpose

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int64 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributei64array.html language=enus -->
## TOPIC 00041: RFmxEVDO_SetAttributeI64Array

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributei64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributei64array.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeI64Array

int32 __stdcall RFmxEVDO_SetAttributeI64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributei8.html language=enus -->
## TOPIC 00042: RFmxEVDO_SetAttributeI8

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributei8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributei8.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeI8

int32 __stdcall RFmxEVDO_SetAttributeI8 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int8 attrVal);

#### Purpose

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int8 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributei8array.html language=enus -->
## TOPIC 00043: RFmxEVDO_SetAttributeI8Array

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributei8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributei8array.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeI8Array

int32 __stdcall RFmxEVDO_SetAttributeI8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributenicomplexdoublearray.html language=enus -->
## TOPIC 00044: RFmxEVDO_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributenicomplexdoublearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributenicomplexdoublearray.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeNIComplexDoubleArray

int32 __stdcall RFmxEVDO_SetAttributeNIComplexDoubleArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 NIComplexDouble attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributeu32array.html language=enus -->
## TOPIC 00045: RFmxEVDO_SetAttributeU32Array

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributeu32array.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeU32Array

int32 __stdcall RFmxEVDO_SetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_setattributeu8.html language=enus -->
## TOPIC 00046: RFmxEVDO_SetAttributeU8

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_setattributeu8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_setattributeu8.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SetAttributeU8

int32 __stdcall RFmxEVDO_SetAttributeU8 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal);

#### Purpose

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt8 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_slotphasefetchmaximumhalfslotphasediscontinuity.html language=enus -->
## TOPIC 00047: RFmxEVDO_SlotPhaseFetchMaximumHalfSlotPhaseDiscontinuity

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_slotphasefetchmaximumhalfslotphasediscontinuity.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_slotphasefetchmaximumhalfslotphasediscontinuity.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SlotPhaseFetchMaximumHalfSlotPhaseDiscontinuity

int32 __stdcall RFmxEVDO_SlotPhaseFetchMaximumHalfSlotPhaseDiscontinuity (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* maximumHalfSlotPhaseDiscontinuity);

#### Purpose

Fetches the maximum phase discontinuity observed at half-slot boundaries in the measurement interval.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| maximumHalfSlotPhaseDiscontinuity | float64* | Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_slotphasefetchphasediscontinuities.html language=enus -->
## TOPIC 00048: RFmxEVDO_SlotPhaseFetchPhaseDiscontinuities

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_slotphasefetchphasediscontinuities.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_slotphasefetchphasediscontinuities.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SlotPhaseFetchPhaseDiscontinuities

int32 __stdcall RFmxEVDO_SlotPhaseFetchPhaseDiscontinuities (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 halfSlotPhaseDiscontinuity[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the phase discontinuity value for the half-slot boundaries in the measurement interval.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| halfSlotPhaseDiscontinuity | float64[] | Returns the array of slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_slotpowercfgsynchronizationmodeandinterval.html language=enus -->
## TOPIC 00049: RFmxEVDO_SlotPowerCfgSynchronizationModeAndInterval

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_slotpowercfgsynchronizationmodeandinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_slotpowercfgsynchronizationmodeandinterval.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SlotPowerCfgSynchronizationModeAndInterval

int32 __stdcall RFmxEVDO_SlotPowerCfgSynchronizationModeAndInterval (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 synchronizationMode,
 int32 measurementOffset,
 int32 measurementLength);

#### Purpose

Configures the synchronization mode, measurement offset, and measurement length.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| synchronizationMode | int32 | Specifies whether the measurement is performed from the frame or the slot boundary. RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME (0) The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length attribute starting at SlotPower Meas Offset slots from the frame boundary. RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT (1) The slot boundary is detected and the measurement is performed over the number of slots specified by SlotPower Measurement Length number of slots, starting at SlotPower Measurement Offset slots from the slot boundary. |
| RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length attribute starting at SlotPower Meas Offset slots from the frame boundary. |  |
| RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by SlotPower Measurement Length number of slots, starting at SlotPower Measurement Offset slots from the slot boundary. |  |
| measurementOffset | int32 | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPower Sync Mode attribute. |
| measurementLength | int32 | Specifies the duration of the SlotPower measurement. This value is expressed in slots. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_slotpowerfetchpowers.html language=enus -->
## TOPIC 00050: RFmxEVDO_SlotPowerFetchPowers

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_slotpowerfetchpowers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_slotpowerfetchpowers.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_SlotPowerFetchPowers

int32 __stdcall RFmxEVDO_SlotPowerFetchPowers (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 halfSlotPower[],
 float64 halfSlotPowerDelta[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the slot power and slot power delta for all half-slots in the measurement length. The slot power delta is the difference in power between adjacent half-slots.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: """signal::sig1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| halfSlotPower | float64[] | Returns the array of half slot powers. This value is expressed in dBm. |
| halfSlotPowerDelta | float64[] | Returns the array of half slot power delta powers. This value is expressed in dB. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_waitforacquisitioncomplete.html language=enus -->
## TOPIC 00051: RFmxEVDO_WaitForAcquisitionComplete

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_waitforacquisitioncomplete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_waitforacquisitioncomplete.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_WaitForAcquisitionComplete

int32 __stdcall RFmxEVDO_WaitForAcquisitionComplete (niRFmxInstrHandle instrumentHandle, float64 timeout);

#### Purpose

Waits and blocks the data flow until the acquisition is complete. This function is typically called after a specific initiate function. 
 


This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_waitforacquisitioncomplete.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=cvirfmxevdo_waitformeasurementcomplete.html language=enus -->
## TOPIC 00052: RFmxEVDO_WaitForMeasurementComplete

- bundle_id: `rfmx-evdo-cvi`
- source_path: `cvirfmxevdo_waitformeasurementcomplete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/cvirfmxevdo_waitformeasurementcomplete.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO_WaitForMeasurementComplete

int32 __stdcall RFmxEVDO_WaitForMeasurementComplete (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout);

#### Purpose

Waits for the specified number for seconds for all the measurements to complete.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxEVDO_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: """signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxEVDO_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxEVDO_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_all_traces_enabled.html language=enus -->
## TOPIC 00053: RFMXEVDO_ATTR_ACP_ALL_TRACES_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_all_traces_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_ACPGetAllTracesEnabled Set Function: RFmxEVDO_ACPSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_averaging_count.html language=enus -->
## TOPIC 00054: RFMXEVDO_ATTR_ACP_AVERAGING_COUNT

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_averaging_count.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXEVDO_ATTR_ACP_AVERAGING_ENABLED attribute to RFMXEVDO_VAL_ACP_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxEVDO_ACPGetAveragingCount Set Function: RFmxEVDO_ACPSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_far_if_output_power_offset.html language=enus -->
## TOPIC 00055: RFMXEVDO_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_far_if_output_power_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_far_if_output_power_offset.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeF64RFmxEVDO_GetAttributeF64 |
| Description: | Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE and set the RFMXEVDO_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to RFMXEVDO_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 20. Get Function: RFmxEVDO_ACPGetFarIFOutputPowerOffset Set Function: RFmxEVDO_ACPSetFarIFOutputPowerOffset |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_if_output_power_offset_auto.html language=enus -->
## TOPIC 00056: RFMXEVDO_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_if_output_power_offset_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_if_output_power_offset_auto.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the measurement calculates an IF output power level offset for the offset channels to improve the dynamic range of the adjacent channel power (ACP) measurement. This attribute is used only if you set the RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE. Get Function: RFmxEVDO_ACPGetIFOutputPowerOffsetAuto Set Function: RFmxEVDO_ACPSetIFOutputPowerOffsetAuto |
| Values: | RFMXEVDO_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE (0)The system does not calculate an IF output power level offset RFMXEVDO_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE (1)The system calculates an IF output power level offset. |
| RFMXEVDO_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE (0) | The system does not calculate an IF output power level offset |
| RFMXEVDO_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE (1) | The system calculates an IF output power level offset. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_measurement_enabled.html language=enus -->
## TOPIC 00057: RFMXEVDO_ATTR_ACP_MEASUREMENT_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_measurement_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the ACP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_ACPGetMeasurementEnabled Set Function: RFmxEVDO_ACPSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_measurement_method.html language=enus -->
## TOPIC 00058: RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_measurement_method.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the method for performing the adjacent channel power (ACP) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_NORMAL. Get Function: RFmxEVDO_ACPGetMeasurementMethod Set Function: RFmxEVDO_ACPSetMeasurementMethod |
| Values: | RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_NORMAL (0)The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE (1)The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT (2)The ACP measurement acquires I/Q samples for a duration specified by the RFMXEVDO_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. These samples are divided into smaller chunks. The size of each chunk is defined by the RFMXEVDO_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize the ACP measurement speed. The accuracy of the results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time averaging is allowed. The following attributes have limited support when you set the RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT. The RFMXEVDO_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute will only support RFMXEVDO_VAL_ACP_RBW_AUTO_TRUE value. The RFMXEVDO_ATTR_ACP_RBW_FILTER_TYPE attribute will only support RFMXEVDO_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED value. The RFMXEVDO_ATTR_ACP_AVERAGING_COUNT attribute will only support a value greater than or equal to 1. The RFMXEVDO_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS attribute will only support a value of 1. Note: For multi-span FFT, the averaging count should be 1. |
| RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_NORMAL (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. |
| RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT (2) | The ACP measurement acquires I/Q samples for a duration specified by the RFMXEVDO_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. These samples are divided into smaller chunks. The size of each chunk is defined by the RFMXEVDO_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize the ACP measurement speed. The accuracy of the results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time averaging is allowed. The following attributes have limited support when you set the RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT. The RFMXEVDO_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH attribute will only support RFMXEVDO_VAL_ACP_RBW_AUTO_TRUE value. The RFMXEVDO_ATTR_ACP_RBW_FILTER_TYPE attribute will only support RFMXEVDO_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED value. The RFMXEVDO_ATTR_ACP_AVERAGING_COUNT attribute will only support a value greater than or equal to 1. The RFMXEVDO_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS attribute will only support a value of 1. Note: For multi-span FFT, the averaging count should be 1. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_near_if_output_power_offset.html language=enus -->
## TOPIC 00059: RFMXEVDO_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_near_if_output_power_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_near_if_output_power_offset.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeF64RFmxEVDO_GetAttributeF64 |
| Description: | Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD attribute to RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE and set the RFMXEVDO_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to RFMXEVDO_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxEVDO_ACPGetNearIFOutputPowerOffset Set Function: RFmxEVDO_ACPSetNearIFOutputPowerOffset |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_number_of_analysis_threads.html language=enus -->
## TOPIC 00060: RFMXEVDO_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_number_of_analysis_threads.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxEVDO_ACPGetNumberOfAnalysisThreads Set Function: RFmxEVDO_ACPSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_number_of_offsets.html language=enus -->
## TOPIC 00061: RFMXEVDO_ATTR_ACP_NUMBER_OF_OFFSETS

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_number_of_offsets.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_NUMBER_OF_OFFSETS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the number of offset channels for the adjacent channel power (ACP) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 2. Get Function: RFmxEVDO_ACPGetNumberOfOffsets Set Function: RFmxEVDO_ACPSetNumberOfOffsets |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_offset_frequency.html language=enus -->
## TOPIC 00062: RFMXEVDO_ATTR_ACP_OFFSET_FREQUENCY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_offset_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_offset_frequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_OFFSET_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxEVDO_ACPGetOffsetFrequency |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_offset_integration_bandwidth.html language=enus -->
## TOPIC 00063: RFMXEVDO_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_offset_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_offset_integration_bandwidth.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxEVDO_ACPGetOffsetIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_offset_power_reference_carrier.html language=enus -->
## TOPIC 00064: RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_offset_power_reference_carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_offset_power_reference_carrier.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the carrier number that is used as the power reference to measure the offset channel relative power. The default value is RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_COMPOSITE. Get Function: RFmxEVDO_ACPGetOffsetPowerReferenceCarrier Set Function: RFmxEVDO_ACPSetOffsetPowerReferenceCarrier |
| Values: | RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_CLOSEST (0)The measurement uses the power measured in the carrier closest to the offset channel center frequency, as the power reference. RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_HIGHEST (1)The measurement uses the highest power measured among all the active carriers as the power reference. RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_COMPOSITE (2)The measurement uses the sum of powers measured in all the active carriers as the power reference. RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_SPECIFIC (3)The measurement uses the power measured in the carrier that has an index specified by the RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC attribute, as the power reference. |
| RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_CLOSEST (0) | The measurement uses the power measured in the carrier closest to the offset channel center frequency, as the power reference. |
| RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_HIGHEST (1) | The measurement uses the highest power measured among all the active carriers as the power reference. |
| RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_COMPOSITE (2) | The measurement uses the sum of powers measured in all the active carriers as the power reference. |
| RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_SPECIFIC (3) | The measurement uses the power measured in the carrier that has an index specified by the RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC attribute, as the power reference. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_offset_power_reference_specific.html language=enus -->
## TOPIC 00065: RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_offset_power_reference_specific.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_offset_power_reference_specific.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the index of the carrier used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute to RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_SPECIFIC. The default value is 0. Get Function: RFmxEVDO_ACPGetOffsetPowerReferenceSpecific Set Function: RFmxEVDO_ACPSetOffsetPowerReferenceSpecific |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_results_carrier_absolute_power.html language=enus -->
## TOPIC 00066: RFMXEVDO_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_results_carrier_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_results_carrier_absolute_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the absolute measured carrier power. This value is expressed in dBm. Use 'carrier(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_ACPGetResultsCarrierAbsolutePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_results_carrier_relative_power.html language=enus -->
## TOPIC 00067: RFMXEVDO_ATTR_ACP_RESULTS_CARRIER_RELATIVE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_results_carrier_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_results_carrier_relative_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_RESULTS_CARRIER_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the relative measured carrier power. This value is expressed in dB. Use 'carrier(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_ACPGetResultsCarrierRelativePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_results_lower_offset_absolute_power.html language=enus -->
## TOPIC 00068: RFMXEVDO_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_results_lower_offset_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_results_lower_offset_absolute_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the absolute measured lower offset channel power. This value is expressed in dBm. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_ACPGetResultsLowerOffsetAbsolutePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_results_lower_offset_relative_power.html language=enus -->
## TOPIC 00069: RFMXEVDO_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_results_lower_offset_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_results_lower_offset_relative_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_ACPGetResultsLowerOffsetRelativePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_results_total_carrier_power.html language=enus -->
## TOPIC 00070: RFMXEVDO_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_results_total_carrier_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_results_total_carrier_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the total carrier power measured by the adjacent channel power (ACP) measurement. This value is expressed in dBm. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ACPGetResultsTotalCarrierPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_results_upper_offset_absolute_power.html language=enus -->
## TOPIC 00071: RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_results_upper_offset_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_results_upper_offset_absolute_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the absolute measured upper offset channel power. This value is expressed in dBm. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_ACPGetResultsUpperOffsetAbsolutePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_results_upper_offset_relative_power.html language=enus -->
## TOPIC 00072: RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_results_upper_offset_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_results_upper_offset_relative_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the upper offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_ACPGetResultsUpperOffsetRelativePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_sequential_fft_size.html language=enus -->
## TOPIC 00073: RFMXEVDO_ATTR_ACP_SEQUENTIAL_FFT_SIZE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_sequential_fft_size.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_sequential_fft_size.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_SEQUENTIAL_FFT_SIZE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the number of bins to use for FFT computation when the RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD attribute is set to RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 512. Get Function: RFmxEVDO_ACPGetSequentialFFTSize Set Function: RFmxEVDO_ACPSetSequentialFFTSize |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_acp_sweep_time_auto.html language=enus -->
## TOPIC 00074: RFMXEVDO_ATTR_ACP_SWEEP_TIME_AUTO

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_acp_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_acp_sweep_time_auto.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_ACP_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxEVDO_ACPGetSweepTimeAuto Set Function: RFmxEVDO_ACPSetSweepTimeAuto |
| Values: | RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the sweep time that you specify in the RFMXEVDO_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_TRUE (1)The measurement uses the default sweep time of 1.67 ms. |
| RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the RFMXEVDO_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. |
| RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the default sweep time of 1.67 ms. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_all_traces_enabled.html language=enus -->
## TOPIC 00075: RFMXEVDO_ATTR_CDA_ALL_TRACES_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_all_traces_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the traces after performing the CDA measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_CDAGetAllTracesEnabled Set Function: RFmxEVDO_CDASetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_iq_offset_removal_enabled.html language=enus -->
## TOPIC 00076: RFMXEVDO_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_iq_offset_removal_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_iq_offset_removal_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to remove the I/Q offset before the CDA measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_FALSE. Get Function: RFmxEVDO_CDAGetIQOffsetRemovalEnabled Set Function: RFmxEVDO_CDASetIQOffsetRemovalEnabled |
| Values: | RFMXEVDO_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_FALSE (0)The I/Q offset is not removed before the CDA measurement. RFMXEVDO_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_TRUE (1)The I/Q offset is removed before the CDA measurement. |
| RFMXEVDO_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_FALSE (0) | The I/Q offset is not removed before the CDA measurement. |
| RFMXEVDO_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_TRUE (1) | The I/Q offset is removed before the CDA measurement. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_results_uplink_peak_active_power.html language=enus -->
## TOPIC 00077: RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_PEAK_ACTIVE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_results_uplink_peak_active_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_results_uplink_peak_active_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_PEAK_ACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the maximum power among all the active code channels. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxEVDO_CDAGetResultsUplinkPeakActivePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_results_uplink_peak_inactive_power.html language=enus -->
## TOPIC 00078: RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_PEAK_INACTIVE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_results_uplink_peak_inactive_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_results_uplink_peak_inactive_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_PEAK_INACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_CDAGetResultsUplinkPeakInactivePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_results_uplink_peak_symbol_evm.html language=enus -->
## TOPIC 00079: RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_PEAK_SYMBOL_EVM

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_results_uplink_peak_symbol_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_results_uplink_peak_symbol_evm.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_PEAK_SYMBOL_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxEVDO_CDAGetResultsUplinkPeakSymbolEVM |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_results_uplink_q_mean_active_power.html language=enus -->
## TOPIC 00080: RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_Q_MEAN_ACTIVE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_results_uplink_q_mean_active_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_results_uplink_q_mean_active_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_Q_MEAN_ACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_CDAGetResultsUplinkQMeanActivePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_results_uplink_q_peak_inactive_power.html language=enus -->
## TOPIC 00081: RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_Q_PEAK_INACTIVE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_results_uplink_q_peak_inactive_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_results_uplink_q_peak_inactive_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_Q_PEAK_INACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. This value is expressed in dB or dBm. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1, and 32 otherwise. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_CDAGetResultsUplinkQPeakInactivePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_results_uplink_rms_symbol_evm.html language=enus -->
## TOPIC 00082: RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_RMS_SYMBOL_EVM

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_results_uplink_rms_symbol_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_results_uplink_rms_symbol_evm.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_RMS_SYMBOL_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxEVDO_CDAGetResultsUplinkRMSSymbolEVM |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_results_uplink_total_active_power.html language=enus -->
## TOPIC 00083: RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_TOTAL_ACTIVE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_results_uplink_total_active_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_results_uplink_total_active_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_TOTAL_ACTIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the sum of the powers of all active code channels. If you set the CDA Power Unit attribute to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxEVDO_CDAGetResultsUplinkTotalActivePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_results_uplink_total_power.html language=enus -->
## TOPIC 00084: RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_TOTAL_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_results_uplink_total_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_results_uplink_total_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_TOTAL_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the mean power of the received signal. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxEVDO_CDAGetResultsUplinkTotalPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_spectrum_inverted.html language=enus -->
## TOPIC 00085: RFMXEVDO_ATTR_CDA_SPECTRUM_INVERTED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_spectrum_inverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_spectrum_inverted.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_SPECTRUM_INVERTED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the signal spectrum is inverted. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_CDA_SPECTRUM_INVERTED_FALSE. Get Function: RFmxEVDO_CDAGetSpectrumInverted Set Function: RFmxEVDO_CDASetSpectrumInverted |
| Values: | RFMXEVDO_VAL_CDA_SPECTRUM_INVERTED_FALSE (0)The spectrum is not inverted. RFMXEVDO_VAL_CDA_SPECTRUM_INVERTED_TRUE (1)The spectrum is inverted. |
| RFMXEVDO_VAL_CDA_SPECTRUM_INVERTED_FALSE (0) | The spectrum is not inverted. |
| RFMXEVDO_VAL_CDA_SPECTRUM_INVERTED_TRUE (1) | The spectrum is inverted. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_cda_synchronization_mode.html language=enus -->
## TOPIC 00086: RFMXEVDO_ATTR_CDA_SYNCHRONIZATION_MODE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_cda_synchronization_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_cda_synchronization_mode.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CDA_SYNCHRONIZATION_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_SLOT. Get Function: RFmxEVDO_CDAGetSynchronizationMode Set Function: RFmxEVDO_CDASetSynchronizationMode |
| Values: | RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_FRAME (0)The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_CDA_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET slots from the frame boundary. RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_SLOT (1)The slot boundary is detected and the measurement is performed over the number of slots specified by RFMXEVDO_ATTR_CDA_MEASUREMENT_LENGTH number of slots, starting at RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET slots from the slot boundary. RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY (2)The symbol boundary is detected and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_CDA_MEASUREMENT_LENGTH attribute, starting at RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET slots from the symbol boundary. |
| RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_CDA_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET slots from the frame boundary. |
| RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by RFMXEVDO_ATTR_CDA_MEASUREMENT_LENGTH number of slots, starting at RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET slots from the slot boundary. |
| RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY (2) | The symbol boundary is detected and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_CDA_MEASUREMENT_LENGTH attribute, starting at RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET slots from the symbol boundary. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_chp_all_traces_enabled.html language=enus -->
## TOPIC 00087: RFMXEVDO_ATTR_CHP_ALL_TRACES_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_chp_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_chp_all_traces_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CHP_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_CHPGetAllTracesEnabled Set Function: RFmxEVDO_CHPSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_chp_averaging_count.html language=enus -->
## TOPIC 00088: RFMXEVDO_ATTR_CHP_AVERAGING_COUNT

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_chp_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_chp_averaging_count.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CHP_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXEVDO_ATTR_CHP_AVERAGING_ENABLED attribute to RFMXEVDO_VAL_CHP_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxEVDO_CHPGetAveragingCount Set Function: RFmxEVDO_CHPSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_chp_averaging_enabled.html language=enus -->
## TOPIC 00089: RFMXEVDO_ATTR_CHP_AVERAGING_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_chp_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_chp_averaging_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CHP_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the channel power (CHP) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_CHP_AVERAGING_ENABLED_FALSE. Get Function: RFmxEVDO_CHPGetAveragingEnabled Set Function: RFmxEVDO_CHPSetAveragingEnabled |
| Values: | RFMXEVDO_VAL_CHP_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXEVDO_VAL_CHP_AVERAGING_ENABLED_TRUE (1)The CHP measurement uses the Averaging Count attribute as the number of acquisitions over which the CHP measurement is averaged. |
| RFMXEVDO_VAL_CHP_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXEVDO_VAL_CHP_AVERAGING_ENABLED_TRUE (1) | The CHP measurement uses the Averaging Count attribute as the number of acquisitions over which the CHP measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_chp_averaging_type.html language=enus -->
## TOPIC 00090: RFMXEVDO_ATTR_CHP_AVERAGING_TYPE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_chp_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_chp_averaging_type.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CHP_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the channel power (CHP) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_CHP_AVERAGING_TYPE_RMS. Get Function: RFmxEVDO_CHPGetAveragingType Set Function: RFmxEVDO_CHPSetAveragingType |
| Values: | RFMXEVDO_VAL_CHP_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXEVDO_VAL_CHP_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. RFMXEVDO_VAL_CHP_AVERAGING_TYPE_SCALAR (2)The square root of the power spectrum is averaged. RFMXEVDO_VAL_CHP_AVERAGING_TYPE_MAXIMUM (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXEVDO_VAL_CHP_AVERAGING_TYPE_MINIMUM (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXEVDO_VAL_CHP_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXEVDO_VAL_CHP_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXEVDO_VAL_CHP_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |
| RFMXEVDO_VAL_CHP_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXEVDO_VAL_CHP_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_chp_carrier_integration_bandwidth.html language=enus -->
## TOPIC 00091: RFMXEVDO_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_chp_carrier_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_chp_carrier_integration_bandwidth.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the CHP carrier integration bandwidth. This value is expressed in Hz. Use 'carrier(k)' as the selector string to read this result. Get Function: RFmxEVDO_CHPGetCarrierIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_chp_measurement_enabled.html language=enus -->
## TOPIC 00092: RFMXEVDO_ATTR_CHP_MEASUREMENT_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_chp_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_chp_measurement_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_CHP_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the channel power (CHP) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_CHPGetMeasurementEnabled Set Function: RFmxEVDO_CHPSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_digital_edge_trigger_edge.html language=enus -->
## TOPIC 00093: RFMXEVDO_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_digital_edge_trigger_edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_digital_edge_trigger_edge.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the active edge for the trigger. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to RFMXEVDO_VAL_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_DIGITAL_EDGE_RISING_EDGE. Get Function: RFmxEVDO_GetDigitalEdgeTriggerEdge Set Function: RFmxEVDO_SetDigitalEdgeTriggerEdge |
| Values: | RFMXEVDO_VAL_DIGITAL_EDGE_RISING_EDGE (0)The trigger asserts on the rising edge of the signal. RFMXEVDO_VAL_DIGITAL_EDGE_FALLING_EDGE (1)The trigger asserts on the falling edge of the signal. |
| RFMXEVDO_VAL_DIGITAL_EDGE_RISING_EDGE (0) | The trigger asserts on the rising edge of the signal. |
| RFMXEVDO_VAL_DIGITAL_EDGE_FALLING_EDGE (1) | The trigger asserts on the falling edge of the signal. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_digital_edge_trigger_source.html language=enus -->
## TOPIC 00094: RFMXEVDO_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_digital_edge_trigger_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_digital_edge_trigger_source.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeStringRFmxEVDO_GetAttributeString |
| Description: | Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to RFMXEVDO_VAL_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default of this attribute is hardware dependent. Get Function: RFmxEVDO_GetDigitalEdgeTriggerSource Set Function: RFmxEVDO_SetDigitalEdgeTriggerSource |
| Values: | RFMXEVDO_VAL_PFI0_STR (PFI0)The trigger is received on PFI 0. RFMXEVDO_VAL_PFI1_STR (PFI1)The trigger is received on PFI 1. RFMXEVDO_VAL_PXI_TRIG0_STR (PXI_Trig0)The trigger is received on PXI trigger line 0. RFMXEVDO_VAL_PXI_TRIG1_STR (PXI_Trig1)The trigger is received on PXI trigger line 1. RFMXEVDO_VAL_PXI_TRIG2_STR (PXI_Trig2)The trigger is received on PXI trigger line 2. RFMXEVDO_VAL_PXI_TRIG3_STR (PXI_Trig3)The trigger is received on PXI trigger line 3. RFMXEVDO_VAL_PXI_TRIG4_STR (PXI_Trig4)The trigger is received on PXI trigger line 4. RFMXEVDO_VAL_PXI_TRIG5_STR (PXI_Trig5)The trigger is received on PXI trigger line 5. RFMXEVDO_VAL_PXI_TRIG6_STR (PXI_Trig6)The trigger is received on PXI trigger line 6. RFMXEVDO_VAL_PXI_TRIG7_STR (PXI_Trig7)The trigger is received on PXI trigger line 7. RFMXEVDO_VAL_PXI_STAR_STR (PXI_STAR)The trigger is received on the PXI star trigger line. RFMXEVDO_VAL_PXIE_DSTARB_STR (PXIe_DStarB)The trigger is received on the PXIe DStar B trigger line. RFMXEVDO_VAL_TIMER_EVENT_STR (TimerEvent)The trigger is received from the timer event. |
| RFMXEVDO_VAL_PFI0_STR (PFI0) | The trigger is received on PFI 0. |
| RFMXEVDO_VAL_PFI1_STR (PFI1) | The trigger is received on PFI 1. |
| RFMXEVDO_VAL_PXI_TRIG0_STR (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| RFMXEVDO_VAL_PXI_TRIG1_STR (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| RFMXEVDO_VAL_PXI_TRIG2_STR (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| RFMXEVDO_VAL_PXI_TRIG3_STR (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| RFMXEVDO_VAL_PXI_TRIG4_STR (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| RFMXEVDO_VAL_PXI_TRIG5_STR (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| RFMXEVDO_VAL_PXI_TRIG6_STR (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| RFMXEVDO_VAL_PXI_TRIG7_STR (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| RFMXEVDO_VAL_PXI_STAR_STR (PXI_STAR) | The trigger is received on the PXI star trigger line. |
| RFMXEVDO_VAL_PXIE_DSTARB_STR (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |
| RFMXEVDO_VAL_TIMER_EVENT_STR (TimerEvent) | The trigger is received from the timer event. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_external_attenuation.html language=enus -->
## TOPIC 00095: RFMXEVDO_ATTR_EXTERNAL_ATTENUATION

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_external_attenuation.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_EXTERNAL_ATTENUATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeF64RFmxEVDO_GetAttributeF64 |
| Description: | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxEVDO_GetExternalAttenuation Set Function: RFmxEVDO_SetExternalAttenuation |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_iq_power_edge_trigger_level.html language=enus -->
## TOPIC 00096: RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_iq_power_edge_trigger_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_iq_power_edge_trigger_level.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeF64RFmxEVDO_GetAttributeF64 |
| Description: | Specifies the power level at which the device triggers. This value is expressed in dB when the RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute is set to RFMXEVDO_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE and in dBm when the RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute is set to RFMXEVDO_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to RFMXEVDO_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default of this attribute is hardware dependent. Get Function: RFmxEVDO_GetIQPowerEdgeTriggerLevel Set Function: RFmxEVDO_SetIQPowerEdgeTriggerLevel |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_iq_power_edge_trigger_level_type.html language=enus -->
## TOPIC 00097: RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_iq_power_edge_trigger_level_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_iq_power_edge_trigger_level_type.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the reference for the RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to RFMXEVDO_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE. Get Function: RFmxEVDO_GetIQPowerEdgeTriggerLevelType Set Function: RFmxEVDO_SetIQPowerEdgeTriggerLevelType |
| Values: | RFMXEVDO_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0)The IQ Power Edge Level attribute is relative to the value of the RFMXEVDO_ATTR_REFERENCE_LEVEL attribute. RFMXEVDO_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1)The IQ Power Edge Level attribute specifies the absolute power. |
| RFMXEVDO_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0) | The IQ Power Edge Level attribute is relative to the value of the RFMXEVDO_ATTR_REFERENCE_LEVEL attribute. |
| RFMXEVDO_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1) | The IQ Power Edge Level attribute specifies the absolute power. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_iq_power_edge_trigger_slope.html language=enus -->
## TOPIC 00098: RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_iq_power_edge_trigger_slope.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_iq_power_edge_trigger_slope.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to RFMXEVDO_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_IQ_POWER_EDGE_RISING_SLOPE. Get Function: RFmxEVDO_GetIQPowerEdgeTriggerSlope Set Function: RFmxEVDO_SetIQPowerEdgeTriggerSlope |
| Values: | RFMXEVDO_VAL_IQ_POWER_EDGE_RISING_SLOPE (0)The trigger asserts when the signal power is rising. RFMXEVDO_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1)The trigger asserts when the signal power is falling. |
| RFMXEVDO_VAL_IQ_POWER_EDGE_RISING_SLOPE (0) | The trigger asserts when the signal power is rising. |
| RFMXEVDO_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1) | The trigger asserts when the signal power is falling. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_iq_power_edge_trigger_source.html language=enus -->
## TOPIC 00099: RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_iq_power_edge_trigger_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_iq_power_edge_trigger_source.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeStringRFmxEVDO_GetAttributeString |
| Description: | Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXEVDO_ATTR_TRIGGER_TYPE attribute to RFMXEVDO_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default of this attribute is hardware dependent. Get Function: RFmxEVDO_GetIQPowerEdgeTriggerSource Set Function: RFmxEVDO_SetIQPowerEdgeTriggerSource |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_measurement_length.html language=enus -->
## TOPIC 00100: RFMXEVDO_ATTR_MODACC_MEASUREMENT_LENGTH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_measurement_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_measurement_length.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_MEASUREMENT_LENGTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the duration of the modulation accuracy measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxEVDO_ModAccGetMeasurementLength Set Function: RFmxEVDO_ModAccSetMeasurementLength |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_measurement_offset.html language=enus -->
## TOPIC 00101: RFMXEVDO_ATTR_MODACC_MEASUREMENT_OFFSET

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_measurement_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_measurement_offset.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_MEASUREMENT_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXEVDO_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. For example, if the RFMXEVDO_ATTR_MODACC_SYNCHRONIZATION_MODE attribute is set to Frame, the measurement synchronizes to the first frame it finds. The measurement offset in slots is added after the boundary of this frame. The analysis is then started. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxEVDO_ModAccGetMeasurementOffset Set Function: RFmxEVDO_ModAccSetMeasurementOffset |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_multi_carrier_filter_enabled.html language=enus -->
## TOPIC 00102: RFMXEVDO_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_multi_carrier_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_multi_carrier_filter_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Enables the multi-carrier filter that can increase the multi-carrier interference suppression to improve ModAcc measurement quality in the presence of neighboring carriers. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_FALSE. Get Function: RFmxEVDO_ModAccGetMultiCarrierFilterEnabled Set Function: RFmxEVDO_ModAccSetMultiCarrierFilterEnabled |
| Values: | RFMXEVDO_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_FALSE (0)The multicarrier filter is disabled. RFMXEVDO_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_TRUE (1)The multicarrier filter is enabled. |
| RFMXEVDO_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_FALSE (0) | The multicarrier filter is disabled. |
| RFMXEVDO_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_TRUE (1) | The multicarrier filter is enabled. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_receive_filter_enabled.html language=enus -->
## TOPIC 00103: RFMXEVDO_ATTR_MODACC_RECEIVE_FILTER_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_receive_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_receive_filter_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RECEIVE_FILTER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable receive filtering. The default value is RFMXEVDO_VAL_MODACC_RECEIVE_FILTER_ENABLED_TRUE. Get Function: RFmxEVDO_ModAccGetReceiveFilterEnabled Set Function: RFmxEVDO_ModAccSetReceiveFilterEnabled |
| Values: | RFMXEVDO_VAL_MODACC_RECEIVE_FILTER_ENABLED_FALSE (0)Receive filtering is disabled. RFMXEVDO_VAL_MODACC_RECEIVE_FILTER_ENABLED_TRUE (1)Receive filtering is enabled. |
| RFMXEVDO_VAL_MODACC_RECEIVE_FILTER_ENABLED_FALSE (0) | Receive filtering is disabled. |
| RFMXEVDO_VAL_MODACC_RECEIVE_FILTER_ENABLED_TRUE (1) | Receive filtering is enabled. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_chip_rate_error.html language=enus -->
## TOPIC 00104: RFMXEVDO_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_chip_rate_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_chip_rate_error.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the chip rate error averaged over all measured slots. This value is expressed in parts per million (ppm). You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ModAccGetResultsChipRateError |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_frequency_error.html language=enus -->
## TOPIC 00105: RFMXEVDO_ATTR_MODACC_RESULTS_FREQUENCY_ERROR

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_frequency_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_frequency_error.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_FREQUENCY_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the frequency error averaged over all measured slots. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ModAccGetResultsFrequencyError |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_iq_gain_imbalance.html language=enus -->
## TOPIC 00106: RFMXEVDO_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_iq_gain_imbalance.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_iq_gain_imbalance.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ModAccGetResultsIQGainImbalance |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_uplink_detected_branch.html language=enus -->
## TOPIC 00107: RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_DETECTED_BRANCH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_uplink_detected_branch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_uplink_detected_branch.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_DETECTED_BRANCH

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | Returns the quadrature branch of a particular detected channel. Use 'channel(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_ModAccGetResultsUplinkDetectedBranch |
| Values: | RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_BRANCH_I (0)The detected channel occupies the in-phase branch. RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_BRANCH_Q (1)The detected channel occupies the quadrature branch. RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_BRANCH_I_AND_Q (2)The detected channel occupies the in-phase branch and the quadrature branch. |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_BRANCH_I (0) | The detected channel occupies the in-phase branch. |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_BRANCH_Q (1) | The detected channel occupies the quadrature branch. |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_BRANCH_I_AND_Q (2) | The detected channel occupies the in-phase branch and the quadrature branch. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_uplink_detected_data_modulation_type.html language=enus -->
## TOPIC 00108: RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_DETECTED_DATA_MODULATION_TYPE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_uplink_detected_data_modulation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_uplink_detected_data_modulation_type.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_DETECTED_DATA_MODULATION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | Returns the modulation type of the uplink data channel. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ModAccGetResultsUplinkDetectedDataModulationType |
| Values: | RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_DATA_CHANNEL_ABSENT (1)The specified uplink data channel is absent. RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_B4 (2)The specified uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q4 (3)The specified uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q2 (4)The specified uplink data channel uses QPSK with the Walsh function W(2,1). RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q4Q2 (5)The specified uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_E4E2 (6)The specified uplink data channel 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_DATA_CHANNEL_ABSENT (1) | The specified uplink data channel is absent. |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_B4 (2) | The specified uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q4 (3) | The specified uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q2 (4) | The specified uplink data channel uses QPSK with the Walsh function W(2,1). |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q4Q2 (5) | The specified uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). |
| RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_E4E2 (6) | The specified uplink data channel 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_uplink_peak_active_cde_walsh_code_length.html language=enus -->
## TOPIC 00109: RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_ACTIVE_CDE_WALSH_CODE_LENGTH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_uplink_peak_active_cde_walsh_code_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_uplink_peak_active_cde_walsh_code_length.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_ACTIVE_CDE_WALSH_CODE_LENGTH

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | The Walsh code length of the active Walsh channel for which the peak CDE has been observed. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ModAccGetResultsUplinkPeakActiveCDEWalshCodeLength |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_uplink_peak_active_cde_walsh_code_number.html language=enus -->
## TOPIC 00110: RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_ACTIVE_CDE_WALSH_CODE_NUMBER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_uplink_peak_active_cde_walsh_code_number.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_uplink_peak_active_cde_walsh_code_number.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_ACTIVE_CDE_WALSH_CODE_NUMBER

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | Returns the Walsh code number of the channel corresponding to the ModAcc:Uplink:Peak Active CDE (dB) result. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ModAccGetResultsUplinkPeakActiveCDEWalshCodeNumber |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_uplink_peak_cde_walsh_code_number.html language=enus -->
## TOPIC 00111: RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_CDE_WALSH_CODE_NUMBER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_uplink_peak_cde_walsh_code_number.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_uplink_peak_cde_walsh_code_number.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_CDE_WALSH_CODE_NUMBER

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | Returns the Walsh code number of the channel corresponding to the ModAcc:Uplink:Peak CDE (db) result. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ModAccGetResultsUplinkPeakCDEWalshCodeNumber |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_uplink_peak_evm.html language=enus -->
## TOPIC 00112: RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_EVM

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_uplink_peak_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_uplink_peak_evm.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the peak value of the uplink error vector magnitude (EVM), averaged over all measured slots. This value is expressed as a percentage. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ModAccGetResultsUplinkPeakEVM |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_uplink_rms_magnitude_error.html language=enus -->
## TOPIC 00113: RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_RMS_MAGNITUDE_ERROR

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_uplink_rms_magnitude_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_uplink_rms_magnitude_error.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_RMS_MAGNITUDE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the RMS of the magnitude error. This value is expressed as a percentage. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ModAccGetResultsUplinkRMSMagnitudeError |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_results_uplink_rms_phase_error.html language=enus -->
## TOPIC 00114: RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_RMS_PHASE_ERROR

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_results_uplink_rms_phase_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_results_uplink_rms_phase_error.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_RMS_PHASE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the RMS of the phase error. This value is expressed in degrees. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_ModAccGetResultsUplinkRMSPhaseError |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_spectrum_inverted.html language=enus -->
## TOPIC 00115: RFMXEVDO_ATTR_MODACC_SPECTRUM_INVERTED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_spectrum_inverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_spectrum_inverted.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_SPECTRUM_INVERTED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the measured spectrum is inverted. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_MODACC_SPECTRUM_INVERTED_FALSE. Get Function: RFmxEVDO_ModAccGetSpectrumInverted Set Function: RFmxEVDO_ModAccSetSpectrumInverted |
| Values: | RFMXEVDO_VAL_MODACC_SPECTRUM_INVERTED_FALSE (0)The measured spectrum is not inverted. RFMXEVDO_VAL_MODACC_SPECTRUM_INVERTED_TRUE (1)The measured spectrum is inverted. |
| RFMXEVDO_VAL_MODACC_SPECTRUM_INVERTED_FALSE (0) | The measured spectrum is not inverted. |
| RFMXEVDO_VAL_MODACC_SPECTRUM_INVERTED_TRUE (1) | The measured spectrum is inverted. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_modacc_synchronization_mode.html language=enus -->
## TOPIC 00116: RFMXEVDO_ATTR_MODACC_SYNCHRONIZATION_MODE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_modacc_synchronization_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_modacc_synchronization_mode.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_MODACC_SYNCHRONIZATION_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the measurement is performed from frame, slot, or symbol boundary. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT. Get Function: RFmxEVDO_ModAccGetSynchronizationMode Set Function: RFmxEVDO_ModAccSetSynchronizationMode |
| Values: | RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME (0)The frame boundary is detected and measurement is performed over the Measurement Length (slots) attribute value, starting at the offset from the frame boundary specified in the Measurement Offset (slots) attribute. RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT (1)The slot boundary is detected and measurement is performed over the Measurement Length (slots) attribute value, starting at the offset from the frame boundary specified in the Measurement Offset (slots) attribute. RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY (2)The symbol boundary is detected and measurement is performed over the Measurement Length (slots) attribute value, starting at the offset from the frame boundary specified in the Measurement Offset (slots) attribute. |
| RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary is detected and measurement is performed over the Measurement Length (slots) attribute value, starting at the offset from the frame boundary specified in the Measurement Offset (slots) attribute. |
| RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary is detected and measurement is performed over the Measurement Length (slots) attribute value, starting at the offset from the frame boundary specified in the Measurement Offset (slots) attribute. |
| RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY (2) | The symbol boundary is detected and measurement is performed over the Measurement Length (slots) attribute value, starting at the offset from the frame boundary specified in the Measurement Offset (slots) attribute. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_number_of_carriers.html language=enus -->
## TOPIC 00117: RFMXEVDO_ATTR_NUMBER_OF_CARRIERS

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_number_of_carriers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_number_of_carriers.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_NUMBER_OF_CARRIERS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the number of carriers in the signal. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxEVDO_GetNumberOfCarriers Set Function: RFmxEVDO_SetNumberOfCarriers |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_all_traces_enabled.html language=enus -->
## TOPIC 00118: RFMXEVDO_ATTR_OBW_ALL_TRACES_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_all_traces_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the occupied bandwidth (OBW) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_OBWGetAllTracesEnabled Set Function: RFmxEVDO_OBWSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_averaging_count.html language=enus -->
## TOPIC 00119: RFMXEVDO_ATTR_OBW_AVERAGING_COUNT

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_averaging_count.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXEVDO_ATTR_OBW_AVERAGING_ENABLED attribute to RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxEVDO_OBWGetAveragingCount Set Function: RFmxEVDO_OBWSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_averaging_enabled.html language=enus -->
## TOPIC 00120: RFMXEVDO_ATTR_OBW_AVERAGING_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_averaging_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the occupied bandwidth (OBW) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_FALSE. Get Function: RFmxEVDO_OBWGetAveragingEnabled Set Function: RFmxEVDO_OBWSetAveragingEnabled |
| Values: | RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_TRUE (1)The occupied bandwidth (OBW) measurement uses the RFMXEVDO_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |
| RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_TRUE (1) | The occupied bandwidth (OBW) measurement uses the RFMXEVDO_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_averaging_type.html language=enus -->
## TOPIC 00121: RFMXEVDO_ATTR_OBW_AVERAGING_TYPE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_averaging_type.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for occupied bandwidth (OBW) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_OBW_AVERAGING_TYPE_RMS. Get Function: RFmxEVDO_OBWGetAveragingType Set Function: RFmxEVDO_OBWSetAveragingType |
| Values: | RFMXEVDO_VAL_OBW_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXEVDO_VAL_OBW_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. RFMXEVDO_VAL_OBW_AVERAGING_TYPE_SCALAR (2)The square root of the power spectrum is averaged. RFMXEVDO_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXEVDO_VAL_OBW_AVERAGING_TYPE_MINIMUM (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXEVDO_VAL_OBW_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXEVDO_VAL_OBW_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXEVDO_VAL_OBW_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |
| RFMXEVDO_VAL_OBW_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXEVDO_VAL_OBW_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_measurement_enabled.html language=enus -->
## TOPIC 00122: RFMXEVDO_ATTR_OBW_MEASUREMENT_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_measurement_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the occupied bandwidth (OBW) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_OBWGetMeasurementEnabled Set Function: RFmxEVDO_OBWSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_number_of_analysis_threads.html language=enus -->
## TOPIC 00123: RFMXEVDO_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_number_of_analysis_threads.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the occupied bandwidth (OBW) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxEVDO_OBWGetNumberOfAnalysisThreads Set Function: RFmxEVDO_OBWSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_rbw_filter_auto_bandwidth.html language=enus -->
## TOPIC 00124: RFMXEVDO_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_rbw_filter_auto_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_rbw_filter_auto_bandwidth.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the RBW. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_OBW_RBW_AUTO_TRUE. Get Function: RFmxEVDO_OBWGetRBWFilterAutoBandwidth Set Function: RFmxEVDO_OBWSetRBWFilterAutoBandwidth |
| Values: | RFMXEVDO_VAL_OBW_RBW_AUTO_FALSE (0)The measurement uses the RBW that you specify in the RFMXEVDO_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. RFMXEVDO_VAL_OBW_RBW_AUTO_TRUE (1)The measurement computes the RBW. |
| RFMXEVDO_VAL_OBW_RBW_AUTO_FALSE (0) | The measurement uses the RBW that you specify in the RFMXEVDO_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |
| RFMXEVDO_VAL_OBW_RBW_AUTO_TRUE (1) | The measurement computes the RBW. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_rbw_filter_bandwidth.html language=enus -->
## TOPIC 00125: RFMXEVDO_ATTR_OBW_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_rbw_filter_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_rbw_filter_bandwidth.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_RBW_FILTER_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeF64RFmxEVDO_GetAttributeF64 |
| Description: | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RFMXEVDO_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH attribute to RFMXEVDO_VAL_OBW_RBW_AUTO_FALSE. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 30 kHz. Get Function: RFmxEVDO_OBWGetRBWFilterBandwidth Set Function: RFmxEVDO_OBWSetRBWFilterBandwidth |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_rbw_filter_type.html language=enus -->
## TOPIC 00126: RFMXEVDO_ATTR_OBW_RBW_FILTER_TYPE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_rbw_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_rbw_filter_type.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_RBW_FILTER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the shape of the digital RBW filter. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN. Get Function: RFmxEVDO_OBWGetRBWFilterType Set Function: RFmxEVDO_OBWSetRBWFilterType |
| Values: | RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED (0)An RBW filter with an FFT-Based response is applied. RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN (1)An RBW filter with a Gaussian response is applied. RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_FLAT (2)An RBW filter with a flat response is applied. |
| RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED (0) | An RBW filter with an FFT-Based response is applied. |
| RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN (1) | An RBW filter with a Gaussian response is applied. |
| RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_FLAT (2) | An RBW filter with a flat response is applied. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_results_absolute_power.html language=enus -->
## TOPIC 00127: RFMXEVDO_ATTR_OBW_RESULTS_ABSOLUTE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_results_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_results_absolute_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_RESULTS_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the absolute power measured in the occupied bandwidth (OBW). This value is expressed in dBm. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_OBWGetResultsAbsolutePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_results_occupied_bandwidth.html language=enus -->
## TOPIC 00128: RFMXEVDO_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_results_occupied_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_results_occupied_bandwidth.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the bandwidth that occupies 99 percent of the total power of the signal. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_OBWGetResultsOccupiedBandwidth |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_results_start_frequency.html language=enus -->
## TOPIC 00129: RFMXEVDO_ATTR_OBW_RESULTS_START_FREQUENCY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_results_start_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_results_start_frequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_RESULTS_START_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the start frequency of the occupied bandwidth (OBW). This value is expressed in Hz. OBW = Stop Frequency - Start Frequency You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_OBWGetResultsStartFrequency |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_results_stop_frequency.html language=enus -->
## TOPIC 00130: RFMXEVDO_ATTR_OBW_RESULTS_STOP_FREQUENCY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_results_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_results_stop_frequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_RESULTS_STOP_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the stop frequency of the occupied bandwidth (OBW). This value is expressed in Hz. OBW = Stop Frequency - Start Frequency You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_OBWGetResultsStopFrequency |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_span.html language=enus -->
## TOPIC 00131: RFMXEVDO_ATTR_OBW_SPAN

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_span.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_span.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_SPAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the frequency span of the OBW measurement. This value is expressed in Hz. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxEVDO_OBWGetSpan |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_sweep_time_auto.html language=enus -->
## TOPIC 00132: RFMXEVDO_ATTR_OBW_SWEEP_TIME_AUTO

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_sweep_time_auto.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxEVDO_OBWGetSweepTimeAuto Set Function: RFmxEVDO_OBWSetSweepTimeAuto |
| Values: | RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the sweep time that you specify in the RFMXEVDO_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1)The measurement uses the default sweep time of 1.67 ms. |
| RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the sweep time that you specify in the RFMXEVDO_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. |
| RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_TRUE (1) | The measurement uses the default sweep time of 1.67 ms. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_obw_sweep_time_interval.html language=enus -->
## TOPIC 00133: RFMXEVDO_ATTR_OBW_SWEEP_TIME_INTERVAL

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_obw_sweep_time_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_obw_sweep_time_interval.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_OBW_SWEEP_TIME_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeF64RFmxEVDO_GetAttributeF64 |
| Description: | Specifies the sweep time when you set the RFMXEVDO_ATTR_OBW_SWEEP_TIME_AUTO attribute to RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.00167 seconds. Get Function: RFmxEVDO_OBWGetSweepTimeInterval Set Function: RFmxEVDO_OBWSetSweepTimeInterval |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_physical_layer_subtype.html language=enus -->
## TOPIC 00134: RFMXEVDO_ATTR_PHYSICAL_LAYER_SUBTYPE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_physical_layer_subtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_physical_layer_subtype.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_PHYSICAL_LAYER_SUBTYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Selects the EV-DO physical layer subtype. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0,1. Get Function: RFmxEVDO_GetPhysicalLayerSubtype Set Function: RFmxEVDO_SetPhysicalLayerSubtype |
| Values: | RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_0_1 (0)Specifies subtype 0, 1. 3GPP2 C.S0024-B v3.0 defines this subtype in 10 DEFAULT (SUBTYPE 0) AND SUBTYPE 1 PHYSICAL LAYER PROTOCOL. RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_2 (1)Specifies subtype 2. 3GPP2 C.S0024-B v3.0 defines this subtype in 11 SUBTYPE 2 PHYSICAL LAYER. RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_3 (2)Specifies subtype 3. 3GPP2 C.S0024-B v3.0 defines this subtype in 12 SUBTYPE 3 PHYSICAL LAYER. |
| RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_0_1 (0) | Specifies subtype 0, 1. 3GPP2 C.S0024-B v3.0 defines this subtype in 10 DEFAULT (SUBTYPE 0) AND SUBTYPE 1 PHYSICAL LAYER PROTOCOL. |
| RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_2 (1) | Specifies subtype 2. 3GPP2 C.S0024-B v3.0 defines this subtype in 11 SUBTYPE 2 PHYSICAL LAYER. |
| RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_3 (2) | Specifies subtype 3. 3GPP2 C.S0024-B v3.0 defines this subtype in 12 SUBTYPE 3 PHYSICAL LAYER. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_reference_level.html language=enus -->
## TOPIC 00135: RFMXEVDO_ATTR_REFERENCE_LEVEL

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_reference_level.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_REFERENCE_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeF64RFmxEVDO_GetAttributeF64 |
| Description: | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default of this attribute is hardware dependent. Get Function: RFmxEVDO_GetReferenceLevel Set Function: RFmxEVDO_SetReferenceLevel |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_reference_level_headroom.html language=enus -->
## TOPIC 00136: RFMXEVDO_ATTR_REFERENCE_LEVEL_HEADROOM

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_reference_level_headroom.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_reference_level_headroom.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_REFERENCE_LEVEL_HEADROOM

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeF64RFmxEVDO_GetAttributeF64 |
| Description: | Specifies the margin RFmx adds to the RFMXEVDO_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow provided that the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise by reducing the Reference Level Headroom. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Valid values: PXIe-5668R: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxEVDO_GetReferenceLevelHeadroom Set Function: RFmxEVDO_SetReferenceLevelHeadroom |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_result_fetch_timeout.html language=enus -->
## TOPIC 00137: RFMXEVDO_ATTR_RESULT_FETCH_TIMEOUT

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_result_fetch_timeout.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_result_fetch_timeout.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_RESULT_FETCH_TIMEOUT

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeF64RFmxEVDO_GetAttributeF64 |
| Description: | Specifies the time to wait before results are available in the RFmx driver. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10 sec. Get Function: RFmxEVDO_GetResultFetchTimeout Set Function: RFmxEVDO_SetResultFetchTimeout |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_selected_ports.html language=enus -->
## TOPIC 00138: RFMXEVDO_ATTR_SELECTED_PORTS

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_selected_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_selected_ports.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SELECTED_PORTS

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeStringRFmxEVDO_GetAttributeString |
| Description: | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Valid values: PXIe-5830: if0, if1 Other devices: (empty string) PXIe-5831/5832: if0, if1, rf<0-1>/port, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values: PXIe-5830: if1 Other devices: (empty string) Get Function: RFmxEVDO_GetSelectedPorts Set Function: RFmxEVDO_SetSelectedPorts |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_all_traces_enabled.html language=enus -->
## TOPIC 00139: RFMXEVDO_ATTR_SEM_ALL_TRACES_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_all_traces_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the spectral emissions mask (SEM) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_SEMGetAllTracesEnabled Set Function: RFmxEVDO_SEMSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_averaging_count.html language=enus -->
## TOPIC 00140: RFMXEVDO_ATTR_SEM_AVERAGING_COUNT

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_averaging_count.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXEVDO_ATTR_SEM_AVERAGING_ENABLED attribute to RFMXEVDO_VAL_SEM_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxEVDO_SEMGetAveragingCount Set Function: RFmxEVDO_SEMSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_averaging_enabled.html language=enus -->
## TOPIC 00141: RFMXEVDO_ATTR_SEM_AVERAGING_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_averaging_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the spectral emissions mask (SEM) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_SEM_AVERAGING_ENABLED_FALSE. Get Function: RFmxEVDO_SEMGetAveragingEnabled Set Function: RFmxEVDO_SEMSetAveragingEnabled |
| Values: | RFMXEVDO_VAL_SEM_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXEVDO_VAL_SEM_AVERAGING_ENABLED_TRUE (1)The SEM measurement uses the RFMXEVDO_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |
| RFMXEVDO_VAL_SEM_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXEVDO_VAL_SEM_AVERAGING_ENABLED_TRUE (1) | The SEM measurement uses the RFMXEVDO_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_averaging_type.html language=enus -->
## TOPIC 00142: RFMXEVDO_ATTR_SEM_AVERAGING_TYPE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_averaging_type.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_SEM_AVERAGING_TYPE_RMS. Get Function: RFmxEVDO_SEMGetAveragingType Set Function: RFmxEVDO_SEMSetAveragingType |
| Values: | RFMXEVDO_VAL_SEM_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXEVDO_VAL_SEM_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. RFMXEVDO_VAL_SEM_AVERAGING_TYPE_SCALAR (2)The square root of the power spectrum is averaged. RFMXEVDO_VAL_SEM_AVERAGING_TYPE_MAXIMUM (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. RFMXEVDO_VAL_SEM_AVERAGING_TYPE_MINIMUM (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXEVDO_VAL_SEM_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXEVDO_VAL_SEM_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXEVDO_VAL_SEM_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |
| RFMXEVDO_VAL_SEM_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXEVDO_VAL_SEM_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_carrier_integration_bandwidth.html language=enus -->
## TOPIC 00143: RFMXEVDO_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_carrier_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_carrier_integration_bandwidth.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the SEM carrier integration bandwidth. This value is expressed in Hz. Use 'carrier(k)' as the selector string to read this result. Get Function: RFmxEVDO_SEMGetCarrierIntegrationBandwidth |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_measurement_enabled.html language=enus -->
## TOPIC 00144: RFMXEVDO_ATTR_SEM_MEASUREMENT_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_measurement_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the spectral emissions mask (SEM) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_SEMGetMeasurementEnabled Set Function: RFmxEVDO_SEMSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_number_of_analysis_threads.html language=enus -->
## TOPIC 00145: RFMXEVDO_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_number_of_analysis_threads.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the spectral emissions mask (SEM) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxEVDO_SEMGetNumberOfAnalysisThreads Set Function: RFmxEVDO_SEMSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_number_of_offsets.html language=enus -->
## TOPIC 00146: RFMXEVDO_ATTR_SEM_NUMBER_OF_OFFSETS

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_number_of_offsets.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_NUMBER_OF_OFFSETS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | Returns the number of SEM offset segments. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxEVDO_SEMGetNumberOfOffsets |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_offset_bandwidth_integral.html language=enus -->
## TOPIC 00147: RFMXEVDO_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_offset_bandwidth_integral.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_offset_bandwidth_integral.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | Returns the bandwidth integral for a specific offset segment. A bandwidth integral greater than 1 indicates that an RBW filter of narrower bandwidth is used for the offset segment measurement, and digital processing is used to achieve the RBW defined for the offset segment. Use the following equation to calculate the value of offset segment RBW: Offset segment RBW = RBW * BW integral. Get Function: RFmxEVDO_SEMGetOffsetBandwidthIntegral |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_offset_rbw_filter_bandwidth.html language=enus -->
## TOPIC 00148: RFMXEVDO_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_offset_rbw_filter_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_offset_rbw_filter_bandwidth.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxEVDO_SEMGetOffsetRBWFilterBandwidth |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_offset_rbw_filter_type.html language=enus -->
## TOPIC 00149: RFMXEVDO_ATTR_SEM_OFFSET_RBW_FILTER_TYPE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_offset_rbw_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_offset_rbw_filter_type.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_OFFSET_RBW_FILTER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | Returns the type of RBW filter used to sweep the offset segment. Get Function: RFmxEVDO_SEMGetOffsetRBWFilterType |
| Values: | RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED (0) The measurement does not use any RBW filtering. RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN (1)The RBW filter has a Gaussian response. RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT (2)The RBW filter has a flat response. RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_4 (3)The RBW filter has a response of a 4-pole synchronously tuned filter. RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_5 (4)The RBW filter has a response of a 5-pole synchronously tuned filter. |
| RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED (0) | The measurement does not use any RBW filtering. |
| RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN (1) | The RBW filter has a Gaussian response. |
| RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT (2) | The RBW filter has a flat response. |
| RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_4 (3) | The RBW filter has a response of a 4-pole synchronously tuned filter. |
| RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_5 (4) | The RBW filter has a response of a 5-pole synchronously tuned filter. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_offset_start_frequency.html language=enus -->
## TOPIC 00150: RFMXEVDO_ATTR_SEM_OFFSET_START_FREQUENCY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_offset_start_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_offset_start_frequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_OFFSET_START_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxEVDO_SEMGetOffsetStartFrequency |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_offset_stop_frequency.html language=enus -->
## TOPIC 00151: RFMXEVDO_ATTR_SEM_OFFSET_STOP_FREQUENCY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_offset_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_offset_stop_frequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_OFFSET_STOP_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxEVDO_SEMGetOffsetStopFrequency |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_carrier_absolute_integrated_power.html language=enus -->
## TOPIC 00152: RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_carrier_absolute_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_carrier_absolute_integrated_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the absolute carrier power measurement. This value is expressed in dBm. Use 'carrier(n)' as the selector string to read this result. Get Function: RFmxEVDO_SEMGetResultsCarrierAbsoluteIntegratedPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_carrier_absolute_peak_power.html language=enus -->
## TOPIC 00153: RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_carrier_absolute_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_carrier_absolute_peak_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the peak absolute carrier power. This value is expressed in dBm. Use 'carrier(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsCarrierAbsolutePeakPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_carrier_peak_frequency.html language=enus -->
## TOPIC 00154: RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_carrier_peak_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_carrier_peak_frequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz. Use 'carrier(n)' as the selector string to read this result. Get Function: RFmxEVDO_SEMGetResultsCarrierPeakFrequency |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_carrier_relative_integrated_power.html language=enus -->
## TOPIC 00155: RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_carrier_relative_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_carrier_relative_integrated_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the relative carrier power measurement. This value is expressed in dB. Use 'carrier(n)' as the selector string to read this result. Get Function: RFmxEVDO_SEMGetResultsCarrierRelativeIntegratedPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_composite_measurement_status.html language=enus -->
## TOPIC 00156: RFMXEVDO_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_composite_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_composite_measurement_status.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_SEMGetResultsCompositeMeasurementStatus |
| Values: | RFMXEVDO_VAL_SEM_MEASUREMENT_STATUS_FAIL (0)The measurement fails. RFMXEVDO_VAL_SEM_MEASUREMENT_STATUS_PASS (1)The measurement passes. |
| RFMXEVDO_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | The measurement fails. |
| RFMXEVDO_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | The measurement passes. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_lower_offset_absolute_integrated_power.html language=enus -->
## TOPIC 00157: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_lower_offset_absolute_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_lower_offset_absolute_integrated_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsLowerOffsetAbsoluteIntegratedPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_lower_offset_absolute_peak_power.html language=enus -->
## TOPIC 00158: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_lower_offset_absolute_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_lower_offset_absolute_peak_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsLowerOffsetAbsolutePeakPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_lower_offset_margin.html language=enus -->
## TOPIC 00159: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_lower_offset_margin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_lower_offset_margin.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsLowerOffsetMargin |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_lower_offset_margin_absolute_power.html language=enus -->
## TOPIC 00160: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_lower_offset_margin_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_lower_offset_margin_absolute_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsLowerOffsetMarginAbsolutePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_lower_offset_margin_frequency.html language=enus -->
## TOPIC 00161: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_lower_offset_margin_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_lower_offset_margin_frequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsLowerOffsetMarginFrequency |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_lower_offset_margin_relative_power.html language=enus -->
## TOPIC 00162: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_lower_offset_margin_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_lower_offset_margin_relative_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsLowerOffsetMarginRelativePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_lower_offset_measurement_status.html language=enus -->
## TOPIC 00163: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_lower_offset_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_lower_offset_measurement_status.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | Indicates the lower offset segment measurement status based on measurement limits and the failure criteria specified by the standard. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsLowerOffsetMeasurementStatus |
| Values: | RFMXEVDO_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL (0)The measurement fails. RFMXEVDO_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS (1)The measurement passes. |
| RFMXEVDO_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL (0) | The measurement fails. |
| RFMXEVDO_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS (1) | The measurement passes. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_lower_offset_peak_frequency.html language=enus -->
## TOPIC 00164: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_lower_offset_peak_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_lower_offset_peak_frequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsLowerOffsetPeakFrequency |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_lower_offset_relative_integrated_power.html language=enus -->
## TOPIC 00165: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_lower_offset_relative_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_lower_offset_relative_integrated_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsLowerOffsetRelativeIntegratedPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_lower_offset_relative_peak_power.html language=enus -->
## TOPIC 00166: RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_lower_offset_relative_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_lower_offset_relative_peak_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the peak power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsLowerOffsetRelativePeakPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_total_carrier_power.html language=enus -->
## TOPIC 00167: RFMXEVDO_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_total_carrier_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_total_carrier_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the total carrier power of the selected carrier. This value is expressed in dBm. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxEVDO_SEMGetResultsTotalCarrierPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_upper_offset_absolute_integrated_power.html language=enus -->
## TOPIC 00168: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_upper_offset_absolute_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_upper_offset_absolute_integrated_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxEVDO_SEMGetResultsUpperOffsetAbsoluteIntegratedPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_upper_offset_absolute_peak_power.html language=enus -->
## TOPIC 00169: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_upper_offset_absolute_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_upper_offset_absolute_peak_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the peak absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsUpperOffsetAbsolutePeakPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_upper_offset_margin.html language=enus -->
## TOPIC 00170: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_upper_offset_margin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_upper_offset_margin.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsUpperOffsetMargin |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_upper_offset_margin_absolute_power.html language=enus -->
## TOPIC 00171: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_upper_offset_margin_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_upper_offset_margin_absolute_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the power at which the margin occurred in the upper (positive) offset segment, relative to the integrated power of the reference carrier. This value is expressed in dBm. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsUpperOffsetMarginAbsolutePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_upper_offset_margin_frequency.html language=enus -->
## TOPIC 00172: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_upper_offset_margin_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_upper_offset_margin_frequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsUpperOffsetMarginFrequency |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_upper_offset_margin_relative_power.html language=enus -->
## TOPIC 00173: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_upper_offset_margin_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_upper_offset_margin_relative_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the power at which the margin occurred in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsUpperOffsetMarginRelativePower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_upper_offset_measurement_status.html language=enus -->
## TOPIC 00174: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_upper_offset_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_upper_offset_measurement_status.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeI32 |
| Description: | Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsUpperOffsetMeasurementStatus |
| Values: | RFMXEVDO_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL (0)The measurement fails. RFMXEVDO_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS (1)The measurement passes. |
| RFMXEVDO_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL (0) | The measurement fails. |
| RFMXEVDO_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS (1) | The measurement passes. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_upper_offset_peak_frequency.html language=enus -->
## TOPIC 00175: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_upper_offset_peak_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_upper_offset_peak_frequency.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsUpperOffsetPeakFrequency |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_upper_offset_relative_integrated_power.html language=enus -->
## TOPIC 00176: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_upper_offset_relative_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_upper_offset_relative_integrated_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxEVDO_SEMGetResultsUpperOffsetRelativeIntegratedPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_results_upper_offset_relative_peak_power.html language=enus -->
## TOPIC 00177: RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_results_upper_offset_relative_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_results_upper_offset_relative_peak_power.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use 'offset(n)' as the selector string to read this attribute. Get Function: RFmxEVDO_SEMGetResultsUpperOffsetRelativePeakPower |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_sweep_time_auto.html language=enus -->
## TOPIC 00178: RFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTO

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_sweep_time_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_sweep_time_auto.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_TRUE. Get Function: RFmxEVDO_SEMGetSweepTimeAuto Set Function: RFmxEVDO_SEMSetSweepTimeAuto |
| Values: | RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_FALSE (0)The measurement uses the default sweep time of 1.67 ms. RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_TRUE (1)The measurement calculates the sweep time using a default value. |
| RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_FALSE (0) | The measurement uses the default sweep time of 1.67 ms. |
| RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_TRUE (1) | The measurement calculates the sweep time using a default value. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_sem_sweep_time_interval.html language=enus -->
## TOPIC 00179: RFMXEVDO_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_sem_sweep_time_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_sem_sweep_time_interval.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SEM_SWEEP_TIME_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeF64RFmxEVDO_GetAttributeF64 |
| Description: | Specifies the sweep time when you set the RFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTO attribute to RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.00167 seconds. Get Function: RFmxEVDO_SEMGetSweepTimeInterval Set Function: RFmxEVDO_SEMSetSweepTimeInterval |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotphase_all_traces_enabled.html language=enus -->
## TOPIC 00180: RFMXEVDO_ATTR_SLOTPHASE_ALL_TRACES_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotphase_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotphase_all_traces_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPHASE_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the traces after performing the SlotPhase measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_SlotPhaseGetAllTracesEnabled Set Function: RFmxEVDO_SlotPhaseSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotphase_measurement_enabled.html language=enus -->
## TOPIC 00181: RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotphase_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotphase_measurement_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the SlotPhase measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_SlotPhaseGetMeasurementEnabled Set Function: RFmxEVDO_SlotPhaseSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotphase_measurement_length.html language=enus -->
## TOPIC 00182: RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotphase_measurement_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotphase_measurement_length.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 16. Get Function: RFmxEVDO_SlotPhaseGetMeasurementLength Set Function: RFmxEVDO_SlotPhaseSetMeasurementLength |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotphase_receive_filter_enabled.html language=enus -->
## TOPIC 00183: RFMXEVDO_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotphase_receive_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotphase_receive_filter_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable receive filtering. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_TRUE. Get Function: RFmxEVDO_SlotPhaseGetReceiveFilterEnabled Set Function: RFmxEVDO_SlotPhaseSetReceiveFilterEnabled |
| Values: | RFMXEVDO_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_FALSE (0)Receive filtering is disabled. RFMXEVDO_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_TRUE (1)Receive filtering is enabled. |
| RFMXEVDO_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_FALSE (0) | Receive filtering is disabled. |
| RFMXEVDO_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_TRUE (1) | Receive filtering is enabled. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotphase_results_maximum_half_slot_phase_discontinuity.html language=enus -->
## TOPIC 00184: RFMXEVDO_ATTR_SLOTPHASE_RESULTS_MAXIMUM_HALF_SLOT_PHASE_DISCONTINUITY

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotphase_results_maximum_half_slot_phase_discontinuity.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotphase_results_maximum_half_slot_phase_discontinuity.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPHASE_RESULTS_MAXIMUM_HALF_SLOT_PHASE_DISCONTINUITY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxEVDO_GetAttributeF64 |
| Description: | Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Get Function: RFmxEVDO_SlotPhaseGetResultsMaximumHalfSlotPhaseDiscontinuity |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotphase_spectrum_inverted.html language=enus -->
## TOPIC 00185: RFMXEVDO_ATTR_SLOTPHASE_SPECTRUM_INVERTED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotphase_spectrum_inverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotphase_spectrum_inverted.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPHASE_SPECTRUM_INVERTED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the signal spectrum is inverted. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_SLOTPHASE_SPECTRUM_INVERTED_FALSE. Get Function: RFmxEVDO_SlotPhaseGetSpectrumInverted Set Function: RFmxEVDO_SlotPhaseSetSpectrumInverted |
| Values: | RFMXEVDO_VAL_SLOTPHASE_SPECTRUM_INVERTED_FALSE (0)The spectrum is not inverted. RFMXEVDO_VAL_SLOTPHASE_SPECTRUM_INVERTED_TRUE (1)The spectrum is inverted. |
| RFMXEVDO_VAL_SLOTPHASE_SPECTRUM_INVERTED_FALSE (0) | The spectrum is not inverted. |
| RFMXEVDO_VAL_SLOTPHASE_SPECTRUM_INVERTED_TRUE (1) | The spectrum is inverted. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotphase_synchronization_mode.html language=enus -->
## TOPIC 00186: RFMXEVDO_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotphase_synchronization_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotphase_synchronization_mode.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the measurement is performed from the frame or the slot boundary. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME. Get Function: RFmxEVDO_SlotPhaseGetSynchronizationMode Set Function: RFmxEVDO_SlotPhaseSetSynchronizationMode |
| Values: | RFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME (0)The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_OFFSET slots from the frame boundary. RFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT (1)The slot boundary is detected and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_OFFSET slots from the slot boundary. |
| RFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_OFFSET slots from the frame boundary. |
| RFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_OFFSET slots from the slot boundary. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotpower_measurement_enabled.html language=enus -->
## TOPIC 00187: RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotpower_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotpower_measurement_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable the SlotPower measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_FALSE. Get Function: RFmxEVDO_SlotPowerGetMeasurementEnabled Set Function: RFmxEVDO_SlotPowerSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotpower_measurement_offset.html language=enus -->
## TOPIC 00188: RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotpower_measurement_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotpower_measurement_offset.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE attribute. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxEVDO_SlotPowerGetMeasurementOffset Set Function: RFmxEVDO_SlotPowerSetMeasurementOffset |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotpower_receive_filter_enabled.html language=enus -->
## TOPIC 00189: RFMXEVDO_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotpower_receive_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotpower_receive_filter_enabled.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether to enable receive filtering. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_TRUE. Get Function: RFmxEVDO_SlotPowerGetReceiveFilterEnabled Set Function: RFmxEVDO_SlotPowerSetReceiveFilterEnabled |
| Values: | RFMXEVDO_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_FALSE (0)Receive filtering is disabled. RFMXEVDO_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_TRUE (1)Receive filtering is enabled. |
| RFMXEVDO_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_FALSE (0) | Receive filtering is disabled. |
| RFMXEVDO_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_TRUE (1) | Receive filtering is enabled. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotpower_spectrum_inverted.html language=enus -->
## TOPIC 00190: RFMXEVDO_ATTR_SLOTPOWER_SPECTRUM_INVERTED

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotpower_spectrum_inverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotpower_spectrum_inverted.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPOWER_SPECTRUM_INVERTED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the signal spectrum is inverted. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_SLOTPOWER_SPECTRUM_INVERTED_FALSE. Get Function: RFmxEVDO_SlotPowerGetSpectrumInverted Set Function: RFmxEVDO_SlotPowerSetSpectrumInverted |
| Values: | RFMXEVDO_VAL_SLOTPOWER_SPECTRUM_INVERTED_FALSE (0)The spectrum is not inverted. RFMXEVDO_VAL_SLOTPOWER_SPECTRUM_INVERTED_TRUE (1)The spectrum is inverted. |
| RFMXEVDO_VAL_SLOTPOWER_SPECTRUM_INVERTED_FALSE (0) | The spectrum is not inverted. |
| RFMXEVDO_VAL_SLOTPOWER_SPECTRUM_INVERTED_TRUE (1) | The spectrum is inverted. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_slotpower_synchronization_mode.html language=enus -->
## TOPIC 00191: RFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_slotpower_synchronization_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_slotpower_synchronization_mode.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Specifies whether the measurement is performed from the frame or the slot boundary. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME. Get Function: RFmxEVDO_SlotPowerGetSynchronizationMode Set Function: RFmxEVDO_SlotPowerSetSynchronizationMode |
| Values: | RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME (0)The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the frame boundary. RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT (1)The slot boundary is detected and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the slot boundary. |
| RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the frame boundary. |
| RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by the RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the slot boundary. |

<!--NI_TOPIC bundle=rfmx-evdo-cvi path=rfmxevdo_attr_uplink_data_modulation_type.html language=enus -->
## TOPIC 00192: RFMXEVDO_ATTR_UPLINK_DATA_MODULATION_TYPE

- bundle_id: `rfmx-evdo-cvi`
- source_path: `rfmxevdo_attr_uplink_data_modulation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-cvi/raw/resource/enus/rfmxevdo_attr_uplink_data_modulation_type.html
- document_id: `rfmx-evdo-cvi`
- page_type: `leaf`
- content_type: ``

RFMXEVDO_ATTR_UPLINK_DATA_MODULATION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxEVDO_SetAttributeI32RFmxEVDO_GetAttributeI32 |
| Description: | Defines the modulation of the data channel. This attribute is used only when you set the RFMXEVDO_ATTR_CHANNEL_CONFIGURATION_MODE attribute to RFMXEVDO_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_AUTO. Get Function: RFmxEVDO_GetUplinkDataModulationType Set Function: RFmxEVDO_SetUplinkDataModulationType |
| Values: | RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_AUTO (0)Specifies that the measurement automatically detects the modulation type. RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_DATA_CHANNEL_ABSENT (1)Specifies that the data channel is absent. RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_B4 (2)Specifies binary phase shift keying (BPSK) with the Walsh function W(4,2). RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_Q4 (3)Specifies quadrature phase shift keying (QPSK) with the Walsh function W(4,2). RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_Q2 (4)Specifies QPSK with the Walsh function W(2,1). RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_Q4Q2 (5)Specifies QPSK with the Walsh functions W(4,2) and W(2,1). RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_E4E2 (6)Specifies 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |
| RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_AUTO (0) | Specifies that the measurement automatically detects the modulation type. |
| RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_DATA_CHANNEL_ABSENT (1) | Specifies that the data channel is absent. |
| RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_B4 (2) | Specifies binary phase shift keying (BPSK) with the Walsh function W(4,2). |
| RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_Q4 (3) | Specifies quadrature phase shift keying (QPSK) with the Walsh function W(4,2). |
| RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_Q2 (4) | Specifies QPSK with the Walsh function W(2,1). |
| RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_Q4Q2 (5) | Specifies QPSK with the Walsh functions W(4,2) and W(2,1). |
| RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_E4E2 (6) | Specifies 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |
