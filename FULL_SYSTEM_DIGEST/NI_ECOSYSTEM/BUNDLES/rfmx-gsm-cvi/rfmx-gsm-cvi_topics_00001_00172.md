# NI DOCUMENT BUNDLE: rfmx-gsm-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-gsm-cvi start=1 end=172 -->
<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_analyzeiq1waveform.html language=enus -->
## TOPIC 00001: RFmxGSM_AnalyzeIQ1Waveform

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_analyzeiq1waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_analyzeiq1waveform.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_AnalyzeIQ1Waveform

int32 __stdcall RFmxGSM_AnalyzeIQ1Waveform (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[],
 float64 x0,
 float64 dx,
 NIComplexSingle IQ[],
 int32 arraySize,
 int32 reset,
 int64 reserved);

#### Purpose

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?topicname=rfmxinstrcvi/rfmxinstr_attr_recommended_acquisition_type.html) attribute value is RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ.

|  | Note Query the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute after calling the RFmxGSM_Commit function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"""result::r1""r1" |
| x0 | float64 | Specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | float64 | Specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| IQ | NIComplexSingle[] | Specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_buildoffsetstring.html language=enus -->
## TOPIC 00002: RFmxGSM_BuildOffsetString

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_buildoffsetstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_buildoffsetstring.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_BuildOffsetString

int32 __stdcall RFmxGSM_BuildOffsetString (char selectorString[],
 int32 offsetNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a offset string to use as the selector string with configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| offsetNumber | int32 | Specifies the offset number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_buildslotstring.html language=enus -->
## TOPIC 00003: RFmxGSM_BuildSlotString

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_buildslotstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_buildslotstring.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_BuildSlotString

int32 __stdcall RFmxGSM_BuildSlotString (char selectorString[],
 int32 slotNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a slot string to use as the selector string with configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| slotNumber | int32 | Specifies the slot number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_cfgautotscdetectionenabled.html language=enus -->
## TOPIC 00004: RFmxGSM_CfgAutoTSCDetectionEnabled

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_cfgautotscdetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_cfgautotscdetectionenabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_CfgAutoTSCDetectionEnabled

int32 __stdcall RFmxGSM_CfgAutoTSCDetectionEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 autoTSCDetectionEnabled);

#### Purpose

Configures whether to auto detect the training sequence code (TSC).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| autoTSCDetectionEnabled | int32 | Specifies whether to auto detect the TSC. RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_FALSE (0) The measurement uses the value which you configure using the RFMXGSM_ATTR_TSC attribute.RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_TRUE (1) The measurement detects the TSC in the burst. |
| RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_FALSE (0) | The measurement uses the value which you configure using the RFMXGSM_ATTR_TSC attribute. |  |
| RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_TRUE (1) | The measurement detects the TSC in the burst. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_cfgburstsynchronizationtype.html language=enus -->
## TOPIC 00005: RFmxGSM_CfgBurstSynchronizationType

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_cfgburstsynchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_cfgburstsynchronizationtype.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_CfgBurstSynchronizationType

int32 __stdcall RFmxGSM_CfgBurstSynchronizationType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 burstSynchronizationType);

#### Purpose

Configures the burst synchronization type.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| burstSynchronizationType | int32 | Specifies the method used to synchronize the burst. RFMXGSM_VAL_BURST_SYNC_TYPE_TSC (0) Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC.RFMXGSM_VAL_BURST_SYNC_TYPE_AMPLITUDE (1) Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF Envelope. RFMXGSM_VAL_BURST_SYNC_TYPE_NONE (2) Sets the T0 point to 273.23 Âµsec after the trigger. |
| RFMXGSM_VAL_BURST_SYNC_TYPE_TSC (0) | Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. |  |
| RFMXGSM_VAL_BURST_SYNC_TYPE_AMPLITUDE (1) | Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF Envelope. |  |
| RFMXGSM_VAL_BURST_SYNC_TYPE_NONE (2) | Sets the T0 point to 273.23 Âµsec after the trigger. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_cfgfrequency.html language=enus -->
## TOPIC 00006: RFmxGSM_CfgFrequency

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_cfgfrequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_cfgfrequency.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_CfgFrequency

int32 __stdcall RFmxGSM_CfgFrequency (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 centerFrequency);

#### Purpose

Configures the center frequency of the RF signal to acquire.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| centerFrequency | float64 | Specifies the expected center frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_cfgfrequencyreference.html language=enus -->
## TOPIC 00007: RFmxGSM_CfgFrequencyReference

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_cfgfrequencyreference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_cfgfrequencyreference.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_CfgFrequencyReference

int32 __stdcall RFmxGSM_CfgFrequencyReference (niRFmxInstrHandle instrumentHandle,
 char channelName[],
 char frequencyReferenceSource[],
 float64 frequencyReferenceFrequency);

#### Purpose

Configures the Reference Clock and the frequency reference source.

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgFrequencyReference](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_cfgfrequencyreference.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| channelName | char[] | Set this parameter to "" (empty string) or NULL. |
| frequencyReferenceSource | char[] | Specifies the frequency reference source. RFMXGSM_VAL_ONBOARD_CLOCK_STR (OnboardClock) PXIe-5663/5663E: The RFmx driver locks the NI 5663/5663E to the NI 5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the NI 5652 to the NI 5622 CLK IN terminal. On versions of the NI 5663/5663E that lack a REF OUT2 connector on the NI 5652, connect the REF IN/OUT connector on the NI 5652 to the NI 5622 CLK IN terminal. PXIe-5665: The RFmx driver locks the NI 5665 to the NI 5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the NI 5653 to the NI 5622CLK IN terminal. PXIe-5668R: Lock the PXIe-5668R to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624R. PXIe-5644R/5645R/5646R: The RFmx driver locks the device to its onboard clock. RFMXGSM_VAL_REF_IN_STR (RefIn) PXIe-5663/5663E: Connect the external signal to the NI 5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the NI 5652 to the NI 5622 CLK IN terminal. PXIe-5665: Connect the external signal to the NI 5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the NI 5653 to the NI 5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal. PXIe-5668R: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal. PXIe-5644R/5645R/5646R: The RFmx driver locks the device to the signal at the external REF IN connector. RFMXGSM_VAL_PXI_CLK_STR(PXI_Clk) PXIe-5668R: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624R. PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665: The RFmx driver locks these devices to the PXI backplane clock. RFMXGSM_VAL_CLK_IN_STR (ClkIn) PXIe-5663/5663E: The RFmx driver locks the NI 5663/5663E to an external 10 MHz signal. Connect the external signal to the NI 5622 CLK IN connector, and connect the NI 5622 CLK OUT connector to the REF IN/OUT connector on the NI 5652. PXIe-5665: The RFmx driver locks the NI 5665 to an external 100 MHz signal. Connect the external signal to the NI 5622 CLK IN connector, and connect the NI 5622 CLK OUT connector to the REF IN connector on the NI 5653. Set the frequencyReferenceFrequency parameter to 100 MHz. PXIe-5668R: Lock the PXIe-5668R to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624R, and connect the PXIe-5624R CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz. PXIe-5644R/5645R/5646R: This configuration does not apply to the NI 5644R/5645R/5646R. |
| RFMXGSM_VAL_ONBOARD_CLOCK_STR (OnboardClock) | PXIe-5663/5663E: The RFmx driver locks the NI 5663/5663E to the NI 5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the NI 5652 to the NI 5622 CLK IN terminal. On versions of the NI 5663/5663E that lack a REF OUT2 connector on the NI 5652, connect the REF IN/OUT connector on the NI 5652 to the NI 5622 CLK IN terminal. PXIe-5665: The RFmx driver locks the NI 5665 to the NI 5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the NI 5653 to the NI 5622CLK IN terminal. PXIe-5668R: Lock the PXIe-5668R to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624R. PXIe-5644R/5645R/5646R: The RFmx driver locks the device to its onboard clock. |  |
| RFMXGSM_VAL_REF_IN_STR (RefIn) | PXIe-5663/5663E: Connect the external signal to the NI 5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the NI 5652 to the NI 5622 CLK IN terminal. PXIe-5665: Connect the external signal to the NI 5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the NI 5653 to the NI 5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal. PXIe-5668R: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal. PXIe-5644R/5645R/5646R: The RFmx driver locks the device to the signal at the external REF IN connector. |  |
| RFMXGSM_VAL_PXI_CLK_STR(PXI_Clk) | PXIe-5668R: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624R. PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665: The RFmx driver locks these devices to the PXI backplane clock. |  |
| RFMXGSM_VAL_CLK_IN_STR (ClkIn) | PXIe-5663/5663E: The RFmx driver locks the NI 5663/5663E to an external 10 MHz signal. Connect the external signal to the NI 5622 CLK IN connector, and connect the NI 5622 CLK OUT connector to the REF IN/OUT connector on the NI 5652. PXIe-5665: The RFmx driver locks the NI 5665 to an external 100 MHz signal. Connect the external signal to the NI 5622 CLK IN connector, and connect the NI 5622 CLK OUT connector to the REF IN connector on the NI 5653. Set the frequencyReferenceFrequency parameter to 100 MHz. PXIe-5668R: Lock the PXIe-5668R to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624R, and connect the PXIe-5624R CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz. PXIe-5644R/5645R/5646R: This configuration does not apply to the NI 5644R/5645R/5646R. |  |
| frequencyReferenceFrequency | float64 | Specifies the Reference Clock rate when you set the frequencyReferenceSource parameter to RFMXGSM_VAL_CLK_IN_STR or RFMXGSM_VAL_REF_IN_STR. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_cfglinkdirection.html language=enus -->
## TOPIC 00008: RFmxGSM_CfgLinkDirection

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_cfglinkdirection.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_cfglinkdirection.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_CfgLinkDirection

int32 __stdcall RFmxGSM_CfgLinkDirection (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 linkDirection);

#### Purpose

Configures the source of the signal to be measured.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| linkDirection | int32 | Specifies the source of the signal to be measured. RFMXGSM_VAL_LINK_DIRECTION_DOWNLINK (0) The source is a base transceiver station.RFMXGSM_VAL_LINK_DIRECTION_UPLINK (1) The source is a mobile station. |
| RFMXGSM_VAL_LINK_DIRECTION_DOWNLINK (0) | The source is a base transceiver station. |  |
| RFMXGSM_VAL_LINK_DIRECTION_UPLINK (1) | The source is a mobile station. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_cfgmechanicalattenuation.html language=enus -->
## TOPIC 00009: RFmxGSM_CfgMechanicalAttenuation

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_cfgmechanicalattenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_cfgmechanicalattenuation.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_CfgMechanicalAttenuation

int32 __stdcall RFmxGSM_CfgMechanicalAttenuation (niRFmxInstrHandle instrumentHandle,
 char channelName[],
 int32 mechanicalAttenuationAuto,
 float64 mechanicalAttenuationValue);

#### Purpose

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgMechanicalAttenuation](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_cfgmechanicalattenuation.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| channelName | char[] | Set this parameter to "" (empty string) or NULL. |
| mechanicalAttenuationAuto | int32 | Specifies whether the RFmx driver chooses an attenuation setting based on the hardware settings. RFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE(0) Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. RFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE(1) Specifies that the measurement computes the mechanical attenuation. |
| RFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE(0) | Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. |  |
| RFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE(1) | Specifies that the measurement computes the mechanical attenuation. |  |
| mechanicalAttenuationValue | float64 | Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_cfgreferencelevel.html language=enus -->
## TOPIC 00010: RFmxGSM_CfgReferenceLevel

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_cfgreferencelevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_cfgreferencelevel.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_CfgReferenceLevel

int32 __stdcall RFmxGSM_CfgReferenceLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 referenceLevel);

#### Purpose

Configures the reference level, which represents the maximum expected power of an RF input signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| referenceLevel | float64 | Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_cfgrf.html language=enus -->
## TOPIC 00011: RFmxGSM_CfgRF

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_cfgrf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_cfgrf.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_CfgRF

int32 __stdcall RFmxGSM_CfgRF (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| centerFrequency | float64 | Specifies the expected center frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| referenceLevel | float64 | Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| externalAttenuation | float64 | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the External Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_clearallnamedresults.html language=enus -->
## TOPIC 00012: RFmxGSM_ClearAllNamedResults

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_clearallnamedresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_clearallnamedresults.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ClearAllNamedResults

int32 __stdcall RFmxGSM_ClearAllNamedResults (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears all results for the signal that you specify in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_clearnamedresult.html language=enus -->
## TOPIC 00013: RFmxGSM_ClearNamedResult

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_clearnamedresult.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_clearnamedresult.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ClearNamedResult

int32 __stdcall RFmxGSM_ClearNamedResult (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears a result instance specified by the result name in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_clonesignalconfiguration.html language=enus -->
## TOPIC 00014: RFmxGSM_CloneSignalConfiguration

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_clonesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_clonesignalconfiguration.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_CloneSignalConfiguration

int32 __stdcall RFmxGSM_CloneSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char oldSignalName[],
 char newSignalName[]);

#### Purpose

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| oldSignalName | char[] | Specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::OldSigName""OldSigName" |
| newSignalName | char[] | Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_close.html language=enus -->
## TOPIC 00015: RFmxGSM_Close

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_close.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_close.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_Close

int32 __stdcall RFmxGSM_Close (niRFmxInstrHandle instrumentHandle, int32 forceDestroy);

#### Purpose

Closes the RFmx session.

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Close](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_close.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| forceDestroy | int32 | Specifies whether to destroy the RFmx session. RFMXGSM_VAL_FALSE (0) Destroys the RFmx session. Call the RFmxGSM_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. RFMXGSM_VAL_TRUE (1) Destroys the RFmx session. You do not have to call the RFmxGSM_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |
| RFMXGSM_VAL_FALSE (0) | Destroys the RFmx session. Call the RFmxGSM_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. |  |
| RFMXGSM_VAL_TRUE (1) | Destroys the RFmx session. You do not have to call the RFmxGSM_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_commit.html language=enus -->
## TOPIC 00016: RFmxGSM_Commit

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_commit.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_Commit

int32 __stdcall RFmxGSM_Commit (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Commits settings to the hardware. Calling this function is optional. RFmxGSM commits settings to the hardware when you call the [RFmxGSM_Initiate](/csh?topicname=rfmxgsmcvi/cvirfmxgsm_initiate.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_createsignalconfiguration.html language=enus -->
## TOPIC 00017: RFmxGSM_CreateSignalConfiguration

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_createsignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_createsignalconfiguration.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_CreateSignalConfiguration

int32 __stdcall RFmxGSM_CreateSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char signalName[]);

#### Purpose

Creates a new instance of a signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| signalName | char[] | Specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::sig1""sig1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_deletesignalconfiguration.html language=enus -->
## TOPIC 00018: RFmxGSM_DeleteSignalConfiguration

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_deletesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_deletesignalconfiguration.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_DeleteSignalConfiguration

int32 __stdcall RFmxGSM_DeleteSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char signalName[]);

#### Purpose

Deletes an instance of a signal that you specify in the **signalName** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| signalName | char[] | Specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::sig1""sig1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_disabletrigger.html language=enus -->
## TOPIC 00019: RFmxGSM_DisableTrigger

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_disabletrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_disabletrigger.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_DisableTrigger

int32 __stdcall RFmxGSM_DisableTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getallnamedresultnames.html language=enus -->
## TOPIC 00020: RFmxGSM_GetAllNamedResultNames

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getallnamedresultnames.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getallnamedresultnames.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAllNamedResultNames

int32 __stdcall RFmxGSM_GetAllNamedResultNames(
 niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultNames[],
 int32 resultNamesBufferSize,
 int32* actualResultNamesSize,
 int32* defaultResultExists
);

#### Purpose

Returns all the named result names of the signal that you specify in the Selector String parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| resultNamesBufferSize | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| Output |  |  |
| Name | Type | Description |
| resultNames | char[] | Returns the comma delimited result names. |
| actualResultNamesSize | int32* | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | int32* | Indicates whether the default result exists. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributef32.html language=enus -->
## TOPIC 00021: RFmxGSM_GetAttributeF32

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributef32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributef32.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeF32

int32 __stdcall RFmxGSM_GetAttributeF32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributef32array.html language=enus -->
## TOPIC 00022: RFmxGSM_GetAttributeF32Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributef32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributef32array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeF32Array

int32 __stdcall RFmxGSM_GetAttributeF32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributef64.html language=enus -->
## TOPIC 00023: RFmxGSM_GetAttributeF64

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributef64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributef64.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeF64

int32 __stdcall RFmxGSM_GetAttributeF64 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 *attrVal);

#### Purpose

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float64* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributef64array.html language=enus -->
## TOPIC 00024: RFmxGSM_GetAttributeF64Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributef64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributef64array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeF64Array

int32 __stdcall RFmxGSM_GetAttributeF64Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float64 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float64[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributei16.html language=enus -->
## TOPIC 00025: RFmxGSM_GetAttributeI16

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributei16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributei16.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeI16

int32 __stdcall RFmxGSM_GetAttributeI16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int16 *attrVal);

#### Purpose

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int16* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributei32.html language=enus -->
## TOPIC 00026: RFmxGSM_GetAttributeI32

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributei32.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeI32

int32 __stdcall RFmxGSM_GetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributei32array.html language=enus -->
## TOPIC 00027: RFmxGSM_GetAttributeI32Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributei32array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeI32Array

int32 __stdcall RFmxGSM_GetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int32 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int32[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributei64.html language=enus -->
## TOPIC 00028: RFmxGSM_GetAttributeI64

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributei64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributei64.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeI64

int32 __stdcall RFmxGSM_GetAttributeI64 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 *attrVal);

#### Purpose

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int64* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributei64array.html language=enus -->
## TOPIC 00029: RFmxGSM_GetAttributeI64Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributei64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributei64array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeI64Array

int32 __stdcall RFmxGSM_GetAttributeI64Array (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 attrVal[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int64[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributei8.html language=enus -->
## TOPIC 00030: RFmxGSM_GetAttributeI8

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributei8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributei8.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeI8

int32 __stdcall RFmxGSM_GetAttributeI8 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributei8array.html language=enus -->
## TOPIC 00031: RFmxGSM_GetAttributeI8Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributei8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributei8array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeI8Array

int32 __stdcall RFmxGSM_GetAttributeI8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributenicomplexdoublearray.html language=enus -->
## TOPIC 00032: RFmxGSM_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributenicomplexdoublearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributenicomplexdoublearray.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeNIComplexDoubleArray

int32 __stdcall RFmxGSM_GetAttributeNIComplexDoubleArray (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributenicomplexsinglearray.html language=enus -->
## TOPIC 00033: RFmxGSM_GetAttributeNIComplexSingleArray

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributenicomplexsinglearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributenicomplexsinglearray.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeNIComplexSingleArray

int32 __stdcall RFmxGSM_GetAttributeNIComplexSingleArray (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | NIComplexSingle[] | Returns the current value of the attribute. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributestring.html language=enus -->
## TOPIC 00034: RFmxGSM_GetAttributeString

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributestring.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeString

int32 __stdcall RFmxGSM_GetAttributeString (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[]);

#### Purpose

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributeu16.html language=enus -->
## TOPIC 00035: RFmxGSM_GetAttributeU16

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributeu16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributeu16.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeU16

int32 __stdcall RFmxGSM_GetAttributeU16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt16 *attrVal);

#### Purpose

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt16* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributeu32.html language=enus -->
## TOPIC 00036: RFmxGSM_GetAttributeU32

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributeu32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributeu32.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeU32

int32 __stdcall RFmxGSM_GetAttributeU32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributeu32array.html language=enus -->
## TOPIC 00037: RFmxGSM_GetAttributeU32Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributeu32array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeU32Array

int32 __stdcall RFmxGSM_GetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributeu64array.html language=enus -->
## TOPIC 00038: RFmxGSM_GetAttributeU64Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributeu64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributeu64array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeU64Array

int32 __stdcall RFmxGSM_GetAttributeU64Array (niRFmxInstrHandle instrumentHandle, 
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributeu8.html language=enus -->
## TOPIC 00039: RFmxGSM_GetAttributeU8

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributeu8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributeu8.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeU8

int32 __stdcall RFmxGSM_GetAttributeU8 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_getattributeu8array.html language=enus -->
## TOPIC 00040: RFmxGSM_GetAttributeU8Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_getattributeu8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_getattributeu8array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetAttributeU8Array

int32 __stdcall RFmxGSM_GetAttributeU8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_geterror.html language=enus -->
## TOPIC 00041: RFmxGSM_GetError

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_geterror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_geterror.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetError

int32 __stdcall RFmxGSM_GetError (niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[]);

#### Purpose

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter. 
 
If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For **Example**, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. 
 

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

|  | Note Use the RFmxGSM_GetErrorString function if the RFmxGSM_GetError function does not return an error message. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. If a valid session handle is passed, the last error stored in that session is retrieved. You can pass NULL to retrieve the last error stored in the current execution thread. |
| errorCode | int32* | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescriptionBufferSize | int32 | Passes the number of bytes in the char array you specify in the errorDescription parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize ? 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string. The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_geterrorstring.html language=enus -->
## TOPIC 00042: RFmxGSM_GetErrorString

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_geterrorstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_geterrorstring.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_GetErrorString

int32 __stdcall RFmxGSM_GetErrorString (niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[]);

#### Purpose

Converts a status code returned by an RFmxGSM function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter. 
 

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For **Example**, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. 
 

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| errorCode | int32* | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescriptionBufferSize | int32 | Passes the number of bytes in the char array you specify in the errorDescription parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize – 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string. The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_initialize.html language=enus -->
## TOPIC 00043: rfmxgsm_Initialize

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_initialize.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_Initialize

int32 __stdcall RFmxGSM_Initialize (char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession);

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
| isNewSession | int32* | Returns RFMXGSM_VAL_TRUE if the function created a new session, or RFMXGSM_VAL_FALSE if the function returned a reference to an existing session. |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Identifies your instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_initializefromnirfsasession.html language=enus -->
## TOPIC 00044: RFmxGSM_InitializeFromNIRFSASession

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_initializefromnirfsasession.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_initializefromnirfsasession.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_InitializeFromNIRFSASession

int32 __stdcall RFmxGSM_InitializeFromNIRFSASession (uInt32 NIRFSASession, niRFmxInstrHandle *handleOut);

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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_initiate.html language=enus -->
## TOPIC 00045: RFmxGSM_Initiate

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_initiate.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_Initiate

int32 __stdcall RFmxGSM_Initiate (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[]);

#### Purpose

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the [RFmxGSM_WaitforMeasurementComplete](/csh?topicname=rfmxgsmcvi/cvirfmxgsm_waitformeasurementcomplete.html) function or [RFmxGSM_CheckMeasurementStatus](/csh?topicname=rfmxgsmcvi/cvirfmxgsm_checkmeasurementstatus.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"""result::r1""r1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modacccfgaveraging.html language=enus -->
## TOPIC 00046: RFmxGSM_ModAccCfgAveraging

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modacccfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modacccfgaveraging.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccCfgAveraging

