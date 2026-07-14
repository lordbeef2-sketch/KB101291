# NI DOCUMENT BUNDLE: rfmx-pulse-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-pulse-cvi start=1 end=125 -->
<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_cfgdigitaledgetrigger.html language=enus -->
## TOPIC 00001: RFmxPulse_CfgDigitalEdgeTrigger

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_cfgdigitaledgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_cfgdigitaledgetrigger.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_CfgDigitalEdgeTrigger

int32 __stdcall RFmxPulse_CfgDigitalEdgeTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char digitalEdgeSource[],
 int32 digitalEdge,
 float64 triggerDelay,
 int32 enableTrigger);

#### Purpose

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| digitalEdgeSource | char[] | Specifies the source terminal for the digital-edge trigger. RFMXPulse_VAL_PFI0_STR (PFI0) The trigger is received on PFI 0.RFMXPulse_VAL_PFI1_STR (PFI1) The trigger is received on PFI 1.RFMXPulse_VAL_PXI_TRIG0_STR (PXI_Trig0) The trigger is received on PXI trigger line 0.RFMXPulse_VAL_PXI_TRIG1_STR (PXI_Trig1) The trigger is received on PXI trigger line 1.RFMXPulse_VAL_PXI_TRIG2_STR (PXI_Trig2) The trigger is received on PXI trigger line 2.RFMXPulse_VAL_PXI_TRIG3_STR (PXI_Trig3) The trigger is received on PXI trigger line 3.RFMXPulse_VAL_PXI_TRIG4_STR (PXI_Trig4) The trigger is received on PXI trigger line 4.RFMXPulse_VAL_PXI_TRIG5_STR (PXI_Trig5) The trigger is received on PXI trigger line 5.RFMXPulse_VAL_PXI_TRIG6_STR (PXI_Trig6) The trigger is received on PXI trigger line 6.RFMXPulse_VAL_PXI_TRIG7_STR (PXI_Trig7) The trigger is received on PXI trigger line 7.RFMXPulse_VAL_PXI_STAR_STR (PXI_STAR) The trigger is received on the PXI star trigger line. |
| RFMXPulse_VAL_PFI0_STR (PFI0) | The trigger is received on PFI 0. |  |
| RFMXPulse_VAL_PFI1_STR (PFI1) | The trigger is received on PFI 1. |  |
| RFMXPulse_VAL_PXI_TRIG0_STR (PXI_Trig0) | The trigger is received on PXI trigger line 0. |  |
| RFMXPulse_VAL_PXI_TRIG1_STR (PXI_Trig1) | The trigger is received on PXI trigger line 1. |  |
| RFMXPulse_VAL_PXI_TRIG2_STR (PXI_Trig2) | The trigger is received on PXI trigger line 2. |  |
| RFMXPulse_VAL_PXI_TRIG3_STR (PXI_Trig3) | The trigger is received on PXI trigger line 3. |  |
| RFMXPulse_VAL_PXI_TRIG4_STR (PXI_Trig4) | The trigger is received on PXI trigger line 4. |  |
| RFMXPulse_VAL_PXI_TRIG5_STR (PXI_Trig5) | The trigger is received on PXI trigger line 5. |  |
| RFMXPulse_VAL_PXI_TRIG6_STR (PXI_Trig6) | The trigger is received on PXI trigger line 6. |  |
| RFMXPulse_VAL_PXI_TRIG7_STR (PXI_Trig7) | The trigger is received on PXI trigger line 7. |  |
| RFMXPulse_VAL_PXI_STAR_STR (PXI_STAR) | The trigger is received on the PXI star trigger line. |  |
| digitalEdge | int32 | Specifies the trigger edge to detect. RFMXPulse_VAL_DIGITAL_EDGE_RISING_EDGE (0) The trigger asserts on the rising edge of the signal.RFMXPulse_VAL_DIGITAL_EDGE_FALLING_EDGE (1) The trigger asserts on the falling edge of the signal. |
| RFMXPulse_VAL_DIGITAL_EDGE_RISING_EDGE (0) | The trigger asserts on the rising edge of the signal. |  |
| RFMXPulse_VAL_DIGITAL_EDGE_FALLING_EDGE (1) | The trigger asserts on the falling edge of the signal. |  |
| triggerDelay | float64 | Specifies the trigger delay time, in seconds. |
| enableTrigger | int32 | Specifies whether to enable the trigger. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_cfgreferencelevel.html language=enus -->
## TOPIC 00002: RFmxPulse_CfgReferenceLevel

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_cfgreferencelevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_cfgreferencelevel.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_CfgReferenceLevel

int32 __stdcall RFmxPulse_CfgReferenceLevel (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 referenceLevel);

#### Purpose

Configures the reference level, which represents the maximum expected power of an RF input signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| referenceLevel | float64 | Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_cfgsoftwareedgetrigger.html language=enus -->
## TOPIC 00003: RFmxPulse_CfgSoftwareEdgeTrigger

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_cfgsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_cfgsoftwareedgetrigger.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_CfgSoftwareEdgeTrigger

int32 __stdcall RFmxPulse_CfgSoftwareEdgeTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 triggerDelay,
 int32 enableTrigger);

#### Purpose

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| triggerDelay | float64 | Specifies the trigger delay time, in seconds. |
| enableTrigger | int32 | Specifies whether to enable the trigger. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_checkmeasurementstatus.html language=enus -->
## TOPIC 00004: RFmxPulse_CheckMeasurementStatus

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_checkmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_checkmeasurementstatus.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_CheckMeasurementStatus

int32 __stdcall RFmxPulse_CheckMeasurementStatus (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32* done);

#### Purpose

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| done | int32* | Indicates whether the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_clearallnamedresults.html language=enus -->
## TOPIC 00005: RFmxPulse_ClearAllNamedResults

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_clearallnamedresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_clearallnamedresults.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_ClearAllNamedResults

