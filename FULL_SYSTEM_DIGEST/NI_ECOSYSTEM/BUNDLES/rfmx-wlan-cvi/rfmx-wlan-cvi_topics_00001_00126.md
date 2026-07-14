# NI DOCUMENT BUNDLE: rfmx-wlan-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-wlan-cvi start=1 end=126 -->
<!--NI_TOPIC bundle=rfmx-wlan-cvi path=bp_help_file_title.html language=enus -->
## TOPIC 00001: RFmx WLAN C Reference

- bundle_id: `rfmx-wlan-cvi`
- source_path: `bp_help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/bp_help_file_title.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmx WLAN C Reference

This help file contains information about the RFmx WLAN functions, attributes, and values that you can use when programming your application.

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_abortmeasurements.html language=enus -->
## TOPIC 00002: RFmxWLAN_AbortMeasurements

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_abortmeasurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_abortmeasurements.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_AbortMeasurements

int32 __stdcall RFmxWLAN_AbortMeasurements (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Stops acquisition and measurements associated with signal instance that you specify in the **selectorString** parameter, which were previously initiated by the [RFmxWLAN_Initiate](/csh?topicname=rfmxwlancvi/cvirfmxwlan_initiate.html) function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_analyzeiq1waveformsplit.html language=enus -->
## TOPIC 00003: RFmxWLAN_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_analyzeiq1waveformsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_analyzeiq1waveformsplit.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_AnalyzeIQ1WaveformSplit

int32 __stdcall RFmxWLAN_AnalyzeIQ1WaveformSplit (niRFmxInstrHandle instrumentHandle,
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
 Use this function only if the Recommended Acquisition Type attribute value is either **IQ** or **IQorSpectral**. 
When using the Analysis-Only mode in RFmxWLAN, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| x0 | float64 | Specifies the start time of the input y array. This value is expressed in seconds. |
| dx | float64 | Specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| I | float32[] | Specifies an array of real part of complex-valued time domain data. This array correspond to the in-phase (I) data. |
| Q | float32[] | Specifies an array of imaginary part of complex-valued time domain data. This array correspond to the quadrature-phase (Q) data. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | int64 | Reserved |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_analyzespectrum1waveform.html language=enus -->
## TOPIC 00004: RFmxWLAN_AnalyzeSpectrum1Waveform

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_analyzespectrum1waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_analyzespectrum1waveform.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_AnalyzeSpectrum1Waveform

int32 __stdcall RFmxWLAN_AnalyzeSpectrum1Waveform (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[],
 float64 x0,
 float64 dx,
 float32 spectrum[],
 int32 arraySize,
 int32 reset,
 int64 reserved);

#### Purpose

Performs the enabled measurements on the spectrum that you specify in the **spectrum** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node.
Use this function only if the Recommended Acquisition Type attribute value is either **spectral** or **IQorSpectral**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session refnum. instrumentHandle is obtained from the RFmxInstr_InitializeNIRFSA function or the RFmxInstr_InitializeNIRFSAArray function. |
| selectorString | char[] | Specifies the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| x0 | float64 | Specifies the start frequency of the spectrum. This value is expressed in Hz. |
| dx | float64 | Specifies the frequency interval between data points in the spectrum. |
| spectrum | float32[] | Specifies the array of real-value power spectrum. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_autodetectsignal.html language=enus -->
## TOPIC 00005: RFmxWLAN_AutoDetectSignal

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_autodetectsignal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_autodetectsignal.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_AutoDetectSignal

int32 __stdcall RFmxWLAN_AutoDetectSignal (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout);

#### Purpose

Automatically detects the standard, channel bandwidth, and burst length of the input signal, and writes the [RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_STANDARD](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_auto_detect_signal_detected_standard.html), [RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_CHANNEL_BANDWIDTH](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_auto_detect_signal_detected_channel_bandwidth.html), and [RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_BURST_LENGTH](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_auto_detect_signal_detected_burst_length.html) attributes. 
You must configure the [RFMXWLAN_ATTR_REFERENCE_LEVEL](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_reference_level.html) attribute before calling this function. If the peak power level of the input is unknown, you can call the [RFmxWLAN_AutoLevel](/csh?topicname=rfmxwlancvi/cvirfmxwlan_autolevel.html) function to configure the RFMXWLAN_ATTR_REFERENCE_LEVEL attribute after you set the [RFMXWLAN_ATTR_STANDARD](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_standard.html) and [RFMXWLAN_ATTR_CHANNEL_BANDWIDTH](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_channel_bandwidth.html) attributes to values corresponding to maximum expected channel bandwidth.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_buildsegmentstring.html language=enus -->
## TOPIC 00006: RFmxWLAN_BuildSegmentString

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_buildsegmentstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_buildsegmentstring.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_BuildSegmentString

int32 __stdcall RFmxWLAN_BuildSegmentString (char selectorString[],
 int32 segmentNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a segment string.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| segmentNumber | int32 | Specifies the segment number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. You can pass NULL for this parameter if selectorStringLength is set to 0, which will return the minimum buffer size required to create the signal string. If the selectorString buffer is not large enough to build the signal string, the function returns an error. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_cfgexternalattenuation.html language=enus -->
## TOPIC 00007: RFmxWLAN_CfgExternalAttenuation

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_cfgexternalattenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_cfgexternalattenuation.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_CfgExternalAttenuation

int32 __stdcall RFmxWLAN_CfgExternalAttenuation (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 externalAttenuation);

#### Purpose

Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. On a MIMO session, use port::(deviceName)/(channelNumber) as a selector string to configure external attenuation for each port.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and port string. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1""port::myrfsa1/0""signal::sig1/port::myrfsa1/0"You can use the RFmxWLAN_BuildSignalString function to build the selector string. On a MIMO session, you can use the RFmxInstr_BuildPortString function to build the selector string. |
| externalAttenuation | float64 | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_cfgselectedportsmultiple.html language=enus -->
## TOPIC 00008: RFmxWLAN_CfgSelectedPortsMultiple

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_cfgselectedportsmultiple.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_cfgselectedportsmultiple.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_CfgSelectedPortsMultiple

int32 __stdcall RFmxWLAN_CfgSelectedPortsMultiple (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char selectedPorts[]);

#### Purpose

Configures the selected ports to each segment/chain based on the values you set in [RFMXWLAN_ATTR_NUMBER_OF_FREQUENCY_SEGMENTS](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_number_of_frequency_segments.html) and [RFMXWLAN_ATTR_NUMBER_OF_RECEIVE_CHAINS](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_number_of_receive_chains.html) attributes.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| selectedPorts | char[] | Specifies the list of MIMO ports to be configured. Use "port::<deviceName>/<channelNumber>" as the format for the selected port. For PXIe-5830/5831/5832 devices on a MIMO session, the selected port includes the instrument port in the format "port::<deviceName>/<channelNumber>/<instrPort>".Example:port::myrfsa1/0/if1You can use the RFmxInstr_BuildPortString function to build the selected port. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_clearallnamedresults.html language=enus -->
## TOPIC 00009: RFmxWLAN_ClearAllNamedResults

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_clearallnamedresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_clearallnamedresults.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_ClearAllNamedResults

int32 __stdcall RFmxWLAN_ClearAllNamedResults (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears all results for the signal that you specify in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_clonesignalconfiguration.html language=enus -->
## TOPIC 00010: RFmxWLAN_CloneSignalConfiguration

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_clonesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_clonesignalconfiguration.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_CloneSignalConfiguration

int32 __stdcall RFmxWLAN_CloneSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char oldSignalName[],
 char newSignalName[]);

#### Purpose

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| oldSignalName | char[] | Specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::OldSigName""OldSigName" |
| newSignalName | char[] | Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_close.html language=enus -->
## TOPIC 00011: RFmxWLAN_Close

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_close.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_close.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_Close

int32 __stdcall RFmxWLAN_Close (niRFmxInstrHandle instrumentHandle, int32 forceDestroy);

#### Purpose

Closes the RFmx session.

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Close](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_close.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| forceDestroy | int32 | Specifies whether to destroy the RFmx session. RFMXWLAN_VAL_FALSE (0) Destroys the RFmx session. Call the RFmxWLAN_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. RFMXWLAN_VAL_TRUE (1) Destroys the RFmx session. You do not have to call the RFmxWLAN_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |
| RFMXWLAN_VAL_FALSE (0) | Destroys the RFmx session. Call the RFmxWLAN_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. |  |
| RFMXWLAN_VAL_TRUE (1) | Destroys the RFmx session. You do not have to call the RFmxWLAN_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_disabletrigger.html language=enus -->
## TOPIC 00012: RFmxWLAN_DisableTrigger

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_disabletrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_disabletrigger.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_DisableTrigger

int32 __stdcall RFmxWLAN_DisableTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_dsssmodacccfgacquisitionlength.html language=enus -->
## TOPIC 00013: RFmxWLAN_DSSSModAccCfgAcquisitionLength

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_dsssmodacccfgacquisitionlength.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_dsssmodacccfgacquisitionlength.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_DSSSModAccCfgAcquisitionLength

int32 __stdcall RFmxWLAN_DSSSModAccCfgAcquisitionLength (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 acquisitionLengthMode,
 float64 acquisitionLength);

#### Purpose

Configures the **acquisitionLength** parameter and the **acquisitionLengthMode** parameter of the acquired waveform for the measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| acquisitionLengthMode | int32 | Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc attributes. RFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_MANUAL (0) Uses the acquisition length specified by the acquisitionLength parameter.RFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_AUTO (1) Computes the acquisition length based on the RFMXWLAN_ATTR_DSSSMODACC_MEASUREMENT_OFFSET attribute and the RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH attribute. |
| RFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_MANUAL (0) | Uses the acquisition length specified by the acquisitionLength parameter. |  |
| RFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_AUTO (1) | Computes the acquisition length based on the RFMXWLAN_ATTR_DSSSMODACC_MEASUREMENT_OFFSET attribute and the RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH attribute. |  |
| acquisitionLength | float64 | Specifies the length of the waveform to be acquired for the DSSSModAcc measurement when you set the acquisitionLengthMode parameter to RFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_MANUAL. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_dsssmodaccfetchconstellationtrace.html language=enus -->
## TOPIC 00014: RFmxWLAN_DSSSModAccFetchConstellationTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_dsssmodaccfetchconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_dsssmodaccfetchconstellationtrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_DSSSModAccFetchConstellationTrace

int32 __stdcall RFmxWLAN_DSSSModAccFetchConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle constellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the constellation trace for the data field.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| constellation | NIComplexSingle[] | Returns the constellation of the received symbols. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributef32.html language=enus -->
## TOPIC 00015: RFmxWLAN_GetAttributeF32

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributef32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributef32.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeF32

int32 __stdcall RFmxWLAN_GetAttributeF32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributef32array.html language=enus -->
## TOPIC 00016: RFmxWLAN_GetAttributeF32Array

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributef32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributef32array.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeF32Array

int32 __stdcall RFmxWLAN_GetAttributeF32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributef64.html language=enus -->
## TOPIC 00017: RFmxWLAN_GetAttributeF64

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributef64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributef64.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeF64

int32 __stdcall RFmxWLAN_GetAttributeF64 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 *attrVal);

#### Purpose

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float64* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributef64array.html language=enus -->
## TOPIC 00018: RFmxWLAN_GetAttributeF64Array

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributef64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributef64array.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeF64Array

int32 __stdcall RFmxWLAN_GetAttributeF64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributei16.html language=enus -->
## TOPIC 00019: RFmxWLAN_GetAttributeI16

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributei16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributei16.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeI16

int32 __stdcall RFmxWLAN_GetAttributeI16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int16 *attrVal);

#### Purpose

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int16* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributei32.html language=enus -->
## TOPIC 00020: RFmxWLAN_GetAttributeI32

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributei32.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeI32

int32 __stdcall RFmxWLAN_GetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributei32array.html language=enus -->
## TOPIC 00021: RFmxWLAN_GetAttributeI32Array

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributei32array.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeI32Array

int32 __stdcall RFmxWLAN_GetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributei64.html language=enus -->
## TOPIC 00022: RFmxWLAN_GetAttributeI64

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributei64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributei64.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeI64

int32 __stdcall RFmxWLAN_GetAttributeI64 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 *attrVal);

#### Purpose

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int64* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributei64array.html language=enus -->
## TOPIC 00023: RFmxWLAN_GetAttributeI64Array

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributei64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributei64array.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeI64Array

int32 __stdcall RFmxWLAN_GetAttributeI64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributei8.html language=enus -->
## TOPIC 00024: RFmxWLAN_GetAttributeI8

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributei8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributei8.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeI8

int32 __stdcall RFmxWLAN_GetAttributeI8 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributenicomplexdoublearray.html language=enus -->
## TOPIC 00025: RFmxWLAN_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributenicomplexdoublearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributenicomplexdoublearray.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeNIComplexDoubleArray

int32 __stdcall RFmxWLAN_GetAttributeNIComplexDoubleArray (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributenicomplexsinglearray.html language=enus -->
## TOPIC 00026: RFmxWLAN_GetAttributeNIComplexSingleArray

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributenicomplexsinglearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributenicomplexsinglearray.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeNIComplexSingleArray

int32 __stdcall RFmxWLAN_GetAttributeNIComplexSingleArray (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributestring.html language=enus -->
## TOPIC 00027: RFmxWLAN_GetAttributeString

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributestring.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeString

int32 __stdcall RFmxWLAN_GetAttributeString (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[]);

#### Purpose

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

 If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributeu16.html language=enus -->
## TOPIC 00028: RFmxWLAN_GetAttributeU16

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributeu16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributeu16.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeU16

int32 __stdcall RFmxWLAN_GetAttributeU16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt16 *attrVal);

#### Purpose

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt16* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributeu32.html language=enus -->
## TOPIC 00029: RFmxWLAN_GetAttributeU32

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributeu32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributeu32.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeU32

int32 __stdcall RFmxWLAN_GetAttributeU32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributeu32array.html language=enus -->
## TOPIC 00030: RFmxWLAN_GetAttributeU32Array

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributeu32array.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeU32Array

int32 __stdcall RFmxWLAN_GetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributeu64array.html language=enus -->
## TOPIC 00031: RFmxWLAN_GetAttributeU64Array

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributeu64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributeu64array.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeU64Array

int32 __stdcall RFmxWLAN_GetAttributeU64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributeu8.html language=enus -->
## TOPIC 00032: RFmxWLAN_GetAttributeU8

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributeu8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributeu8.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeU8

int32 __stdcall RFmxWLAN_GetAttributeU8 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_getattributeu8array.html language=enus -->
## TOPIC 00033: RFmxWLAN_GetAttributeU8Array

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_getattributeu8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_getattributeu8array.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetAttributeU8Array

int32 __stdcall RFmxWLAN_GetAttributeU8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_geterror.html language=enus -->
## TOPIC 00034: RFmxWLAN_GetError

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_geterror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_geterror.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_GetError

int32 __stdcall RFmxWLAN_GetError (niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[]);

#### Purpose

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter. 
 
If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For **Example**, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. 
 

 If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

|  | Note Use the RFmxWLAN_GetErrorString function if the RFmxWLAN_GetError function does not return an error message. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the RFmx session. If a valid session handle is passed, the last error stored in that session is retrieved. You can pass NULL to retrieve the last error stored in the current execution thread. |
| errorCode | int32* | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescriptionBufferSize | int32 | Passes the number of bytes in the char array you specify in the errorDescription parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string. The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_initialize.html language=enus -->
## TOPIC 00035: rfmxwlan_Initialize

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_initialize.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_Initialize

int32 __stdcall RFmxWLAN_Initialize (char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession);

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
| isNewSession | int32* | Returns RFMXWLAN_VAL_TRUE if the function created a new session, or RFMXWLAN_VAL_FALSE if the function returned a reference to an existing session. |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Identifies your instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_initiate.html language=enus -->
## TOPIC 00036: RFmxWLAN_Initiate

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_initiate.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_Initiate

int32 __stdcall RFmxWLAN_Initiate (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[]);

#### Purpose

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the [RFmxWLAN_WaitforMeasurementComplete](/csh?topicname=rfmxwlancvi/cvirfmxwlan_waitformeasurementcomplete.html) function or [RFmxWLAN_CheckMeasurementStatus](/csh?topicname=rfmxwlancvi/cvirfmxwlan_checkmeasurementstatus.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"""result::r1""r1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfg1referencewaveform.html language=enus -->
## TOPIC 00037: RFmxWLAN_OFDMModAccCfg1ReferenceWaveform

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfg1referencewaveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfg1referencewaveform.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfg1ReferenceWaveform

int32 __stdcall RFmxWLAN_OFDMModAccCfg1ReferenceWaveform (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 x0,
 float64 dx,
 NIComplexSingle referenceWaveform[],
 int32 arraySize);

#### Purpose

Configures the reference waveform for a SISO measurement when you set the [RFMXWLAN_ATTR_OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_ofdmmodacc_evm_reference_data_symbols_mode.html) attribute to RFMXWLAN_VAL_OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_REFERENCE_WAVEFORM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| x0 | float64 | Specifies the starting time of the reference waveform. This value is expressed in seconds. |
| dx | float64 | Specifies the sampling interval of the reference waveform. This value is expressed in seconds. |
| referenceWaveform | NIComplexSingle[] | Specifies an array of waveform samples of the reference waveform. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgamplitudetrackingenabled.html language=enus -->
## TOPIC 00038: RFmxWLAN_OFDMModAccCfgAmplitudeTrackingEnabled

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgamplitudetrackingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgamplitudetrackingenabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgAmplitudeTrackingEnabled

int32 __stdcall RFmxWLAN_OFDMModAccCfgAmplitudeTrackingEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 amplitudeTrackingEnabled);

#### Purpose

Configures whether to enable pilot-based mean amplitude tracking per OFDM data symbol.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| amplitudeTrackingEnabled | int32 | Specifies whether to enable pilot-based mean amplitude tracking per OFDM data symbol. Amplitude tracking is useful if the mean amplitude of the OFDM symbols in a PPDU varies over time. However, enabling tracking may degrade EVM because of attempts to track random amplitude distortions caused by additive noise and other distortions. RFMXWLAN_VAL_OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE (0) Amplitude tracking is disabled.RFMXWLAN_VAL_OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_TRUE (1) Amplitude tracking is enabled. |
| RFMXWLAN_VAL_OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE (0) | Amplitude tracking is disabled. |  |
| RFMXWLAN_VAL_OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_TRUE (1) | Amplitude tracking is enabled. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgevmunit.html language=enus -->
## TOPIC 00039: RFmxWLAN_OFDMModAccCfgEVMUnit

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgevmunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgevmunit.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgEVMUnit

int32 __stdcall RFmxWLAN_OFDMModAccCfgEVMUnit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 EVMUnit);

#### Purpose

Configures EVM unit for the measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| EVMUnit | int32 | Specifies the unit for the EVM results. RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_PERCENTAGE (0) EVM results are returned in dB. RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_DB (1) EVM results are returned as a percentage. |
| RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_PERCENTAGE (0) | EVM results are returned in dB. |  |
| RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_DB (1) | EVM results are returned as a percentage. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgfrequencyerrorestimationmethod.html language=enus -->
## TOPIC 00040: RFmxWLAN_OFDMModAccCfgFrequencyErrorEstimationMethod

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgfrequencyerrorestimationmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgfrequencyerrorestimationmethod.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgFrequencyErrorEstimationMethod

int32 __stdcall RFmxWLAN_OFDMModAccCfgFrequencyErrorEstimationMethod (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 frequencyErrorEstimationMethod);

#### Purpose

Configures the frequency error estimation method for the OFDMModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| frequencyErrorEstimationMethod | int32 | Specifies the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal. RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_DISABLED (0) Carrier frequency error is not computed and the corresponding result is returned as NaN. RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_INITIAL_PREAMBLE (1) Initial short and long training fields in the PPDU are used.RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE (2) Initial short and long training fields along with the SIGnal fields are used.RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS (3) The initial short and long training fields, SIGnal fields, and the pilot subcarriers in the DATA field are used.RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_PILOTS_AND_DATA (4) The initial short and long training fields, SIGnal fields, and all the subcarriers in the DATA field are used. |
| RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_DISABLED (0) | Carrier frequency error is not computed and the corresponding result is returned as NaN. |  |
| RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_INITIAL_PREAMBLE (1) | Initial short and long training fields in the PPDU are used. |  |
| RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE (2) | Initial short and long training fields along with the SIGnal fields are used. |  |
| RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS (3) | The initial short and long training fields, SIGnal fields, and the pilot subcarriers in the DATA field are used. |  |
| RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_PILOTS_AND_DATA (4) | The initial short and long training fields, SIGnal fields, and all the subcarriers in the DATA field are used. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgmeasurementlength.html language=enus -->
## TOPIC 00041: RFmxWLAN_OFDMModAccCfgMeasurementLength

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgmeasurementlength.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgmeasurementlength.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgMeasurementLength

int32 __stdcall RFmxWLAN_OFDMModAccCfgMeasurementLength (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 measurementOffset,
 int32 maximumMeasurementLength);

#### Purpose

Configures the measurement offset and maximum measurement length for the OFDMModAcc EVM measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| measurementOffset | int32 | Specifies the number of data OFDM symbols to be ignored from the start of the data field for EVM computation. |
| maximumMeasurementLength | int32 | Specifies the maximum number of data OFDM symbols that the measurement uses to compute EVM. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgmeasurementmode.html language=enus -->
## TOPIC 00042: RFmxWLAN_OFDMModAccCfgMeasurementMode

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgmeasurementmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgmeasurementmode.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgMeasurementMode

int32 __stdcall RFmxWLAN_OFDMModAccCfgMeasurementMode (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 measurementMode);

#### Purpose

Configures the measurement mode for the OFDMModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| measurementMode | int32 | Specifies whether the measurement should calibrate the noise floor of the analyzer or perform the OFDMModAcc measurement. RFMXWLAN_VAL_OFDMMODACC_MEASUREMENT_MODE_MEASURE (0) The OFDMModAcc measurement is performed on the acquired signal. RFMXWLAN_VAL_OFDMMODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR (1) The OFDMModAcc measurement measures the noise floor of the instrument across the frequency range of interest determined by the carrier frequency and channel bandwidth. In this mode, the measurement expects that the signal generator to be turned off and checks whether no signal power is detected at the RF In port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is previously calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |
| RFMXWLAN_VAL_OFDMMODACC_MEASUREMENT_MODE_MEASURE (0) | The OFDMModAcc measurement is performed on the acquired signal. |  |
| RFMXWLAN_VAL_OFDMMODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR (1) | The OFDMModAcc measurement measures the noise floor of the instrument across the frequency range of interest determined by the carrier frequency and channel bandwidth. In this mode, the measurement expects that the signal generator to be turned off and checks whether no signal power is detected at the RF In port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is previously calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgnoisecompensationenabled.html language=enus -->
## TOPIC 00043: RFmxWLAN_OFDMModAccCfgNoiseCompensationEnabled

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgnoisecompensationenabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgNoiseCompensationEnabled

int32 __stdcall RFmxWLAN_OFDMModAccCfgNoiseCompensationEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 noiseCompensationEnabled);

#### Purpose

Configures whether to enable EVM noise compensation for the OFDMModAcc measurement. 
**supporteddevices:**PXIe-5830/5831/5832/5646/5840/5841/5842/5860.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| noiseCompensationEnabled | int32 | Specifies whether the contribution of the instrument noise is compensated for EVM computation. RFMXWLAN_VAL_OFDMMODACC_NOISE_COMPENSATION_ENABLED_FALSE (0) Disables instrument noise compensation for EVM results.RFMXWLAN_VAL_OFDMMODACC_NOISE_COMPENSATION_ENABLED_TRUE (1) Enables instrument noise compensation for EVM results. |
| RFMXWLAN_VAL_OFDMMODACC_NOISE_COMPENSATION_ENABLED_FALSE (0) | Disables instrument noise compensation for EVM results. |  |
| RFMXWLAN_VAL_OFDMMODACC_NOISE_COMPENSATION_ENABLED_TRUE (1) | Enables instrument noise compensation for EVM results. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgnreferencewaveforms.html language=enus -->
## TOPIC 00044: RFmxWLAN_OFDMModAccCfgNReferenceWaveforms

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgnreferencewaveforms.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgnreferencewaveforms.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgNReferenceWaveforms

int32 __stdcall RFmxWLAN_OFDMModAccCfgNReferenceWaveforms (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 x0[],
 float64 dx[],
 NIComplexSingle referenceWaveform[],
 int32 referenceWaveformSize[],
 int32 arraySize);

#### Purpose

Configures the reference waveform array for a MIMO measurement when you set the [RFMXWLAN_ATTR_OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_ofdmmodacc_evm_reference_data_symbols_mode.html) attribute to RFMXWLAN_VAL_OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_REFERENCE_WAVEFORM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| x0 | float64[] | Specifies the starting time of the reference waveform. This value is expressed in seconds. |
| dx | float64[] | Specifies the sampling interval of the reference waveform. This value is expressed in seconds. |
| referenceWaveform | NIComplexSingle[] | Specifies an array of waveform samples of the reference waveform. |
| referenceWaveformSize | int32[] | Specifies the size of reference waveform. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgnreferencewaveformssplit.html language=enus -->
## TOPIC 00045: RFmxWLAN_OFDMModAccCfgNReferenceWaveformsSplit

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgnreferencewaveformssplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgnreferencewaveformssplit.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgNReferenceWaveformsSplit

int32 __stdcall RFmxWLAN_OFDMModAccCfgNReferenceWaveformsSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 x0[],
 float64 dx[],
 float32 I[],
 float32 Q[],
 int32 referenceWaveformSize[],
 int32 arraySize);

#### Purpose

Configures the reference waveform array for a MIMO measurement when you set the [RFMXWLAN_ATTR_OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_ofdmmodacc_evm_reference_data_symbols_mode.html) attribute to RFMXWLAN_VAL_OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_REFERENCE_WAVEFORM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| x0 | float64[] | Specifies the starting time of the reference waveform. This value is expressed in seconds. |
| dx | float64[] | Specifies the sampling interval of the reference waveform. This value is expressed in seconds. |
| referenceWaveform | NIComplexSingle[] | Specifies an imaginary part of an array of waveform samples of the reference waveform. |
| referenceWaveform | NIComplexSingle[] | Specifies the real part of an array of waveform samples of the reference waveform. |
| referenceWaveformSize | int32[] | Specifies the size of reference waveform. |
| arraySize | int32 | Specifies the size of the array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgoptimizedynamicrangeforevm.html language=enus -->
## TOPIC 00046: RFmxWLAN_OFDMModAccCfgOptimizeDynamicRangeForEVM

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgoptimizedynamicrangeforevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgoptimizedynamicrangeforevm.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgOptimizeDynamicRangeForEVM

int32 __stdcall RFmxWLAN_OFDMModAccCfgOptimizeDynamicRangeForEVM (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 optimizeDynamicRangeForEVMEnabled,
 float64 optimizeDynamicRangeForEVMMargin);

#### Purpose

Specifies whether to optimize analyzerâ€™s dynamic range for the EVM measurement. 
**supporteddevices:**PXIe-5646/5840/5841/5842/5860.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| optimizeDynamicRangeForEVMEnabled | int32 | Specifies whether to optimize the analyzerâ€™s dynamic range for the EVM measurement. This parameter computes optimum attenuation settings for the analyzer based on the reference level you specify while still avoiding ADC or onboard signal processing (OSP) overflow. When you specify the reference level and you notice an overflow error, you can increase the reference level or specify a margin above the reference level by configuring the optimizeDynamicRangeForEVMMargin parameter. RFMXWLAN_VAL_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED_FALSE (0) Specifies that the dynamic range is not optimized for EVM measurement. RFMXWLAN_VAL_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED_TRUE (1) Specifies that the dynamic range is optimized for EVM measurement. |
| RFMXWLAN_VAL_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED_FALSE (0) | Specifies that the dynamic range is not optimized for EVM measurement. |  |
| RFMXWLAN_VAL_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED_TRUE (1) | Specifies that the dynamic range is optimized for EVM measurement. |  |
| optimizeDynamicRangeForEVMMargin | float64 | Specifies the margin above the reference level you specify when you set the optimizeDynamicRangeForEVMEnabled parameter to RFMXWLAN_VAL_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED_TRUE. This value is expressed in dB. When the parameter's value is 0, the dynamic range is optimized. When you set a positive value to the parameter, the dynamic range reduces from the optimized dynamic range. You can use this parameter to avoid ADC and onboard signal processing (OSP) overflows. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgphasetrackingenabled.html language=enus -->
## TOPIC 00047: RFmxWLAN_OFDMModAccCfgPhaseTrackingEnabled

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgphasetrackingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgphasetrackingenabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgPhaseTrackingEnabled

int32 __stdcall RFmxWLAN_OFDMModAccCfgPhaseTrackingEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 phaseTrackingEnabled);

#### Purpose

Configures whether to enable pilot-based common phase error correction per OFDM data symbol.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| phaseTrackingEnabled | int32 | Specifies whether to enable pilot-based common phase error correction per OFDM data symbol. Phase tracking is useful for tracking the phase variation over the modulation symbol caused by the residual frequency offset and phase noise. RFMXWLAN_VAL_OFDMMODACC_PHASE_TRACKING_ENABLED_FALSE (0) Phase tracking is disabled. RFMXWLAN_VAL_OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE (1) Phase tracking is enabled. |
| RFMXWLAN_VAL_OFDMMODACC_PHASE_TRACKING_ENABLED_FALSE (0) | Phase tracking is disabled. |  |
| RFMXWLAN_VAL_OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE (1) | Phase tracking is enabled. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodacccfgsymbolclockerrorcorrectionenabled.html language=enus -->
## TOPIC 00048: RFmxWLAN_OFDMModAccCfgSymbolClockErrorCorrectionEnabled

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodacccfgsymbolclockerrorcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodacccfgsymbolclockerrorcorrectionenabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccCfgSymbolClockErrorCorrectionEnabled

int32 __stdcall RFmxWLAN_OFDMModAccCfgSymbolClockErrorCorrectionEnabled (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 symbolClockErrorCorrectionEnabled);

#### Purpose

Configures whether to enable symbol clock error correction.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| symbolClockErrorCorrectionEnabled | int32 | Specifies whether to enable symbol clock error correction. RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_FALSE (0) Symbol clock error correction is disabled.RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE (1) Symbol clock error correction is enabled. |
| RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_FALSE (0) | Symbol clock error correction is disabled. |  |
| RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE (1) | Symbol clock error correction is enabled. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccclearnoisecalibrationdatabase.html language=enus -->
## TOPIC 00049: RFmxWLAN_OFDMModAccClearNoiseCalibrationDatabase

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccclearnoisecalibrationdatabase.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccclearnoisecalibrationdatabase.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccClearNoiseCalibrationDatabase

int32 __stdcall RFmxWLAN_OFDMModAccClearNoiseCalibrationDatabase (niRFmxInstrHandle instrumentHandle);

#### Purpose

Clears the noise calibration database used for EVM noise compensation.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchchainpilotrmsevmpersymbolmeantrace.html language=enus -->
## TOPIC 00050: RFmxWLAN_OFDMModAccFetchChainPilotRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchchainpilotrmsevmpersymbolmeantrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchchainpilotrmsevmpersymbolmeantrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchChainPilotRMSEVMPerSymbolMeanTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchChainPilotRMSEVMPerSymbolMeanTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 chainPilotRMSEVMPerSymbolMean[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the chain pilot-subcarriers RMS EVM per symbol trace. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_ofdmmodacc_averaging_enabled.html) attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this function returns the mean of the chain pilot RMS EVM per symbol computed for each averaging count. 
Use "segment(*n*)/chain(*k*)" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | float64* | Returns the OFDM symbol increment value. This value is always equal to 1. |
| chainPilotRMSEVMPerSymbolMean | float32[] | Returns an array of chain pilot-subcarriers RMS EVM of each OFDM symbol. When you set the RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT attribute to RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT attribute to RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_DB, the measurement returns this result in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchdecodedservicebitstrace.html language=enus -->
## TOPIC 00051: RFmxWLAN_OFDMModAccFetchDecodedServiceBitsTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchdecodedservicebitstrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchdecodedservicebitstrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchDecodedServiceBitsTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedServiceBitsTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 decodedServiceBits[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the decoded Service bits.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"user0""signal::sig1/user0""signal::sig1/result::r1/user0""result::r1/user0"You can use the RFmxWLAN_BuildUserString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| decodedServiceBits | int32[] | Returns an array of Service bits obtained after demodulation and decoding. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchdecodedsigbbitstrace.html language=enus -->
## TOPIC 00052: RFmxWLAN_OFDMModAccFetchDecodedSIGBBitsTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchdecodedsigbbitstrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchdecodedsigbbitstrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchDecodedSIGBBitsTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedSIGBBitsTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 decodedSIGBBits[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the decoded SIG-B bits.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| decodedSIGBBits | int32[] | Returns an array of bits in the VHT-SIG-B field of the 802.11ac waveform or the HE-SIG-B field of the 802.11ax waveform. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchdecodedusigbitstrace.html language=enus -->
## TOPIC 00053: RFmxWLAN_OFDMModAccFetchDecodedUSIGBitsTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchdecodedusigbitstrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchdecodedusigbitstrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchDecodedUSIGBitsTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedUSIGBitsTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 decodedUSIGBits[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the decoded U-SIG bits trace.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| decodedUSIGBits | int32[] | Returns the array of bits in the U-SIG field of the 802.11be waveform for all 80 MHz subblocks. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchfrequencyerrorccdf10percent.html language=enus -->
## TOPIC 00054: RFmxWLAN_OFDMModAccFetchFrequencyErrorCCDF10Percent

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchfrequencyerrorccdf10percent.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchfrequencyerrorccdf10percent.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchFrequencyErrorCCDF10Percent

int32 __stdcall RFmxWLAN_OFDMModAccFetchFrequencyErrorCCDF10Percent (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* frequencyErrorCCDF10Percent);

#### Purpose

Fetches the 10% point of the complementary cumulative distribution function (CCDF) of frequency error across the number of iterations. 
Use "segment<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. Example:"segment0""signal::sig1/segment0""result::r1/segment0""signal::sig1/result::r1/segment0"You can use the RFmxWLAN_BuildSegmentString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| frequencyErrorCCDF10Percent | float64* | Returns the 10% point of the CCDF of absolute frequency error. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, the CCDF is computed over each averaging count. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchfrequencyerrormean.html language=enus -->
## TOPIC 00055: RFmxWLAN_OFDMModAccFetchFrequencyErrorMean

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchfrequencyerrormean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchfrequencyerrormean.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchFrequencyErrorMean

int32 __stdcall RFmxWLAN_OFDMModAccFetchFrequencyErrorMean (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* frequencyErrorMean);

#### Purpose

Fetches the carrier frequency error of the transmitter. 
Use "segment<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. Example:"segment0""signal::sig1/segment0""result::r1/segment0""signal::sig1/result::r1/segment0"You can use the RFmxWLAN_BuildSegmentString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| frequencyErrorMean | float64* | Returns the carrier frequency error of the transmitter. This value is expressed in Hz. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this attribute returns the mean of the carrier frequency error results computed for each averaging count. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchiqimpairments.html language=enus -->
## TOPIC 00056: RFmxWLAN_OFDMModAccFetchIQImpairments

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchiqimpairments.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchiqimpairments.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchIQImpairments

int32 __stdcall RFmxWLAN_OFDMModAccFetchIQImpairments (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* relativeIQOriginOffsetMean,
 float64* IQGainImbalanceMean,
 float64* IQQuadratureErrorMean,
 float64* absoluteIQOriginOffsetMean,
 float64* IQTimingSkewMean);

#### Purpose

Fetches the I/Q Impairment results for the OFDMModAcc measurement. 
Use "segment<*n*>/chain<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| relativeIQOriginOffsetMean | float64* | Returns the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this attribute returns the mean of the relative I/Q origin offset computed for each averaging count. This value is expressed in dB. |
| IQGainImbalanceMean | float64* | Returns the I/Q gain imbalance, which is the ratio of the RMS amplitude of the in-phase (I) component of the signal to the RMS amplitude of the quadrature-phase (Q) component of the signal. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this attribute returns the mean of the I/Q gain imbalance computed for each averaging count. This value is expressed in dB. |
| IQQuadratureErrorMean | float64* | Returns the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this attribute returns the I/Q quadrature error computed for each averaging count. This value is expressed in degrees. |
| absoluteIQOriginOffsetMean | float64* | Returns the absolute I/Q origin offset, which is the power of the DC subcarrier. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this attribute returns the mean of the absolute I/Q origin offset computed for each averaging count. This value is expressed in dBm. |
| IQTimingSkewMean | float64* | Returns the I/Q timing skew, which is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this attribute returns the mean of the I/Q timing skew computed for each averaging count. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchnumberofhesigbsymbols.html language=enus -->
## TOPIC 00057: RFmxWLAN_OFDMModAccFetchNumberOfHESIGBSymbols

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchnumberofhesigbsymbols.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchnumberofhesigbsymbols.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchNumberOfHESIGBSymbols

int32 __stdcall RFmxWLAN_OFDMModAccFetchNumberOfHESIGBSymbols (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* numberOfHESIGBSymbols);

#### Purpose

Fetches the number of HE-SIG-B symbols.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| numberOfHESIGBSymbols | int32* | Returns the number of HE-SIG-B symbols. This result is applicable for 802.11ax MU PPDU signals, and is decoded from the HE-SIG-A field. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchnumberofsymbolsused.html language=enus -->
## TOPIC 00058: RFmxWLAN_OFDMModAccFetchNumberofSymbolsUsed

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchnumberofsymbolsused.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchnumberofsymbolsused.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchNumberofSymbolsUsed

int32 __stdcall RFmxWLAN_OFDMModAccFetchNumberofSymbolsUsed (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* numberOfSymbolsUsed);

#### Purpose

Fetches the number of OFDM symbols used for EVM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| numberOfSymbolsUsed | int32* | Returns the number of OFDM symbols used by the measurement. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchpeduration.html language=enus -->
## TOPIC 00059: RFmxWLAN_OFDMModAccFetchPEDuration

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchpeduration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchpeduration.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchPEDuration

int32 __stdcall RFmxWLAN_OFDMModAccFetchPEDuration (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* PEDuration);

#### Purpose

Fetches the duration of the packet extension field.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| PEDuration | float64* | Returns the duration of the packet extension field for the 802.11ax and 802.11be signals. This parameter is applicable only when you set the RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED attribute to RFMXWLAN_VAL_OFDM_HEADER_DECODING_ENABLED_TRUE. This value is expressed in seconds. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11ac.html language=enus -->
## TOPIC 00060: RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ac

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11ac.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11ac.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ac

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ac (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* VHTSIGAAveragePowerMean,
 float64* VHTSTFAveragePowerMean,
 float64* VHTLTFAveragePowerMean,
 float64* VHTSIGBAveragePowerMean);

#### Purpose

Fetches the average power of the 802.11ac specific preamble fields. 
Use "segment<*n*>/chain<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| VHTSIGAAveragePowerMean | float64* | Returns the average power of the VHT-SIG-A field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the VHT-SIG-A field average power results computed for each averaging count. This value is expressed in dBm. |
| VHTSTFAveragePowerMean | float64* | Returns the average power of the VHT-STF field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the VHT-STF average power results computed for each averaging count. This value is expressed in dBm. |
| VHTLTFAveragePowerMean | float64* | Returns the average power of the VHT-LTF field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this paramter returns the mean of the VHT-LTF average power results computed for each averaging count. This value is expressed in dBm. |
| VHTSIGBAveragePowerMean | float64* | Returns the average power of the VHT-SIG-B field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the VHT-SIG-B field average power results computed for each averaging count. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11ax.html language=enus -->
## TOPIC 00061: RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ax

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11ax.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11ax.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ax (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* RLSIGAveragePowerMean,
 float64* HESIGAAveragePowerMean,
 float64* HESIGBAveragePowerMean,
 float64* HESTFAveragePowerMean,
 float64* HELTFAveragePowerMean);

#### Purpose

Fetches the average power of the 802.11ax specific preamble fields. 
Use "segment<*n*>/chain<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| RLSIGAveragePowerMean | float64* | Returns the average power of the RL-SIG field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the RL-SIG field average power results computed for each averaging count. This value is expressed in dBm. |
| HESIGAAveragePowerMean | float64* | Returns the average power of the HE-SIG-A field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the HE-SIG-A field average power results computed for each averaging count. This value is expressed in dBm. |
| HESIGBAveragePowerMean | float64* | Returns the average power of the HE-SIG-B field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the HE-SIG-B field average power results computed for each averaging count. This value is expressed in dBm. |
| HESTFAveragePowerMean | float64* | Returns the average power of the HE-STF field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the HE-STF average power results computed for each averaging count. This value is expressed in dBm. |
| HELTFAveragePowerMean | float64* | Returns the average power of the HE-LTF field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the HE-LTF average power results computed for each averaging count. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11be.html language=enus -->
## TOPIC 00062: RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11be

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11be.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11be.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11be

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11be (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* RLSIGAveragePowerMean,
 float64* USIGAveragePowerMean,
 float64* EHTSIGAveragePowerMean,
 float64* EHTSTFAveragePowerMean,
 float64* EHTLTFAveragePowerMean);

#### Purpose

Fetches the average power of the 802.11be specific preamble fields. 
Use "segment<*n*>/chain<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| RLSIGAveragePowerMean | float64* | Returns the average power of the RL-SIG field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the RL-SIG field average power results computed for each averaging count. This value is expressed in dBm. |
| USIGAveragePowerMean | float64* | Returns the average power of the U-SIG field. When you set the OFDMModAcc Averaging Enabled attribute to true, this paramter returns the mean of the U-SIG average power results computed for each averaging count. This value is expressed in dBm. |
| EHTSIGAveragePowerMean | float64* | Returns the average power of the EHT-SIG field. When you set the OFDMModAcc Averaging Enabled attribute to true, this parameter returns the mean of the EHT-SIG average power results computed for each averaging count. This value is expressed in dBm. |
| EHTSTFAveragePowerMean | float64* | Returns the average power of the EHT-STF field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the EHT-STF average power results computed for each averaging count. This value is expressed in dBm. |
| EHTLTFAveragePowerMean | float64* | Returns the average power of the EHT-LTF field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the EHT-LTF average power results computed for each averaging count. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11n.html language=enus -->
## TOPIC 00063: RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11n

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11n.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchpreambleaveragepowers802_11n.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11n

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11n (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* HTSIGAveragePowerMean,
 float64* HTSTFAveragePowerMean,
 float64* HTDLTFAveragePowerMean,
 float64* HTELTFAveragePowerMean);

#### Purpose

Fetches the average power of the 802.11n specific preamble fields. 
Use "segment<*n*>/chain<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| HTSIGAveragePowerMean | float64* | Returns the average power of the HT-SIG field. When you set the OFDMModAcc Averaging Enabled attribute to true, this parameter returns the mean of the HT-SIG field average power results computed for each averaging count. This value is expressed in dBm. |
| HTSTFAveragePowerMean | float64* | Returns the average power of the HT-STF field. When you set the OFDMModAcc Averaging Enabled attribute to true, this parameter returns the mean of the HT-STF average power results computed for each averaging count. This value is expressed in dBm. |
| HTDLTFAveragePowerMean | float64* | Returns the average power of the HT-DLTF. When you set the OFDMModAcc Averaging Enabled attribute to true, this parameter returns the mean of the HT-DLTF average power results computed for each averaging count. This value is expressed in dBm. |
| HTELTFAveragePowerMean | float64* | Returns the average power of the HT-ELTF field. When you set the OFDMModAcc Averaging Enabled attribute to true, this parameter returns the mean of the HT-ELTF average power results computed for each averaging count. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchpreamblefrequencyerrortrace.html language=enus -->
## TOPIC 00064: RFmxWLAN_OFDMModAccFetchPreambleFrequencyErrorTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchpreamblefrequencyerrortrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchpreamblefrequencyerrortrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchPreambleFrequencyErrorTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleFrequencyErrorTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 preambleFrequencyError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the preamble frequency error trace for signals containing an OFDM payload. Preamble frequency error computes the variations, across time, of the frequency error over initial 16us which comprises of the short training field (STF) and long training field (LTF) symbols.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time in seconds. |
| dx | float64* | Returns the time increment value. This value is the reciprocal of OFDM ModAcc processing rate. |
| preambleFrequencyError | float32[] | Returns the preamble frequency error at every sampling time. This value is expressed in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchsigbcrcstatus.html language=enus -->
## TOPIC 00065: RFmxWLAN_OFDMModAccFetchSIGBCRCStatus

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchsigbcrcstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchsigbcrcstatus.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchSIGBCRCStatus

int32 __stdcall RFmxWLAN_OFDMModAccFetchSIGBCRCStatus (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* SIGBCRCStatus);

#### Purpose

Fetches the SIG-B CRC Status.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| SIGBCRCStatus | int32* | Returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform. RFMXWLAN_VAL_OFDMMODACC_SIG_B_CRC_STATUS_NOT_APPLICABLE (-1) Returns that the SIG-B CRC is invalid for the current waveform. RFMXWLAN_VAL_OFDMMODACC_SIG_B_CRC_STATUS_FAIL (0) Returns that the SIG-B CRC failed. RFMXWLAN_VAL_OFDMMODACC_SIG_B_CRC_STATUS_PASS (1) Returns that the SIG-B CRC passed. |
| RFMXWLAN_VAL_OFDMMODACC_SIG_B_CRC_STATUS_NOT_APPLICABLE (-1) | Returns that the SIG-B CRC is invalid for the current waveform. |  |
| RFMXWLAN_VAL_OFDMMODACC_SIG_B_CRC_STATUS_FAIL (0) | Returns that the SIG-B CRC failed. |  |
| RFMXWLAN_VAL_OFDMMODACC_SIG_B_CRC_STATUS_PASS (1) | Returns that the SIG-B CRC passed. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchsigcrcstatus.html language=enus -->
## TOPIC 00066: RFmxWLAN_OFDMModAccFetchSIGCRCStatus

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchsigcrcstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchsigcrcstatus.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchSIGCRCStatus

int32 __stdcall RFmxWLAN_OFDMModAccFetchSIGCRCStatus (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* SIGCRCStatus);

#### Purpose

Fetches the SIG CRC Status.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| SIGCRCStatus | int32* | Returns whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform. RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_NOT_APPLICABLE (-1) Returns that the SIG CRC is invalid for the current waveform. RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_FAIL (0) Returns that the SIG CRC failed. RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_PASS (1) Returns that the SIG CRC passed. |
| RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_NOT_APPLICABLE (-1) | Returns that the SIG CRC is invalid for the current waveform. |  |
| RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_FAIL (0) | Returns that the SIG CRC failed. |  |
| RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_PASS (1) | Returns that the SIG CRC passed. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchspectralflatness.html language=enus -->
## TOPIC 00067: RFmxWLAN_OFDMModAccFetchSpectralFlatness

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchspectralflatness.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchspectralflatness.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchSpectralFlatness

int32 __stdcall RFmxWLAN_OFDMModAccFetchSpectralFlatness (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* spectralFlatnessMargin,
 int32* spectralFlatnessMarginSubcarrierIndex);

#### Purpose

Fetches the spectral flatness margin results. 
Use "segment<*n*>/chain<*k*>/stream<*l*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, chain number, and stream number. If you do not specify the signal name, the default signal instance is used. Example:"segment0/chain0/stream0""signal::sig1/segment0/chain0/stream0""signal::sig1/result::r1/segment0/chain0/stream0""result::r1/segment0/chain0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| spectralFlatnessMargin | float64* | Returns the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. The upper spectral flatness margin is the minimum difference between the upper mask and the spectral flatness across subcarriers. The lower spectral flatness margin is the minimum difference between the spectral flatness and the lower mask across subcarriers. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, the spectral flatness is computed using the mean of the channel frequency response magnitude computed for each averaging count. This value is expressed in dB. |
| spectralFlatnessMarginSubcarrierIndex | int32* | Returns the subcarrier index corresponding to the spectralFlatnessMargin parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchspectralflatnessmeantrace.html language=enus -->
## TOPIC 00068: RFmxWLAN_OFDMModAccFetchSpectralFlatnessMeanTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchspectralflatnessmeantrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchspectralflatnessmeantrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchSpectralFlatnessMeanTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchSpectralFlatnessMeanTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 spectralFlatnessMean[],
 float32 spectralFlatnessLowerMask[],
 float32 spectralFlatnessUpperMask[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the spectral flatness trace, and the lower and upper spectral flatness mask traces. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_ofdmmodacc_averaging_enabled.html) attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this function returns the spectral flatness trace computed on the mean of the channel estimates computed for each averaging count. 
Use "segment<*n*>/chain<*k*>/stream<*l*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, chain number, and stream number. If you do not specify the signal name, the default signal instance is used. Example:"segment0/chain0/stream0""signal::sig1/segment0/chain0/stream0""signal::sig1/result::r1/segment0/chain0/stream0""result::r1/segment0/chain0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting subcarrier index. |
| dx | float64* | Returns the subcarrier increment value. This value is always 1. |
| spectralFlatnessMean | float32[] | Returns an array of spectral flatness for each subcarrier. This value is expressed in dB. |
| spectralFlatnessLowerMask | float32[] | Returns an array of spectral flatness lower mask for each subcarrier. This value is expressed in dB. |
| spectralFlatnessUpperMask | float32[] | Returns an array of spectral flatness upper mask for each subcarrier. This value is expressed in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchstreampilotrmsevmpersymbolmeantrace.html language=enus -->
## TOPIC 00069: RFmxWLAN_OFDMModAccFetchStreamPilotRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchstreampilotrmsevmpersymbolmeantrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchstreampilotrmsevmpersymbolmeantrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchStreamPilotRMSEVMPerSymbolMeanTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamPilotRMSEVMPerSymbolMeanTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 streamPilotRMSEVMPerSymbolMean[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the stream pilot subcarriers RMS EVM per symbol trace.
 
Use "segment<*n*>/stream<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | float64* | Returns the OFDM symbol increment value. This value is always equal to 1. |
| streamPilotRMSEVMPerSymbolMean | float32[] | Returns the stream pilot subcarriers RMS EVM of each OFDM symbol. This value is expressed as a percentage or in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchstreamrmsevm.html language=enus -->
## TOPIC 00070: RFmxWLAN_OFDMModAccFetchStreamRMSEVM

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchstreamrmsevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchstreamrmsevm.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchStreamRMSEVM

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamRMSEVM (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* streamRMSEVMMean,
 float64* streamDataRMSEVMMean,
 float64* streamPilotRMSEVMMean);

#### Purpose

Fetches the stream RMS EVM results.
 
Use "segment<*n*>/stream<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| streamRMSEVMMean | float64* | Returns the stream RMS EVM of all subcarriers in all OFDM symbols. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. |
| streamDataRMSEVMMean | float64* | Returns the stream RMS EVM of data subcarriers in all OFDM symbols. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of data stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. |
| streamPilotRMSEVMMean | float64* | Returns the stream RMS EVM of pilot subcarriers in all OFDM symbols. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of pilot stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchstreamrmsevmpersubcarriermeantrace.html language=enus -->
## TOPIC 00071: RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchstreamrmsevmpersubcarriermeantrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchstreamrmsevmpersubcarriermeantrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 streamRMSEVMPerSubcarrierMean[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the stream RMS EVM per subcarrier trace.
 
Use "segment<*n*>/stream<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting subcarrier index. |
| dx | float64* | Returns the subcarrier increment value. This value is always 1. |
| streamRMSEVMPerSubcarrierMean | float32[] | Returns the stream RMS EVM for each subcarrier. This value is expressed as a percentage or in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchstreamrmsevmpersymbolmeantrace.html language=enus -->
## TOPIC 00072: RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchstreamrmsevmpersymbolmeantrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchstreamrmsevmpersymbolmeantrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSymbolMeanTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSymbolMeanTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 streamRMSEVMPerSymbolMean[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the stream RMS EVM per symbol trace.
 
Use "segment<*n*>/stream<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | float64* | Returns the OFDM symbol increment value. This value is always equal to 1. |
| streamRMSEVMPerSymbolMean | float32[] | Returns the stream RMS EVM of each OFDM symbol. This value is expressed as a percentage or in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchsubcarrierchainevmpersymboltrace.html language=enus -->
## TOPIC 00073: RFmxWLAN_OFDMModAccFetchSubcarrierChainEVMPerSymbolTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchsubcarrierchainevmpersymboltrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchsubcarrierchainevmpersymboltrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchSubcarrierChainEVMPerSymbolTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchSubcarrierChainEVMPerSymbolTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 subcarrierIndex,
 float64* x0,
 float64* dx,
 float32 subcarrierChainEVMPerSymbol[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the chain EVM per symbol trace for a subcarrier. For unoccupied subcarriers, the trace value is NaN. 
Use "segment<*n*>/chain<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| subcarrierIndex | int32 | Specifies the subcarrier index for which the trace is fetched. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | float64* | Returns the OFDM symbol increment value. This value is always equal to 1. |
| subcarrierChainEVMPerSymbol | float32[] | Returns an array of chain EVM of each OFDM symbol for the specified subcarrier index. When you set the RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT attribute to RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT attribute to RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_DB, the measurement returns this result in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchsubcarrierstreamevmpersymboltrace.html language=enus -->
## TOPIC 00074: RFmxWLAN_OFDMModAccFetchSubcarrierStreamEVMPerSymbolTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchsubcarrierstreamevmpersymboltrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchsubcarrierstreamevmpersymboltrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchSubcarrierStreamEVMPerSymbolTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchSubcarrierStreamEVMPerSymbolTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 subcarrierIndex,
 float64* x0,
 float64* dx,
 float32 subcarrierStreamEVMPerSymbol[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the stream EVM per symbol trace for a subcarrier. 
Use "segment(*n*)/stream(*k*)" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| subcarrierIndex | int32 | Specifies the subcarrier index for which to fetch the trace. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | float64* | Returns the OFDM symbol increment value. This value is always equal to 1. |
| subcarrierStreamEVMPerSymbol | float32[] | Returns the stream EVM of each OFDM symbol for the specified subcarrier index. This value is expressed as a percentage or in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchsymbolchainevmpersubcarriertrace.html language=enus -->
## TOPIC 00075: RFmxWLAN_OFDMModAccFetchSymbolChainEVMPerSubcarrierTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchsymbolchainevmpersubcarriertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchsymbolchainevmpersubcarriertrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchSymbolChainEVMPerSubcarrierTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchSymbolChainEVMPerSubcarrierTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 symbolIndex,
 float64* x0,
 float64* dx,
 float32 symbolChainEVMPerSubcarrier[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the chain EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN. 
Use "segment<*n*>/chain<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| symbolIndex | int32 | Specifies the symbol index for which to fetch the trace. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting subcarrier index. |
| dx | float64* | Returns the subcarrier increment value. This value is always 1. |
| symbolChainEVMPerSubcarrier | float32[] | Returns an array of chain EVM for each subcarrier for the specified symbol index. When you set the RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT attribute to RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_PERCENTAGE, the measurement returns this result as a percentage. When you set the RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT attribute to RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_DB, the measurement returns this result in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchsymbolclockerrormean.html language=enus -->
## TOPIC 00076: RFmxWLAN_OFDMModAccFetchSymbolClockErrorMean

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchsymbolclockerrormean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchsymbolclockerrormean.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchSymbolClockErrorMean

int32 __stdcall RFmxWLAN_OFDMModAccFetchSymbolClockErrorMean (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* symbolClockErrorMean);

#### Purpose

Fetches the symbol clock error of the transmitter. 
Use "segment<*n*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. Example:"segment0""signal::sig1/segment0""result::r1/segment0""signal::sig1/result::r1/segment0"You can use the RFmxWLAN_BuildSegmentString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| symbolClockErrorMean | float64* | Returns the symbol clock error of the transmitter. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this parameter returns the mean of the symbol clock error results computed for each averaging count. This value is expressed in parts per million (ppm). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchsymbolstreamevmpersubcarriertrace.html language=enus -->
## TOPIC 00077: RFmxWLAN_OFDMModAccFetchSymbolStreamEVMPerSubcarrierTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchsymbolstreamevmpersubcarriertrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchsymbolstreamevmpersubcarriertrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchSymbolStreamEVMPerSubcarrierTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchSymbolStreamEVMPerSubcarrierTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32 symbolIndex,
 float64* x0,
 float64* dx,
 float32 symbolStreamEVMPerSubcarrier[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the stream EVM per subcarrier trace for a symbol.
 
Use "segment<*n*>/stream<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| symbolIndex | int32 | Specifies the symbol index for which to fetch the trace. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting subcarrier index. |
| dx | float64* | Returns the subcarrier increment value. This value is always 1. |
| symbolStreamEVMPerSubcarrier | float32[] | Returns the stream EVM for each subcarrier for the specified symbol index. This value is expressed as a percentage or in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchunusedtoneerror.html language=enus -->
## TOPIC 00078: RFmxWLAN_OFDMModAccFetchUnusedToneError

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchunusedtoneerror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchunusedtoneerror.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchUnusedToneError

int32 __stdcall RFmxWLAN_OFDMModAccFetchUnusedToneError (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* unusedToneErrorMargin,
 int32* unusedToneErrorMarginRUIndex);

#### Purpose

Fetches the unused tone error margin results. 
Refer to Unused Tone Error Measurement for more information. 
Use "segment<*n*>/chain<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| unusedToneErrorMargin | float64* | Describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| unusedToneErrorMarginRUIndex | int32* | Returns the 26-tone RU index corresponding to the unusedToneErrorMargin parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchuserstreamdatarmsevmpersymbolmeantrace.html language=enus -->
## TOPIC 00079: RFmxWLAN_OFDMModAccFetchUserStreamDataRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchuserstreamdatarmsevmpersymbolmeantrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchuserstreamdatarmsevmpersymbolmeantrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchUserStreamDataRMSEVMPerSymbolMeanTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserStreamDataRMSEVMPerSymbolMeanTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 userStreamDataRMSEVMPerSymbolMean[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_ofdmmodacc_averaging_enabled.html) attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this function returns the mean of the user stream data RMS EVM per symbol computed for each averaging count.
 
Use "user<*n*>/stream<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"user0/stream0""signal::sig1/user0/stream0""signal::sig1/result::r1/user0/stream0""result::r1/user0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | float64* | Returns the OFDM symbol increment value. This value is always equal to 1. |
| userStreamDataRMSEVMPerSymbolMean | float32[] | Returns the stream data subcarriers RMS EVM of each OFDM symbol for each user. This value is expressed as a percentage or in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_ofdmmodaccfetchuserstreamrmsevmpersymbolmeantrace.html language=enus -->
## TOPIC 00080: RFmxWLAN_OFDMModAccFetchUserStreamRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_ofdmmodaccfetchuserstreamrmsevmpersymbolmeantrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_ofdmmodaccfetchuserstreamrmsevmpersymbolmeantrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_OFDMModAccFetchUserStreamRMSEVMPerSymbolMeanTrace

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserStreamRMSEVMPerSymbolMeanTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 userStreamRMSEVMPerSymbolMean[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the stream RMS EVM per symbol trace for each user. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_ofdmmodacc_averaging_enabled.html) attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this function returns the mean of the user stream RMS EVM per symbol computed for each averaging count.
 
Use "user<*n*>/stream<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"user0/stream0""signal::sig1/user0/stream0""signal::sig1/result::r1/user0/stream0""result::r1/user0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | float64* | Returns the OFDM symbol increment value. This value is always equal to 1. |
| userStreamRMSEVMPerSymbolMean | float32[] | Returns the stream RMS EVM of each OFDM symbol for each user. This value is expressed as a percentage or in dB. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_powerrampfetchfalltrace.html language=enus -->
## TOPIC 00081: RFmxWLAN_PowerRampFetchFallTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_powerrampfetchfalltrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_powerrampfetchfalltrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_PowerRampFetchFallTrace

int32 __stdcall RFmxWLAN_PowerRampFetchFallTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 rawWaveform[],
 float32 processedWaveform[],
 float32 threshold[],
 float32 powerReference[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the raw, processed, thresholding and power reference waveforms at the end of a burst.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the trace start time. This value is expressed in seconds. |
| dx | float64* | Returns the sampling interval. This value is expressed in seconds. |
| rawWaveform | float32[] | Returns an array of measured signal power. This value is expressed as a percentage. |
| processedWaveform | float32[] | Returns an array of measured envelope power. This value is expressed as a percentage. |
| threshold | float32[] | Returns an array of threshold values. This value is expressed as a percentage. |
| powerReference | float32[] | Returns an array of power reference values. This value is expressed as a percentage. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_powerrampfetchrisetrace.html language=enus -->
## TOPIC 00082: RFmxWLAN_PowerRampFetchRiseTrace

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_powerrampfetchrisetrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_powerrampfetchrisetrace.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_PowerRampFetchRiseTrace

int32 __stdcall RFmxWLAN_PowerRampFetchRiseTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 rawWaveform[],
 float32 processedWaveform[],
 float32 threshold[],
 float32 powerReference[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the raw, processed, threshold and power-reference traces at the beginning of a burst.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the trace start time. This value is expressed in seconds. |
| dx | float64* | Returns the sampling interval. This value is expressed in seconds. |
| rawWaveform | float32[] | Returns an array of measured signal power. This value is expressed as a percentage. |
| processedWaveform | float32[] | Returns an array of measured envelope power. This value is expressed as a percentage. |
| threshold | float32[] | Returns an array of threshold values. This value is expressed as a percentage. |
| powerReference | float32[] | Returns an array of power reference values. This value is expressed as a percentage. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_resettodefault.html language=enus -->
## TOPIC 00083: RFmxWLAN_ResetToDefault

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_resettodefault.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_resettodefault.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_ResetToDefault

int32 __stdcall RFmxWLAN_ResetToDefault (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Resets a signal to the default values.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_semcfgaveraging.html language=enus -->
## TOPIC 00084: RFmxWLAN_SEMCfgAveraging

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_semcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_semcfgaveraging.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_SEMCfgAveraging

int32 __stdcall RFmxWLAN_SEMCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount,
 int32 averagingType);

#### Purpose

Configures averaging for the measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the SEM. RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition. RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_TRUE (1) The measurement uses the averagingCount parameter as the number of acquisitions over which the results are averaged. |
| RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_TRUE (1) | The measurement uses the averagingCount parameter as the number of acquisitions over which the results are averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_TRUE. |
| averagingType | int32 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. RFMXWLAN_VAL_SEM_AVERAGING_TYPE_RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXWLAN_VAL_SEM_AVERAGING_TYPE_LOG (1) The power spectrum is averaged in a logarithmic scale.RFMXWLAN_VAL_SEM_AVERAGING_TYPE_SCALAR (2) The square root of the power spectrum is averaged.RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM (3) The peak power in the spectrum at each frequency bin is retained from one record to the next.RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MINIMUM (4) The least power in the spectrum at each frequency bin is retained from one record to the next. |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |  |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum at each frequency bin is retained from one record to the next. |  |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum at each frequency bin is retained from one record to the next. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_semcfgmasktype.html language=enus -->
## TOPIC 00085: RFmxWLAN_SEMCfgMaskType

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_semcfgmasktype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_semcfgmasktype.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_SEMCfgMaskType

int32 __stdcall RFmxWLAN_SEMCfgMaskType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 maskType);

#### Purpose

Configures the mask type for the SEM measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| maskType | int32 | Specifies whether the mask used for the SEM measurement is as per the 3GPP standard or specified by you. RFMXWLAN_VAL_SEM_MASK_TYPE_STANDARD (0) Mask limits are configured as per the standard.RFMXWLAN_VAL_SEM_MASK_TYPE_CUSTOM (1) Mask limits are configured by you. |
| RFMXWLAN_VAL_SEM_MASK_TYPE_STANDARD (0) | Mask limits are configured as per the standard. |  |
| RFMXWLAN_VAL_SEM_MASK_TYPE_CUSTOM (1) | Mask limits are configured by you. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_semcfgnumberofoffsets.html language=enus -->
## TOPIC 00086: RFmxWLAN_SEMCfgNumberOfOffsets

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_semcfgnumberofoffsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_semcfgnumberofoffsets.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_SEMCfgNumberOfOffsets

int32 __stdcall RFmxWLAN_SEMCfgNumberOfOffsets (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfOffsets);

#### Purpose

Configures the number of offset segments for the SEM measurement when you set the [RFMXWLAN_ATTR_SEM_MASK_TYPE](/csh?topicname=rfmxwlancvi/rfmxwlan_attr_sem_mask_type.html) attribute to RFMXWLAN_VAL_SEM_MASK_TYPE_CUSTOM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| numberOfOffsets | int32 | Specifies the number of SEM offset segments. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=cvirfmxwlan_waitformeasurementcomplete.html language=enus -->
## TOPIC 00087: RFmxWLAN_WaitForMeasurementComplete

- bundle_id: `rfmx-wlan-cvi`
- source_path: `cvirfmxwlan_waitformeasurementcomplete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/cvirfmxwlan_waitformeasurementcomplete.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN_WaitForMeasurementComplete