int32 __stdcall RFmxGSM_ModAccCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount);

#### Purpose

Configures averaging for the modulation accuracy (ModAcc) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_TRUE (1) The measurement is averaged over multiple acquisitions. |
| RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_TRUE (1) | The measurement is averaged over multiple acquisitions. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_TRUE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modacccfgdroopcompensationenabled.html language=enus -->
## TOPIC 00047: RFmxGSM_ModAccCfgDroopCompensationEnabled

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modacccfgdroopcompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modacccfgdroopcompensationenabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccCfgDroopCompensationEnabled

int32 __stdcall RFmxGSM_ModAccCfgDroopCompensationEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 droopCompensationEnabled);

#### Purpose

Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| droopCompensationEnabled | int32 | Specifies whether to enable droop compensation for the ModAcc measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_FALSE (0) Disables the power droop compensation in the EVM measurement. RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_TRUE (1) Enables the power droop compensation in the EVM measurement. |
| RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_FALSE (0) | Disables the power droop compensation in the EVM measurement. |  |
| RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_TRUE (1) | Enables the power droop compensation in the EVM measurement. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchconstellationtrace.html language=enus -->
## TOPIC 00048: RFmxGSM_ModAccFetchConstellationTrace

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchconstellationtrace.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchConstellationTrace

int32 __stdcall RFmxGSM_ModAccFetchConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle constellationTrace[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the constellation trace concatenated over all slots for the last acquisition.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| constellationTrace | NIComplexSingle[] | Returns the constellation trace concatenated over all slots for the last acquisition. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchconstellationtracesplit.html language=enus -->
## TOPIC 00049: RFmxGSM_ModAccFetchConstellationTraceSplit

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchconstellationtracesplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchconstellationtracesplit.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchConstellationTraceSplit

int32 __stdcall RFmxGSM_ModAccFetchConstellationTraceSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the constellation trace concatenated over all slots for the last acquisition.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| I | float32[] | Returns the real part of constellation trace concatenated over all slots for the last acquisition. |
| Q | float32[] | Returns the imaginary part of constellation trace concatenated over all slots for the last acquisition. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchdemodulatedbits.html language=enus -->
## TOPIC 00050: RFmxGSM_ModAccFetchDemodulatedBits

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchdemodulatedbits.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchdemodulatedbits.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchDemodulatedBits

int32 __stdcall RFmxGSM_ModAccFetchDemodulatedBits (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int8 demodulatedBits[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the array of demodulated bits concatenated over all slots for the last acquisition.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| demodulatedBits | int8[] | Returns an array of demodulated bits concatenated over all slots for the last acquisition. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchdetectedtsc.html language=enus -->
## TOPIC 00051: RFmxGSM_ModAccFetchDetectedTSC

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchdetectedtsc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchdetectedtsc.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchDetectedTSC

int32 __stdcall RFmxGSM_ModAccFetchDetectedTSC (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* detectedTSC);

#### Purpose

Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS. 
Use "slot<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and slot number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"slot0""signal::sig1/slot0""result::r1/slot0""signal::sig1/result::r1/slot0"You can use the RFmxGSM_BuildSlotString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| detectedTSC | int32* | Returns the detected TSC when you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to RFMXGSM_VAL_BURST_SYNC_TYPE_TSC. RFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN (-1) Burst synchronization is not found and measurements correspond to best estimate of synchronization. RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC0 (0) The detected TSC is TSC0.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC1 (1) The detected TSC is TSC1.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC2 (2) The detected TSC is TSC2.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC3 (3) The detected TSC is TSC3.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC4 (4) The detected TSC is TSC4.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC5 (5) The detected TSC is TSC5.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC6 (6) The detected TSC is TSC6.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC7 (7) The detected TSC is TSC7. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN (-1) | Burst synchronization is not found and measurements correspond to best estimate of synchronization. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC0 (0) | The detected TSC is TSC0. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC1 (1) | The detected TSC is TSC1. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC2 (2) | The detected TSC is TSC2. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC3 (3) | The detected TSC is TSC3. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC4 (4) | The detected TSC is TSC4. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC5 (5) | The detected TSC is TSC5. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC6 (6) | The detected TSC is TSC6. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC7 (7) | The detected TSC is TSC7. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchdetectedtscarray.html language=enus -->
## TOPIC 00052: RFmxGSM_ModAccFetchDetectedTSCArray

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchdetectedtscarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchdetectedtscarray.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchDetectedTSCArray

int32 __stdcall RFmxGSM_ModAccFetchDetectedTSCArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 detectedTSC[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| detectedTSC | int32[] | Returns an array of the detected TSCs when you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to RFMXGSM_VAL_BURST_SYNC_TYPE_TSC. RFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN (-1) The synchronization is not found and measurements correspond to best estimate of synchronization. RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC0 (0) The detected TSC is TSC0.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC1 (1) The detected TSC is TSC1.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC2 (2) The detected TSC is TSC2.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC3 (3) The detected TSC is TSC3.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC4 (4) The detected TSC is TSC4.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC5 (5) The detected TSC is TSC5.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC6 (6) The detected TSC is TSC6.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC7 (7) The detected TSC is TSC7. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN (-1) | The synchronization is not found and measurements correspond to best estimate of synchronization. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC0 (0) | The detected TSC is TSC0. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC1 (1) | The detected TSC is TSC1. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC2 (2) | The detected TSC is TSC2. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC3 (3) | The detected TSC is TSC3. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC4 (4) | The detected TSC is TSC4. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC5 (5) | The detected TSC is TSC5. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC6 (6) | The detected TSC is TSC6. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC7 (7) | The detected TSC is TSC7. |  |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchevm.html language=enus -->
## TOPIC 00053: RFmxGSM_ModAccFetchEVM

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchevm.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchEVM

int32 __stdcall RFmxGSM_ModAccFetchEVM (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* meanRMSEVM,
 float64* maximumRMSEVM,
 float64* meanPeakEVM,
 float64* maximumPeakEVM,
 float64* ninetyFifthPercentileEVM,
 float64* meanFrequencyError,
 int32* peakEVMSymbol);

#### Purpose

Fetches the EVM measurement results for EDGE/EGPRS.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanRMSEVM | float64* | Returns the mean of RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. |
| maximumRMSEVM | float64* | Returns the maximum of RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. |
| meanPeakEVM | float64* | Returns the mean of peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. |
| maximumPeakEVM | float64* | Returns the maximum of peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. |
| ninetyFifthPercentileEVM | float64* | Returns the EVM value, at which no more than 5 percent of the symbols have an EVM exceeding this value. This value is expressed as a percentage. |
| meanFrequencyError | float64* | Returns the mean of frequency error values measured over all acquisition time slots. This value is expressed in Hz. |
| peakEVMSymbol | int32* | Returns the symbol number in the burst measurement interval corresponding to the EVM value returned by the maximumPeakEVM parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchevmamplitudedroop.html language=enus -->
## TOPIC 00054: RFmxGSM_ModAccFetchEVMAmplitudeDroop

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchevmamplitudedroop.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchevmamplitudedroop.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchEVMAmplitudeDroop

int32 __stdcall RFmxGSM_ModAccFetchEVMAmplitudeDroop (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* meanAmplitudeDroop,
 float64* maximumAmplitudeDroop);

#### Purpose

Fetches the amplitude droop measurement results for EDGE/EGPRS.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanAmplitudeDroop | float64* | Returns the mean of amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. |
| maximumAmplitudeDroop | float64* | Returns the maximum of amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchevmmagnitudeerror.html language=enus -->
## TOPIC 00055: RFmxGSM_ModAccFetchEVMMagnitudeError

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchevmmagnitudeerror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchevmmagnitudeerror.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchEVMMagnitudeError

int32 __stdcall RFmxGSM_ModAccFetchEVMMagnitudeError (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* meanMagnitudeError,
 float64* maximumMagnitudeError);

#### Purpose

Fetches the magnitude error measurement results for EDGE/EGPRS.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanMagnitudeError | float64* | Returns the mean of RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. |
| maximumMagnitudeError | float64* | Returns the maximum of RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchevmphaseerror.html language=enus -->
## TOPIC 00056: RFmxGSM_ModAccFetchEVMPhaseError

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchevmphaseerror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchevmphaseerror.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchEVMPhaseError

int32 __stdcall RFmxGSM_ModAccFetchEVMPhaseError (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* meanPhaseError,
 float64* maximumPhaseError);

#### Purpose

Fetches the phase error measurement results for EDGE/EGPRS.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanPhaseError | float64* | Returns the mean of RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. |
| maximumPhaseError | float64* | Returns the maximum of RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchevmtrace.html language=enus -->
## TOPIC 00057: RFmxGSM_ModAccFetchEVMTrace

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchevmtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchevmtrace.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchEVMTrace

int32 __stdcall RFmxGSM_ModAccFetchEVMTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 EVM[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the EDGE/EGPRS RMS EVM trace concatenated over all slots for the last acquisition.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time, in seconds. |
| dx | float64* | Returns the sample duration, in seconds. |
| EVM | float32[] | Returns the EVM trace measured at each time instance. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchiqimpairments.html language=enus -->
## TOPIC 00058: RFmxGSM_ModAccFetchIQImpairments

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchiqimpairments.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchiqimpairments.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchIQImpairments

int32 __stdcall RFmxGSM_ModAccFetchIQImpairments (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* meanIQGainImbalance,
 float64* maximumIQGainImbalance,
 float64* meanIQOriginOffset,
 float64* maximumIQOriginOffset);

#### Purpose

Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanIQGainImbalance | float64* | Returns the mean of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| maximumIQGainImbalance | float64* | Returns the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| meanIQOriginOffset | float64* | Returns the mean of I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The measurement returns this result for GSM/EDGE/EGPRS. |
| maximumIQOriginOffset | float64* | Returns the maximum of I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The measurement returns this result for GSM/EDGE/EGPRS. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchmagnitudeerrortrace.html language=enus -->
## TOPIC 00059: RFmxGSM_ModAccFetchMagnitudeErrorTrace

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchmagnitudeerrortrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchmagnitudeerrortrace.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchMagnitudeErrorTrace

int32 __stdcall RFmxGSM_ModAccFetchMagnitudeErrorTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 magnitudeError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the EDGE/EGPRS magnitude error trace concatenated over all slots for the last acquisition.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time, in seconds. |
| dx | float64* | Returns the sample duration, in seconds. |
| magnitudeError | float32[] | Returns an array of magnitude error values measured at each time instance. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchpfer.html language=enus -->
## TOPIC 00060: RFmxGSM_ModAccFetchPFER

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchpfer.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchpfer.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchPFER

int32 __stdcall RFmxGSM_ModAccFetchPFER (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* meanRMSPhaseError,
 float64* maximumRMSPhaseError,
 float64* meanPeakPhaseError,
 float64* maximumPeakPhaseError,
 float64* meanFrequencyError,
 int32* peakSymbol);

#### Purpose

Fetches the phase and frequency error measurement results for GSM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| meanRMSPhaseError | float64* | Returns the mean of RMS phase error values measured over all acquisition time slots. This value is expressed in degrees. |
| maximumRMSPhaseError | float64* | Returns the maximum of RMS phase error values measured over all acquisition time slots. This value is expressed in degrees. |
| meanPeakPhaseError | float64* | Returns the mean of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. |
| maximumPeakPhaseError | float64* | Returns the maximum of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. |
| meanFrequencyError | float64* | Returns the mean of frequency error values measured over all acquisition time slots. This value is expressed in Hz. |
| peakSymbol | int32* | Returns the symbol number in the useful portion of the burst corresponding to phase error value in the maximumPeakPhaseError parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_modaccfetchphaseerrortrace.html language=enus -->
## TOPIC 00061: RFmxGSM_ModAccFetchPhaseErrorTrace

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_modaccfetchphaseerrortrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_modaccfetchphaseerrortrace.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ModAccFetchPhaseErrorTrace

int32 __stdcall RFmxGSM_ModAccFetchPhaseErrorTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 phaseError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the phase error trace concatenated over all slots for the last acquisition.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time, in seconds. |
| dx | float64* | Returns the sample duration, in symbols. |
| phaseError | float32[] | Returns an array of phase error values measured at each time instance. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfscfgaveraging.html language=enus -->
## TOPIC 00062: RFmxGSM_ORFSCfgAveraging

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfscfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfscfgaveraging.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSCfgAveraging

int32 __stdcall RFmxGSM_ORFSCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount,
 int32 averagingType);

#### Purpose

Configures averaging for the output radio frequency spectrum (ORFS) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_TRUE (1) The measurement is averaged over multiple acquisitions. |
| RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_TRUE (1) | The measurement is averaged over multiple acquisitions. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_TRUE. |
| averagingType | int32 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. RFMXGSM_VAL_ORFS_AVERAGING_TYPE_RMS (0) The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor.RFMXGSM_VAL_ORFS_AVERAGING_TYPE_LOG (1) The measurement averages the power spectrum in a logarithmic scale. |
| RFMXGSM_VAL_ORFS_AVERAGING_TYPE_RMS (0) | The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXGSM_VAL_ORFS_AVERAGING_TYPE_LOG (1) | The measurement averages the power spectrum in a logarithmic scale. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfscfgevaluationsymbols.html language=enus -->
## TOPIC 00063: RFmxGSM_ORFSCfgEvaluationSymbols

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfscfgevaluationsymbols.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfscfgevaluationsymbols.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSCfgEvaluationSymbols

int32 __stdcall RFmxGSM_ORFSCfgEvaluationSymbols (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 evaluationSymbolsStart,
 int32 evaluationSymbolsIncludeTSC,
 float64 evaluationSymbolsStop);

#### Purpose

Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify the portion of the burst to measure for ORFS due to modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| evaluationSymbolsStart | float64 | Specifies the start position of the burst over which you perform the ORFS measurement. This value is expressed as a percentage. |
| evaluationSymbolsIncludeTSC | int32 | Specifies whether to include the TSC portion of burst in the ORFS measurement. RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_FALSE (0) The TSC portion of the burst is excluded in the ORFS measurement. RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_TRUE (1) The TSC portion of the burst is included in the ORFS measurement. |
| RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_FALSE (0) | The TSC portion of the burst is excluded in the ORFS measurement. |  |
| RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_TRUE (1) | The TSC portion of the burst is included in the ORFS measurement. |  |
| evaluationSymbolsStop | float64 | Specifies the stop position of the burst over which you perform the ORFS measurement. This value is expressed as a percentage. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfscfgmeasurementtype.html language=enus -->
## TOPIC 00064: RFmxGSM_ORFSCfgMeasurementType

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfscfgmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfscfgmeasurementtype.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSCfgMeasurementType

int32 __stdcall RFmxGSM_ORFSCfgMeasurementType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 measurementType);

#### Purpose

Configures the type of spectral distortion to be measured.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| measurementType | int32 | Specifies the type of spectral distortion to be measured. RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION_AND_SWITCHING (0) Measures the spectrum on the modulated part and switching part of the waveform.RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION (1) Measures the spectrum on the modulated part of the waveform. RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_SWITCHING (2) Measures the spectrum on the switching part of the waveform. |
| RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION_AND_SWITCHING (0) | Measures the spectrum on the modulated part and switching part of the waveform. |  |
| RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION (1) | Measures the spectrum on the modulated part of the waveform. |  |
| RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_SWITCHING (2) | Measures the spectrum on the switching part of the waveform. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfscfgmodulationcustomoffsetfrequencyarray.html language=enus -->
## TOPIC 00065: RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfscfgmodulationcustomoffsetfrequencyarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfscfgmodulationcustomoffsetfrequencyarray.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray

int32 __stdcall RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float32 modulationCustomOffsetFrequency[],
 int32 arraySize);

#### Purpose

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the [RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE](/csh?topicname=rfmxgsmcvi/rfmxgsm_attr_orfs_offset_frequency_mode.html) attribute to RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_CUSTOM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| modulationCustomOffsetFrequency | float32[] | Specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of modulation when you set the RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE attribute to RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_CUSTOM. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfscfgnoisecompensationenabled.html language=enus -->
## TOPIC 00066: RFmxGSM_ORFSCfgNoiseCompensationEnabled

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfscfgnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfscfgnoisecompensationenabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSCfgNoiseCompensationEnabled

int32 __stdcall RFmxGSM_ORFSCfgNoiseCompensationEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 noiseCompensationEnabled);

#### Purpose

Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. 
**supportedDevices:** PXIe-5663/5665/5668R, PXIe-5830/5831/5832

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| noiseCompensationEnabled | int32 | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_FALSE (0) Disables compensation of the channel powers for the signal analyzer noise floor.RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_TRUE (1) Enables compensation of the channel powers for the signal analyzer noise floor. The measurement calculates the signal analyzer noise floor for the RF path used by the output radio frequency spectrum (ORFS) measurement and caches the noise floor for future use. If signal analyzer parameters or measurement parameters change, the measurement calculates noise floors again. |
| RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_FALSE (0) | Disables compensation of the channel powers for the signal analyzer noise floor. |  |
| RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_TRUE (1) | Enables compensation of the channel powers for the signal analyzer noise floor. The measurement calculates the signal analyzer noise floor for the RF path used by the output radio frequency spectrum (ORFS) measurement and caches the noise floor for future use. If signal analyzer parameters or measurement parameters change, the measurement calculates noise floors again. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfscfgoffsetfrequencymode.html language=enus -->
## TOPIC 00067: RFmxGSM_ORFSCfgOffsetFrequencyMode

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfscfgoffsetfrequencymode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfscfgoffsetfrequencymode.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSCfgOffsetFrequencyMode

int32 __stdcall RFmxGSM_ORFSCfgOffsetFrequencyMode (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 offsetFrequencyMode);

#### Purpose

Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| offsetFrequencyMode | int32 | Specifies the list of frequency offsets for which you can perform the ORFS measurements. RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_STANDARD (0) Uses a list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_SHORT (1) Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_CUSTOM (2) Uses the list of frequencies that is configured using the RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray and RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray functions for measurement of spectrum produced by modulation and switching measurements. |
| RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_STANDARD (0) | Uses a list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |  |
| RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_SHORT (1) | Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |  |
| RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_CUSTOM (2) | Uses the list of frequencies that is configured using the RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray and RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray functions for measurement of spectrum produced by modulation and switching measurements. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfscfgswitchingcustomoffsetfrequencyarray.html language=enus -->
## TOPIC 00068: RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfscfgswitchingcustomoffsetfrequencyarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfscfgswitchingcustomoffsetfrequencyarray.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray

int32 __stdcall RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float32 switchingCustomOffsetFrequency[],
 int32 arraySize);