int32 __stdcall RFmxPulse_ClearAllNamedResults (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears all results for the signal that you specify in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_clonesignalconfiguration.html language=enus -->
## TOPIC 00006: RFmxPulse_CloneSignalConfiguration

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_clonesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_clonesignalconfiguration.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_CloneSignalConfiguration

int32 __stdcall RFmxPulse_CloneSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char oldSignalName[],
 char newSignalName[]);

#### Purpose

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| oldSignalName | char[] | Specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::OldSigName""OldSigName" |
| newSignalName | char[] | Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_disabletrigger.html language=enus -->
## TOPIC 00007: RFmxPulse_DisableTrigger

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_disabletrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_disabletrigger.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_DisableTrigger

int32 __stdcall RFmxPulse_DisableTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_fetchacquiredamplitudetrace.html language=enus -->
## TOPIC 00008: RFmxPulse_FetchAcquiredAmplitudeTrace

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_fetchacquiredamplitudetrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_fetchacquiredamplitudetrace.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_FetchAcquiredAmplitudeTrace

int32 __stdcall RFmxPulse_FetchAcquiredAmplitudeTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* sampleDuration,
 float32 amplitude[],
 int32 amplitudeArraySize,
 int32* amplitudeActualArraySize,
 int32 startIndex[],
 float64 startTimeStamp[],
 int32 startArraysSize,
 int32* startActualArraysSize);

#### Purpose

Fetches the acquired amplitude trace in the measurement, where the Amplitude array forms the y-axis of the trace. You can use the [RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT](/csh?topicname=rfmxpulsecvi/rfmxpulse_attr_pulse_acquisition_trace_select.html) attribute to select all pulses or the subset of acquired pulses. When you set the [RFMXPULSE_ATTR_SEGMENTED_ACQUISITION_ENABLED](/csh?topicname=rfmxpulsecvi/rfmxpulse_attr_segmented_acquisition_enabled.html) attribute to RFMXPULSE_VAL_SEGMENTED_ACQUISITION_ENABLED_FALSE, returns a single element in the Start Indices and Start Time Stamp array.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| amplitudeArraySize | int32 | Specifies the size of amplitude array. Set the amplitudeArraySize parameter to 0 to get the size of amplitude array in the amplitudeActualArraySize parameter. |
| startArraysSize | int32 | Specifies the size of start index and start time stamp array. Set the startArraysSize parameter to 0 to get the size of start index and start time stamp arrays in the startActualArraysSize parameter. |
| Output |  |  |
| Name | Type | Description |
| sampleDuration | float64* | Returns the sample duration, in seconds. |
| amplitude | float32[] | Returns the trace of amplitude measured in units specified by RFMXPULSE_ATTR_PULSE_AMPLITUDE_TRACE_UNIT attribute. |
| amplitudeActualArraySize | int32* | Returns the actual size of the amplitude array, if you pass NULL to amplitude output array parameters, and set the amplitudeArraySize parameter to 0. |
| startIndex | int32[] | Returns the array of sample indices for the start of each segment. |
| startTimeStamp | float64[] | Returns the array of timestamps of each segment start, in seconds. |
| startActualArraysSize | int32* | Returns the actual size of the start index and start time stamp array, if you pass NULL to start index and start time stamp output array parameters, and set the startArraysSize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_fetchburstintrapulsestabilitytrace.html language=enus -->
## TOPIC 00009: RFmxPulse_FetchBurstIntrapulseStabilityTrace

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_fetchburstintrapulsestabilitytrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_fetchburstintrapulsestabilitytrace.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_FetchBurstIntrapulseStabilityTrace