int32 __stdcall RFmxWLAN_WaitForMeasurementComplete (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout);

#### Purpose

Waits for the specified number for seconds for all the measurements to complete.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxWLAN_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxWLAN_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_maximum_measurement_length.html language=enus -->
## TOPIC 00088: RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_maximum_measurement_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_maximum_measurement_length.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies the maximum number of data chips that the measurement uses to compute EVM. This value is expressed in chips. If you set this attribute to -1, all chips in the signal are used for measurement.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1000. Get Function: RFmxWLAN_DSSSModAccGetMaximumMeasurementLength Set Function: RFmxWLAN_DSSSModAccSetMaximumMeasurementLength |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_measurement_enabled.html language=enus -->
## TOPIC 00089: RFMXWLAN_ATTR_DSSSMODACC_MEASUREMENT_ENABLED

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_measurement_enabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies whether to enable the DSSSModAcc measurement, which is a measurement of the modulation accuracy on signals conforming to the DSSS PHY defined in section 15 and the High Rate DSSS PHY defined in section 16 of IEEE Standard 802.11-2016. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWLAN_VAL_FALSE. Get Function: RFmxWLAN_DSSSModAccGetMeasurementEnabled Set Function: RFmxWLAN_DSSSModAccSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_measurement_offset.html language=enus -->
## TOPIC 00090: RFMXWLAN_ATTR_DSSSMODACC_MEASUREMENT_OFFSET

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_measurement_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_measurement_offset.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_MEASUREMENT_OFFSET

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies the number of data chips to be ignored from the start of the data field for the EVM computation. This value is expressed in chips. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxWLAN_DSSSModAccGetMeasurementOffset Set Function: RFmxWLAN_DSSSModAccSetMeasurementOffset |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_header_average_power_mean.html language=enus -->
## TOPIC 00091: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_AVERAGE_POWER_MEAN

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_header_average_power_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_header_average_power_mean.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_AVERAGE_POWER_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the average power of the header field of the PPDU. This value is expressed in dBm. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE, this result returns the mean of the average header field power computed for each averaging count.You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsHeaderAveragePowerMean |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_header_crc_status.html language=enus -->
## TOPIC 00092: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_CRC_STATUS

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_header_crc_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_header_crc_status.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_CRC_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeI32 |
| Description: | Returns whether the header cyclic redundancy check (CRC) is successfully passed, as defined in section 16.2.3.7 of IEEE Standard 802.11 2016. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsHeaderCRCStatus |
| Values: | RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_FAIL (0)Returns that the header CRC failed. RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_PASS (1)Returns that the header CRC passed. |
| RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_FAIL (0) | Returns that the header CRC failed. |
| RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_PASS (1) | Returns that the header CRC passed. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_locked_clocks_bit.html language=enus -->
## TOPIC 00093: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_LOCKED_CLOCKS_BIT

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_locked_clocks_bit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_locked_clocks_bit.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_LOCKED_CLOCKS_BIT

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeI32 |
| Description: | Returns the value of the locked clocks bit in the Long PHY SERVICE field. A value of 1 indicates that the transmit frequency and the symbol clock are derived from the same oscillator. A value of 0 indicates that the transmit frequency and the symbol clock are derived from independent oscillators.You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsLockedClocksBit |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_number_of_chips_used.html language=enus -->
## TOPIC 00094: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_NUMBER_OF_CHIPS_USED

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_number_of_chips_used.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_number_of_chips_used.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_NUMBER_OF_CHIPS_USED

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeI32 |
| Description: | Returns the number of chips used for the DSSSModAcc measurement. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsNumberOfChipsUsed |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_peak_evm_802_11_1999_maximum.html language=enus -->
## TOPIC 00095: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_1999_MAXIMUM

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_peak_evm_802_11_1999_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_peak_evm_802_11_1999_maximum.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_1999_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the peak EVM of the burst. This value is expressed as percentage or in dB. This measurement is performed in accordance with section 18.4.7.8 of IEEE Standard 802.11b-1999. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE, this result returns the maximum of the peak EVM computed for each averaging count. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsPeakEVM802_11_1999Maximum |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_peak_evm_802_11_2007_maximum.html language=enus -->
## TOPIC 00096: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2007_MAXIMUM

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_peak_evm_802_11_2007_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_peak_evm_802_11_2007_maximum.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2007_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. This measurement is performed in accordance with section 18.4.7.8 of IEEE Standard 802.11-2007. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE, this result returns the maximum value of the peak EVM computed for each averaging count. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsPeakEVM802_11_2007Maximum |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_peak_evm_802_11_2016_maximum.html language=enus -->
## TOPIC 00097: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2016_MAXIMUM

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_peak_evm_802_11_2016_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_peak_evm_802_11_2016_maximum.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2016_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. This measurement is performed in accordance with section 16.3.7.9 of IEEE Standard 802.11-2016. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE, this result returns the maximum value of the peak EVM computed for each averaging count.You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsPeakEVM802_11_2016Maximum |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_preamble_average_power_mean.html language=enus -->
## TOPIC 00098: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PREAMBLE_AVERAGE_POWER_MEAN

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_preamble_average_power_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_preamble_average_power_mean.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PREAMBLE_AVERAGE_POWER_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the average power of the preamble field of the PPDU. This value is expressed in dBm. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE, this result returns the mean of the average preamble field power computed for each averaging count. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsPreambleAveragePowerMean |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_psdu_crc_status.html language=enus -->
## TOPIC 00099: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PSDU_CRC_STATUS

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_psdu_crc_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_psdu_crc_status.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PSDU_CRC_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeI32 |
| Description: | IndicatesÂ whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. The measurement calculates the CRC over the decoded bits, excluding the last 32 bits. The measurement then compares this value with the CRC value in the received payload, which is represented by the last 32 bits of the PSDU. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsPSDUCRCStatus |
| Values: | RFMXWLAN_VAL_DSSSMODACC_PSDU_CRC_STATUS_FAIL (0) Indicates that the PSDU CRC failed. RFMXWLAN_VAL_DSSSMODACC_PSDU_CRC_STATUS_PASS (1) Indicates that the PSDU CRC passed. |
| RFMXWLAN_VAL_DSSSMODACC_PSDU_CRC_STATUS_FAIL (0) | Indicates that the PSDU CRC failed. |
| RFMXWLAN_VAL_DSSSMODACC_PSDU_CRC_STATUS_PASS (1) | Indicates that the PSDU CRC passed. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_rms_evm_mean.html language=enus -->
## TOPIC 00100: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_RMS_EVM_MEAN

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_rms_evm_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_rms_evm_mean.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_RMS_EVM_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the RMS EVM of the burst. This value is expressed as a percentage or in dB. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE, this result returns the mean of the RMS EVM computed for each averaging count.You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsRMSEVMMean |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_rms_magnitude_error_mean.html language=enus -->
## TOPIC 00101: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_RMS_MAGNITUDE_ERROR_MEAN

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_rms_magnitude_error_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_rms_magnitude_error_mean.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_RMS_MAGNITUDE_ERROR_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the RMS magnitude error of the received constellation, which is the RMS level of the one minus the magnitude error of the received constellation symbols. This value is expressed as a percentage. When you set this RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE, this result returns the mean of the RMS magnitude error computed for each averaging count.You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsRMSMagnitudeErrorMean |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_dsssmodacc_results_rms_phase_error_mean.html language=enus -->
## TOPIC 00102: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_RMS_PHASE_ERROR_MEAN

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_dsssmodacc_results_rms_phase_error_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_dsssmodacc_results_rms_phase_error_mean.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_RMS_PHASE_ERROR_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the RMS phase error of the received constellation, which is the RMS level of difference between the ideal and the actual values of the phase of the received constellation symbols. This value is expressed in degrees. When you set this RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE, this result returns the mean of the RMS phase error computed for each averaging count.You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_DSSSModAccGetResultsRMSPhaseErrorMean |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_ofdm_mu_mimo_ltf_mode_enabled.html language=enus -->
## TOPIC 00103: RFMXWLAN_ATTR_OFDM_MU_MIMO_LTF_MODE_ENABLED

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_ofdm_mu_mimo_ltf_mode_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_ofdm_mu_mimo_ltf_mode_enabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_OFDM_MU_MIMO_LTF_MODE_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code. This attribute is valid for 802.11ax TB PPDU only.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWLAN_VAL_OFDM_MU_MIMO_LTF_MODE_ENABLED_FALSE. Get Function: RFmxWLAN_GetOFDMMUMIMOLTFModeEnabled Set Function: RFmxWLAN_SetOFDMMUMIMOLTFModeEnabled |
| Values: | RFMXWLAN_VAL_OFDM_MU_MIMO_LTF_MODE_ENABLED_FALSE (0)Specifies that the LTF sequence uses single stream pilots. RFMXWLAN_VAL_OFDM_MU_MIMO_LTF_MODE_ENABLED_TRUE (1)Specifies that the LTF sequence is HE masked. |
| RFMXWLAN_VAL_OFDM_MU_MIMO_LTF_MODE_ENABLED_FALSE (0) | Specifies that the LTF sequence uses single stream pilots. |
| RFMXWLAN_VAL_OFDM_MU_MIMO_LTF_MODE_ENABLED_TRUE (1) | Specifies that the LTF sequence is HE masked. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_ofdm_number_of_he_sig_b_symbols.html language=enus -->
## TOPIC 00104: RFMXWLAN_ATTR_OFDM_NUMBER_OF_HE_SIG_B_SYMBOLS

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_ofdm_number_of_he_sig_b_symbols.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_ofdm_number_of_he_sig_b_symbols.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_OFDM_NUMBER_OF_HE_SIG_B_SYMBOLS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies the number of HE-SIG-B symbols. This attribute is applicable only to 802.11ax MU PPDU signals. You must configure this attribute if the RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED attribute is set to RFMXWLAN_VAL_OFDM_HEADER_DECODING_ENABLED_FALSE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxWLAN_GetOFDMNumberOfHESIGBSymbols Set Function: RFmxWLAN_SetOFDMNumberOfHESIGBSymbols |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_ofdmmodacc_results_power_custom_gate_peak_power_maximum.html language=enus -->
## TOPIC 00105: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_CUSTOM_GATE_PEAK_POWER_MAXIMUM

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_ofdmmodacc_results_power_custom_gate_peak_power_maximum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_ofdmmodacc_results_power_custom_gate_peak_power_maximum.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_CUSTOM_GATE_PEAK_POWER_MAXIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the peak power of the custom gate. This value is expressed in dBm. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this attribute returns the maximum of the custom gate peak power results computed for each averaging count.Use 'gate(n)' as the selector string to read this result. Get Function: RFmxWLAN_OFDMModAccGetResultsCustomGatePeakPowerMaximum |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_ofdmmodacc_results_power_eht_sig_average_power_mean.html language=enus -->
## TOPIC 00106: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_EHT_SIG_AVERAGE_POWER_MEAN

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_ofdmmodacc_results_power_eht_sig_average_power_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_ofdmmodacc_results_power_eht_sig_average_power_mean.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_EHT_SIG_AVERAGE_POWER_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the average power of the EHT-SIG field. This value is expressed in dBm. This result is applicable only to 802.11be signals. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE, this attribute returns the mean of the EHT-SIG field average power results computed for each averaging count.You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_OFDMModAccGetResultsEHTSIGAveragePowerMean |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_ofdmmodacc_symbol_clock_error_correction_enabled.html language=enus -->
## TOPIC 00107: RFMXWLAN_ATTR_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_ofdmmodacc_symbol_clock_error_correction_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_ofdmmodacc_symbol_clock_error_correction_enabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies whether to enable symbol clock error correction. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE. Get Function: RFmxWLAN_OFDMModAccGetSymbolClockErrorCorrectionEnabled Set Function: RFmxWLAN_OFDMModAccSetSymbolClockErrorCorrectionEnabled |
| Values: | RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_FALSE (0)Symbol clock error correction is disabled. RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE (1)Symbol clock error correction is enabled. |
| RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_FALSE (0) | Symbol clock error correction is disabled. |
| RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE (1) | Symbol clock error correction is enabled. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_powerramp_number_of_analysis_threads.html language=enus -->
## TOPIC 00108: RFMXWLAN_ATTR_POWERRAMP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_powerramp_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_powerramp_number_of_analysis_threads.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_POWERRAMP_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for PowerRamp measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxWLAN_PowerRampGetNumberOfAnalysisThreads Set Function: RFmxWLAN_PowerRampSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_sem_averaging_enabled.html language=enus -->
## TOPIC 00109: RFMXWLAN_ATTR_SEM_AVERAGING_ENABLED

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_sem_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_sem_averaging_enabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_SEM_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the SEM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_FALSE. Get Function: RFmxWLAN_SEMGetAveragingEnabled Set Function: RFmxWLAN_SEMSetAveragingEnabled |
| Values: | RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_TRUE (1)The SEM measurement uses the RFMXWLAN_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |
| RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_TRUE (1) | The SEM measurement uses the RFMXWLAN_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_sem_averaging_type.html language=enus -->
## TOPIC 00110: RFMXWLAN_ATTR_SEM_AVERAGING_TYPE

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_sem_averaging_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_sem_averaging_type.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_SEM_AVERAGING_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWLAN_VAL_SEM_AVERAGING_TYPE_RMS. Get Function: RFmxWLAN_SEMGetAveragingType Set Function: RFmxWLAN_SEMSetAveragingType |
| Values: | RFMXWLAN_VAL_SEM_AVERAGING_TYPE_RMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. RFMXWLAN_VAL_SEM_AVERAGING_TYPE_LOG (1)The power spectrum is averaged in a logarithmic scale. RFMXWLAN_VAL_SEM_AVERAGING_TYPE_SCALAR (2)The square root of the power spectrum is averaged. RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM (3)The peak power in the spectrum is retained from one acquisition to the next at each frequency bin. RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MINIMUM (4)The least power in the spectrum is retained from one acquisition to the next at each frequency bin. |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_LOG (1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_SCALAR (2) | The square root of the power spectrum is averaged. |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM (3) | The peak power in the spectrum is retained from one acquisition to the next at each frequency bin. |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MINIMUM (4) | The least power in the spectrum is retained from one acquisition to the next at each frequency bin. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_sem_offset_relative_limit_stop.html language=enus -->
## TOPIC 00111: RFMXWLAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_sem_offset_relative_limit_stop.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_sem_offset_relative_limit_stop.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeF64RFmxWLAN_GetAttributeF64 |
| Description: | Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. Use 'offset(n)' as the selector string to configure this attribute. The default value is -20. Get Function: RFmxWLAN_SEMGetOffsetRelativeLimitStop Set Function: RFmxWLAN_SEMSetOffsetRelativeLimitStop |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_sem_offset_sideband.html language=enus -->
## TOPIC 00112: RFMXWLAN_ATTR_SEM_OFFSET_SIDEBAND

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_sem_offset_sideband.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_sem_offset_sideband.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_SEM_OFFSET_SIDEBAND

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies whether the offset segment is present on one side or on both sides of the carrier. Use 'offset(n)' as the selector string to configure this attribute. The default value is RFMXWLAN_VAL_SEM_OFFSET_SIDEBAND_BOTH. Get Function: RFmxWLAN_SEMGetOffsetSideband Set Function: RFmxWLAN_SEMSetOffsetSideband |
| Values: | RFMXWLAN_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE (0)Configures a lower offset segment to the left of the carrier. RFMXWLAN_VAL_SEM_OFFSET_SIDEBAND_POSITIVE (1)Configures an upper offset segment to the right of the carrier. RFMXWLAN_VAL_SEM_OFFSET_SIDEBAND_BOTH (2)Configures both negative and positive offset segments. |
| RFMXWLAN_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE (0) | Configures a lower offset segment to the left of the carrier. |
| RFMXWLAN_VAL_SEM_OFFSET_SIDEBAND_POSITIVE (1) | Configures an upper offset segment to the right of the carrier. |
| RFMXWLAN_VAL_SEM_OFFSET_SIDEBAND_BOTH (2) | Configures both negative and positive offset segments. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_sem_results_measurement_status.html language=enus -->
## TOPIC 00113: RFMXWLAN_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_sem_results_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_sem_results_measurement_status.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeI32 |
| Description: | Returns the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxWLAN_SEMGetResultsMeasurementStatus |
| Values: | RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_FAIL (0)The spectrum exceeds the SEM measurement mask limits for at least one of the offset segments. RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_PASS (1)The spectrum does not exceed the SEM measurement mask limits for any offset segment. |
| RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_FAIL (0) | The spectrum exceeds the SEM measurement mask limits for at least one of the offset segments. |
| RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_PASS (1) | The spectrum does not exceed the SEM measurement mask limits for any offset segment. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_sem_results_upper_offset_margin_frequency.html language=enus -->
## TOPIC 00114: RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_sem_results_upper_offset_margin_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_sem_results_upper_offset_margin_frequency.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the frequency of the spectrum corresponding to the result of the RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxWLAN_SEMGetResultsUpperOffsetMarginFrequency |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_sem_results_upper_offset_measurement_status.html language=enus -->
## TOPIC 00115: RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_sem_results_upper_offset_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_sem_results_upper_offset_measurement_status.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeI32 |
| Description: | Returns the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxWLAN_SEMGetResultsUpperOffsetMeasurementStatus |
| Values: | RFMXWLAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL (0)The spectrum exceeds the SEM measurement mask and limits for the upper offset segment. RFMXWLAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS (1)The spectrum does not exceed the SEM measurement mask and limits for the upper offset segment. |
| RFMXWLAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL (0) | The spectrum exceeds the SEM measurement mask and limits for the upper offset segment. |
| RFMXWLAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS (1) | The spectrum does not exceed the SEM measurement mask and limits for the upper offset segment. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_sem_results_upper_offset_peak_frequency.html language=enus -->
## TOPIC 00116: RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_sem_results_upper_offset_peak_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_sem_results_upper_offset_peak_frequency.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the frequency at which the peak power occurs in the offset (positive) channel. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxWLAN_SEMGetResultsUpperOffsetPeakFrequency |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_sem_results_upper_offset_relative_integrated_power.html language=enus -->
## TOPIC 00117: RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_sem_results_upper_offset_relative_integrated_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_sem_results_upper_offset_relative_integrated_power.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxWLAN_GetAttributeF64 |
| Description: | Returns the average power of the offset (positive) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxWLAN_SEMGetResultsUpperOffsetRelativeIntegratedPower |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_sem_sweep_time_interval.html language=enus -->
## TOPIC 00118: RFMXWLAN_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_sem_sweep_time_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_sem_sweep_time_interval.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_SEM_SWEEP_TIME_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeF64RFmxWLAN_GetAttributeF64 |
| Description: | Specifies the sweep time for the SEM measurement. This value is expressed in seconds. This attribute is ignored when you set the RFMXWLAN_ATTR_SEM_SWEEP_TIME_AUTO attribute to RFMXWLAN_VAL_SEM_SWEEP_TIME_AUTO_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1 millisecond. Get Function: RFmxWLAN_SEMGetSweepTimeInterval Set Function: RFmxWLAN_SEMSetSweepTimeInterval |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_standard.html language=enus -->
## TOPIC 00119: RFMXWLAN_ATTR_STANDARD

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_standard.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_standard.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_STANDARD

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies the signal under analysis as defined in IEEE RFMXWLAN_ATTR_STANDARD 802.11. On a MIMO session, the supported standards are 802.11n, 802.11ac, 802.11ax, and 802.11be.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWLAN_VAL_STANDARD_802_11_AG.11a/g. Get Function: RFmxWLAN_GetStandard Set Function: RFmxWLAN_SetStandard |
| Values: | RFMXWLAN_VAL_STANDARD_802_11_AG (0)Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11a-1999 and IEEE Standard 802.11g-2003. RFMXWLAN_VAL_STANDARD_802_11_B (1)Corresponds to the DSSS based PPDU formats as defined in IEEE Standard 802.11b-1999. RFMXWLAN_VAL_STANDARD_802_11_J (2)Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11j-2004. RFMXWLAN_VAL_STANDARD_802_11_P (3)Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11p-2010. RFMXWLAN_VAL_STANDARD_802_11_N (4)Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11n-2009. RFMXWLAN_VAL_STANDARD_802_11_AC (5)Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11ac-2013. RFMXWLAN_VAL_STANDARD_802_11_AX (6)Corresponds to the OFDM based PPDU formats as defined in IEEE Standard P802.11ax/D8.0. RFMXWLAN_VAL_STANDARD_802_11_BE (7)Corresponds to the OFDM based PPDU formats as defined in IEEE Standard P802.11be/D7.0. |
| RFMXWLAN_VAL_STANDARD_802_11_AG (0) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11a-1999 and IEEE Standard 802.11g-2003. |
| RFMXWLAN_VAL_STANDARD_802_11_B (1) | Corresponds to the DSSS based PPDU formats as defined in IEEE Standard 802.11b-1999. |
| RFMXWLAN_VAL_STANDARD_802_11_J (2) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11j-2004. |
| RFMXWLAN_VAL_STANDARD_802_11_P (3) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11p-2010. |
| RFMXWLAN_VAL_STANDARD_802_11_N (4) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11n-2009. |
| RFMXWLAN_VAL_STANDARD_802_11_AC (5) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11ac-2013. |
| RFMXWLAN_VAL_STANDARD_802_11_AX (6) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard P802.11ax/D8.0. |
| RFMXWLAN_VAL_STANDARD_802_11_BE (7) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard P802.11be/D7.0. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_trigger_delay.html language=enus -->
## TOPIC 00120: RFMXWLAN_ATTR_TRIGGER_DELAY

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_trigger_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_trigger_delay.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_TRIGGER_DELAY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeF64RFmxWLAN_GetAttributeF64 |
| Description: | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre-trigger samples. If the delay is positive, the measurement acquires post-trigger samples.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFmxWLAN measurement dependent. Get Function: RFmxWLAN_GetTriggerDelay Set Function: RFmxWLAN_SetTriggerDelay |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_trigger_gate_enabled.html language=enus -->
## TOPIC 00121: RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_trigger_gate_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_trigger_gate_enabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Enables time-domain gating of the acquired signal for SEM measurement. If you set this attribute to True and the required measurement interval exceeds the value you set for the RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH attribute, then the measurement restricts the acquisition duration of each record to RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH attribute and acquires as many additional records as necessary for the required measurement interval. If you want to ignore the idle duration between multiple PPDUs during an SEM measurement, you must set RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED to True and set RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH to a value less than or equal to the length of the PPDU under analysis. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWLAN_VAL_TRIGGER_GATE_ENABLED_FALSE. Get Function: RFmxWLAN_GetTriggerGateEnabled Set Function: RFmxWLAN_SetTriggerGateEnabled |
| Values: | RFMXWLAN_VAL_TRIGGER_GATE_ENABLED_FALSE (0)Gate for SEM measurements is disabled. RFMXWLAN_VAL_TRIGGER_GATE_ENABLED_TRUE (1)Gate for SEM measurements is enabled. |
| RFMXWLAN_VAL_TRIGGER_GATE_ENABLED_FALSE (0) | Gate for SEM measurements is disabled. |
| RFMXWLAN_VAL_TRIGGER_GATE_ENABLED_TRUE (1) | Gate for SEM measurements is enabled. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_trigger_gate_length.html language=enus -->
## TOPIC 00122: RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_trigger_gate_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_trigger_gate_length.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeF64RFmxWLAN_GetAttributeF64 |
| Description: | Specifies the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED attribute to RFMXWLAN_VAL_TRIGGER_GATE_ENABLED_TRUE. If the measurement interval required to perform the measurement exceeds the gate length, the measurement acquires as many additional records as necessary to honor the required measurement interval. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1 millisecond. Get Function: RFmxWLAN_GetTriggerGateLength Set Function: RFmxWLAN_SetTriggerGateLength |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_txp_averaging_count.html language=enus -->
## TOPIC 00123: RFMXWLAN_ATTR_TXP_AVERAGING_COUNT

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_txp_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_txp_averaging_count.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_TXP_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXWLAN_ATTR_TXP_AVERAGING_ENABLED attribute to RFMXWLAN_VAL_TXP_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxWLAN_TXPGetAveragingCount Set Function: RFmxWLAN_TXPSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_txp_averaging_enabled.html language=enus -->
## TOPIC 00124: RFMXWLAN_ATTR_TXP_AVERAGING_ENABLED

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_txp_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_txp_averaging_enabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_TXP_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the TXP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWLAN_VAL_TXP_AVERAGING_ENABLED_FALSE. Get Function: RFmxWLAN_TXPGetAveragingEnabled Set Function: RFmxWLAN_TXPSetAveragingEnabled |
| Values: | RFMXWLAN_VAL_TXP_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXWLAN_VAL_TXP_AVERAGING_ENABLED_TRUE (1)The TXP measurement uses the RFMXWLAN_ATTR_TXP_AVERAGING_COUNT attribute as the number of acquisitions over which the TXP measurement is averaged. |
| RFMXWLAN_VAL_TXP_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXWLAN_VAL_TXP_AVERAGING_ENABLED_TRUE (1) | The TXP measurement uses the RFMXWLAN_ATTR_TXP_AVERAGING_COUNT attribute as the number of acquisitions over which the TXP measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_txp_burst_detection_enabled.html language=enus -->
## TOPIC 00125: RFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLED

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_txp_burst_detection_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_txp_burst_detection_enabled.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeI32RFmxWLAN_GetAttributeI32 |
| Description: | Specifies whether the measurement detects the start and the end of a WLAN packet automatically. When you set this attribute to True, the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for the RFMXWLAN_ATTR_TXP_MAXIMUM_MEASUREMENT_INTERVAL attribute.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXWLAN_VAL_TXP_BURST_DETECTION_ENABLED_TRUE. Get Function: RFmxWLAN_TXPGetBurstDetectionEnabled Set Function: RFmxWLAN_TXPSetBurstDetectionEnabled |
| Values: | RFMXWLAN_VAL_TXP_BURST_DETECTION_ENABLED_FALSE (0)Disables burst detection. RFMXWLAN_VAL_TXP_BURST_DETECTION_ENABLED_TRUE (1)Enables burst detection. |
| RFMXWLAN_VAL_TXP_BURST_DETECTION_ENABLED_FALSE (0) | Disables burst detection. |
| RFMXWLAN_VAL_TXP_BURST_DETECTION_ENABLED_TRUE (1) | Enables burst detection. |

<!--NI_TOPIC bundle=rfmx-wlan-cvi path=rfmxwlan_attr_txp_maximum_measurement_interval.html language=enus -->
## TOPIC 00126: RFMXWLAN_ATTR_TXP_MAXIMUM_MEASUREMENT_INTERVAL

- bundle_id: `rfmx-wlan-cvi`
- source_path: `rfmxwlan_attr_txp_maximum_measurement_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-cvi/raw/resource/enus/rfmxwlan_attr_txp_maximum_measurement_interval.html
- document_id: `rfmx-wlan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXWLAN_ATTR_TXP_MAXIMUM_MEASUREMENT_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxWLAN_SetAttributeF64RFmxWLAN_GetAttributeF64 |
| Description: | Specifies the maximum measurement interval. This value is expressed in seconds. When you set the RFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLED attribute to RFMXWLAN_VAL_TXP_BURST_DETECTION_ENABLED_TRUE, the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for this attribute. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1 millisecond. Get Function: RFmxWLAN_TXPGetMaximumMeasurementInterval Set Function: RFmxWLAN_TXPSetMaximumMeasurementInterval |