#### Purpose

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the [RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE](/csh?topicname=rfmxgsmcvi/rfmxgsm_attr_orfs_offset_frequency_mode.html) attribute to RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_CUSTOM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| switchingCustomOffsetFrequency | float32[] | Specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of switching when you set the RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE attribute to RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_CUSTOM. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfsfetchmodulationpowertrace.html language=enus -->
## TOPIC 00069: RFmxGSM_ORFSFetchModulationPowerTrace

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfsfetchmodulationpowertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfsfetchmodulationpowertrace.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSFetchModulationPowerTrace

int32 __stdcall RFmxGSM_ORFSFetchModulationPowerTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 offsetFrequency[],
 float32 absolutePower[],
 float32 relativePower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the modulation power trace and frequency offset.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| offsetFrequency | float32[] | Returns an array of modulation offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz. |
| absolutePower | float32[] | Returns an array of absolute powers corresponding to the modulation offset frequency list. This value is expressed in dBm. |
| relativePower | float32[] | Returns an array of relative powers corresponding to modulation offset frequency list. This value is expressed in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfsfetchmodulationresultsarray.html language=enus -->
## TOPIC 00070: RFmxGSM_ORFSFetchModulationResultsArray

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfsfetchmodulationresultsarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfsfetchmodulationresultsarray.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSFetchModulationResultsArray

int32 __stdcall RFmxGSM_ORFSFetchModulationResultsArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* modulationCarrierPower,
 float64 lowerRelativePower[],
 float64 upperRelativePower[],
 float64 lowerAbsolutePower[],
 float64 upperAbsolutePower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| modulationCarrierPower | float64* | Returns the modulation carrier power. This value is expressed in dBm. |
| lowerRelativePower | float64[] | Returns an array of relative powers measured at the negative modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier. |
| upperRelativePower | float64[] | Returns an array of relative powers measured at the positive modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier. |
| lowerAbsolutePower | float64[] | Returns an array of absolute powers measured at the negative modulation offset frequencies. This value is expressed in dBm. |
| upperAbsolutePower | float64[] | Returns an array of absolute powers measured at the positive modulation offset frequencies. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfsfetchswitchingpowertrace.html language=enus -->
## TOPIC 00071: RFmxGSM_ORFSFetchSwitchingPowerTrace

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfsfetchswitchingpowertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfsfetchswitchingpowertrace.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSFetchSwitchingPowerTrace

int32 __stdcall RFmxGSM_ORFSFetchSwitchingPowerTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 offsetFrequency[],
 float32 absolutePower[],
 float32 relativePower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the switching power trace and frequency offsets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| offsetFrequency | float32[] | Returns an array of switching offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz. |
| absolutePower | float32[] | Returns an array of absolute powers corresponding to the switching offset frequency list. This value is expressed in dBm. |
| relativePower | float32[] | Returns an array of relative powers corresponding to the switching offset frequencies. This value is expressed in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_orfsfetchswitchingresultsarray.html language=enus -->
## TOPIC 00072: RFmxGSM_ORFSFetchSwitchingResultsArray

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_orfsfetchswitchingresultsarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_orfsfetchswitchingresultsarray.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ORFSFetchSwitchingResultsArray

int32 __stdcall RFmxGSM_ORFSFetchSwitchingResultsArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* switchingCarrierPower,
 float64 lowerRelativePower[],
 float64 upperRelativePower[],
 float64 lowerAbsolutePower[],
 float64 upperAbsolutePower[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| switchingCarrierPower | float64* | Returns the switching carrier power. This value is expressed in dBm. |
| lowerRelativePower | float64[] | Returns an array of relative powers measured at the negative switching offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated switching power of the carrier. |
| upperRelativePower | float64[] | Returns an array of relative powers measured at the positive switching offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated switching power of the carrier. |
| lowerAbsolutePower | float64[] | Returns an array of absolute powers measured at the negative switching offset frequencies. This value is expressed in dBm. |
| upperAbsolutePower | float64[] | Returns an array of absolute powers measured at the positive switching offset frequencies. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_pvtcfgaveraging.html language=enus -->
## TOPIC 00073: RFmxGSM_PVTCfgAveraging

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_pvtcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_pvtcfgaveraging.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_PVTCfgAveraging

int32 __stdcall RFmxGSM_PVTCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount,
 int32 averagingType);

#### Purpose

Configures averaging for the power versus time (PVT) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the measurement. RFMXGSM_VAL_PVT_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXGSM_VAL_PVT_AVERAGING_ENABLED_TRUE (1) The measurement is averaged over multiple acquisitions. |
| RFMXGSM_VAL_PVT_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXGSM_VAL_PVT_AVERAGING_ENABLED_TRUE (1) | The measurement is averaged over multiple acquisitions. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXGSM_VAL_PVT_AVERAGING_ENABLED_TRUE. |
| averagingType | int32 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. RFMXGSM_VAL_PVT_AVERAGING_TYPE_RMS (0) The power at each sample interval is linearly averaged from an acquisition to the next acquisition. RFMXGSM_VAL_PVT_AVERAGING_TYPE_LOG (1) The power at each sample interval is averaged on logarithmic scale from an acquisition to the next acquisition.RFMXGSM_VAL_PVT_AVERAGING_TYPE_MAXIMUM (3) The peak power at each sample interval is retained from an acquisition to the next acquisition.RFMXGSM_VAL_PVT_AVERAGING_TYPE_MINIMUM (4) The lowest power at each sample interval is retained from an acquisition to the next acquisition. |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_RMS (0) | The power at each sample interval is linearly averaged from an acquisition to the next acquisition. |  |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_LOG (1) | The power at each sample interval is averaged on logarithmic scale from an acquisition to the next acquisition. |  |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_MAXIMUM (3) | The peak power at each sample interval is retained from an acquisition to the next acquisition. |  |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_MINIMUM (4) | The lowest power at each sample interval is retained from an acquisition to the next acquisition. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_pvtfetchmeasurementstatus.html language=enus -->
## TOPIC 00074: RFmxGSM_PVTFetchMeasurementStatus

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_pvtfetchmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_pvtfetchmeasurementstatus.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_PVTFetchMeasurementStatus

int32 __stdcall RFmxGSM_PVTFetchMeasurementStatus (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* measurementStatus);

#### Purpose

Fetches the overall PVT measurement status based on the standard defined measurement limits.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1/result::r1""signal::sig1""result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| measurementStatus | int32* | Indicates the overall measurement status based on standard-defined limits. RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_FAIL (0) The measurement failed because the average power of at least one slot is outside the standard-defined limits.RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_PASS (1) The measurement passed because the average power of all slots is within the standard-defined limits. |
| RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_FAIL (0) | The measurement failed because the average power of at least one slot is outside the standard-defined limits. |  |
| RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_PASS (1) | The measurement passed because the average power of all slots is within the standard-defined limits. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_pvtfetchpowertrace.html language=enus -->
## TOPIC 00075: RFmxGSM_PVTFetchPowerTrace

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_pvtfetchpowertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_pvtfetchpowertrace.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_PVTFetchPowerTrace

int32 __stdcall RFmxGSM_PVTFetchPowerTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 upperMask[],
 float32 signalPower[],
 float32 lowerMask[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the upper mask, signal power, and lower mask trace.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1/result::r1""signal::sig1""result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time, in seconds. |
| dx | float64* | Returns the sample duration, in seconds. |
| upperMask | float32[] | Returns an array of upper mask values measured at each time instance. |
| signalPower | float32[] | Returns an array of signal power values measured at each time instance. |
| lowerMask | float32[] | Returns an array of lower mask values measured at each time instance. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_pvtfetchslotmeasurement.html language=enus -->
## TOPIC 00076: RFmxGSM_PVTFetchSlotMeasurement

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_pvtfetchslotmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_pvtfetchslotmeasurement.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_PVTFetchSlotMeasurement

int32 __stdcall RFmxGSM_PVTFetchSlotMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* slotAveragePower,
 float64* slotBurstWidth,
 int32* slotMeasurementStatus,
 float64* slotMaximumPower,
 float64* slotMinimumPower,
 float64* slotBurstThreshold);

#### Purpose

Fetches the measurement results for a single-slot PVT measurement. 
Use "slot<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and slot number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"slot0""signal::sig1/slot0""result::r1/slot0""signal::sig1/result::r1/slot0"You can use the RFmxGSM_BuildSlotString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| slotAveragePower | float64* | Returns the mean power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstWidth | float64* | Returns the burst width of the slot where the -3 dB transition points occur. This value is expressed in seconds. |
| slotMeasurementStatus | int32* | Indicates the PVT measurement status for a particular slot. RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL (0) The signal power is outside the standard-defined upper or lower maskRFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS (1) The signal power is within the standard-defined upper and lower mask. |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL (0) | The signal power is outside the standard-defined upper or lower mask |  |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS (1) | The signal power is within the standard-defined upper and lower mask. |  |
| slotMaximumPower | float64* | Returns the maximum power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotMinimumPower | float64* | Returns the minimum power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstThreshold | float64* | Returns the threshold that the PVT measurement uses to determine the burst validity. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_pvtfetchslotmeasurementarray.html language=enus -->
## TOPIC 00077: RFmxGSM_PVTFetchSlotMeasurementArray

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_pvtfetchslotmeasurementarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_pvtfetchslotmeasurementarray.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_PVTFetchSlotMeasurementArray