int32 __stdcall RFmxPulse_FetchBurstIntrapulseStabilityTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 intrapulseAverageAmplitudeStability[],
 float32 intrapulseAveragePhaseStability[],
 float32 intrapulseAverageTotalStability[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the burst intrapulse stability trace, averaged across the pulses within a positional average burst, over multiple measurement points.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the <strong>arraySize</strong> parameter to 0 to get the size of all the arrays in the <strong>actualArraySize</strong> parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time of measurement window, in seconds. |
| dx | float64* | Returns the sample duration of measurement window, in seconds. |
| intrapulseAverageAmplitudeStability | float32[] | Returns the intrapulse average amplitude stability of multiple measurement points, in dB. |
| intrapulseAveragePhaseStability | float32[] | Returns the intrapulse average phase stability of multiple measurement points, in dB. |
| intrapulseAverageTotalStability | float32[] | Returns the intrapulse average total stability of multiple measurement points, in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the <strong>arraySize</strong> parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_fetchfrequencytrace.html language=enus -->
## TOPIC 00010: RFmxPulse_FetchFrequencyTrace

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_fetchfrequencytrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_fetchfrequencytrace.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_FetchFrequencyTrace

int32 __stdcall RFmxPulse_FetchFrequencyTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 frequency[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the frequency trace of the selected pulse.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time, in seconds. |
| dx | float64* | Returns the sample duration, in seconds. |
| frequency | float32[] | Returns the frequency, in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=cvirfmxpulse_fetchintrapulsestabilitytrace.html language=enus -->
## TOPIC 00011: RFmxPulse_FetchIntrapulseStabilityTrace

- bundle_id: `rfmx-pulse-cvi`
- source_path: `cvirfmxpulse_fetchintrapulsestabilitytrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/cvirfmxpulse_fetchintrapulsestabilitytrace.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFmxPulse_FetchIntrapulseStabilityTrace

int32 __stdcall RFmxPulse_FetchIntrapulseStabilityTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 intrapulseAmplitudeStability[],
 float32 intrapulsePhaseStability[],
 float32 intrapulseTotalStability[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the intrapulse stability trace over multiple measurement points, for the selected pulse or position.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxPulse_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the <strong>arraySize</strong> parameter to 0 to get the size of all the arrays in the <strong>actualArraySize</strong> parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time of measurement window, in seconds. |
| dx | float64* | Returns the sample duration of measurement window, in seconds. |
| intrapulseAmplitudeStability | float32[] | Returns the intrapulse amplitude stability of multiple measurement points, in dB. |
| intrapulsePhaseStability | float32[] | Returns the intrapulse phase stability of multiple measurement points, in dB. |
| intrapulseTotalStability | float32[] | Returns the intrapulse total stability of multiple measurement points, in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the <strong>arraySize</strong> parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxPulse_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_measurement_bandwidth.html language=enus -->
## TOPIC 00012: RFMXPULSE_ATTR_MEASUREMENT_BANDWIDTH

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_measurement_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_measurement_bandwidth.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_MEASUREMENT_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeF64RFmxPulse_GetAttributeF64 |
| Description: | Specifies the bandwidth of the filter used for the required sample rate. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 80 MHz. Get Function: RFmxPulse_GetMeasurementBandwidth Set Function: RFmxPulse_SetMeasurementBandwidth |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_acquisition_trace_subset_length.html language=enus -->
## TOPIC 00013: RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SUBSET_LENGTH

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_acquisition_trace_subset_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_acquisition_trace_subset_length.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SUBSET_LENGTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies the total number of pulses starting from offset to be used for display acquisition trace. You must configure this attribute when you set the RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT attribute to RFMXPULSE_VAL_PULSE_ACQUISITION_TRACE_SELECT_SUBSET. Set length to 0 to disable the acquisition trace. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Valid values are 0 to 10000, inclusive. Get Function: RFmxPulse_PulseGetAcquisitionTraceSubsetLength Set Function: RFmxPulse_PulseSetAcquisitionTraceSubsetLength |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_all_traces_enabled.html language=enus -->
## TOPIC 00014: RFMXPULSE_ATTR_PULSE_ALL_TRACES_ENABLED

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_all_traces_enabled.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies whether to enable storing and retrieving traces after performing the measurements. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXPULSE_VAL_FALSE. Get Function: RFmxPulse_PulseGetAllTracesEnabled Set Function: RFmxPulse_PulseSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_detection_reference.html language=enus -->
## TOPIC 00015: RFMXPULSE_ATTR_PULSE_DETECTION_REFERENCE

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_detection_reference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_detection_reference.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_DETECTION_REFERENCE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies the reference used for RFMXPULSE_ATTR_PULSE_DETECTION_THRESHOLD attribute. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Ref Level. Get Function: RFmxPulse_PulseGetDetectionReference Set Function: RFmxPulse_PulseSetDetectionReference |
| Values: | RFMXPULSE_VAL_PULSE_DETECTION_REFERENCE_REFERENCE_LEVEL (0)The threshold is relative to the reference level of the samples. RFMXPULSE_VAL_PULSE_DETECTION_REFERENCE_ABSOLUTE (1)The threshold is the absolute power, in dBm. RFMXPULSE_VAL_PULSE_DETECTION_REFERENCE_PEAK (2)The threshold is relative to the peak level of the samples. |
| RFMXPULSE_VAL_PULSE_DETECTION_REFERENCE_REFERENCE_LEVEL (0) | The threshold is relative to the reference level of the samples. |
| RFMXPULSE_VAL_PULSE_DETECTION_REFERENCE_ABSOLUTE (1) | The threshold is the absolute power, in dBm. |
| RFMXPULSE_VAL_PULSE_DETECTION_REFERENCE_PEAK (2) | The threshold is relative to the peak level of the samples. |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_detection_threshold.html language=enus -->
## TOPIC 00016: RFMXPULSE_ATTR_PULSE_DETECTION_THRESHOLD

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_detection_threshold.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_detection_threshold.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_DETECTION_THRESHOLD

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeF64RFmxPulse_GetAttributeF64 |
| Description: | Specifies the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the RFMXPULSE_ATTR_PULSE_DETECTION_REFERENCE attribute. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is -20. Valid values are -100 to 100, inclusive. Get Function: RFmxPulse_PulseGetDetectionThreshold Set Function: RFmxPulse_PulseSetDetectionThreshold |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_frequency_and_phase_cw_frequency_offset.html language=enus -->
## TOPIC 00017: RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_frequency_and_phase_cw_frequency_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_frequency_and_phase_cw_frequency_offset.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeF64RFmxPulse_GetAttributeF64 |
| Description: | Specifies to manually enter the CW frequency offset. This attribute is valid only when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE attribute to RFMXPULSE_VAL_PULSE_MODULATION_TYPE_CW. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxPulse_PulseGetFrequencyAndPhaseCWFrequencyOffset Set Function: RFmxPulse_PulseSetFrequencyAndPhaseCWFrequencyOffset |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_frequency_and_phase_cw_frequency_offset_auto.html language=enus -->
## TOPIC 00018: RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET_AUTO

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_frequency_and_phase_cw_frequency_offset_auto.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_frequency_and_phase_cw_frequency_offset_auto.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET_AUTO

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies whether the CW frequency offset computation of every detected pulse is automatic or manual. This attribute is valid only when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE attribute to RFMXPULSE_VAL_PULSE_MODULATION_TYPE_CW. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXPULSE_VAL_PULSE_CW_FREQUENCY_OFFSET_AUTO_TRUE. Get Function: RFmxPulse_PulseGetFrequencyAndPhaseCWFrequencyOffsetAuto Set Function: RFmxPulse_PulseSetFrequencyAndPhaseCWFrequencyOffsetAuto |
| Values: | RFMXPULSE_VAL_PULSE_CW_FREQUENCY_OFFSET_AUTO_FALSE (0)CW frequency offset computation is set to manual. RFMXPULSE_VAL_PULSE_CW_FREQUENCY_OFFSET_AUTO_TRUE (1)CW frequency offset computation is set to automatic. |
| RFMXPULSE_VAL_PULSE_CW_FREQUENCY_OFFSET_AUTO_FALSE (0) | CW frequency offset computation is set to manual. |
| RFMXPULSE_VAL_PULSE_CW_FREQUENCY_OFFSET_AUTO_TRUE (1) | CW frequency offset computation is set to automatic. |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_frequency_and_phase_deviation_range_edge_start.html language=enus -->
## TOPIC 00019: RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_START

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_frequency_and_phase_deviation_range_edge_start.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_frequency_and_phase_deviation_range_edge_start.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_START

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeF64RFmxPulse_GetAttributeF64 |
| Description: | Specifies the start of the pulse data used for the phase/frequency deviation and error measurements when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE attribute to RFMXPULSE_VAL_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxPulse_PulseGetFrequencyAndPhaseDeviationRangeEdgeStart Set Function: RFmxPulse_PulseSetFrequencyAndPhaseDeviationRangeEdgeStart |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_frequency_and_phase_deviation_range_edge_stop.html language=enus -->
## TOPIC 00020: RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_STOP

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_frequency_and_phase_deviation_range_edge_stop.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_frequency_and_phase_deviation_range_edge_stop.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_STOP

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeF64RFmxPulse_GetAttributeF64 |
| Description: | Specifies the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE attribute to RFMXPULSE_VAL_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxPulse_PulseGetFrequencyAndPhaseDeviationRangeEdgeStop Set Function: RFmxPulse_PulseSetFrequencyAndPhaseDeviationRangeEdgeStop |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_frequency_and_phase_deviation_range_length.html language=enus -->
## TOPIC 00021: RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_frequency_and_phase_deviation_range_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_frequency_and_phase_deviation_range_length.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeF64RFmxPulse_GetAttributeF64 |
| Description: | Specifies the length of the pulse data used for the phase/frequency deviation and error measurements when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE attribute to RFMXPULSE_VAL_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE_CENTER. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 75. Valid values are 0 to 100, inclusive. Get Function: RFmxPulse_PulseGetFrequencyAndPhaseDeviationRangeLength Set Function: RFmxPulse_PulseSetFrequencyAndPhaseDeviationRangeLength |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_frequency_and_phase_modulation_type.html language=enus -->
## TOPIC 00022: RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_frequency_and_phase_modulation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_frequency_and_phase_modulation_type.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXPULSE_VAL_PULSE_MODULATION_TYPE_CW. Get Function: RFmxPulse_PulseGetFrequencyAndPhaseModulationType Set Function: RFmxPulse_PulseSetFrequencyAndPhaseModulationType |
| Values: | RFMXPULSE_VAL_PULSE_MODULATION_TYPE_CW (0)Continous wave where the frequency remains constant over pulse ON duration. RFMXPULSE_VAL_PULSE_MODULATION_TYPE_LINEAR_FM (1)Frequency varies linearly within pulse ON duration. RFMXPULSE_VAL_PULSE_MODULATION_TYPE_TRIANGULAR_FM (2)Frequency varies with two lienar FM chirps with opposite slopes within pulse ON duration. |
| RFMXPULSE_VAL_PULSE_MODULATION_TYPE_CW (0) | Continous wave where the frequency remains constant over pulse ON duration. |
| RFMXPULSE_VAL_PULSE_MODULATION_TYPE_LINEAR_FM (1) | Frequency varies linearly within pulse ON duration. |
| RFMXPULSE_VAL_PULSE_MODULATION_TYPE_TRIANGULAR_FM (2) | Frequency varies with two lienar FM chirps with opposite slopes within pulse ON duration. |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_metrics_amplitude_deviation_unit.html language=enus -->
## TOPIC 00023: RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_metrics_amplitude_deviation_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_metrics_amplitude_deviation_unit.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies the unit for amplitude deviation results. This attribute is applicable only for droop, ripple and overshoot results. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXPULSE_VAL_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT_PERCENTAGE. Get Function: RFmxPulse_PulseGetMetricsAmplitudeDeviationUnit Set Function: RFmxPulse_PulseSetMetricsAmplitudeDeviationUnit |
| Values: | RFMXPULSE_VAL_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT_PERCENTAGE (0)Amplitude deviation results are returned as a percentage. RFMXPULSE_VAL_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT_DB (1)Amplitude deviation results are returned in dB. |
| RFMXPULSE_VAL_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT_PERCENTAGE (0) | Amplitude deviation results are returned as a percentage. |
| RFMXPULSE_VAL_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT_DB (1) | Amplitude deviation results are returned in dB. |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_metrics_enabled.html language=enus -->
## TOPIC 00024: RFMXPULSE_ATTR_PULSE_METRICS_ENABLED

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_metrics_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_metrics_enabled.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_METRICS_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies whether to enable pulse metrics results computation. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXPULSE_VAL_PULSE_METRICS_ENABLED_TRUE. Get Function: RFmxPulse_PulseGetMetricsEnabled Set Function: RFmxPulse_PulseSetMetricsEnabled |
| Values: | RFMXPULSE_VAL_PULSE_METRICS_ENABLED_FALSE (0)Pulse Metric results computation is disabled. RFMXPULSE_VAL_PULSE_METRICS_ENABLED_TRUE (1)Pulse Metric results computation is enabled. |
| RFMXPULSE_VAL_PULSE_METRICS_ENABLED_FALSE (0) | Pulse Metric results computation is disabled. |
| RFMXPULSE_VAL_PULSE_METRICS_ENABLED_TRUE (1) | Pulse Metric results computation is enabled. |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_multiple_measurement_points_enabled.html language=enus -->
## TOPIC 00025: RFMXPULSE_ATTR_PULSE_MULTIPLE_MEASUREMENT_POINTS_ENABLED

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_multiple_measurement_points_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_multiple_measurement_points_enabled.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_MULTIPLE_MEASUREMENT_POINTS_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies whether to enable pulse stability measurements on multiple measurement points. This attribute is used to enable the multiple measurement points stability trace when you set the All Traces Enabled attribute to TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXPULSE_VAL_PULSE_MULTIPLE_MEASUREMENT_POINTS_ENABLED_FALSE. Get Function: RFmxPulse_PulseGetMultipleMeasurementPointsEnabled Set Function: RFmxPulse_PulseSetMultipleMeasurementPointsEnabled |
| Values: | RFMXPULSE_VAL_PULSE_MULTIPLE_MEASUREMENT_POINTS_ENABLED_FALSE (0)Multiple Measurement Points related computation is disabled. RFMXPULSE_VAL_PULSE_MULTIPLE_MEASUREMENT_POINTS_ENABLED_TRUE (1)Multiple Measurement Points related computation is enabled. |
| RFMXPULSE_VAL_PULSE_MULTIPLE_MEASUREMENT_POINTS_ENABLED_FALSE (0) | Multiple Measurement Points related computation is disabled. |
| RFMXPULSE_VAL_PULSE_MULTIPLE_MEASUREMENT_POINTS_ENABLED_TRUE (1) | Multiple Measurement Points related computation is enabled. |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_number_of_analysis_threads.html language=enus -->
## TOPIC 00026: RFMXPULSE_ATTR_PULSE_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_number_of_analysis_threads.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the pulse measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Valid values are 1 to 10, inclusive. Get Function: RFmxPulse_PulseGetNumberOfAnalysisThreads Set Function: RFmxPulse_PulseSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_average_level.html language=enus -->
## TOPIC 00027: RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_LEVEL

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_average_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_average_level.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_LEVEL

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the average power levels during the pulse period for all measured pulses. The values are expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsAverageLevel |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_average_level_mean.html language=enus -->
## TOPIC 00028: RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_LEVEL_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_average_level_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_average_level_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_LEVEL_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsAverageLevelMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_average_level_minimum.html language=enus -->
## TOPIC 00029: RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_LEVEL_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_average_level_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_average_level_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_LEVEL_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum average power level during the pulse period across the measured pulses. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsAverageLevelMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_average_on_level.html language=enus -->
## TOPIC 00030: RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_ON_LEVEL

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_average_on_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_average_on_level.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_ON_LEVEL

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the average power levels during the ON duration for all measured pulses. The values are expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsAverageOnLevel |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_average_on_level_maximum.html language=enus -->
## TOPIC 00031: RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_ON_LEVEL_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_average_on_level_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_average_on_level_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_ON_LEVEL_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum average power level during the ON duration across the measured pulses. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsAverageOnLevelMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_average_on_level_minimum.html language=enus -->
## TOPIC 00032: RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_ON_LEVEL_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_average_on_level_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_average_on_level_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_ON_LEVEL_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum average power level during the ON duration across the measured pulses. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsAverageOnLevelMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_average_total_stability.html language=enus -->
## TOPIC 00033: RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_TOTAL_STABILITY

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_average_total_stability.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_average_total_stability.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_TOTAL_STABILITY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the average total stability over measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsAverageTotalStability |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_droop.html language=enus -->
## TOPIC 00034: RFMXPULSE_ATTR_PULSE_RESULTS_DROOP

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_droop.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_droop.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_DROOP

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the droop values computed for all measured pulses. Droop values are defined as the rate at which the pulse top levels decays from the beginning to the end during On duration. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsDroop |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_droop_mean.html language=enus -->
## TOPIC 00035: RFMXPULSE_ATTR_PULSE_RESULTS_DROOP_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_droop_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_droop_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_DROOP_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the droop values computed for all measured pulses. This value is expressed in units specified by RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT attribute. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsDroopMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_duty_cycle.html language=enus -->
## TOPIC 00036: RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_duty_cycle.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_duty_cycle.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsDutyCycle |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_duty_cycle_maximum.html language=enus -->
## TOPIC 00037: RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_duty_cycle_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_duty_cycle_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum duty cycle across the measured pulses. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsDutyCycleMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_duty_cycle_mean.html language=enus -->
## TOPIC 00038: RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_duty_cycle_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_duty_cycle_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of duty cycle values across the measured pulses. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsDutyCycleMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fall_time_mean.html language=enus -->
## TOPIC 00039: RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fall_time_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fall_time_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the fall time values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFallTimeMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fall_time_minimum.html language=enus -->
## TOPIC 00040: RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fall_time_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fall_time_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum fall time across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFallTimeMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_rate2_maximum.html language=enus -->
## TOPIC 00041: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE2_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_rate2_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_rate2_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE2_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpRate2Maximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_rate2_mean.html language=enus -->
## TOPIC 00042: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE2_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_rate2_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_rate2_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE2_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpRate2Mean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_rate_minimum.html language=enus -->
## TOPIC 00043: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_rate_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_rate_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpRateMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_rate_standard_deviation.html language=enus -->
## TOPIC 00044: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_rate_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_rate_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpRateStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_start_frequency.html language=enus -->
## TOPIC 00045: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_start_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_start_frequency.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the start frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStartFrequency |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_start_frequency2.html language=enus -->
## TOPIC 00046: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_start_frequency2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_start_frequency2.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStartFrequency2 |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_start_frequency2_minimum.html language=enus -->
## TOPIC 00047: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_start_frequency2_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_start_frequency2_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStartFrequency2Minimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_start_frequency_maximum.html language=enus -->
## TOPIC 00048: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_start_frequency_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_start_frequency_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStartFrequencyMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_start_frequency_mean.html language=enus -->
## TOPIC 00049: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_start_frequency_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_start_frequency_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the FM chirp start frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStartFrequencyMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_start_frequency_standard_deviation.html language=enus -->
## TOPIC 00050: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_start_frequency_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_start_frequency_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the FM chirp start frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStartFrequencyStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency.html language=enus -->
## TOPIC 00051: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the stop frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStopFrequency |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency2.html language=enus -->
## TOPIC 00052: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency2.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the stop frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStopFrequency2 |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency2_maximum.html language=enus -->
## TOPIC 00053: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency2_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency2_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStopFrequency2Maximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency_maximum.html language=enus -->
## TOPIC 00054: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStopFrequencyMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency_mean.html language=enus -->
## TOPIC 00055: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStopFrequencyMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency_standard_deviation.html language=enus -->
## TOPIC 00056: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_fm_chirp_stop_frequency_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the FM chirp stop frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsFMChirpStopFrequencyStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_overshoot_mean.html language=enus -->
## TOPIC 00057: RFMXPULSE_ATTR_PULSE_RESULTS_OVERSHOOT_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_overshoot_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_overshoot_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_OVERSHOOT_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the overshoot values computed for all measured pulses. This value is expressed in units specified by RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT attribute. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsOvershootMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_peak_level_minimum.html language=enus -->
## TOPIC 00058: RFMXPULSE_ATTR_PULSE_RESULTS_PEAK_LEVEL_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_peak_level_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_peak_level_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PEAK_LEVEL_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum peak power level during the pulse period across the measured pulses. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPeakLevelMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_deviation.html language=enus -->
## TOPIC 00059: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_DEVIATION

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the peak-to-peak phase deviation for all measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_deviation_maximum.html language=enus -->
## TOPIC 00060: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_DEVIATION_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_deviation_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_deviation_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_DEVIATION_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseDeviationMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_deviation_mean.html language=enus -->
## TOPIC 00061: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_DEVIATION_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_deviation_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_deviation_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_DEVIATION_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseDeviationMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_deviation_minimum.html language=enus -->
## TOPIC 00062: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_DEVIATION_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_deviation_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_deviation_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_DEVIATION_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseDeviationMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_error_peak_location.html language=enus -->
## TOPIC 00063: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_PEAK_LOCATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_error_peak_location.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_error_peak_location.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_PEAK_LOCATION

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the time locations corresponding to the peak phase error for all measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseErrorPeakLocation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_error_peak_maximum.html language=enus -->
## TOPIC 00064: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_PEAK_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_error_peak_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_error_peak_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_PEAK_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum peak phase error across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseErrorPeakMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_error_peak_mean.html language=enus -->
## TOPIC 00065: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_PEAK_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_error_peak_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_error_peak_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_PEAK_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the peak phase error across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseErrorPeakMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_error_peak_minimum.html language=enus -->
## TOPIC 00066: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_PEAK_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_error_peak_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_error_peak_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_PEAK_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum peak phase error across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseErrorPeakMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_error_peak_standard_deviation.html language=enus -->
## TOPIC 00067: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_PEAK_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_error_peak_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_error_peak_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_PEAK_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of the peak phase error across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseErrorPeakStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_error_rms.html language=enus -->
## TOPIC 00068: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_error_rms.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_error_rms.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the RMS phase error for all measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseErrorRMS |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_error_rms_maximum.html language=enus -->
## TOPIC 00069: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_error_rms_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_error_rms_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum RMS phase error across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseErrorRMSMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_error_rms_mean.html language=enus -->
## TOPIC 00070: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_error_rms_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_error_rms_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the RMS phase error across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseErrorRMSMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_error_rms_minimum.html language=enus -->
## TOPIC 00071: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_error_rms_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_error_rms_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum RMS phase error across the measured pulses. This value is expressed in degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseErrorRMSMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_phase_stability_minimum.html language=enus -->
## TOPIC 00072: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_STABILITY_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_phase_stability_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_phase_stability_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_STABILITY_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum phase stability across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPhaseStabilityMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_pulse_off_duration.html language=enus -->
## TOPIC 00073: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_pulse_off_duration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_pulse_off_duration.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the OFF duration values for all measured pulses. OFF duration value is the duration of the pulse for the first falling-edge and the subsequent rising-edge transition at width threshold. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPulseOffDuration |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_pulse_off_duration_standard_deviation.html language=enus -->
## TOPIC 00074: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_pulse_off_duration_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_pulse_off_duration_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPulseOffDurationStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_pulse_repetition_interval.html language=enus -->
## TOPIC 00075: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_pulse_repetition_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_pulse_repetition_interval.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPulseRepetitionInterval |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_pulse_repetition_interval_maximum.html language=enus -->
## TOPIC 00076: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_pulse_repetition_interval_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_pulse_repetition_interval_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum pulse period across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPulseRepetitionIntervalMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_pulse_repetition_interval_standard_deviation.html language=enus -->
## TOPIC 00077: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_pulse_repetition_interval_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_pulse_repetition_interval_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPulseRepetitionIntervalStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_pulse_to_pulse_frequency_difference.html language=enus -->
## TOPIC 00078: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_pulse_to_pulse_frequency_difference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_pulse_to_pulse_frequency_difference.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the frequency difference of the pulses with respect to the frequency of the first pulse. This value is expressed in Hz. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPulseToPulseFrequencyDifference |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_pulse_to_pulse_frequency_difference_mean.html language=enus -->
## TOPIC 00079: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_pulse_to_pulse_frequency_difference_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_pulse_to_pulse_frequency_difference_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPulseToPulseFrequencyDifferenceMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_pulse_width_mean.html language=enus -->
## TOPIC 00080: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_WIDTH_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_pulse_width_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_pulse_width_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_WIDTH_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the ON duration values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPulseWidthMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_pulse_width_minimum.html language=enus -->
## TOPIC 00081: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_WIDTH_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_pulse_width_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_pulse_width_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_WIDTH_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum ON duration across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsPulseWidthMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_rise_time_maximum.html language=enus -->
## TOPIC 00082: RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_rise_time_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_rise_time_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum rise time across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsRiseTimeMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_rise_time_mean.html language=enus -->
## TOPIC 00083: RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_rise_time_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_rise_time_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the rise time values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsRiseTimeMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_rise_time_minimum.html language=enus -->
## TOPIC 00084: RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_rise_time_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_rise_time_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum rise time across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsRiseTimeMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_rise_time_standard_deviation.html language=enus -->
## TOPIC 00085: RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_rise_time_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_rise_time_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsRiseTimeStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio.html language=enus -->
## TOPIC 00086: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeCompressionRatio |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_maximum.html language=enus -->
## TOPIC 00087: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum compression ratio across the measured pulses. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeCompressionRatioMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_mean.html language=enus -->
## TOPIC 00088: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the compression ratio values across the measured pulses. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeCompressionRatioMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_minimum.html language=enus -->
## TOPIC 00089: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum compression ratio across the measured pulses. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeCompressionRatioMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_standard_deviation.html language=enus -->
## TOPIC 00090: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_compression_ratio_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of the compression ratio values across the measured pulses. This value is expressed as a percentage. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeCompressionRatioStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_delay.html language=enus -->
## TOPIC 00091: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_delay.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeDelay |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_delay_maximum.html language=enus -->
## TOPIC 00092: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_delay_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_delay_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum sidelobe delay across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeDelayMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_delay_mean.html language=enus -->
## TOPIC 00093: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_delay_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_delay_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the sidelobe delay values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeDelayMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_delay_minimum.html language=enus -->
## TOPIC 00094: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_delay_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_delay_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum sidelobe delay across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeDelayMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_delay_standard_deviation.html language=enus -->
## TOPIC 00095: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_delay_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_delay_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeDelayStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width.html language=enus -->
## TOPIC 00096: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the mainlobe width for all measured pulses. Mainlobe width is the width at 3dB below from its peak level. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeMainlobeWidth |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_maximum.html language=enus -->
## TOPIC 00097: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum mainlobe width across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeMainlobeWidthMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_mean.html language=enus -->
## TOPIC 00098: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the mainlobe width values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeMainlobeWidthMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_minimum.html language=enus -->
## TOPIC 00099: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum mainlobe width across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeMainlobeWidthMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_standard_deviation.html language=enus -->
## TOPIC 00100: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_mainlobe_width_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobeMainlobeWidthStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation.html language=enus -->
## TOPIC 00101: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the peak correlation for all measured pulses. Peak correlation is the normalized peak power of the correlated output by both measured and reference pulse powers. This values ranges in between 0 to 1. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobePeakCorrelation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_maximum.html language=enus -->
## TOPIC 00102: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum peak correlation across the measured pulses. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobePeakCorrelationMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_mean.html language=enus -->
## TOPIC 00103: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the peak correlation values across the measured pulses. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobePeakCorrelationMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_minimum.html language=enus -->
## TOPIC 00104: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum peak correlation across the measured pulses. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobePeakCorrelationMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_standard_deviation.html language=enus -->
## TOPIC 00105: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_peak_correlation_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of the peak correlation values across the measured pulses. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobePeakCorrelationStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level.html language=enus -->
## TOPIC 00106: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the peak sidelobe level for all measured pulses. Peak sidelobe level is the ratio of the highest sidelobe peak to the mainlobe peak level. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobePeakSidelobeLevel |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_maximum.html language=enus -->
## TOPIC 00107: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum peak sidelobe level across the measured pulses. This value is expressed in seconds. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobePeakSidelobeLevelMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_mean.html language=enus -->
## TOPIC 00108: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the peak sidelobe level values across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobePeakSidelobeLevelMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_minimum.html language=enus -->
## TOPIC 00109: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum peak sidelobe level across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobePeakSidelobeLevelMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_standard_deviation.html language=enus -->
## TOPIC 00110: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_time_sidelobe_peak_sidelobe_level_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTimeSidelobePeakSidelobeLevelStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_top_level.html language=enus -->
## TOPIC 00111: RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_top_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_top_level.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL

| Data Type: | float64 [] |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64Array |
| Description: | Returns the top levels for all measured pulses. The values are expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTopLevel |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_top_level_maximum.html language=enus -->
## TOPIC 00112: RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_top_level_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_top_level_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum top level across the measured pulses. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTopLevelMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_top_level_mean.html language=enus -->
## TOPIC 00113: RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MEAN

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_top_level_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_top_level_mean.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the mean of the top levels across the measured pulses. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTopLevelMean |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_top_level_minimum.html language=enus -->
## TOPIC 00114: RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MINIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_top_level_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_top_level_minimum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the minimum top level across the measured pulses. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTopLevelMinimum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_top_level_standard_deviation.html language=enus -->
## TOPIC 00115: RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_STANDARD_DEVIATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_top_level_standard_deviation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_top_level_standard_deviation.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_STANDARD_DEVIATION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the standard deviation of the top levels across the measured pulses. This value is expressed in dBm. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTopLevelStandardDeviation |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_results_total_stability_maximum.html language=enus -->
## TOPIC 00116: RFMXPULSE_ATTR_PULSE_RESULTS_TOTAL_STABILITY_MAXIMUM

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_results_total_stability_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_results_total_stability_maximum.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_RESULTS_TOTAL_STABILITY_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxPulse_GetAttributeF64 |
| Description: | Returns the maximum total stability across the measured pulses. This value is expressed in dB. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxPulse_PulseGetResultsTotalStabilityMaximum |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_stability_pulse_to_pulse_offset.html language=enus -->
## TOPIC 00117: RFMXPULSE_ATTR_PULSE_STABILITY_PULSE_TO_PULSE_OFFSET

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_stability_pulse_to_pulse_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_stability_pulse_to_pulse_offset.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_STABILITY_PULSE_TO_PULSE_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies the offset in number of pulses used for pulse-to-pulse stability measurement trace. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxPulse_PulseGetStabilityPulseToPulseOffset Set Function: RFmxPulse_PulseSetStabilityPulseToPulseOffset |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_time_sidelobe_keep_out_time.html language=enus -->
## TOPIC 00118: RFMXPULSE_ATTR_PULSE_TIME_SIDELOBE_KEEP_OUT_TIME

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_time_sidelobe_keep_out_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_time_sidelobe_keep_out_time.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_TIME_SIDELOBE_KEEP_OUT_TIME

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeF64RFmxPulse_GetAttributeF64 |
| Description: | Specifies keep out time for the time sidelobe measurements. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.000001 seconds. Get Function: RFmxPulse_PulseGetTimeSidelobeKeepOutTime Set Function: RFmxPulse_PulseSetTimeSidelobeKeepOutTime |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_time_sidelobe_reference_window_type.html language=enus -->
## TOPIC 00119: RFMXPULSE_ATTR_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_time_sidelobe_reference_window_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_time_sidelobe_reference_window_type.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_NONE. Get Function: RFmxPulse_PulseGetTimeSidelobeReferenceWindowType Set Function: RFmxPulse_PulseSetTimeSidelobeReferenceWindowType |
| Values: | RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_NONE (0)Indicates no windowing. RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_FLATTOP (1)Indicates Flat Top window type. RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_HANNING (2)Indicates Hanning window type. RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_HAMMING (3)Indicates Hamming window type. RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_GAUSSIAN (4)Indicates Gaussian window type. RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_BLACKMAN (5)Indicates Blackman window type. RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_DOLPH_CHEBYSHEV (6)Indicates Chebyshev window type. |
| RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_NONE (0) | Indicates no windowing. |
| RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_FLATTOP (1) | Indicates Flat Top window type. |
| RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_HANNING (2) | Indicates Hanning window type. |
| RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_HAMMING (3) | Indicates Hamming window type. |
| RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_GAUSSIAN (4) | Indicates Gaussian window type. |
| RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_BLACKMAN (5) | Indicates Blackman window type. |
| RFMXPULSE_VAL_PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE_DOLPH_CHEBYSHEV (6) | Indicates Chebyshev window type. |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_pulse_trace_range_offset.html language=enus -->
## TOPIC 00120: RFMXPULSE_ATTR_PULSE_TRACE_RANGE_OFFSET

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_pulse_trace_range_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_pulse_trace_range_offset.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_PULSE_TRACE_RANGE_OFFSET

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeF64RFmxPulse_GetAttributeF64 |
| Description: | Specifies the time offset in seconds from the reference point to position the trace range. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxPulse_PulseGetTraceRangeOffset Set Function: RFmxPulse_PulseSetTraceRangeOffset |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_reference_level.html language=enus -->
## TOPIC 00121: RFMXPULSE_ATTR_REFERENCE_LEVEL

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_reference_level.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_REFERENCE_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeF64RFmxPulse_GetAttributeF64 |
| Description: | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default of this attribute is hardware dependent. Get Function: RFmxPulse_GetReferenceLevel Set Function: RFmxPulse_SetReferenceLevel |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_segmented_acquisition_enabled.html language=enus -->
## TOPIC 00122: RFMXPULSE_ATTR_SEGMENTED_ACQUISITION_ENABLED

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_segmented_acquisition_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_segmented_acquisition_enabled.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_SEGMENTED_ACQUISITION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXPULSE_VAL_SEGMENTED_ACQUISITION_ENABLED_FALSE. Get Function: RFmxPulse_GetSegmentedAcquisitionEnabled Set Function: RFmxPulse_SetSegmentedAcquisitionEnabled |
| Values: | RFMXPULSE_VAL_SEGMENTED_ACQUISITION_ENABLED_FALSE (0)Segmented acquisition is disabled. RFMXPULSE_VAL_SEGMENTED_ACQUISITION_ENABLED_TRUE (1)Segmented acquisition is enabled. |
| RFMXPULSE_VAL_SEGMENTED_ACQUISITION_ENABLED_FALSE (0) | Segmented acquisition is disabled. |
| RFMXPULSE_VAL_SEGMENTED_ACQUISITION_ENABLED_TRUE (1) | Segmented acquisition is enabled. |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_selected_ports.html language=enus -->
## TOPIC 00123: RFMXPULSE_ATTR_SELECTED_PORTS

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_selected_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_selected_ports.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_SELECTED_PORTS

| Data Type: | char [] |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeStringRFmxPulse_GetAttributeString |
| Description: | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Valid values: PXIe-5830: if0, if1 Other devices: (empty string) PXIe-5831/5832: if0, if1, rf<0-1>/port, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values: PXIe-5830: if1 Other devices: (empty string) Get Function: RFmxPulse_GetSelectedPorts Set Function: RFmxPulse_SetSelectedPorts |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_trigger_minimum_quiet_time_duration.html language=enus -->
## TOPIC 00124: RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_trigger_minimum_quiet_time_duration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_trigger_minimum_quiet_time_duration.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeF64RFmxPulse_GetAttributeF64 |
| Description: | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to RFMXPULSE_VAL_IQ_POWER_EDGE_RISING_SLOPE, the signal is quiet below the trigger level. If you set the RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to RFMXPULSE_VAL_IQ_POWER_EDGE_FALLING_SLOPE, the signal is quiet above the trigger level. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default of this attribute is hardware dependent. Get Function: RFmxPulse_GetTriggerMinimumQuietTimeDuration Set Function: RFmxPulse_SetTriggerMinimumQuietTimeDuration |

<!--NI_TOPIC bundle=rfmx-pulse-cvi path=rfmxpulse_attr_trigger_minimum_quiet_time_mode.html language=enus -->
## TOPIC 00125: RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

- bundle_id: `rfmx-pulse-cvi`
- source_path: `rfmxpulse_attr_trigger_minimum_quiet_time_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-cvi/raw/resource/enus/rfmxpulse_attr_trigger_minimum_quiet_time_mode.html
- document_id: `rfmx-pulse-cvi`
- page_type: `leaf`
- content_type: ``

RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxPulse_SetAttributeI32RFmxPulse_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the minimum quiet time used for triggering. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXPULSE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL. Get Function: RFmxPulse_GetTriggerMinimumQuietTimeMode Set Function: RFmxPulse_SetTriggerMinimumQuietTimeMode |
| Values: | RFMXPULSE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL (0)The minimum quiet time for triggering is the value of the RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. RFMXPULSE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO (1)The measurement computes the minimum quiet time used for triggering. |
| RFMXPULSE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL (0) | The minimum quiet time for triggering is the value of the RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |
| RFMXPULSE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO (1) | The measurement computes the minimum quiet time used for triggering. |