int32 __stdcall RFmxGSM_PVTFetchSlotMeasurementArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 slotAveragePower[],
 float64 slotBurstWidth[],
 int32 slotMeasurementStatus[],
 float64 slotMaximumPower[],
 float64 slotMinimumPower[],
 float64 slotBurstThreshold[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the PVT measurement results for each slot.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| slotAveragePower | float64[] | Returns an array of mean powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstWidth | float64[] | Returns an array of burst widths for the slots where the -3 dB transition points occur. This value is expressed in seconds. |
| slotMeasurementStatus | int32[] | Indicates an array of PVT measurement statuses for multiple slots. RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL (0) The signal power is outside the standard-defined upper or lower maskRFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS (1) The signal power is within the standard-defined upper and lower mask. |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL (0) | The signal power is outside the standard-defined upper or lower mask |  |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS (1) | The signal power is within the standard-defined upper and lower mask. |  |
| slotMaximumPower | float64[] | Returns an array of maximum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotMinimumPower | float64[] | Returns an array of minimum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstThreshold | float64[] | Returns an array of thresholds that the PVT measurement uses to determine the burst validity. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_resetattribute.html language=enus -->
## TOPIC 00078: RFmxGSM_ResetAttribute

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_resetattribute.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_resetattribute.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ResetAttribute

int32 __stdcall RFmxGSM_ResetAttribute (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID);

#### Purpose

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being reset. Refer to the selector string topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_resettodefault.html language=enus -->
## TOPIC 00079: RFmxGSM_ResetToDefault

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_resettodefault.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_resettodefault.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_ResetToDefault

int32 __stdcall RFmxGSM_ResetToDefault (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Resets a signal to the default values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_selectmeasurements.html language=enus -->
## TOPIC 00080: RFmxGSM_SelectMeasurements

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_selectmeasurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_selectmeasurements.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SelectMeasurements

int32 __stdcall RFmxGSM_SelectMeasurements (niRFmxInstrHandle instrumentHandle, 
 char selectorString[],
 uInt32 measurements,
 int32 enableAllTraces);

#### Purpose

Enables all the measurements that you specify in the **measurements** parameter and disables all other measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| measurements | uInt32 | Specifies the measurement to perform. You can specify one or more of the following measurements. |

| RFMXGSM_VAL_MEASUREMENT_MODACC (1) | Enables ModAcc measurement. |
| --- | --- |
| RFMXGSM_VAL_MEASUREMENT_ORFS (2) | Enables output radio frequency spectrum (ORFS) measurement. |
| RFMXGSM_VAL_MEASUREMENT_PVT (4) | Enables power versus time (PVT) measurement. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00081: RFmxGSM_SendSoftwareEdgeTrigger

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_sendsoftwareedgetrigger.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SendSoftwareEdgeTrigger

int32 __stdcall RFmxGSM_SendSoftwareEdgeTrigger (niRFmxInstrHandle instrumentHandle);

#### Purpose

Sends a trigger to the device when you use the [RFmxGSM_CfgSoftwareEdgeTrigger](/csh?topicname=rfmxgsmcvi/cvirfmxgsm_cfgsoftwareedgetrigger.html) function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. 
This function returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxGSM_Initiate function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributef32.html language=enus -->
## TOPIC 00082: RFmxGSM_SetAttributeF32

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributef32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributef32.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeF32

int32 __stdcall RFmxGSM_SetAttributeF32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributef32array.html language=enus -->
## TOPIC 00083: RFmxGSM_SetAttributeF32Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributef32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributef32array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeF32Array

int32 __stdcall RFmxGSM_SetAttributeF32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributef64.html language=enus -->
## TOPIC 00084: RFmxGSM_SetAttributeF64

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributef64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributef64.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeF64

int32 __stdcall RFmxGSM_SetAttributeF64 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal);

#### Purpose

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float64 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributef64array.html language=enus -->
## TOPIC 00085: RFmxGSM_SetAttributeF64Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributef64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributef64array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeF64Array

int32 __stdcall RFmxGSM_SetAttributeF64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributei16.html language=enus -->
## TOPIC 00086: RFmxGSM_SetAttributeI16

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributei16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributei16.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeI16

int32 __stdcall RFmxGSM_SetAttributeI16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int16 attrVal);

#### Purpose

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int16 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributei32.html language=enus -->
## TOPIC 00087: RFmxGSM_SetAttributeI32

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributei32.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeI32

int32 __stdcall RFmxGSM_SetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributei32array.html language=enus -->
## TOPIC 00088: RFmxGSM_SetAttributeI32Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributei32array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeI32Array

int32 __stdcall RFmxGSM_SetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributei64.html language=enus -->
## TOPIC 00089: RFmxGSM_SetAttributeI64

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributei64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributei64.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeI64

int32 __stdcall RFmxGSM_SetAttributeI64 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 attrVal);

#### Purpose

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int64 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributei64array.html language=enus -->
## TOPIC 00090: RFmxGSM_SetAttributeI64Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributei64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributei64array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeI64Array

int32 __stdcall RFmxGSM_SetAttributeI64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributei8.html language=enus -->
## TOPIC 00091: RFmxGSM_SetAttributeI8

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributei8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributei8.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeI8

int32 __stdcall RFmxGSM_SetAttributeI8 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int8 attrVal);

#### Purpose

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int8 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributei8array.html language=enus -->
## TOPIC 00092: RFmxGSM_SetAttributeI8Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributei8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributei8array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeI8Array

int32 __stdcall RFmxGSM_SetAttributeI8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributenicomplexdoublearray.html language=enus -->
## TOPIC 00093: RFmxGSM_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributenicomplexdoublearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributenicomplexdoublearray.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeNIComplexDoubleArray

int32 __stdcall RFmxGSM_SetAttributeNIComplexDoubleArray (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributenicomplexsinglearray.html language=enus -->
## TOPIC 00094: RFmxGSM_SetAttributeNIComplexSingleArray

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributenicomplexsinglearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributenicomplexsinglearray.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeNIComplexSingleArray

int32 __stdcall RFmxGSM_SetAttributeNIComplexSingleArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 NIComplexSingle attrVal[],
 int32 arraySize);

#### Purpose

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributestring.html language=enus -->
## TOPIC 00095: RFmxGSM_SetAttributeString

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributestring.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeString

int32 __stdcall RFmxGSM_SetAttributeString (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, char attrVal[]);

#### Purpose

Sets the value of an RFmx string attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | char[] | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributeu16.html language=enus -->
## TOPIC 00096: RFmxGSM_SetAttributeU16

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributeu16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributeu16.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeU16

int32 __stdcall RFmxGSM_SetAttributeU16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt16 attrVal);

#### Purpose

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt16 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributeu32.html language=enus -->
## TOPIC 00097: RFmxGSM_SetAttributeU32

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributeu32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributeu32.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeU32

int32 __stdcall RFmxGSM_SetAttributeU32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt32 attrVal);

#### Purpose

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt32 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributeu32array.html language=enus -->
## TOPIC 00098: RFmxGSM_SetAttributeU32Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributeu32array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeU32Array

int32 __stdcall RFmxGSM_SetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributeu64array.html language=enus -->
## TOPIC 00099: RFmxGSM_SetAttributeU64Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributeu64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributeu64array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeU64Array

int32 __stdcall RFmxGSM_SetAttributeU64Array (niRFmxInstrHandle instrumentHandle, 
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt64[] | Pass the value to which you want to set the attribute. Note Some of the values might not be valid depending on the current state of the instrument session. |
|  | Note Some of the values might not be valid depending on the current state of the instrument session. |  |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributeu8.html language=enus -->
## TOPIC 00100: RFmxGSM_SetAttributeU8

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributeu8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributeu8.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeU8

int32 __stdcall RFmxGSM_SetAttributeU8 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal);

#### Purpose

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt8 | Pass the value to which you want to set the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_setattributeu8array.html language=enus -->
## TOPIC 00101: RFmxGSM_SetAttributeU8Array

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_setattributeu8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_setattributeu8array.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_SetAttributeU8Array

int32 __stdcall RFmxGSM_SetAttributeU8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| attrVal | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_waitforacquisitioncomplete.html language=enus -->
## TOPIC 00102: RFmxGSM_WaitForAcquisitionComplete

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_waitforacquisitioncomplete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_waitforacquisitioncomplete.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_WaitForAcquisitionComplete

int32 __stdcall RFmxGSM_WaitForAcquisitionComplete (niRFmxInstrHandle instrumentHandle, float64 timeout);

#### Purpose

Waits and blocks the data flow until the acquisition is complete. This function is typically called after a specific initiate function. 
 


This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_waitforacquisitioncomplete.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=cvirfmxgsm_waitformeasurementcomplete.html language=enus -->
## TOPIC 00103: RFmxGSM_WaitForMeasurementComplete

- bundle_id: `rfmx-gsm-cvi`
- source_path: `cvirfmxgsm_waitformeasurementcomplete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/cvirfmxgsm_waitformeasurementcomplete.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFmxGSM_WaitForMeasurementComplete

int32 __stdcall RFmxGSM_WaitForMeasurementComplete (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout);

#### Purpose

Waits for the specified number for seconds for all the measurements to complete.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxGSM_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxGSM_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_auto_level_initial_reference_level.html language=enus -->
## TOPIC 00104: RFMXGSM_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_auto_level_initial_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_auto_level_initial_reference_level.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the initial reference level the RFmxGSM_AutoLevel function uses to estimate the peak power of the input signal. This value is expressed in dBm. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 30. Get Function: RFmxGSM_GetAutoLevelInitialReferenceLevel Set Function: RFmxGSM_SetAutoLevelInitialReferenceLevel |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_auto_tsc_detection_enabled.html language=enus -->
## TOPIC 00105: RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_auto_tsc_detection_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_auto_tsc_detection_enabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether the measurement automatically detects the training sequence code (TSC). You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_TRUE. Get Function: RFmxGSM_GetAutoTscDetectionEnabled Set Function: RFmxGSM_SetAutoTscDetectionEnabled |
| Values: | RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_FALSE (0)The measurement uses the value that you configure using the RFMXGSM_ATTR_RFMXGSM_ATTR_TSC attribute. RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_TRUE (1)The measurement detects the RFMXGSM_ATTR_TSC in the burst. |
| RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_FALSE (0) | The measurement uses the value that you configure using the RFMXGSM_ATTR_RFMXGSM_ATTR_TSC attribute. |
| RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_TRUE (1) | The measurement detects the RFMXGSM_ATTR_TSC in the burst. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_band.html language=enus -->
## TOPIC 00106: RFMXGSM_ATTR_BAND

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_band.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_band.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_BAND

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the operation band. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_BAND_PGSM. Get Function: RFmxGSM_GetBand Set Function: RFmxGSM_SetBand |
| Values: | RFMXGSM_VAL_BAND_PGSM (0)The operation band is Primary GSM in the 900 MHz band. RFMXGSM_VAL_BAND_EGSM (1)The operation band is Extended GSM in the 900 MHz band. RFMXGSM_VAL_BAND_RGSM (2)The operation band is Railway GSM in the 900 MHz band. RFMXGSM_VAL_BAND_DCS1800 (3)The operation band is GSM in the 1800 MHz band. RFMXGSM_VAL_BAND_PCS1900 (4)The operation band is GSM in the 1900 MHz band. RFMXGSM_VAL_BAND_GSM450 (5)The operation band is GSM in the 450 MHz band. RFMXGSM_VAL_BAND_GSM480 (6)The operation band is GSM in the 480 MHz band. RFMXGSM_VAL_BAND_GSM850 (7)The operation band is GSM in the 850 MHz band. RFMXGSM_VAL_BAND_GSM750 (8)The operation band is GSM in the 750 MHz band. RFMXGSM_VAL_BAND_TGSM810 (9)The operation band is terrestrial GSM in the 810 MHz band. |
| RFMXGSM_VAL_BAND_PGSM (0) | The operation band is Primary GSM in the 900 MHz band. |
| RFMXGSM_VAL_BAND_EGSM (1) | The operation band is Extended GSM in the 900 MHz band. |
| RFMXGSM_VAL_BAND_RGSM (2) | The operation band is Railway GSM in the 900 MHz band. |
| RFMXGSM_VAL_BAND_DCS1800 (3) | The operation band is GSM in the 1800 MHz band. |
| RFMXGSM_VAL_BAND_PCS1900 (4) | The operation band is GSM in the 1900 MHz band. |
| RFMXGSM_VAL_BAND_GSM450 (5) | The operation band is GSM in the 450 MHz band. |
| RFMXGSM_VAL_BAND_GSM480 (6) | The operation band is GSM in the 480 MHz band. |
| RFMXGSM_VAL_BAND_GSM850 (7) | The operation band is GSM in the 850 MHz band. |
| RFMXGSM_VAL_BAND_GSM750 (8) | The operation band is GSM in the 750 MHz band. |
| RFMXGSM_VAL_BAND_TGSM810 (9) | The operation band is terrestrial GSM in the 810 MHz band. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_burst_synchronization_type.html language=enus -->
## TOPIC 00107: RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_burst_synchronization_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_burst_synchronization_type.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the method used to synchronize the burst. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_BURST_SYNC_TYPE_TSC. Get Function: RFmxGSM_GetBurstSynchronizationType Set Function: RFmxGSM_SetBurstSynchronizationType |
| Values: | RFMXGSM_VAL_BURST_SYNC_TYPE_TSC (0)Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. RFMXGSM_VAL_BURST_SYNC_TYPE_AMPLITUDE (1)Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF envelope. RFMXGSM_VAL_BURST_SYNC_TYPE_NONE (2)Sets the T0 point to 273.23 microseconds after the trigger. |
| RFMXGSM_VAL_BURST_SYNC_TYPE_TSC (0) | Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. |
| RFMXGSM_VAL_BURST_SYNC_TYPE_AMPLITUDE (1) | Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF envelope. |
| RFMXGSM_VAL_BURST_SYNC_TYPE_NONE (2) | Sets the T0 point to 273.23 microseconds after the trigger. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_burst_type.html language=enus -->
## TOPIC 00108: RFMXGSM_ATTR_BURST_TYPE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_burst_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_burst_type.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_BURST_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the burst type. Use 'slot(n)' as the selector string to configure or read this attribute. The default value is RFMXGSM_VAL_BURST_TYPE_NB. Get Function: RFmxGSM_GetBurstType Set Function: RFmxGSM_SetBurstType |
| Values: | RFMXGSM_VAL_BURST_TYPE_NB (0)The burst type is Normal Burst. RFMXGSM_VAL_BURST_TYPE_HB (1)The burst type is Higher Symbol Rate Burst. RFMXGSM_VAL_BURST_TYPE_AB (2)The burst type is Access Burst. |
| RFMXGSM_VAL_BURST_TYPE_NB (0) | The burst type is Normal Burst. |
| RFMXGSM_VAL_BURST_TYPE_HB (1) | The burst type is Higher Symbol Rate Burst. |
| RFMXGSM_VAL_BURST_TYPE_AB (2) | The burst type is Access Burst. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_center_frequency.html language=enus -->
## TOPIC 00109: RFMXGSM_ATTR_CENTER_FREQUENCY

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_center_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_center_frequency.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_CENTER_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 890.2 MHz. Get Function: RFmxGSM_GetCenterFrequency Set Function: RFmxGSM_SetCenterFrequency |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_digital_edge_trigger_edge.html language=enus -->
## TOPIC 00110: RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_digital_edge_trigger_edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_digital_edge_trigger_edge.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the active edge for the trigger. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to RFMXGSM_VAL_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_DIGITAL_EDGE_RISING_EDGE. Get Function: RFmxGSM_GetDigitalEdgeTriggerEdge Set Function: RFmxGSM_SetDigitalEdgeTriggerEdge |
| Values: | RFMXGSM_VAL_DIGITAL_EDGE_RISING_EDGE (0)The trigger asserts on the rising edge of the signal. RFMXGSM_VAL_DIGITAL_EDGE_FALLING_EDGE (1)The trigger asserts on the falling edge of the signal. |
| RFMXGSM_VAL_DIGITAL_EDGE_RISING_EDGE (0) | The trigger asserts on the rising edge of the signal. |
| RFMXGSM_VAL_DIGITAL_EDGE_FALLING_EDGE (1) | The trigger asserts on the falling edge of the signal. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_digital_edge_trigger_source.html language=enus -->
## TOPIC 00111: RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_digital_edge_trigger_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_digital_edge_trigger_source.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeStringRFmxGSM_GetAttributeString |
| Description: | Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to RFMXGSM_VAL_TRIGGER_TYPE_DIGITAL_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default oof this attribute is hardware dependent. Get Function: RFmxGSM_GetDigitalEdgeTriggerSource Set Function: RFmxGSM_SetDigitalEdgeTriggerSource |
| Values: | RFMXGSM_VAL_PFI0_STR (PFI0)The trigger is received on PFI 0. RFMXGSM_VAL_PFI1_STR (PFI1)The trigger is received on PFI 1. RFMXGSM_VAL_PXI_TRIG0_STR (PXI_Trig0)The trigger is received on PXI trigger line 0. RFMXGSM_VAL_PXI_TRIG1_STR (PXI_Trig1)The trigger is received on PXI trigger line 1. RFMXGSM_VAL_PXI_TRIG2_STR (PXI_Trig2)The trigger is received on PXI trigger line 2. RFMXGSM_VAL_PXI_TRIG3_STR (PXI_Trig3)The trigger is received on PXI trigger line 3. RFMXGSM_VAL_PXI_TRIG4_STR (PXI_Trig4)The trigger is received on PXI trigger line 4. RFMXGSM_VAL_PXI_TRIG5_STR (PXI_Trig5)The trigger is received on PXI trigger line 5. RFMXGSM_VAL_PXI_TRIG6_STR (PXI_Trig6)The trigger is received on PXI trigger line 6. RFMXGSM_VAL_PXI_TRIG7_STR (PXI_Trig7)The trigger is received on PXI trigger line 7. RFMXGSM_VAL_PXI_STAR_STR (PXI_STAR)The trigger is received on the PXI star trigger line. RFMXGSM_VAL_PXIE_DSTARB_STR (PXIe_DStarB)The trigger is received on the PXIe DStar B trigger line. RFMXGSM_VAL_TIMER_EVENT_STR (TimerEvent)The trigger is received from the timer event. |
| RFMXGSM_VAL_PFI0_STR (PFI0) | The trigger is received on PFI 0. |
| RFMXGSM_VAL_PFI1_STR (PFI1) | The trigger is received on PFI 1. |
| RFMXGSM_VAL_PXI_TRIG0_STR (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| RFMXGSM_VAL_PXI_TRIG1_STR (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| RFMXGSM_VAL_PXI_TRIG2_STR (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| RFMXGSM_VAL_PXI_TRIG3_STR (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| RFMXGSM_VAL_PXI_TRIG4_STR (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| RFMXGSM_VAL_PXI_TRIG5_STR (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| RFMXGSM_VAL_PXI_TRIG6_STR (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| RFMXGSM_VAL_PXI_TRIG7_STR (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| RFMXGSM_VAL_PXI_STAR_STR (PXI_STAR) | The trigger is received on the PXI star trigger line. |
| RFMXGSM_VAL_PXIE_DSTARB_STR (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |
| RFMXGSM_VAL_TIMER_EVENT_STR (TimerEvent) | The trigger is received from the timer event. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_external_attenuation.html language=enus -->
## TOPIC 00112: RFMXGSM_ATTR_EXTERNAL_ATTENUATION

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_external_attenuation.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_EXTERNAL_ATTENUATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxGSM_GetExternalAttenuation Set Function: RFmxGSM_SetExternalAttenuation |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_hb_filter_width.html language=enus -->
## TOPIC 00113: RFMXGSM_ATTR_HB_FILTER_WIDTH

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_hb_filter_width.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_hb_filter_width.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_HB_FILTER_WIDTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the filter width when you set the RFMXGSM_ATTR_BURST_TYPE attribute to RFMXGSM_VAL_BURST_TYPE_HB. Use 'slot(n)' as the selector string to configure or read this attribute. The default value is RFMXGSM_VAL_HB_FILTER_WIDTH_NARROW. Get Function: RFmxGSM_GetHBFilterWidth Set Function: RFmxGSM_SetHBFilterWidth |
| Values: | RFMXGSM_VAL_HB_FILTER_WIDTH_NARROW (0)The measurement uses a narrow filter. RFMXGSM_VAL_HB_FILTER_WIDTH_WIDE (1)The measurement uses a wide filter. |
| RFMXGSM_VAL_HB_FILTER_WIDTH_NARROW (0) | The measurement uses a narrow filter. |
| RFMXGSM_VAL_HB_FILTER_WIDTH_WIDE (1) | The measurement uses a wide filter. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_iq_power_edge_trigger_level.html language=enus -->
## TOPIC 00114: RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_iq_power_edge_trigger_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_iq_power_edge_trigger_level.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE and in dBm when you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to RFMXGSM_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is -20 dB. Get Function: RFmxGSM_GetIQPowerEdgeTriggerLevel Set Function: RFmxGSM_SetIQPowerEdgeTriggerLevel |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_iq_power_edge_trigger_level_type.html language=enus -->
## TOPIC 00115: RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_iq_power_edge_trigger_level_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_iq_power_edge_trigger_level_type.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the reference for the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to RFMXGSM_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE. Get Function: RFmxGSM_GetIQPowerEdgeTriggerLevelType Set Function: RFmxGSM_SetIQPowerEdgeTriggerLevelType |
| Values: | RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0)The value of the IQ Power Edge Level attribute is relative to the value of the RFMXGSM_ATTR_REFERENCE_LEVEL attribute. RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1)The IQ Power Edge Level attribute specifies the absolute power. |
| RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0) | The value of the IQ Power Edge Level attribute is relative to the value of the RFMXGSM_ATTR_REFERENCE_LEVEL attribute. |
| RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1) | The IQ Power Edge Level attribute specifies the absolute power. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_iq_power_edge_trigger_slope.html language=enus -->
## TOPIC 00116: RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_iq_power_edge_trigger_slope.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_iq_power_edge_trigger_slope.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute with the slope you specify. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to RFMXGSM_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_IQ_POWER_EDGE_RISING_SLOPE. Get Function: RFmxGSM_GetIQPowerEdgeTriggerSlope Set Function: RFmxGSM_SetIQPowerEdgeTriggerSlope |
| Values: | RFMXGSM_VAL_IQ_POWER_EDGE_RISING_SLOPE (0)The trigger asserts when the signal power is rising. RFMXGSM_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1)The trigger asserts when the signal power is falling. |
| RFMXGSM_VAL_IQ_POWER_EDGE_RISING_SLOPE (0) | The trigger asserts when the signal power is rising. |
| RFMXGSM_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1) | The trigger asserts when the signal power is falling. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_iq_power_edge_trigger_source.html language=enus -->
## TOPIC 00117: RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_iq_power_edge_trigger_source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_iq_power_edge_trigger_source.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeStringRFmxGSM_GetAttributeString |
| Description: | Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to RFMXGSM_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default of this attribute is hardware dependent. Get Function: RFmxGSM_GetIQPowerEdgeTriggerSource Set Function: RFmxGSM_SetIQPowerEdgeTriggerSource |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_limited_configuration_change.html language=enus -->
## TOPIC 00118: RFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_limited_configuration_change.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_limited_configuration_change.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this property can help achieve faster measurements. When you set this attribute to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this attribute, you need to be aware of the limitations of this feature, which are listed in the Limitations of the RFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGE Attribute topic. You can also use this attribute to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr attributes from a locked configuration. NI recommends you use this attribute in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this attribute to a value other than Disabled for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this attribute if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality attributes while testing each device under test. RFmx automatically optimizes that use case. Specify the named signal configuration you are setting this attribute in the selector string input. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED. Get Function: RFmxGSM_GetLimitedConfigurationChange Set Function: RFmxGSM_SetLimitedConfigurationChange |
| Values: | RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED (0)This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE (1)Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY (2)Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and RFMXGSM_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL (3)Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXGSM_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL (4)Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, RFMXGSM_ATTR_REFERENCE_LEVEL, and RFMXGSM_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL (5)Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, RFMXGSM_ATTR_REFERENCE_LEVEL, and RFMXGSM_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED (0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE (1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY (2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and RFMXGSM_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL (3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXGSM_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL (4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, RFMXGSM_ATTR_REFERENCE_LEVEL, and RFMXGSM_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL (5) | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, RFMXGSM_ATTR_REFERENCE_LEVEL, and RFMXGSM_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Attribute topic for more details about the limitations of using this mode. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_link_direction.html language=enus -->
## TOPIC 00119: RFMXGSM_ATTR_LINK_DIRECTION

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_link_direction.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_link_direction.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_LINK_DIRECTION

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the source of the signal to be measured. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_LINK_DIRECTION_UPLINK. Get Function: RFmxGSM_GetLinkDirection Set Function: RFmxGSM_SetLinkDirection |
| Values: | RFMXGSM_VAL_LINK_DIRECTION_DOWNLINK (0)The source is a base transceiver station. RFMXGSM_VAL_LINK_DIRECTION_UPLINK (1)The source is a mobile station. |
| RFMXGSM_VAL_LINK_DIRECTION_DOWNLINK (0) | The source is a base transceiver station. |
| RFMXGSM_VAL_LINK_DIRECTION_UPLINK (1) | The source is a mobile station. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_all_traces_enabled.html language=enus -->
## TOPIC 00120: RFMXGSM_ATTR_MODACC_ALL_TRACES_ENABLED

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_all_traces_enabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_FALSE. Get Function: RFmxGSM_ModAccGetAllTracesEnabled Set Function: RFmxGSM_ModAccSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_averaging_count.html language=enus -->
## TOPIC 00121: RFMXGSM_ATTR_MODACC_AVERAGING_COUNT

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_averaging_count.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxGSM_ModAccGetAveragingCount Set Function: RFmxGSM_ModAccSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_averaging_enabled.html language=enus -->
## TOPIC 00122: RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_averaging_enabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_FALSE. Get Function: RFmxGSM_ModAccGetAveragingEnabled Set Function: RFmxGSM_ModAccSetAveragingEnabled |
| Values: | RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_TRUE (1)The measurement is averaged over multiple acquisitions. |
| RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_TRUE (1) | The measurement is averaged over multiple acquisitions. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_droop_compensation_enabled.html language=enus -->
## TOPIC 00123: RFMXGSM_ATTR_MODACC_DROOP_COMPENSATION_ENABLED

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_droop_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_droop_compensation_enabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_DROOP_COMPENSATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_FALSE. Get Function: RFmxGSM_ModAccGetDroopCompensationEnabled Set Function: RFmxGSM_ModAccSetDroopCompensationEnabled |
| Values: | RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_FALSE (0)Disables power droop compensation in the EVM measurement. RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_TRUE (1)Enables power droop compensation in the EVM measurement. |
| RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_FALSE (0) | Disables power droop compensation in the EVM measurement. |
| RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_TRUE (1) | Enables power droop compensation in the EVM measurement. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_measurement_enabled.html language=enus -->
## TOPIC 00124: RFMXGSM_ATTR_MODACC_MEASUREMENT_ENABLED

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_measurement_enabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_FALSE. Get Function: RFmxGSM_ModAccGetMeasurementEnabled Set Function: RFmxGSM_ModAccSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_number_of_analysis_threads.html language=enus -->
## TOPIC 00125: RFMXGSM_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_number_of_analysis_threads.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxGSM_ModAccGetNumberOfAnalysisThreads Set Function: RFmxGSM_ModAccSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_detected_tsc.html language=enus -->
## TOPIC 00126: RFMXGSM_ATTR_MODACC_RESULTS_DETECTED_TSC

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_detected_tsc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_detected_tsc.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_DETECTED_TSC

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeI32 |
| Description: | Returns the detected training sequence code (TSC) if you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to RFMXGSM_VAL_BURST_SYNC_TYPE_TSC. Use 'slot(n)' as the selector string to read this result. Get Function: RFmxGSM_ModAccGetResultsDetectedTSC |
| Values: | RFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN (-1)The synchronization is not found, and measurements correspond to best estimate of synchronization. RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC0 (0)The detected TSC is TSC0. RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC1 (1)The detected TSC is TSC1. RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC2 (2)The detected TSC is TSC2. RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC3 (3)The detected TSC is TSC3. RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC4 (4)The detected TSC is TSC4. RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC5 (5)The detected TSC is TSC5. RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC6 (6)The detected TSC is TSC6. RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC7 (7)The detected TSC is TSC7. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN (-1) | The synchronization is not found, and measurements correspond to best estimate of synchronization. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC0 (0) | The detected TSC is TSC0. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC1 (1) | The detected TSC is TSC1. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC2 (2) | The detected TSC is TSC2. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC3 (3) | The detected TSC is TSC3. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC4 (4) | The detected TSC is TSC4. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC5 (5) | The detected TSC is TSC5. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC6 (6) | The detected TSC is TSC6. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC7 (7) | The detected TSC is TSC7. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_evm_95th_percentile_evm.html language=enus -->
## TOPIC 00127: RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_EVM

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_evm_95th_percentile_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_evm_95th_percentile_evm.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsEVM95thpercentileEVM |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_evm_maximum_peak_evm.html language=enus -->
## TOPIC 00128: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_evm_maximum_peak_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_evm_maximum_peak_evm.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the maximum of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsEVMMaximumPeakEVM |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_evm_maximum_phase_error.html language=enus -->
## TOPIC 00129: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PHASE_ERROR

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_evm_maximum_phase_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_evm_maximum_phase_error.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PHASE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the maximum of the RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. The attribute returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsEVMMaximumPhaseError |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_evm_maximum_rms_evm.html language=enus -->
## TOPIC 00130: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_RMS_EVM

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_evm_maximum_rms_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_evm_maximum_rms_evm.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_RMS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the maximum of RMS values of EVM measured over all acquisition time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsEVMMaximumRMSEVM |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_evm_mean_amplitude_droop.html language=enus -->
## TOPIC 00131: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_AMPLITUDE_DROOP

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_evm_mean_amplitude_droop.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_evm_mean_amplitude_droop.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_AMPLITUDE_DROOP

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the mean of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The attribute returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsEVMMeanAmplitudeDroop |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_evm_mean_frequency_error.html language=enus -->
## TOPIC 00132: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_FREQUENCY_ERROR

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_evm_mean_frequency_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_evm_mean_frequency_error.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_FREQUENCY_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The attribute returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsEVMMeanFrequencyError |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_evm_mean_magnitude_error.html language=enus -->
## TOPIC 00133: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_MAGNITUDE_ERROR

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_evm_mean_magnitude_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_evm_mean_magnitude_error.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_MAGNITUDE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the mean of RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsEVMMeanMagnitudeError |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_evm_mean_rms_evm.html language=enus -->
## TOPIC 00134: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_RMS_EVM

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_evm_mean_rms_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_evm_mean_rms_evm.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_RMS_EVM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the mean of RMS values of EVM measured over all acquisition time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsEVMMeanRMSEVM |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_evm_peak_evm_symbol.html language=enus -->
## TOPIC 00135: RFMXGSM_ATTR_MODACC_RESULTS_EVM_PEAK_EVM_SYMBOL

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_evm_peak_evm_symbol.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_evm_peak_evm_symbol.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_EVM_PEAK_EVM_SYMBOL

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeI32 |
| Description: | Returns the symbol number in the useful portion of the burst corresponding to RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM result. The attribute returns this result for ModAcc EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsEVMPeakEVMSymbol |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_mean_iq_origin_offset.html language=enus -->
## TOPIC 00136: RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_mean_iq_origin_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_mean_iq_origin_offset.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the mean of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The attribute returns this result for GSM/EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsMeanIQOriginOffset |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_pfer_maximum_frequency_error.html language=enus -->
## TOPIC 00137: RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_FREQUENCY_ERROR

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_pfer_maximum_frequency_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_pfer_maximum_frequency_error.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_FREQUENCY_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The attribute returns this result for GSM ModAcc measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsPFERMaximumFrequencyError |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_pfer_mean_frequency_error.html language=enus -->
## TOPIC 00138: RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_FREQUENCY_ERROR

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_pfer_mean_frequency_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_pfer_mean_frequency_error.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_FREQUENCY_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The attribute returns this result for GSM ModAcc measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsPFERMeanFrequencyError |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_pfer_mean_peak_phase_error.html language=enus -->
## TOPIC 00139: RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_PEAK_PHASE_ERROR

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_pfer_mean_peak_phase_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_pfer_mean_peak_phase_error.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_PEAK_PHASE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the mean of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsPFERMeanPeakPhaseError |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_pfer_mean_rms_phase_error.html language=enus -->
## TOPIC 00140: RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_RMS_PHASE_ERROR

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_pfer_mean_rms_phase_error.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_pfer_mean_rms_phase_error.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_RMS_PHASE_ERROR

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the mean of RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsPFERMeanRMSPhaseError |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modacc_results_pfer_peak_phase_error_symbol.html language=enus -->
## TOPIC 00141: RFMXGSM_ATTR_MODACC_RESULTS_PFER_PEAK_PHASE_ERROR_SYMBOL

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modacc_results_pfer_peak_phase_error_symbol.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modacc_results_pfer_peak_phase_error_symbol.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODACC_RESULTS_PFER_PEAK_PHASE_ERROR_SYMBOL

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeI32 |
| Description: | Returns the symbol number in the useful portion of the burst corresponding to the phase error value in the RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERROR result. The attribute returns this result for GSM ModAcc measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. Get Function: RFmxGSM_ModAccGetResultsPFERPeakPhaseErrorSymbol |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_modulation_type.html language=enus -->
## TOPIC 00142: RFMXGSM_ATTR_MODULATION_TYPE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_modulation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_modulation_type.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_MODULATION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the modulation scheme used for the signal. Use 'slot(n)' as the selector string to configure or read this attribute. The default value is RFMXGSM_VAL_MODULATION_TYPE_8PSK. Get Function: RFmxGSM_GetModulationType Set Function: RFmxGSM_SetModulationType |
| Values: | RFMXGSM_VAL_MODULATION_TYPE_GMSK (0)The modulation type is Gaussian minimum shift keying. This value is valid only when you set the RFMXGSM_ATTR_BURST_TYPE attribute to RFMXGSM_VAL_BURST_TYPE_NB or RFMXGSM_VAL_BURST_TYPE_AB. RFMXGSM_VAL_MODULATION_TYPE_8PSK (1)The modulation type is 8-PSK. This value is valid only when you set the RFMXGSM_ATTR_BURST_TYPE attribute to NB. RFMXGSM_VAL_MODULATION_TYPE_QPSK (2)The modulation type is QPSK. This value is valid only when you set the RFMXGSM_ATTR_BURST_TYPE attribute to HB. RFMXGSM_VAL_MODULATION_TYPE_16QAM (3)The modulation type is 16-QAM. RFMXGSM_VAL_MODULATION_TYPE_32QAM (4)The modulation type is 32-QAM. |
| RFMXGSM_VAL_MODULATION_TYPE_GMSK (0) | The modulation type is Gaussian minimum shift keying. This value is valid only when you set the RFMXGSM_ATTR_BURST_TYPE attribute to RFMXGSM_VAL_BURST_TYPE_NB or RFMXGSM_VAL_BURST_TYPE_AB. |
| RFMXGSM_VAL_MODULATION_TYPE_8PSK (1) | The modulation type is 8-PSK. This value is valid only when you set the RFMXGSM_ATTR_BURST_TYPE attribute to NB. |
| RFMXGSM_VAL_MODULATION_TYPE_QPSK (2) | The modulation type is QPSK. This value is valid only when you set the RFMXGSM_ATTR_BURST_TYPE attribute to HB. |
| RFMXGSM_VAL_MODULATION_TYPE_16QAM (3) | The modulation type is 16-QAM. |
| RFMXGSM_VAL_MODULATION_TYPE_32QAM (4) | The modulation type is 32-QAM. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_number_of_timeslots.html language=enus -->
## TOPIC 00143: RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_number_of_timeslots.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_number_of_timeslots.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the number of time slots to be measured. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxGSM_GetNumberOfTimeslots Set Function: RFmxGSM_SetNumberOfTimeslots |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_orfs_evaluation_symbols_start.html language=enus -->
## TOPIC 00144: RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_START

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_orfs_evaluation_symbols_start.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_orfs_evaluation_symbols_start.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_START

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the start position within the useful part of the burst, in percentage, for measuring ORFS due to modulation. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 50. Get Function: RFmxGSM_ORFSGetEvaluationSymbolsStart Set Function: RFmxGSM_ORFSSetEvaluationSymbolsStart |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_orfs_evaluation_symbols_stop.html language=enus -->
## TOPIC 00145: RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_STOP

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_orfs_evaluation_symbols_stop.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_orfs_evaluation_symbols_stop.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_STOP

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the stop position within the useful part of the burst, in percentage, for measuring ORFS due to modulation. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 90. Get Function: RFmxGSM_ORFSGetEvaluationSymbolsStop Set Function: RFmxGSM_ORFSSetEvaluationSymbolsStop |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_orfs_measurement_enabled.html language=enus -->
## TOPIC 00146: RFMXGSM_ATTR_ORFS_MEASUREMENT_ENABLED

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_orfs_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_orfs_measurement_enabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_ORFS_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether to enable the output radio frequency spectrum (ORFS) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_FALSE. Get Function: RFmxGSM_ORFSGetMeasurementEnabled Set Function: RFmxGSM_ORFSSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_orfs_modulation_offset_rbw.html language=enus -->
## TOPIC 00147: RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_RBW

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_orfs_modulation_offset_rbw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_orfs_modulation_offset_rbw.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_RBW

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Specifies the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz. Use 'offset(n)' as the selector string to configure or read this attribute. The default value is 30000. Get Function: RFmxGSM_ORFSGetModulationOffsetRBW |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_orfs_noise_compensation_enabled.html language=enus -->
## TOPIC 00148: RFMXGSM_ATTR_ORFS_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_orfs_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_orfs_noise_compensation_enabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_ORFS_NOISE_COMPENSATION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_FALSE. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832 Get Function: RFmxGSM_ORFSGetNoiseCompensationEnabled Set Function: RFmxGSM_ORFSSetNoiseCompensationEnabled |
| Values: | RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_FALSE (0)Disables compensation of the channel powers for the signal analyzer noise floor. RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_TRUE (1)Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the output radio frequency spectrum (ORFS) measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. |
| RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_FALSE (0) | Disables compensation of the channel powers for the signal analyzer noise floor. |
| RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_TRUE (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the output radio frequency spectrum (ORFS) measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_orfs_number_of_analysis_threads.html language=enus -->
## TOPIC 00149: RFMXGSM_ATTR_ORFS_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_orfs_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_orfs_number_of_analysis_threads.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_ORFS_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxGSM_ORFSGetNumberOfAnalysisThreads Set Function: RFmxGSM_ORFSSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_orfs_switching_number_of_offsets.html language=enus -->
## TOPIC 00150: RFMXGSM_ATTR_ORFS_SWITCHING_NUMBER_OF_OFFSETS

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_orfs_switching_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_orfs_switching_number_of_offsets.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_ORFS_SWITCHING_NUMBER_OF_OFFSETS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxGSM_ORFSGetSwitchingNumberOfOffsets Set Function: RFmxGSM_ORFSSetSwitchingNumberOfOffsets |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_orfs_switching_offset_frequency.html language=enus -->
## TOPIC 00151: RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_FREQUENCY

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_orfs_switching_offset_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_orfs_switching_offset_frequency.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_FREQUENCY

| Data Type: | float32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF32RFmxGSM_GetAttributeF32 |
| Description: | Specifies the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. Use 'offset(n)' as the selector string to configure or read this attribute. The default value is 0. Get Function: RFmxGSM_ORFSGetSwitchingOffsetFrequency Set Function: RFmxGSM_ORFSSetSwitchingOffsetFrequency |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_pvt_all_traces_enabled.html language=enus -->
## TOPIC 00152: RFMXGSM_ATTR_PVT_ALL_TRACES_ENABLED

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_pvt_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_pvt_all_traces_enabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_PVT_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. The default value is RFMXGSM_VAL_FALSE. Get Function: RFmxGSM_PVTGetAllTracesEnabled Set Function: RFmxGSM_PVTSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_pvt_averaging_count.html language=enus -->
## TOPIC 00153: RFMXGSM_ATTR_PVT_AVERAGING_COUNT

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_pvt_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_pvt_averaging_count.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_PVT_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_PVT_AVERAGING_ENABLED attribute to RFMXGSM_VAL_PVT_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxGSM_PVTGetAveragingCount Set Function: RFmxGSM_PVTSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_pvt_averaging_enabled.html language=enus -->
## TOPIC 00154: RFMXGSM_ATTR_PVT_AVERAGING_ENABLED

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_pvt_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_pvt_averaging_enabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_PVT_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the power versus time (PVT) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_PVT_AVERAGING_ENABLED_FALSE. Get Function: RFmxGSM_PVTGetAveragingEnabled Set Function: RFmxGSM_PVTSetAveragingEnabled |
| Values: | RFMXGSM_VAL_PVT_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXGSM_VAL_PVT_AVERAGING_ENABLED_TRUE (1)The measurement is averaged over multiple acquisitions. |
| RFMXGSM_VAL_PVT_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXGSM_VAL_PVT_AVERAGING_ENABLED_TRUE (1) | The measurement is averaged over multiple acquisitions. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_pvt_averaging_type.html language=enus -->
## TOPIC 00155: RFMXGSM_ATTR_PVT_AVERAGING_TYPE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_pvt_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_pvt_averaging_type.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_PVT_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the averaging type for multiple acquisitions. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_PVT_AVERAGING_TYPE_RMS. Get Function: RFmxGSM_PVTGetAveragingType Set Function: RFmxGSM_PVTSetAveragingType |
| Values: | RFMXGSM_VAL_PVT_AVERAGING_TYPE_RMS (0)The power at each sample interval is linearly averaged from one acquisition to the next acquisition. RFMXGSM_VAL_PVT_AVERAGING_TYPE_LOG (1)The power at each sample interval is averaged on a logarithmic scale from one acquisition to the next acquisition. RFMXGSM_VAL_PVT_AVERAGING_TYPE_MAXIMUM (3)The peak power at each sample interval is retained from one acquisition to the next acquisition. RFMXGSM_VAL_PVT_AVERAGING_TYPE_MINIMUM (4)The lowest power at each sample interval is retained from one acquisition to the next acquisition. |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_RMS (0) | The power at each sample interval is linearly averaged from one acquisition to the next acquisition. |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_LOG (1) | The power at each sample interval is averaged on a logarithmic scale from one acquisition to the next acquisition. |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_MAXIMUM (3) | The peak power at each sample interval is retained from one acquisition to the next acquisition. |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_MINIMUM (4) | The lowest power at each sample interval is retained from one acquisition to the next acquisition. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_pvt_measurement_enabled.html language=enus -->
## TOPIC 00156: RFMXGSM_ATTR_PVT_MEASUREMENT_ENABLED

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_pvt_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_pvt_measurement_enabled.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_PVT_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether to enable the power versus time (PVT) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_FALSE. Get Function: RFmxGSM_PVTGetMeasurementEnabled Set Function: RFmxGSM_PVTSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_pvt_number_of_analysis_threads.html language=enus -->
## TOPIC 00157: RFMXGSM_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_pvt_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_pvt_number_of_analysis_threads.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxGSM_PVTGetNumberOfAnalysisThreads Set Function: RFmxGSM_PVTSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_pvt_rbw_filter_bandwidth.html language=enus -->
## TOPIC 00158: RFMXGSM_ATTR_PVT_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_pvt_rbw_filter_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_pvt_rbw_filter_bandwidth.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_PVT_RBW_FILTER_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the RBW Filter Bandwidth in Hz The default value is 500 kHz Get Function: RFmxGSM_PVTGetRbwFilterBandwidth Set Function: RFmxGSM_PVTSetRbwFilterBandwidth |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_pvt_results_slot_maximum_power.html language=enus -->
## TOPIC 00159: RFMXGSM_ATTR_PVT_RESULTS_SLOT_MAXIMUM_POWER

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_pvt_results_slot_maximum_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_pvt_results_slot_maximum_power.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_PVT_RESULTS_SLOT_MAXIMUM_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use 'slot(n)' as the selector string to read this attribute. Get Function: RFmxGSM_PVTGetResultsSlotMaximumPower |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_pvt_results_slot_measurement_status.html language=enus -->
## TOPIC 00160: RFMXGSM_ATTR_PVT_RESULTS_SLOT_MEASUREMENT_STATUS

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_pvt_results_slot_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_pvt_results_slot_measurement_status.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_PVT_RESULTS_SLOT_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeI32 |
| Description: | Indicates the power versus time (PVT) measurement status for a particular slot. Use 'slot(n)' as the selector string to read this attribute. Get Function: RFmxGSM_PVTGetResultsSlotMeasurementStatus |
| Values: | RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL (0)The average power for at least one slot is outside the standard-defined limits. RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS (1)The average power for each slot is within the standard-defined limits. |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL (0) | The average power for at least one slot is outside the standard-defined limits. |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS (1) | The average power for each slot is within the standard-defined limits. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_pvt_results_slot_minimum_power.html language=enus -->
## TOPIC 00161: RFMXGSM_ATTR_PVT_RESULTS_SLOT_MINIMUM_POWER

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_pvt_results_slot_minimum_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_pvt_results_slot_minimum_power.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_PVT_RESULTS_SLOT_MINIMUM_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxGSM_GetAttributeF64 |
| Description: | Returns the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use 'slot(n)' as the selector string to read this attribute. Get Function: RFmxGSM_PVTGetResultsSlotMinimumPower |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_reference_level.html language=enus -->
## TOPIC 00162: RFMXGSM_ATTR_REFERENCE_LEVEL

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_reference_level.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_REFERENCE_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxGSM_GetReferenceLevel Set Function: RFmxGSM_SetReferenceLevel |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_reference_level_headroom.html language=enus -->
## TOPIC 00163: RFMXGSM_ATTR_REFERENCE_LEVEL_HEADROOM

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_reference_level_headroom.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_reference_level_headroom.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_REFERENCE_LEVEL_HEADROOM

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the margin RFmx adds to the RFMXGSM_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow provided that the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise by reducing the Reference Level Headroom. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Valid values: PXIe-5668R: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860 Get Function: RFmxGSM_GetReferenceLevelHeadroom Set Function: RFmxGSM_SetReferenceLevelHeadroom |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_result_fetch_timeout.html language=enus -->
## TOPIC 00164: RFMXGSM_ATTR_RESULT_FETCH_TIMEOUT

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_result_fetch_timeout.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_result_fetch_timeout.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_RESULT_FETCH_TIMEOUT

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the time to wait before results are available in the RFmxGSM_AttributeNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxGSM Attribute Node waits until the measurement is complete. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxGSM_GetResultFetchTimeout Set Function: RFmxGSM_SetResultFetchTimeout |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_selected_ports.html language=enus -->
## TOPIC 00165: RFMXGSM_ATTR_SELECTED_PORTS

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_selected_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_selected_ports.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_SELECTED_PORTS

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeStringRFmxGSM_GetAttributeString |
| Description: | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Valid values: PXIe-5830: if0, if1 Other devices: (empty string) PXIe-5831/5832: if0, if1, rf<0-1>/port, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values: PXIe-5830: if1 Other devices: (empty string) Get Function: RFmxGSM_GetSelectedPorts Set Function: RFmxGSM_SetSelectedPorts |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_signal_structure.html language=enus -->
## TOPIC 00166: RFMXGSM_ATTR_SIGNAL_STRUCTURE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_signal_structure.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_signal_structure.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_SIGNAL_STRUCTURE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the RFMXGSM_ATTR_TRIGGER_TYPE to RFMXGSM_VAL_TRIGGER_TYPE_IQ_POWER_EDGE and RFMXGSM_VAL_TRIGGER_TYPE_NONE, respectively. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_SIGNAL_STRUCTURE_BURSTED. Get Function: RFmxGSM_GetSignalStructure Set Function: RFmxGSM_SetSignalStructure |
| Values: | RFMXGSM_VAL_SIGNAL_STRUCTURE_BURSTED (0)The signal is bursted. RFMXGSM_VAL_SIGNAL_STRUCTURE_CONTINUOUS (1)The signal is continuous. |
| RFMXGSM_VAL_SIGNAL_STRUCTURE_BURSTED (0) | The signal is bursted. |
| RFMXGSM_VAL_SIGNAL_STRUCTURE_CONTINUOUS (1) | The signal is continuous. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_timing_advance.html language=enus -->
## TOPIC 00167: RFMXGSM_ATTR_TIMING_ADVANCE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_timing_advance.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_timing_advance.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_TIMING_ADVANCE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxGSM_GetTimingAdvance Set Function: RFmxGSM_SetTimingAdvance |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_trigger_delay.html language=enus -->
## TOPIC 00168: RFMXGSM_ATTR_TRIGGER_DELAY

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_trigger_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_trigger_delay.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_TRIGGER_DELAY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxGSM_GetTriggerDelay Set Function: RFmxGSM_SetTriggerDelay |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_trigger_minimum_quiet_time_duration.html language=enus -->
## TOPIC 00169: RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_trigger_minimum_quiet_time_duration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_trigger_minimum_quiet_time_duration.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeF64RFmxGSM_GetAttributeF64 |
| Description: | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to RFMXGSM_VAL_IQ_POWER_EDGE_RISING_SLOPE, the signal is quiet below the trigger level. If you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to RFMXGSM_VAL_IQ_POWER_EDGE_FALLING_SLOPE, the signal is quiet above the trigger level. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is 582 microseconds. Get Function: RFmxGSM_GetTriggerMinimumQuietTimeDuration Set Function: RFmxGSM_SetTriggerMinimumQuietTimeDuration |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_trigger_minimum_quiet_time_mode.html language=enus -->
## TOPIC 00170: RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_trigger_minimum_quiet_time_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_trigger_minimum_quiet_time_mode.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the minimum quiet time used for triggering. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO. Get Function: RFmxGSM_GetTriggerMinimumQuietTimeMode Set Function: RFmxGSM_SetTriggerMinimumQuietTimeMode |
| Values: | RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL (0)The minimum quiet time for triggering is the value of the RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO (1)The measurement computes the minimum quiet time used for triggering. |
| RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL (0) | The minimum quiet time for triggering is the value of the RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |
| RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO (1) | The measurement computes the minimum quiet time used for triggering. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_trigger_type.html language=enus -->
## TOPIC 00171: RFMXGSM_ATTR_TRIGGER_TYPE

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_trigger_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_trigger_type.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_TRIGGER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the trigger type. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is RFMXGSM_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. Get Function: RFmxGSM_GetTriggerType Set Function: RFmxGSM_SetTriggerType |
| Values: | RFMXGSM_VAL_TRIGGER_TYPE_NONE (0)No Reference Trigger is configured. RFMXGSM_VAL_TRIGGER_TYPE_DIGITAL_EDGE (1)The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. RFMXGSM_VAL_TRIGGER_TYPE_IQ_POWER_EDGE (2)The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. RFMXGSM_VAL_TRIGGER_TYPE_SOFTWARE (3)The Reference Trigger is not asserted until a software trigger occurs. |
| RFMXGSM_VAL_TRIGGER_TYPE_NONE (0) | No Reference Trigger is configured. |
| RFMXGSM_VAL_TRIGGER_TYPE_DIGITAL_EDGE (1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. |
| RFMXGSM_VAL_TRIGGER_TYPE_IQ_POWER_EDGE (2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. |
| RFMXGSM_VAL_TRIGGER_TYPE_SOFTWARE (3) | The Reference Trigger is not asserted until a software trigger occurs. |

<!--NI_TOPIC bundle=rfmx-gsm-cvi path=rfmxgsm_attr_tsc.html language=enus -->
## TOPIC 00172: RFMXGSM_ATTR_TSC

- bundle_id: `rfmx-gsm-cvi`
- source_path: `rfmxgsm_attr_tsc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-cvi/raw/resource/enus/rfmxgsm_attr_tsc.html
- document_id: `rfmx-gsm-cvi`
- page_type: `leaf`
- content_type: ``

RFMXGSM_ATTR_TSC

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxGSM_SetAttributeI32RFmxGSM_GetAttributeI32 |
| Description: | Specifies the training sequence code (RFMXGSM_ATTR_TSC) to use. This attribute is applicable only when you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to RFMXGSM_VAL_BURST_SYNC_TYPE_RFMXGSM_ATTR_TSC and the RFMXGSM_ATTR_AUTO_RFMXGSM_ATTR_TSC_DETECTION_ENABLED attribute to RFMXGSM_VAL_AUTO_RFMXGSM_ATTR_TSC_DETECTION_ENABLED_FALSE. For access burst RFMXGSM_ATTR_TSC0, RFMXGSM_ATTR_TSC1, and RFMXGSM_ATTR_TSC2 are applicable. Use 'slot(n)' as the selector string to configure or read this attribute. The default value is RFMXGSM_VAL_RFMXGSM_ATTR_TSC0. Get Function: RFmxGSM_GetTsc Set Function: RFmxGSM_SetTsc |
| Values: | RFMXGSM_VAL_TSC0 (0)The measurement uses training sequence code 0. RFMXGSM_VAL_TSC1 (1)The measurement uses training sequence code 1. RFMXGSM_VAL_TSC2 (2)The measurement uses training sequence code 2. RFMXGSM_VAL_TSC3 (3)The measurement uses training sequence code 3. RFMXGSM_VAL_TSC4 (4)The measurement uses training sequence code 4. RFMXGSM_VAL_TSC5 (5)The measurement uses training sequence code 5. RFMXGSM_VAL_TSC6 (6)The measurement uses training sequence code 6. RFMXGSM_VAL_TSC7 (7)The measurement uses training sequence code 7. |
| RFMXGSM_VAL_TSC0 (0) | The measurement uses training sequence code 0. |
| RFMXGSM_VAL_TSC1 (1) | The measurement uses training sequence code 1. |
| RFMXGSM_VAL_TSC2 (2) | The measurement uses training sequence code 2. |
| RFMXGSM_VAL_TSC3 (3) | The measurement uses training sequence code 3. |
| RFMXGSM_VAL_TSC4 (4) | The measurement uses training sequence code 4. |
| RFMXGSM_VAL_TSC5 (5) | The measurement uses training sequence code 5. |
| RFMXGSM_VAL_TSC6 (6) | The measurement uses training sequence code 6. |
| RFMXGSM_VAL_TSC7 (7) | The measurement uses training sequence code 7. |
