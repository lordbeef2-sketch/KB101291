# NI DOCUMENT BUNDLE: rfmx-bt-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-bt-cvi start=1 end=120 -->
<!--NI_TOPIC bundle=rfmx-bt-cvi path=bp_help_file_title.html language=enus -->
## TOPIC 00001: RFmx for Bluetooth® Test C Reference

- bundle_id: `rfmx-bt-cvi`
- source_path: `bp_help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/bp_help_file_title.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmx for Bluetooth® Test C Reference

This help file contains information about the RFmx for Bluetooth® Test functions, attributes, and values that you can use when programming your application.

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_20dbbandwidthcfgaveraging.html language=enus -->
## TOPIC 00002: RFmxBT_20dBBandwidthCfgAveraging

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_20dbbandwidthcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_20dbbandwidthcfgaveraging.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_20dBBandwidthCfgAveraging

int32 __stdcall RFmxBT_20dBBandwidthCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount);

#### Purpose

Configures averaging for the 20dBBandwidth measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for 20dBBandwidth measurement. RFMXBT_VAL_20DB_BANDWIDTH_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXBT_VAL_20DB_BANDWIDTH_AVERAGING_ENABLED_TRUE (1) The measurement uses the averagingCount parameter as the number of acquisitions over which the 20dBBandwidth measurement is averaged. |
| RFMXBT_VAL_20DB_BANDWIDTH_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXBT_VAL_20DB_BANDWIDTH_AVERAGING_ENABLED_TRUE (1) | The measurement uses the averagingCount parameter as the number of acquisitions over which the 20dBBandwidth measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXBT_VAL_20DB_BANDWIDTH_AVERAGING_ENABLED_TRUE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_20dbbandwidthfetchmeasurement.html language=enus -->
## TOPIC 00003: RFmxBT_20dBBandwidthFetchMeasurement

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_20dbbandwidthfetchmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_20dbbandwidthfetchmeasurement.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_20dBBandwidthFetchMeasurement

int32 __stdcall RFmxBT_20dBBandwidthFetchMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* peakPower,
 float64* bandwidth,
 float64* highFrequency,
 float64* lowFrequency);

#### Purpose

Fetches the 20dBBandwidth measurement results.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| peakPower | float64* | Returns the peak power of the measured spectrum. This value is expressed in dBm. |
| bandwidth | float64* | Returns the 20dB bandwidth of the received signal. It is computed as the difference between highFrequency and lowFrequency parameters. This value is expressed in Hz. |
| highFrequency | float64* | Returns the highest frequency above the center frequency at which transmit power drops 20 dB below the peak power. This value is expressed in Hz. |
| lowFrequency | float64* | Returns the lowest frequency below the center frequency at which transmit power drops 20 dB below the peak power. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_20dbbandwidthfetchspectrum.html language=enus -->
## TOPIC 00004: RFmxBT_20dBBandwidthFetchSpectrum

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_20dbbandwidthfetchspectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_20dbbandwidthfetchspectrum.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_20dBBandwidthFetchSpectrum

int32 __stdcall RFmxBT_20dBBandwidthFetchSpectrum (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 spectrum[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the 20dBBandwidth spectrum trace.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency. This value is expressed in Hz. |
| dx | float64* | Returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | float32[] | Returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_acpcfgburstsynchronizationtype.html language=enus -->
## TOPIC 00005: RFmxBT_ACPCfgBurstSynchronizationType

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_acpcfgburstsynchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_acpcfgburstsynchronizationtype.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ACPCfgBurstSynchronizationType

int32 __stdcall RFmxBT_ACPCfgBurstSynchronizationType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 burstSynchronizationType);

#### Purpose

Configures the type of synchronization used for detecting the start of the packet in the adjacent channel power (ACP) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| burstSynchronizationType | int32 | Specifies the type of synchronization used for detecting the start of packet in the measurement. RFMXBT_VAL_ACP_BURST_SYNCHRONIZATION_TYPE_NONE (0) Specifies that the measurement does not perform synchronization to detect the start of the packet.RFMXBT_VAL_ACP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE (1) Specifies that the measurement uses the preamble field to detect the start of the packet.RFMXBT_VAL_ACP_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD (2) Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the RFMXBT_ATTR_BD_ADDRESS_LAP attribute. |
| RFMXBT_VAL_ACP_BURST_SYNCHRONIZATION_TYPE_NONE (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |  |
| RFMXBT_VAL_ACP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE (1) | Specifies that the measurement uses the preamble field to detect the start of the packet. |  |
| RFMXBT_VAL_ACP_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD (2) | Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the RFMXBT_ATTR_BD_ADDRESS_LAP attribute. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_acpcfgnumberofoffsets.html language=enus -->
## TOPIC 00006: RFmxBT_ACPCfgNumberOfOffsets

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_acpcfgnumberofoffsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_acpcfgnumberofoffsets.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ACPCfgNumberOfOffsets

int32 __stdcall RFmxBT_ACPCfgNumberOfOffsets (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 numberOfOffsets);

#### Purpose

Configures the number of offsets for the adjacent channel power (ACP) measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| numberOfOffsets | int32 | Specifies the number of offset channels used on either side of the reference channel for the ACP measurement when you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC. This parameter returns the actual number of offsets used in the ACP measurement when you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_acpfetchmasktrace.html language=enus -->
## TOPIC 00007: RFmxBT_ACPFetchMaskTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_acpfetchmasktrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_acpfetchmasktrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ACPFetchMaskTrace

int32 __stdcall RFmxBT_ACPFetchMaskTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 limitWithExceptionMask[],
 float32 limitWithoutExceptionMask[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the limit with exception mask and limit without exception mask traces for ACP measurement. This function returns a valid trace only if you set the [RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE](/csh?topicname=rfmxbtcvi/rfmxbt_attr_acp_offset_channel_mode.html) attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency, which is the center frequency of the lowest offset. This value is expressed in Hz. |
| dx | float64* | Returns the frequency bin spacing. This value is expressed in Hz. |
| limitWithExceptionMask | float32[] | Returns the limit with exception mask used for the measurement. This value is expressed in dBm. |
| limitWithoutExceptionMask | float32[] | Returns the limit without exception mask used for the measurement. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_acpfetchmeasurementstatus.html language=enus -->
## TOPIC 00008: RFmxBT_ACPFetchMeasurementStatus

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_acpfetchmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_acpfetchmeasurementstatus.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ACPFetchMeasurementStatus

int32 __stdcall RFmxBT_ACPFetchMeasurementStatus (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int32* measurementStatus);

#### Purpose

Fetches the overall ACP measurement status based on the measurement limits as defined by the standard if you set the [RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE](/csh?topicname=rfmxbtcvi/rfmxbt_attr_acp_offset_channel_mode.html) attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND. This function is not valid if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| measurementStatus | int32* | Returns the overall measurement status based on the measurement limits specified by the standard when you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND. Refer to RFMXBT_ATTR_ACP_RESULTS_MEASUREMENT_STATUS attribute for more information about measurement status. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_acpfetchoffsetmeasurement.html language=enus -->
## TOPIC 00009: RFmxBT_ACPFetchOffsetMeasurement

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_acpfetchoffsetmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_acpfetchoffsetmeasurement.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ACPFetchOffsetMeasurement

int32 __stdcall RFmxBT_ACPFetchOffsetMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* lowerAbsolutePower,
 float64* upperAbsolutePower,
 float64* lowerRelativePower,
 float64* upperRelativePower,
 float64* lowerMargin,
 float64* upperMargin);

#### Purpose

Fetches the absolute powers, relative powers and margins measured in the offset channel. 
Use "offset<*k*>" as the selector string to read results from this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name, offset number, and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"offset0""signal::sig1/offset0""signal::sig1/result::r1/offset0""result::r1/offset0"You can use the RFmxBT_BuildOffsetString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| lowerAbsolutePower | float64* | Returns the absolute power measured in the lower offset channel. This value is expressed in dBm. |
| upperAbsolutePower | float64* | Returns the absolute power measured in the upper offset channel. This value is expressed in dBm. |
| lowerRelativePower | float64* | Returns the relative power in the lower offset channel measured with respect to the reference channel power. This value is expressed in dB. |
| upperRelativePower | float64* | Returns the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB. |
| lowerMargin | float64* | Returns the margin from the limit specified by the mask with exception for lower offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This parameter is valid only if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND. This parameter returns NaN if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC. |
| upperMargin | float64* | Returns the margin from the limit specified by the mask with exception for upper offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This parameter is valid only if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND. This parameter returns NaN if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_acpfetchoffsetmeasurementarray.html language=enus -->
## TOPIC 00010: RFmxBT_ACPFetchOffsetMeasurementArray

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_acpfetchoffsetmeasurementarray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_acpfetchoffsetmeasurementarray.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ACPFetchOffsetMeasurementArray

int32 __stdcall RFmxBT_ACPFetchOffsetMeasurementArray (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64 lowerAbsolutePower[],
 float64 upperAbsolutePower[],
 float64 lowerRelativePower[],
 float64 upperRelativePower[],
 float64 lowerMargin[],
 float64 upperMargin[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the array of absolute powers, relative powers and margins measured in the offset channels.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| lowerAbsolutePower | float64[] | Returns the array of absolute power measured in the lower offset channel. This value is expressed in dBm. |
| upperAbsolutePower | float64[] | Returns the array of absolute power measured in the upper offset channel. This value is expressed in dBm. |
| lowerRelativePower | float64[] | Returns the array of relative power in the lower offset channel measured with respect to the reference channel power. This value is expressed in dB. |
| upperRelativePower | float64[] | Returns array of the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB. |
| lowerMargin | float64[] | Returns the array of margin from the limit specified by the mask with Exception for lower offset channel. This value is expressed in dB. Margin is defined as the difference between the Offset Absolute Power and Mask with Exception. This parameter is valid only if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND. This parameter returns NaN if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC. |
| upperMargin | float64[] | Returns the array of the margin from the limit specified by the mask with Exception for upper offset channel. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This parameter is valid only if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND. This parameter returns NaN if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_acpfetchreferencechannelpower.html language=enus -->
## TOPIC 00011: RFmxBT_ACPFetchReferenceChannelPower

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_acpfetchreferencechannelpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_acpfetchreferencechannelpower.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ACPFetchReferenceChannelPower

int32 __stdcall RFmxBT_ACPFetchReferenceChannelPower (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* referenceChannelPower);

#### Purpose

Returns the measured power of the reference channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| referenceChannelPower | float64* | Returns the measured power of the reference channel. This value is expressed in dBm. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_analyzeiq1waveformsplit.html language=enus -->
## TOPIC 00012: RFmxBT_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_analyzeiq1waveformsplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_analyzeiq1waveformsplit.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_AnalyzeIQ1WaveformSplit

int32 __stdcall RFmxBT_AnalyzeIQ1WaveformSplit (niRFmxInstrHandle instrumentHandle,
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

Performs the enabled measurements on the I/Q complex waveform that you specify in I and Q parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes. Use this function only if the Recommended Acquisition Type attribute value is either IQ or IQorSpectral. 

 When using the Analysis-Only mode in RFmxBT, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | >Specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| x0 | float64 | Specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | float64 | Specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| I | float32[] | Specifies an array of the real part of complex-valued time domain data. This array corresponds to the in-phase (I) data. |
| Q | float32[] | Specifies an array of the imaginary part of complex-valued time domain data. This array corresponds to the quadrature-phase (Q) data. |
| arraySize | int32 | Specifies the size of the array. |
| reset | int32 | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_autodetectsignal.html language=enus -->
## TOPIC 00013: RFmxBT_AutoDetectSignal

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_autodetectsignal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_autodetectsignal.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_AutoDetectSignal

int32 __stdcall RFmxBT_AutoDetectSignal (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout);

#### Purpose

Detects the Bluetooth packet and returns the detected packet type, data rate, and payload length.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_buildslotstring.html language=enus -->
## TOPIC 00014: RFmxBT_BuildSlotString

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_buildslotstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_buildslotstring.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_BuildSlotString

int32 __stdcall RFmxBT_BuildSlotString (char selectorString[],
 int32 slotNumber,
 int32 selectorStringOutLength,
 char selectorStringOut[]);

#### Purpose

Creates a slot string for use with the TXP configuration or fetch attributes and functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| slotNumber | int32 | Specifies the slot number for building the selector string. |
| selectorStringOutLength | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| Output |  |  |
| Name | Type | Description |
| selectorStringOut | char[] | Returns the selector string created by this function. You can pass NULL for this parameter if selectorStringLength is set to 0, which will return the minimum buffer size required to create the signal string. If the selectorString buffer is not large enough to build the signal string, the function returns an error. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_cfgchannelnumber.html language=enus -->
## TOPIC 00015: RFmxBT_CfgChannelNumber

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_cfgchannelnumber.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_cfgchannelnumber.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_CfgChannelNumber

int32 __stdcall RFmxBT_CfgChannelNumber (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 channelNumber);

#### Purpose

Configures the RF channel number of the signal generated by the device under test (DUT), as defined in the Bluetooth specification.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| channelNumber | int32 | Specifies the RF channel number of the signal generated by the device under test (DUT), as defined in the Bluetooth specification. This parameter is applicable when you enable the ACP measurement and when you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_cfgiqpoweredgetrigger.html language=enus -->
## TOPIC 00016: RFmxBT_CfgIQPowerEdgeTrigger

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_cfgiqpoweredgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_cfgiqpoweredgetrigger.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_CfgIQPowerEdgeTrigger

int32 __stdcall RFmxBT_CfgIQPowerEdgeTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char IQPowerEdgeSource[],
 int32 IQPowerEdgeSlope,
 float64 IQPowerEdgeLevel,
 float64 triggerDelay,
 int32 triggerMinQuietTimeMode,
 float64 triggerMinQuietTimeDuration,
 int32 IQPowerEdgeLevelType,
 int32 enableTrigger);

#### Purpose

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. 
To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| IQPowerEdgeSource | char[] | Specifies the channel from which the device monitors the trigger. The default of this attribute is hardware dependent. |
| IQPowerEdgeSlope | int32 | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. RFMXBT_VAL_IQ_POWER_EDGE_RISING_SLOPE (0) The trigger asserts when the signal power is rising.RFMXBT_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1) The trigger asserts when the signal power is falling. |
| RFMXBT_VAL_IQ_POWER_EDGE_RISING_SLOPE (0) | The trigger asserts when the signal power is rising. |  |
| RFMXBT_VAL_IQ_POWER_EDGE_FALLING_SLOPE (1) | The trigger asserts when the signal power is falling. |  |
| IQPowerEdgeLevel | float64 | Specifies the power level at which the device triggers. This value is expressed in dB when you set the IQPowerEdgeLevelType parameter to RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE; and is expressed in dBm when you set the IQPowerEdgeLevelType parameter to RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this attribute is hardware dependent. |
| triggerDelay | float64 | Specifies the trigger delay time, in seconds. |
| triggerMinQuietTimeMode | int32 | Specifies whether the measurement computes the minimum quiet time used for triggering. RFMXBT_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL (0) The minimum quiet time used for triggering is the value of the triggerMinQuietTimeDuration parameter. RFMXBT_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO (1) The measurement computes the minimum quiet time used for triggering. |
| RFMXBT_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL (0) | The minimum quiet time used for triggering is the value of the triggerMinQuietTimeDuration parameter. |  |
| RFMXBT_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO (1) | The measurement computes the minimum quiet time used for triggering. |  |
| triggerMinQuietTimeDuration | float64 | Specifies the duration, in seconds, for which the signal must be quiet before the signal analyzer arms the I/Q Power Edge trigger. If you set the IQPowerEdgeSlope parameter to RFMXBT_VAL_IQ_POWER_EDGE_RISING_SLOPE, the signal is quiet when it is below the trigger level. If you set the IQPowerEdgeSlope parameter to RFMXBT_VAL_IQ_POWER_EDGE_FALLING_SLOPE, the signal is quiet when it is above the trigger level. |
| IQPowerEdgeLevelType | int32 | Specifies the reference for the IQPowerEdgeLevel parameter. RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0) The IQPowerEdgeLevel parameter is relative to the value of the RFMXBT_ATTR_REFERENCE_LEVEL attribute.RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1) The IQPowerEdgeLevel parameter specifies the absolute power. |
| RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0) | The IQPowerEdgeLevel parameter is relative to the value of the RFMXBT_ATTR_REFERENCE_LEVEL attribute. |  |
| RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1) | The IQPowerEdgeLevel parameter specifies the absolute power. |  |
| enableTrigger | int32 | Specifies whether to enable the trigger. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_cfgledirectionfinding.html language=enus -->
## TOPIC 00017: RFmxBT_CfgLEDirectionFinding

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_cfgledirectionfinding.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_cfgledirectionfinding.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_CfgLEDirectionFinding

int32 __stdcall RFmxBT_CfgLEDirectionFinding (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 directionFindingMode,
 float64 CTELength,
 float64 CTESlotDuration);

#### Purpose

Configures the mode of direction finding, length of the constant tone extension field, and the duration of the switching slot in the generated signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| directionFindingMode | int32 | Specifies the mode of direction finding. The default value is RFMXBT_VAL_DIRECTION_FINDING_MODE_DISABLED. RFMXBT_VAL_DIRECTION_FINDING_MODE_DISABLED (0) Specifies that the LE packet does not have fields required for direction finding. RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) Specifies the LE packets uses the angle of arrival method of direction finding. RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) Specifies the LE packet uses angle of departure method of direction finding. |
| RFMXBT_VAL_DIRECTION_FINDING_MODE_DISABLED (0) | Specifies that the LE packet does not have fields required for direction finding. |  |
| RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |  |
| RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) | Specifies the LE packet uses angle of departure method of direction finding. |  |
| CTELength | float64 | Specifies the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the Direction Finding Mode parameter to either RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. The default value is 160 microseconds. |
| CTESlotDuration | float64 | Specifies the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_cfgpayloadlength.html language=enus -->
## TOPIC 00018: RFmxBT_CfgPayloadLength

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_cfgpayloadlength.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_cfgpayloadlength.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_CfgPayloadLength

int32 __stdcall RFmxBT_CfgPayloadLength (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 payloadLengthMode,
 int32 payloadLength);

#### Purpose

Configures the **payloadLengthMode** and RFMXBT_VAL_PAYLOAD_LENGTH_MODE_AUTO parameters that decide the length of the payload to be used for the measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| payloadLengthMode | int32 | Specifies the payload length mode of the signal to be measured. The payloadLengthMode and RFMXBT_VAL_PAYLOAD_LENGTH_MODE_AUTO parameters decide the length of the payload to be used for measurement. RFMXBT_VAL_PAYLOAD_LENGTH_MODE_MANUAL (0) Enables the value specified by the payloadLength parameter. The acquisition and measurement durations will be decided based on this value.RFMXBT_VAL_PAYLOAD_LENGTH_MODE_AUTO (1) Enables the standard defined maximum payload length for the selected packet type. If this parameter is set to Auto, the maximum standard defined payload length for the selected packet type is chosen. For LE, the maximum payload length that a device under test(DUT) can generate varies from 37 to 255 bytes. When you set the payload length mode for the LE packet type to auto, RFmx chooses 37 bytes as the payload length. |
| RFMXBT_VAL_PAYLOAD_LENGTH_MODE_MANUAL (0) | Enables the value specified by the payloadLength parameter. The acquisition and measurement durations will be decided based on this value. |  |
| RFMXBT_VAL_PAYLOAD_LENGTH_MODE_AUTO (1) | Enables the standard defined maximum payload length for the selected packet type. If this parameter is set to Auto, the maximum standard defined payload length for the selected packet type is chosen. For LE, the maximum payload length that a device under test(DUT) can generate varies from 37 to 255 bytes. When you set the payload length mode for the LE packet type to auto, RFmx chooses 37 bytes as the payload length. |  |
| payloadLength | int32 | Specifies the payload length of the signal in bytes. The parameter is applicable only when you set the payloadLengthMode parameter to RFMXBT_VAL_PAYLOAD_LENGTH_MODE_MANUAL. This parameter returns the payload length used for measurement if you set the Payload Length Mode parameter to RFMXBT_VAL_PAYLOAD_LENGTH_MODE_AUTO. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_cfgsoftwareedgetrigger.html language=enus -->
## TOPIC 00019: RFmxBT_CfgSoftwareEdgeTrigger

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_cfgsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_cfgsoftwareedgetrigger.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_CfgSoftwareEdgeTrigger

int32 __stdcall RFmxBT_CfgSoftwareEdgeTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 triggerDelay,
 int32 enableTrigger);

#### Purpose

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| triggerDelay | float64 | Specifies the trigger delay time, in seconds. |
| enableTrigger | int32 | Specifies whether to enable the trigger. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_checkmeasurementstatus.html language=enus -->
## TOPIC 00020: RFmxBT_CheckMeasurementStatus

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_checkmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_checkmeasurementstatus.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_CheckMeasurementStatus

int32 __stdcall RFmxBT_CheckMeasurementStatus (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32* isDone);

#### Purpose

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| Output |  |  |
| Name | Type | Description |
| isDone | int32* | Indicates whether the measurement is complete. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_clearallnamedresults.html language=enus -->
## TOPIC 00021: RFmxBT_ClearAllNamedResults

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_clearallnamedresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_clearallnamedresults.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ClearAllNamedResults

int32 __stdcall RFmxBT_ClearAllNamedResults (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears all results for the signal that you specify in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_clearnamedresult.html language=enus -->
## TOPIC 00022: RFmxBT_ClearNamedResult

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_clearnamedresult.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_clearnamedresult.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ClearNamedResult

int32 __stdcall RFmxBT_ClearNamedResult (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Clears a result instance specified by the result name in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_clonesignalconfiguration.html language=enus -->
## TOPIC 00023: RFmxBT_CloneSignalConfiguration

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_clonesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_clonesignalconfiguration.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_CloneSignalConfiguration

int32 __stdcall RFmxBT_CloneSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char oldSignalName[],
 char newSignalName[]);

#### Purpose

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| oldSignalName | char[] | Specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::OldSigName""OldSigName" |
| newSignalName | char[] | Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_close.html language=enus -->
## TOPIC 00024: RFmxBT_Close

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_close.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_close.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_Close

int32 __stdcall RFmxBT_Close (niRFmxInstrHandle instrumentHandle, int32 forceDestroy);

#### Purpose

Closes the RFmx session.

This function is a wrapper over the NI-RFmx Instruments API, and calls the [RFmxInstr_Close](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_close.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| forceDestroy | int32 | Specifies whether to destroy the NI-RFmx session. RFMXBT_VAL_FALSE (0) Destroys the NI-RFmx session. Call the RFmxBT_Close function a number of times equal to the number of times you obtained a reference to the NI-RFmx session. RFMXBT_VAL_TRUE (1) Destroys the NI-RFmx session. You do not have to call the RFmxBT_Close function multiple times. Destroying the NI-RFmx session invalidates all references to the session. |
| RFMXBT_VAL_FALSE (0) | Destroys the NI-RFmx session. Call the RFmxBT_Close function a number of times equal to the number of times you obtained a reference to the NI-RFmx session. |  |
| RFMXBT_VAL_TRUE (1) | Destroys the NI-RFmx session. You do not have to call the RFmxBT_Close function multiple times. Destroying the NI-RFmx session invalidates all references to the session. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_commit.html language=enus -->
## TOPIC 00025: RFmxBT_Commit

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_commit.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_Commit

int32 __stdcall RFmxBT_Commit (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Commits settings to the hardware. Calling this function is optional. RFmxBT commits settings to the hardware when you call the [RFmxBT_Initiate](/csh?topicname=rfmxbtcvi/cvirfmxbt_initiate.html) function or any of the measurement Read functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_createsignalconfiguration.html language=enus -->
## TOPIC 00026: RFmxBT_CreateSignalConfiguration

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_createsignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_createsignalconfiguration.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_CreateSignalConfiguration

int32 __stdcall RFmxBT_CreateSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char signalName[]);

#### Purpose

Creates a new instance of a signal.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| signalName | char[] | Specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::s1""sig1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_deletesignalconfiguration.html language=enus -->
## TOPIC 00027: RFmxBT_DeleteSignalConfiguration

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_deletesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_deletesignalconfiguration.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_DeleteSignalConfiguration

int32 __stdcall RFmxBT_DeleteSignalConfiguration (niRFmxInstrHandle instrumentHandle,
 char signalName[]);

#### Purpose

Deletes an instance of a signal that you specify in the **signalName** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| signalName | char[] | Specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::s1""sig1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_disabletrigger.html language=enus -->
## TOPIC 00028: RFmxBT_DisableTrigger

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_disabletrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_disabletrigger.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_DisableTrigger

int32 __stdcall RFmxBT_DisableTrigger (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_frequencyrangecfgaveraging.html language=enus -->
## TOPIC 00029: RFmxBT_FrequencyRangeCfgAveraging

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_frequencyrangecfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_frequencyrangecfgaveraging.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_FrequencyRangeCfgAveraging

int32 __stdcall RFmxBT_FrequencyRangeCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount);

#### Purpose

Configures averaging for the FrequencyRange measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the FrequencyRange measurement. RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_TRUE (1) The measurement uses the averagingCount parameter as the number of acquisitions over which the FrequencyRange measurement is averaged. |
| RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_TRUE (1) | The measurement uses the averagingCount parameter as the number of acquisitions over which the FrequencyRange measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_TRUE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_frequencyrangecfgspan.html language=enus -->
## TOPIC 00030: RFmxBT_FrequencyRangeCfgSpan

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_frequencyrangecfgspan.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_frequencyrangecfgspan.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_FrequencyRangeCfgSpan

int32 __stdcall RFmxBT_FrequencyRangeCfgSpan (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 span);

#### Purpose

Configures the span for the FrequencyRange measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| span | float64 | Specifies the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_frequencyrangefetchmeasurement.html language=enus -->
## TOPIC 00031: RFmxBT_FrequencyRangeFetchMeasurement

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_frequencyrangefetchmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_frequencyrangefetchmeasurement.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_FrequencyRangeFetchMeasurement

int32 __stdcall RFmxBT_FrequencyRangeFetchMeasurement (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* highFrequency,
 float64* lowFrequency);

#### Purpose

Fetches the FrequencyRange measurement results.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| highFrequency | float64* | Returns the highest frequency above the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
| lowFrequency | float64* | Returns the lowest frequency below the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_frequencyrangefetchspectrum.html language=enus -->
## TOPIC 00032: RFmxBT_FrequencyRangeFetchSpectrum

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_frequencyrangefetchspectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_frequencyrangefetchspectrum.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_FrequencyRangeFetchSpectrum

int32 __stdcall RFmxBT_FrequencyRangeFetchSpectrum (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 spectrum[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the FrequencyRange spectrum trace.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start frequency. This value is expressed in Hz. |
| dx | float64* | Returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | float32[] | Returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getallnamedresultnames.html language=enus -->
## TOPIC 00033: RFmxBT_GetAllNamedResultNames

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getallnamedresultnames.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getallnamedresultnames.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAllNamedResultNames

int32 __stdcall RFmxBT_GetAllNamedResultNames (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultNames[],
 int32 resultNamesBufferSize,
 int32* actualResultNamesSize,
 int32* defaultResultExists);

#### Purpose

Returns all the named result names of the signal that you specify in the **selectorString** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| resultNamesBufferSize | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| Output |  |  |
| Name | Type | Description |
| resultNames | char[] | Returns an array of result names. |
| actualResultNamesSize | int32* | Returns the actual size of the resultNames array if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | int32* | Indicates whether the default result exists. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributef32.html language=enus -->
## TOPIC 00034: RFmxBT_GetAttributeF32

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributef32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributef32.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeF32

int32 __stdcall RFmxBT_GetAttributeF32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 float32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributef32array.html language=enus -->
## TOPIC 00035: RFmxBT_GetAttributeF32Array

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributef32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributef32array.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeF32Array

int32 __stdcall RFmxBT_GetAttributeF32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributef64.html language=enus -->
## TOPIC 00036: RFmxBT_GetAttributeF64

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributef64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributef64.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeF64

int32 __stdcall RFmxBT_GetAttributeF64 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 *attrVal);

#### Purpose

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | float64* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributef64array.html language=enus -->
## TOPIC 00037: RFmxBT_GetAttributeF64Array

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributef64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributef64array.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeF64Array

int32 __stdcall RFmxBT_GetAttributeF64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributei16.html language=enus -->
## TOPIC 00038: RFmxBT_GetAttributeI16

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributei16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributei16.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeI16

int32 __stdcall RFmxBT_GetAttributeI16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int16 *attrVal);

#### Purpose

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int16* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributei32.html language=enus -->
## TOPIC 00039: RFmxBT_GetAttributeI32

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributei32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributei32.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeI32

int32 __stdcall RFmxBT_GetAttributeI32 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributei32array.html language=enus -->
## TOPIC 00040: RFmxBT_GetAttributeI32Array

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributei32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributei32array.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeI32Array

int32 __stdcall RFmxBT_GetAttributeI32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributei64.html language=enus -->
## TOPIC 00041: RFmxBT_GetAttributeI64

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributei64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributei64.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeI64

int32 __stdcall RFmxBT_GetAttributeI64 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int64 *attrVal);

#### Purpose

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int64* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributei64array.html language=enus -->
## TOPIC 00042: RFmxBT_GetAttributeI64Array

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributei64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributei64array.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeI64Array

int32 __stdcall RFmxBT_GetAttributeI64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributei8.html language=enus -->
## TOPIC 00043: RFmxBT_GetAttributeI8

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributei8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributei8.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeI8

int32 __stdcall RFmxBT_GetAttributeI8 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 int8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | int8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributei8array.html language=enus -->
## TOPIC 00044: RFmxBT_GetAttributeI8Array

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributei8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributei8array.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeI8Array

int32 __stdcall RFmxBT_GetAttributeI8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributenicomplexdoublearray.html language=enus -->
## TOPIC 00045: RFmxBT_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributenicomplexdoublearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributenicomplexdoublearray.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeNIComplexDoubleArray

int32 __stdcall RFmxBT_GetAttributeNIComplexDoubleArray (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributenicomplexsinglearray.html language=enus -->
## TOPIC 00046: RFmxBT_GetAttributeNIComplexSingleArray

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributenicomplexsinglearray.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributenicomplexsinglearray.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeNIComplexSingleArray

int32 __stdcall RFmxBT_GetAttributeNIComplexSingleArray (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributestring.html language=enus -->
## TOPIC 00047: RFmxBT_GetAttributeString

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributestring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributestring.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeString

int32 __stdcall RFmxBT_GetAttributeString (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[]);

#### Purpose

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer. 
 

 If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| arraySize | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| Output |  |  |
| Name | Type | Description |
| attrVal | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributeu16.html language=enus -->
## TOPIC 00048: RFmxBT_GetAttributeU16

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributeu16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributeu16.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeU16

int32 __stdcall RFmxBT_GetAttributeU16 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt16 *attrVal);

#### Purpose

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt16* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributeu32.html language=enus -->
## TOPIC 00049: RFmxBT_GetAttributeU32

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributeu32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributeu32.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeU32

int32 __stdcall RFmxBT_GetAttributeU32 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 attributeID,
 uInt32 *attrVal);

#### Purpose

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributeu32array.html language=enus -->
## TOPIC 00050: RFmxBT_GetAttributeU32Array

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributeu32array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributeu32array.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeU32Array

int32 __stdcall RFmxBT_GetAttributeU32Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributeu64array.html language=enus -->
## TOPIC 00051: RFmxBT_GetAttributeU64Array

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributeu64array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributeu64array.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeU64Array

int32 __stdcall RFmxBT_GetAttributeU64Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributeu8.html language=enus -->
## TOPIC 00052: RFmxBT_GetAttributeU8

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributeu8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributeu8.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeU8

int32 __stdcall RFmxBT_GetAttributeU8 (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 *attrVal);

#### Purpose

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeID | int32 | Pass the ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| attrVal | uInt8* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_getattributeu8array.html language=enus -->
## TOPIC 00053: RFmxBT_GetAttributeU8Array

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_getattributeu8array.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_getattributeu8array.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetAttributeU8Array

int32 __stdcall RFmxBT_GetAttributeU8Array (niRFmxInstrHandle instrumentHandle,
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
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
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
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_geterror.html language=enus -->
## TOPIC 00054: RFmxBT_GetError

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_geterror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_geterror.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetError

int32 __stdcall RFmxBT_GetError (niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[]);

#### Purpose

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter. 
 
If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For **Example**, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. 
 

 If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

|  | Note Use the RFmxBT_GetErrorString function if the RFmxBT_GetError function does not return an error message. |
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
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_geterrorstring.html language=enus -->
## TOPIC 00055: RFmxBT_GetErrorString

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_geterrorstring.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_geterrorstring.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_GetErrorString

int32 __stdcall RFmxBT_GetErrorString (niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[]);

#### Purpose

Converts a status code returned by an RFmxBT function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter. 
 

 If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For **Example**, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. 
 

 If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| errorCode | int32* | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescriptionBufferSize | int32 | Passes the number of bytes in the char array you specify in the errorDescription parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize – 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string. The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| statusOrRequiredSize | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. When the statusOrRequiredSize return value returns the buffer size, the status code is not returned. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_initialize.html language=enus -->
## TOPIC 00056: rfmxbt_Initialize

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_initialize.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_Initialize

int32 __stdcall RFmxBT_Initialize (char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession);

#### Purpose

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

This function is a wrapper over the NI-RFmx Instruments API, and calls the [RFmxInstr_Initialize](/csh?topicname=rfmxinstrcvi/cvirfmxinstr_initialize.html) function.

[IMAGE alt='image' src='note.gif'] Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| resourceName | char[] | Specifies the resource name of the device to initialize. The following table shows examples of how to specify the resource name. Example # Device Type Syntax 1 myRFmxDevice NI-RFmx device, device name is "myRFmxDevice" 2 myLogicalName IVI logical name or virtual instrument, name is "myLogicalName" For NI-DAQmx devices, the syntax is the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot2. You can rename an NI-DAQmx device by right-clicking the name in MAX, selecting Rename from the pull-down menu, and entering a new name. You can also pass the name of an IVI logical name configured with the IVI Configuration utility. For additional information about IVI, refer to the IVI section of the Measurement & Automation Explorer Help. |
| Example # | Device Type | Syntax |
| 1 | myRFmxDevice | NI-RFmx device, device name is "myRFmxDevice" |
| 2 | myLogicalName | IVI logical name or virtual instrument, name is "myLogicalName" |
| optionString | char[] | Sets the initial value of certain attributes for the session. The following attributes are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about attributes used in this parameter, refer to the NI RF Vector Signal Analyzers Help. The format of this string is "AttributeName=Value", where AttributeName is the name of the attribute and Value is the value to which the attribute is set. For example, you can simulate an NI 5663E using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple attributes, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx uses yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and NI-RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements. Note To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the NI 5665. |
|  | Note To simulate a device using the NI 5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the NI 5665. |  |
| isNewSession | int32* | Returns RFMXBT_VAL_TRUE if the function created a new session, or RFMXBT_VAL_FALSE if the function returned a reference to an existing session. |
| Output |  |  |
| Name | Type | Description |
| handleOut | niRFmxInstrHandle* | Identifies your instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_initiate.html language=enus -->
## TOPIC 00057: RFmxBT_Initiate

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_initiate.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_Initiate

int32 __stdcall RFmxBT_Initiate (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 char resultName[]);

#### Purpose

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the [RFmxBT_WaitforMeasurementComplete](/csh?topicname=rfmxbtcvi/cvirfmxbt_waitformeasurementcomplete.html) function or [RFmxBT_CheckMeasurementStatus](/csh?topicname=rfmxbtcvi/cvirfmxbt_checkmeasurementstatus.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies the signal name and result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| resultName | char[] | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"""result::r1""r1" |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modacccfgaveraging.html language=enus -->
## TOPIC 00058: RFmxBT_ModAccCfgAveraging

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modacccfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modacccfgaveraging.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccCfgAveraging

int32 __stdcall RFmxBT_ModAccCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount);

#### Purpose

Configures averaging for the ModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| averagingEnabled | int32 | Specifies whether to enable averaging for the ModAcc measurement. RFMXBT_VAL_MODACC_AVERAGING_ENABLED_FALSE (0) The measurement is performed on a single acquisition.RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE (1) The measurement uses the averagingCount parameter as the number of acquisitions over which the ModAcc measurement is averaged. |
| RFMXBT_VAL_MODACC_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |  |
| RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE (1) | The measurement uses the averagingCount parameter as the number of acquisitions over which the ModAcc measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modacccfgburstsynchronizationtype.html language=enus -->
## TOPIC 00059: RFmxBT_ModAccCfgBurstSynchronizationType

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modacccfgburstsynchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modacccfgburstsynchronizationtype.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccCfgBurstSynchronizationType

int32 __stdcall RFmxBT_ModAccCfgBurstSynchronizationType (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 burstSynchronizationType);

#### Purpose

Configures the burst synchronization type for ModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples:"""signal::sig1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| burstSynchronizationType | int32 | Specifies the type of synchronization used for detecting the start of packet in the measurement. RFMXBT_VAL_MODACC_BURST_SYNCHRONIZATION_TYPE_NONE (0) Specifies that the measurement does not perform synchronization to detect the start of the packet.RFMXBT_VAL_MODACC_BURST_SYNCHRONIZATION_TYPE_PREAMBLE (1) Specifies that the measurement uses the preamble field to detect the start of the packet.RFMXBT_VAL_MODACC_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD (2) Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the RFMXBT_ATTR_BD_ADDRESS_LAP attribute. |
| RFMXBT_VAL_MODACC_BURST_SYNCHRONIZATION_TYPE_NONE (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |  |
| RFMXBT_VAL_MODACC_BURST_SYNCHRONIZATION_TYPE_PREAMBLE (1) | Specifies that the measurement uses the preamble field to detect the start of the packet. |  |
| RFMXBT_VAL_MODACC_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD (2) | Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the RFMXBT_ATTR_BD_ADDRESS_LAP attribute. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchconstellationtrace.html language=enus -->
## TOPIC 00060: RFmxBT_ModAccFetchConstellationTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchconstellationtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchconstellationtrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchConstellationTrace

int32 __stdcall RFmxBT_ModAccFetchConstellationTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 NIComplexSingle constellation[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the demodulated symbols from the enhanced data rate (EDR) portion of the EDR packet. This function is valid only for EDR packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| constellation | NIComplexSingle[] | Returns the array of demodulated symbols from over the EDR portion of the EDR packet. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchconstellationtracesplit.html language=enus -->
## TOPIC 00061: RFmxBT_ModAccFetchConstellationTraceSplit

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchconstellationtracesplit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchconstellationtracesplit.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchConstellationTraceSplit

int32 __stdcall RFmxBT_ModAccFetchConstellationTraceSplit (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 I[],
 float32 Q[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Returns the complex chips of the corrected received signal for the ModAcc measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| constellation | NIComplexSingle[] | Returns the real part of the array of demodulated symbols from over the EDR portion of the EDR packet. |
| constellation | NIComplexSingle[] | Returns the imaginary part of the array of demodulated symbols from over the EDR portion of the EDR packet. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchcsdetrendedphasetrace.html language=enus -->
## TOPIC 00062: RFmxBT_ModAccFetchCSDetrendedPhaseTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchcsdetrendedphasetrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchcsdetrendedphasetrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchCSDetrendedPhaseTrace

int32 __stdcall RFmxBT_ModAccFetchCSDetrendedPhaseTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 CSDetrendedPhase[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the zero-mean Detrended Phase (deg) versus time trace. This function is valid only for low energy CS (LE-CS) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time. This value is expressed in seconds. |
| dx | float64* | Returns the sample duration. This value is expressed in seconds. |
| CSDetrendedPhase | float32[] | Returns the zero-mean detrended phase versus time trace. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchcstonetrace.html language=enus -->
## TOPIC 00063: RFmxBT_ModAccFetchCSToneTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchcstonetrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchcstonetrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchCSToneTrace

int32 __stdcall RFmxBT_ModAccFetchCSToneTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 CSToneAmplitude[],
 float32 CSTonePhase[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the CS Tone Amplitude (dBm) versus time and CS Tone Phase (deg) versus time traces. This function is valid only for low energy CS (LE-CS) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time. This value is expressed in seconds. |
| dx | float64* | Returns the sample duration. This value is expressed in seconds. |
| CSToneAmplitude | float32[] | Returns the CS Tone Amplitude (dBm) versus time trace. |
| CSTonePhase | float32[] | Returns the CS Tone Phase (deg) versus time trace |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchdemodulatedbittrace.html language=enus -->
## TOPIC 00064: RFmxBT_ModAccFetchDemodulatedBitTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchdemodulatedbittrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchdemodulatedbittrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchDemodulatedBitTrace

int32 __stdcall RFmxBT_ModAccFetchDemodulatedBitTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 int8 demodulatedBits[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the ModAcc demodulated bit trace.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| demodulatedBits | int8[] | Returns the array of demodulated bits of the packet |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchdevm.html language=enus -->
## TOPIC 00065: RFmxBT_ModAccFetchDEVM

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchdevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchdevm.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchDEVM

int32 __stdcall RFmxBT_ModAccFetchDEVM (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* peakRMSDEVMMaximum,
 float64* peakDEVMMaximum,
 float64* ninetyninePercentDEVM);

#### Purpose

Fetches ModAcc differential EVM (DEVM) measurement results. These results are valid only for enhanced data rate (EDR) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| peakRMSDEVMMaximum | float64* | Returns the peak of the RMS DEVM values computed on each 50us block of the EDR portion of the EDR packet. When you set RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the maximum of the peak RMS DEVM values computed for each averaging count. This value is expressed in percentage. |
| peakDEVMMaximum | float64* | Returns the peak of the DEVM values computed on symbols in the EDR portion of the EDR packet. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the maximum of the peak symbol DEVM values computed for each averaging count. This value is expressed in percentage. |
| ninetyninePercentDEVM | float64* | Returns the 99th percentile of the DEVM values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed in percentage. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchdevmmagnitudeerror.html language=enus -->
## TOPIC 00066: RFmxBT_ModAccFetchDEVMMagnitudeError

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchdevmmagnitudeerror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchdevmmagnitudeerror.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchDEVMMagnitudeError

int32 __stdcall RFmxBT_ModAccFetchDEVMMagnitudeError (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* averageRMSMagnitudeErrorMean,
 float64* peakRMSMagnitudeErrorMaximum);

#### Purpose

Fetches ModAcc RMS magnitude error results. These results are valid only for enhanced data rate (EDR) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| averageRMSMagnitudeErrorMean | float64* | Returns the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled attribute to true, it returns the mean of the average RMS magnitude error values computed for each averaging count. This value is expressed as a percentage. |
| peakRMSMagnitudeErrorMaximum | float64* | Returns the peak of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled attribute to true, it returns the maximum of the peak RMS magnitude error values computed for each averaging count. This value is expressed as a percentage. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchdevmpersymboltrace.html language=enus -->
## TOPIC 00067: RFmxBT_ModAccFetchDEVMPerSymbolTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchdevmpersymboltrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchdevmpersymboltrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchDEVMPerSymbolTrace

int32 __stdcall RFmxBT_ModAccFetchDEVMPerSymbolTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 DEVMPerSymbol[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the DEVM values for symbols from the enhanced data rate (EDR) portion of the EDR packet. This function is valid only for EDR packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| DEVMPerSymbol | float32[] | Returns the array of DEVM values computed over the symbols in the EDR portion of EDR packet. This value is expressed in percentage. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchdevmphaseerror.html language=enus -->
## TOPIC 00068: RFmxBT_ModAccFetchDEVMPhaseError

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchdevmphaseerror.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchdevmphaseerror.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchDEVMPhaseError

int32 __stdcall RFmxBT_ModAccFetchDEVMPhaseError (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* averageRMSPhaseErrorMean,
 float64* peakRMSPhaseErrorMaximum);

#### Purpose

Fetches ModAcc RMS phase error results. These results are valid only for enhanced data rate (EDR) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| averageRMSPhaseErrorMean | float64* | Returns the average of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled attribute to true, it returns the mean of the average RMS phase error values computed for each averaging count. This value is expressed in degrees. |
| peakRMSPhaseErrorMaximum | float64* | Returns the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled attribute to true, it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchdf1.html language=enus -->
## TOPIC 00069: RFmxBT_ModAccFetchDf1

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchdf1.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchdf1.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchDf1

int32 __stdcall RFmxBT_ModAccFetchDf1 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* df1avgMaximum,
 float64* df1avgMinimum);

#### Purpose

Fetches the ModAcc df1 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| df1avgMaximum | float64* | Returns the df1avg value computed on the signal. This value is expressed in Hz. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the maximum of the df1avg results computed for each averaging count. |
| df1avgMinimum | float64* | Returns the df1avg value computed on the signal. This value is expressed in Hz. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the minimum of the df1avg results computed for each averaging count. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchdf1maxtrace.html language=enus -->
## TOPIC 00070: RFmxBT_ModAccFetchDf1maxTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchdf1maxtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchdf1maxtrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchDf1maxTrace

int32 __stdcall RFmxBT_ModAccFetchDf1maxTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 time[],
 float32 df1max[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the df1max versus the time trace. This function is applicable only for basic rate (BR) and low energy (LE) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| time | float32[] | Returns the array of time instances at which the df1max values are computed. This value is expressed in seconds. |
| df1max | float32[] | Returns the array of df1max values computed over the packet at each time instance. This value is expressed in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchdf2.html language=enus -->
## TOPIC 00071: RFmxBT_ModAccFetchDf2

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchdf2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchdf2.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchDf2

int32 __stdcall RFmxBT_ModAccFetchDf2 (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* df2avgMinimum,
 float64* percentageOfSymbolsAboveDf2maxThreshold);

#### Purpose

Fetches the ModAcc df2 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| df2avgMinimum | float64* | Returns the df2avg value computed on the signal. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the minimum of the df2avg results computed for each averaging count. This value is expressed in Hz. |
| percentageOfSymbolsAboveDf2maxThreshold | float64* | Returns the percentage of symbols with df2max values that are greater than the df2max threshold defined by the standard. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it computes this result using the df2max values from all averaging counts. This value is expressed as a percentage. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchdf2maxtrace.html language=enus -->
## TOPIC 00072: RFmxBT_ModAccFetchDf2maxTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchdf2maxtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchdf2maxtrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchDf2maxTrace

int32 __stdcall RFmxBT_ModAccFetchDf2maxTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 time[],
 float32 df2max[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the df2max versus the time trace. This function is valid only for basic rate (BR) and low energy (LE) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| time | float32[] | Returns the array of time instances at which the df2max values are computed. This value is expressed in seconds. |
| df2max | float32[] | Returns the array of df2max values computed over the packet at each time instance. This value is expressed in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchdf4avgtrace.html language=enus -->
## TOPIC 00073: RFmxBT_ModAccFetchDf4avgTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchdf4avgtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchdf4avgtrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchDf4avgTrace

int32 __stdcall RFmxBT_ModAccFetchDf4avgTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 time[],
 float32 df4avg[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the df4avg versus the time trace. This function is valid only for LE-CS Packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| time | float32[] | Returns the array of time instances at which the df2max values are computed. This value is expressed in seconds. |
| df4avg | float32[] | Returns the array of df4avg values computed over the packet at each time instance. This value is expressed in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchfrequencyerrorbr.html language=enus -->
## TOPIC 00074: RFmxBT_ModAccFetchFrequencyErrorBR

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchfrequencyerrorbr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchfrequencyerrorbr.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchFrequencyErrorBR

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorBR (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* initialFrequencyErrorMaximum,
 float64* peakFrequencyDriftMaximum,
 float64* peakFrequencyDriftRateMaximum);

#### Purpose

Fetches the ModAcc frequency error trace for basic rate (BR) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| initialFrequencyErrorMaximum | float64* | Returns the initial frequency error value computed on the preamble of the BR packet. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns a value corresponding to the maximum of absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
| peakFrequencyDriftMaximum | float64* | Returns the peak frequency drift value computed on the BR packet. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the value corresponding to the maximum of absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
| peakFrequencyDriftRateMaximum | float64* | Returns the peak frequency drift rate value computed on the BR packet. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the value corresponding to the maximum of absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchfrequencyerroredr.html language=enus -->
## TOPIC 00075: RFmxBT_ModAccFetchFrequencyErrorEDR

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchfrequencyerroredr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchfrequencyerroredr.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchFrequencyErrorEDR

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorEDR (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* headerFrequencyErrorWiMaximum,
 float64* peakFrequencyErrorWiPlusW0Maximum,
 float64* peakFrequencyErrorW0Maximum);

#### Purpose

Fetches ModAcc frequency error measurement results for enhanced data rate (EDR) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| headerFrequencyErrorWiMaximum | float64* | Returns the frequency error value computed on the header of the EDR packet. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the value corresponding to the maximum of absolute header frequency error values computed for each averaging count. This value is expressed in Hz. |
| peakFrequencyErrorWiPlusW0Maximum | float64* | Returns the peak frequency error value computed on the EDR portion of the EDR packet. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the value corresponding to the maximum of the absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
| peakFrequencyErrorW0Maximum | float64* | Returns the peak frequency error value computed on the EDR portion of the EDR packet, relative to the header frequency error. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchfrequencyerrorle.html language=enus -->
## TOPIC 00076: RFmxBT_ModAccFetchFrequencyErrorLE

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchfrequencyerrorle.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchfrequencyerrorle.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchFrequencyErrorLE

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorLE (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* peakFrequencyErrorMaximum,
 float64* initialFrequencyDriftMaximum,
 float64* peakFrequencyDriftMaximum,
 float64* peakFrequencyDriftRateMaximum);

#### Purpose

Fetches ModAcc frequency error measurement results for low energy (LE) or low energy - channel sounding (LE-CS) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| peakFrequencyErrorMaximum | float64* | When you set the RFMXBT_ATTR_DIRECTION_FINDING_MODE attribute to RFMXBT_VAL_DIRECTION_FINDING_MODE_DISABLED, it returns the peak frequency error value computed on the LE/LE-CS packet. When you set the RFMXBT_ATTR_DIRECTION_FINDING_MODE attribute to RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL, it returns the peak frequency error value computed on the Constant tone extension field of the LE packet. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, , it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
| initialFrequencyDriftMaximum | float64* | Returns the initial frequency drift value computed on the LE packet. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the value corresponding to the maximum of absolute initial frequency drift values computed for each averaging count. This value is expressed in Hz. |
| peakFrequencyDriftMaximum | float64* | Returns the peak frequency drift value computed on the LE packet. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the value corresponding to the maximum of absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
| peakFrequencyDriftRateMaximum | float64* | Returns the peak frequency drift rate value computed on the LE packet. When you set the RFMXBT_ATTR_MODACC_AVERAGING_ENABLED attribute to RFMXBT_VAL_MODACC_AVERAGING_ENABLED_TRUE, it returns the value corresponding to the maximum of absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchfrequencyerrortracebr.html language=enus -->
## TOPIC 00077: RFmxBT_ModAccFetchFrequencyErrorTraceBR

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchfrequencyerrortracebr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchfrequencyerrortracebr.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchFrequencyErrorTraceBR

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorTraceBR (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 time[],
 float32 frequencyError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the ModAcc frequency error trace for basic rate (BR) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| time | float32[] | Returns an array of time instances corresponding to the start of the bit blocks at which the frequency error values are computed. This value is expressed in seconds. |
| frequencyError | float32[] | Returns an array of frequency errors computed over the packet. This value is expressed in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchfrequencyerrortracele.html language=enus -->
## TOPIC 00078: RFmxBT_ModAccFetchFrequencyErrorTraceLE

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchfrequencyerrortracele.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchfrequencyerrortracele.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchFrequencyErrorTraceLE

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorTraceLE (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 time[],
 float32 frequencyError[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the ModAcc frequency error trace for low energy (LE) or low energy - channel sounding (LE-CS) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| time | float32[] | Returns an array of time instances corresponding to the start of the bit blocks at which the frequency error values are computed. This value is expressed in seconds. |
| frequencyError | float32[] | Returns an array of frequency errors computed over the packet. This value is expressed in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchfrequencyerrorwiplusw0traceedr.html language=enus -->
## TOPIC 00079: RFmxBT_ModAccFetchFrequencyErrorWiPlusW0TraceEDR

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchfrequencyerrorwiplusw0traceedr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchfrequencyerrorwiplusw0traceedr.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchFrequencyErrorWiPlusW0TraceEDR

int32 __stdcall RFmxBT_ModAccFetchFrequencyErrorWiPlusW0TraceEDR (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 time[],
 float32 frequencyErrorWiPlusW0[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the ModAcc frequency error trace for enhanced data rate (EDR) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| time | float32[] | Returns an array of time instances corresponding to the start of the 50us blocks of the EDR portion of EDR packet at which the frequency error values are computed. This value is expressed in seconds. |
| frequencyErrorWiPlusW0 | float32[] | Returns an array of frequency errors wi+w0 computed over the packet. This value is expressed in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchfrequencytrace.html language=enus -->
## TOPIC 00080: RFmxBT_ModAccFetchFrequencyTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchfrequencytrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchfrequencytrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchFrequencyTrace

int32 __stdcall RFmxBT_ModAccFetchFrequencyTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* x0,
 float64* dx,
 float32 frequency[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the frequency versus time trace. This trace is valid for basic rate (BR), low energy (LE) and low energy - channel sounding (LE-CS) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| x0 | float64* | Returns the start time. This value is expressed in seconds. |
| dx | float64* | Returns the sample duration. This value is expressed in seconds. |
| frequency | float32[] | Returns the frequency at each time instance. This value is expressed in Hz. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modaccfetchrmsdevmtrace.html language=enus -->
## TOPIC 00081: RFmxBT_ModAccFetchRMSDEVMTrace

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modaccfetchrmsdevmtrace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modaccfetchrmsdevmtrace.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModAccFetchRMSDEVMTrace

int32 __stdcall RFmxBT_ModAccFetchRMSDEVMTrace (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float32 RMSDEVM[],
 int32 arraySize,
 int32* actualArraySize);

#### Purpose

Fetches the RMS DEVM values from each 50us block of EDR portion of EDR packet. This function is valid only for enhanced data rate (EDR) packets.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxBT_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| RMSDEVM | float32[] | Returns the array of RMS DEVM values computed on each 50us block of the EDR portion of the EDR packet. This value is expressed in percentage. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=cvirfmxbt_modspectrumcfgaveraging.html language=enus -->
## TOPIC 00082: RFmxBT_ModSpectrumCfgAveraging

- bundle_id: `rfmx-bt-cvi`
- source_path: `cvirfmxbt_modspectrumcfgaveraging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/cvirfmxbt_modspectrumcfgaveraging.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFmxBT_ModSpectrumCfgAveraging

int32 __stdcall RFmxBT_ModSpectrumCfgAveraging (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 int32 averagingEnabled,
 int32 averagingCount);

#### Purpose

Configures averaging for the ModSpectrum measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxBT_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
| averagingEnabled | int32 | Specifies specifies whether to enable averaging for the ModSpectrum measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the ModSpectrum measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |  |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the ModSpectrum measurement is averaged. |  |
| averagingCount | int32 | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to RFMXBT_VAL_MODSPECTRUM_AVERAGING_ENABLED_TRUE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxBT_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_acp_number_of_analysis_threads.html language=enus -->
## TOPIC 00083: RFMXBT_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_acp_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_acp_number_of_analysis_threads.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxBT_ACPGetNumberOfAnalysisThreads Set Function: RFmxBT_ACPSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_acp_number_of_offsets.html language=enus -->
## TOPIC 00084: RFMXBT_ATTR_ACP_NUMBER_OF_OFFSETS

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_acp_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_acp_number_of_offsets.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_ACP_NUMBER_OF_OFFSETS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the number of offset channels used on either side of the reference channel for the adjacent channel power (ACP) measurement when you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC. This attribute also returns the actual number of offsets used in the ACP measurement when you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 5. Valid values are 0 to 100, inclusive. Get Function: RFmxBT_ACPGetNumberOfOffsets Set Function: RFmxBT_ACPSetNumberOfOffsets |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_acp_offset_channel_mode.html language=enus -->
## TOPIC 00085: RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_acp_offset_channel_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_acp_offset_channel_mode.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies which offset channels are used for the measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC. Get Function: RFmxBT_ACPGetOffsetChannelMode Set Function: RFmxBT_ACPSetOffsetChannelMode |
| Values: | RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC (0)Specifies that the offset channels are symmetrically located around the reference channel. The number of offsets on either side of the reference channel is specified by the RFMXBT_ATTR_ACP_NUMBER_OF_OFFSETS attribute. In symmetric mode, the RFMX_ATTR_CENTER_FREQUENCY attribute specifies the frequency of the reference channel, expressed in Hz. RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND (1)Specifies that the measurement is performed over all the channels as specified by the standard. For BR and EDR packets, 79 channels starting from 2.402GHz to 2.48GHz are used for the measurement. For LE packets, 81 channels starting from 2.401GHz to 2.481GHz are used for the measurement. In In-band mode, the RFMX_ATTR_CENTER_FREQUENCY attribute specifies the frequency of acquisition which must be equal to 2.441GHz. Configure the RFMXBT_ATTR_CHANNEL_NUMBER attribute to specify the frequency of the reference channel. |
| RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC (0) | Specifies that the offset channels are symmetrically located around the reference channel. The number of offsets on either side of the reference channel is specified by the RFMXBT_ATTR_ACP_NUMBER_OF_OFFSETS attribute. In symmetric mode, the RFMX_ATTR_CENTER_FREQUENCY attribute specifies the frequency of the reference channel, expressed in Hz. |
| RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND (1) | Specifies that the measurement is performed over all the channels as specified by the standard. For BR and EDR packets, 79 channels starting from 2.402GHz to 2.48GHz are used for the measurement. For LE packets, 81 channels starting from 2.401GHz to 2.481GHz are used for the measurement. In In-band mode, the RFMX_ATTR_CENTER_FREQUENCY attribute specifies the frequency of acquisition which must be equal to 2.441GHz. Configure the RFMXBT_ATTR_CHANNEL_NUMBER attribute to specify the frequency of the reference channel. |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_acp_offset_frequency.html language=enus -->
## TOPIC 00086: RFMXBT_ATTR_ACP_OFFSET_FREQUENCY

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_acp_offset_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_acp_offset_frequency.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_ACP_OFFSET_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeF64 |
| Description: | Returns the frequency of the offset channel with respect to the reference channel frequency. This value is expressed in Hz. Use 'offset(n)' as the selector string to configure or read this attribute. The default value is 1 MHz. Get Function: RFmxBT_ACPGetOffsetFrequency |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_acp_results_lower_offset_absolute_power.html language=enus -->
## TOPIC 00087: RFMXBT_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_acp_results_lower_offset_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_acp_results_lower_offset_absolute_power.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeF64 |
| Description: | Returns the absolute power measured in the lower offset channel. This value is expressed in dBm. Use 'offset(k)' as the selector string to read this result. Get Function: RFmxBT_ACPGetResultsLowerOffsetAbsolutePower |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_acp_results_upper_offset_absolute_power.html language=enus -->
## TOPIC 00088: RFMXBT_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_acp_results_upper_offset_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_acp_results_upper_offset_absolute_power.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeF64 |
| Description: | Returns the absolute power measured in the upper offset channel. This value is expressed in dBm. Use 'offset(k)' as the selector string to read this result. Get Function: RFmxBT_ACPGetResultsUpperOffsetAbsolutePower |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_acp_results_upper_offset_margin.html language=enus -->
## TOPIC 00089: RFMXBT_ATTR_ACP_RESULTS_UPPER_OFFSET_MARGIN

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_acp_results_upper_offset_margin.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_acp_results_upper_offset_margin.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_ACP_RESULTS_UPPER_OFFSET_MARGIN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeF64 |
| Description: | Returns the margin from the limit specified by the mask with exception for upper offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_INBAND. This attribute returns NaN if you set the RFMXBT_ATTR_ACP_OFFSET_CHANNEL_MODE attribute to RFMXBT_VAL_ACP_OFFSET_CHANNEL_MODE_SYMMETRIC. Use 'offset(k)' as the selector string to read this result. Get Function: RFmxBT_ACPGetResultsUpperOffsetMargin |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_acp_results_upper_offset_relative_power.html language=enus -->
## TOPIC 00090: RFMXBT_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_acp_results_upper_offset_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_acp_results_upper_offset_relative_power.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeF64 |
| Description: | Returns the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB. Use 'offset(k)' as the selector string to read this result. Get Function: RFmxBT_ACPGetResultsUpperOffsetRelativePower |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_auto_level_initial_reference_level.html language=enus -->
## TOPIC 00091: RFMXBT_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_auto_level_initial_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_auto_level_initial_reference_level.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeF64RFmxBT_GetAttributeF64 |
| Description: | Specifies the initial reference level which the RFmxBT Auto Level function uses to estimate the peak power of the input signal. This value is expressed in dBm. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 30. Get Function: RFmxBT_GetAutoLevelInitialReferenceLevel Set Function: RFmxBT_SetAutoLevelInitialReferenceLevel |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_bandwidth_bit_period_product.html language=enus -->
## TOPIC 00092: RFMXBT_ATTR_BANDWIDTH_BIT_PERIOD_PRODUCT

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_bandwidth_bit_period_product.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_bandwidth_bit_period_product.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_BANDWIDTH_BIT_PERIOD_PRODUCT

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeF64RFmxBT_GetAttributeF64 |
| Description: | Specifies the bandwidth bit period product of GFSK modulation for LE-CS packet type. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.5.5. Get Function: RFmxBT_GetBandwidthBitPeriodProduct Set Function: RFmxBT_SetBandwidthBitPeriodProduct |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_bd_address_lap.html language=enus -->
## TOPIC 00093: RFMXBT_ATTR_BD_ADDRESS_LAP

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_bd_address_lap.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_bd_address_lap.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_BD_ADDRESS_LAP

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR). This value is used to generate the sync word if you set the burst synchronization type attribute in TXP, ACP, or ModAcc measurements to Sync Word. This attribute is applicable only to BR and EDR packet types.You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxBT_GetBDAddressLAP Set Function: RFmxBT_SetBDAddressLAP |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_center_frequency.html language=enus -->
## TOPIC 00094: RFMXBT_ATTR_CENTER_FREQUENCY

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_center_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_center_frequency.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_CENTER_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeF64RFmxBT_GetAttributeF64 |
| Description: | Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is hardware dependent. The default value for the devices PXIe-5645/5820 is 0 Hz. The default value for devices PXIe-5644/5646/5840/5663/5663E/5665/5668R is 2.402 GHz. Get Function: RFmxBT_GetCenterFrequency Set Function: RFmxBT_SetCenterFrequency |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_channel_sounding_packet_format.html language=enus -->
## TOPIC 00095: RFMXBT_ATTR_CHANNEL_SOUNDING_PACKET_FORMAT

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_channel_sounding_packet_format.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_channel_sounding_packet_format.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_CHANNEL_SOUNDING_PACKET_FORMAT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the format of the Channel Sounding packet depending on the position and presence of SYNC and CS Tone fields. This attribute is applicable only when you set the RFMXBT_ATTR_PACKET_TYPE attribute to RFMXBT_VAL_PACKET_TYPE_LE_CS. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_SYNC. Get Function: RFmxBT_GetChannelSoundingPacketFormat Set Function: RFmxBT_SetChannelSoundingPacketFormat |
| Values: | RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_SYNC (0)Specifies that the LE-CS packet contains only SYNC portion. RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_CS_TONE (1)Specifies that the LE-CS packet contains only CS Tone. RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_CS_TONE_AFTER_SYNC (2)Specifies that the CS Tone portion is at the end of the LE-CS packet. RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_CS_TONE_BEFORE_SYNC (3)Specifies that the CS Tone portion is at the beginning of the LE-CS packet. |
| RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_SYNC (0) | Specifies that the LE-CS packet contains only SYNC portion. |
| RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_CS_TONE (1) | Specifies that the LE-CS packet contains only CS Tone. |
| RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_CS_TONE_AFTER_SYNC (2) | Specifies that the CS Tone portion is at the end of the LE-CS packet. |
| RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_CS_TONE_BEFORE_SYNC (3) | Specifies that the CS Tone portion is at the beginning of the LE-CS packet. |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_channel_sounding_phase_measurement_period.html language=enus -->
## TOPIC 00096: RFMXBT_ATTR_CHANNEL_SOUNDING_PHASE_MEASUREMENT_PERIOD

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_channel_sounding_phase_measurement_period.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_channel_sounding_phase_measurement_period.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_CHANNEL_SOUNDING_PHASE_MEASUREMENT_PERIOD

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeF64RFmxBT_GetAttributeF64 |
| Description: | Specifies the Channel Sounding Phase Measurement Period for the LE-CS packet. This attribute is applicable only when you set the RFMXBT_ATTR_PACKET_TYPE attribute to RFMXBT_VAL_PACKET_TYPE_LE_CS and the RFMXBT_ATTR_CHANNEL_SOUNDING_PACKET_FORMAT attribute to any value other than RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_SYNC. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10 us. Get Function: RFmxBT_GetChannelSoundingPhaseMeasurementPeriod Set Function: RFmxBT_SetChannelSoundingPhaseMeasurementPeriod |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_channel_sounding_sync_sequence.html language=enus -->
## TOPIC 00097: RFMXBT_ATTR_CHANNEL_SOUNDING_SYNC_SEQUENCE

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_channel_sounding_sync_sequence.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_channel_sounding_sync_sequence.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_CHANNEL_SOUNDING_SYNC_SEQUENCE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the type of sequence present in the SYNC portion after trailer bits. This attribute is applicable only when you set the RFMXBT_ATTR_PACKET_TYPE attribute to RFMXBT_VAL_PACKET_TYPE_LE_CS and the RFMXBT_ATTR_CHANNEL_SOUNDING_PACKET_FORMAT attribute to any value other than RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_CS_TONE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_NONE. Get Function: RFmxBT_GetChannelSoundingSyncSequence Set Function: RFmxBT_SetChannelSoundingSyncSequence |
| Values: | RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_NONE (0)Specifies that there is no optional sequence at the end of the SYNC portion of the LE-CS packet. RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_SOUNDING_SEQUENCE_32_BIT (1)Specifies that there is a 32-bit sounding sequence at the end of the SYNC portion of the LE-CS packet. RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_SOUNDING_SEQUENCE_96_BIT (2)Specifies that there is a 96-bit sounding sequence at the end of the SYNC portion of the LE-CS packet. RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_PAYLOAD_PATTERN (3)Specifies that the payload bit pattern is present at the end of the SYNC portion of the LE-CS packet. |
| RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_NONE (0) | Specifies that there is no optional sequence at the end of the SYNC portion of the LE-CS packet. |
| RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_SOUNDING_SEQUENCE_32_BIT (1) | Specifies that there is a 32-bit sounding sequence at the end of the SYNC portion of the LE-CS packet. |
| RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_SOUNDING_SEQUENCE_96_BIT (2) | Specifies that there is a 96-bit sounding sequence at the end of the SYNC portion of the LE-CS packet. |
| RFMXBT_VAL_CHANNEL_SOUNDING_SYNC_SEQUENCE_PAYLOAD_PATTERN (3) | Specifies that the payload bit pattern is present at the end of the SYNC portion of the LE-CS packet. |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_channel_sounding_tone_extension_slot.html language=enus -->
## TOPIC 00098: RFMXBT_ATTR_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_channel_sounding_tone_extension_slot.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_channel_sounding_tone_extension_slot.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies whether the tone extension slot transmission is enabled after CS Tone. This attribute is applicable only when you set the RFMXBT_ATTR_PACKET_TYPE attribute to RFMXBT_VAL_PACKET_TYPE_LE_CS and the RFMXBT_ATTR_CHANNEL_SOUNDING_PACKET_FORMAT attribute to any value other than RFMXBT_VAL_CHANNEL_SOUNDING_PACKET_FORMAT_SYNC. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT_DISABLED. Get Function: RFmxBT_GetChannelSoundingToneExtensionSlot Set Function: RFmxBT_SetChannelSoundingToneExtensionSlot |
| Values: | RFMXBT_VAL_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT_DISABLED (0)Specifies that there is no transmission in the CS Tone extension slot. RFMXBT_VAL_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT_ENABLED (1)Specifies that there is transmission in the CS Tone extension slot. |
| RFMXBT_VAL_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT_DISABLED (0) | Specifies that there is no transmission in the CS Tone extension slot. |
| RFMXBT_VAL_CHANNEL_SOUNDING_TONE_EXTENSION_SLOT_ENABLED (1) | Specifies that there is transmission in the CS Tone extension slot. |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_cte_length.html language=enus -->
## TOPIC 00099: RFMXBT_ATTR_CTE_LENGTH

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_cte_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_cte_length.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_CTE_LENGTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeF64RFmxBT_GetAttributeF64 |
| Description: | Specifies the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This attribute is applicable only when you set the RFMXBT_ATTR_DIRECTION_FINDING_MODE attribute to either RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 160 microseconds. Get Function: RFmxBT_GetCTELength Set Function: RFmxBT_SetCTELength |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_cte_number_of_transmit_slots.html language=enus -->
## TOPIC 00100: RFMXBT_ATTR_CTE_NUMBER_OF_TRANSMIT_SLOTS

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_cte_number_of_transmit_slots.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_cte_number_of_transmit_slots.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_CTE_NUMBER_OF_TRANSMIT_SLOTS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeI32 |
| Description: | Returns the number of transmit slots in the constant time extension portion of the generated LE packet. This attribute is applicable only when you set the RFMXBT_ATTR_DIRECTION_FINDING_MODE attribute to RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxBT_GetCTENumberOfTransmitSlots |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_cte_slot_duration.html language=enus -->
## TOPIC 00101: RFMXBT_ATTR_CTE_SLOT_DURATION

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_cte_slot_duration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_cte_slot_duration.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_CTE_SLOT_DURATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeF64RFmxBT_GetAttributeF64 |
| Description: | Specifies the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. This attribute is applicable only when you set the RFMXBT_ATTR_DIRECTION_FINDING_MODE attribute to RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1u. Get Function: RFmxBT_GetCTESlotDuration Set Function: RFmxBT_SetCTESlotDuration |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_data_rate.html language=enus -->
## TOPIC 00102: RFMXBT_ATTR_DATA_RATE

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_data_rate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_data_rate.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_DATA_RATE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the data rate of the LE or LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This attribute is applicable only to LE or LE-CS packet type. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1M. Get Function: RFmxBT_GetDataRate Set Function: RFmxBT_SetDataRate |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_detected_data_rate.html language=enus -->
## TOPIC 00103: RFMXBT_ATTR_DETECTED_DATA_RATE

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_detected_data_rate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_detected_data_rate.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_DETECTED_DATA_RATE

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeI32 |
| Description: | Returns the data rate detected by the RFmxBT Auto Detect Signal function. This attribute returns a valid data rate only if the Detected Packet Type attribute returns LE. This attribute can be queried only after calling the RFmxBT Auto Detect Signal function. You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Not Applicable. Get Function: RFmxBT_GetDetectedDataRate |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_direction_finding_mode.html language=enus -->
## TOPIC 00104: RFMXBT_ATTR_DIRECTION_FINDING_MODE

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_direction_finding_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_direction_finding_mode.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_DIRECTION_FINDING_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the mode of direction finding. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_DIRECTION_FINDING_MODE_DISABLED. Get Function: RFmxBT_GetDirectionFindingMode Set Function: RFmxBT_SetDirectionFindingMode |
| Values: | RFMXBT_VAL_DIRECTION_FINDING_MODE_DISABLED (0)Specifies that the LE packet does not have fields required for direction finding. RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) Specifies that the LE packets uses the Angle of Arrival method of direction finding. RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) Specifies that the LE packets uses the Angle of Departure method of direction finding. |
| RFMXBT_VAL_DIRECTION_FINDING_MODE_DISABLED (0) | Specifies that the LE packet does not have fields required for direction finding. |
| RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) | Specifies that the LE packets uses the Angle of Arrival method of direction finding. |
| RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) | Specifies that the LE packets uses the Angle of Departure method of direction finding. |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_external_attenuation.html language=enus -->
## TOPIC 00105: RFMXBT_ATTR_EXTERNAL_ATTENUATION

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_external_attenuation.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_EXTERNAL_ATTENUATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeF64RFmxBT_GetAttributeF64 |
| Description: | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. Get Function: RFmxBT_GetExternalAttenuation Set Function: RFmxBT_SetExternalAttenuation |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_frequency_range_all_traces_enabled.html language=enus -->
## TOPIC 00106: RFMXBT_ATTR_FREQUENCY_RANGE_ALL_TRACES_ENABLED

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_frequency_range_all_traces_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_frequency_range_all_traces_enabled.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_FREQUENCY_RANGE_ALL_TRACES_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies whether to enable all the traces for FrequencyRange measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_FALSE. Get Function: RFmxBT_FrequencyRangeGetAllTracesEnabled Set Function: RFmxBT_FrequencyRangeSetAllTracesEnabled |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_frequency_range_averaging_count.html language=enus -->
## TOPIC 00107: RFMXBT_ATTR_FREQUENCY_RANGE_AVERAGING_COUNT

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_frequency_range_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_frequency_range_averaging_count.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_FREQUENCY_RANGE_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXBT_ATTR_FREQUENCY_RANGE_AVERAGING_ENABLED attribute to RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxBT_FrequencyRangeGetAveragingCount Set Function: RFmxBT_FrequencyRangeSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_frequency_range_averaging_enabled.html language=enus -->
## TOPIC 00108: RFMXBT_ATTR_FREQUENCY_RANGE_AVERAGING_ENABLED

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_frequency_range_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_frequency_range_averaging_enabled.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_FREQUENCY_RANGE_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the FrequencyRange measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_FALSE. Get Function: RFmxBT_FrequencyRangeGetAveragingEnabled Set Function: RFmxBT_FrequencyRangeSetAveragingEnabled |
| Values: | RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_TRUE (1)The FrequencyRange measurement uses the RFMXBT_ATTR_FREQUENCY_RANGE_AVERAGING_COUNT attribute as the number of acquisitions over which the FrequencyRange measurement is averaged. |
| RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXBT_VAL_FREQUENCY_RANGE_AVERAGING_ENABLED_TRUE (1) | The FrequencyRange measurement uses the RFMXBT_ATTR_FREQUENCY_RANGE_AVERAGING_COUNT attribute as the number of acquisitions over which the FrequencyRange measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_frequency_range_measurement_enabled.html language=enus -->
## TOPIC 00109: RFMXBT_ATTR_FREQUENCY_RANGE_MEASUREMENT_ENABLED

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_frequency_range_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_frequency_range_measurement_enabled.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_FREQUENCY_RANGE_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. This measurement is valid only for basic rate (BR) packets. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_FALSE. Get Function: RFmxBT_FrequencyRangeGetMeasurementEnabled Set Function: RFmxBT_FrequencyRangeSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_frequency_range_number_of_analysis_threads.html language=enus -->
## TOPIC 00110: RFMXBT_ATTR_FREQUENCY_RANGE_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_frequency_range_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_frequency_range_number_of_analysis_threads.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_FREQUENCY_RANGE_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for the frequency range measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxBT_FrequencyRangeGetNumberOfAnalysisThreads Set Function: RFmxBT_FrequencyRangeSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_frequency_range_span.html language=enus -->
## TOPIC 00111: RFMXBT_ATTR_FREQUENCY_RANGE_SPAN

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_frequency_range_span.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_frequency_range_span.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_FREQUENCY_RANGE_SPAN

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeF64RFmxBT_GetAttributeF64 |
| Description: | Specifies the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification RF.TS.p33. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10 MHz. Get Function: RFmxBT_FrequencyRangeGetSpan Set Function: RFmxBT_FrequencyRangeSetSpan |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_iq_power_edge_trigger_level.html language=enus -->
## TOPIC 00112: RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_iq_power_edge_trigger_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_iq_power_edge_trigger_level.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeF64RFmxBT_GetAttributeF64 |
| Description: | Specifies the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. This value is expressed in dB when you set the RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE and in dBm when you set the RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE. This attribute is valid only when you set the RFMXBT_ATTR_TRIGGER_TYPE attribute to RFMXBT_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is hardware dependent. Get Function: RFmxBT_GetIQPowerEdgeTriggerLevel Set Function: RFmxBT_SetIQPowerEdgeTriggerLevel |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_iq_power_edge_trigger_level_type.html language=enus -->
## TOPIC 00113: RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_iq_power_edge_trigger_level_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_iq_power_edge_trigger_level_type.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the reference for the RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The RFMXBT_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute is used only when you set the RFMXBT_ATTR_TRIGGER_TYPE attribute to RFMXBT_VAL_TRIGGER_TYPE_IQ_POWER_EDGE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE. Get Function: RFmxBT_GetIQPowerEdgeTriggerLevelType Set Function: RFmxBT_SetIQPowerEdgeTriggerLevelType |
| Values: | RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0)The IQ Power Edge Level attribute is relative to the value of the RFMXBT_ATTR_REFERENCE_LEVEL attribute. RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1)The IQ Power Edge Level attribute specifies the absolute power. |
| RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE (0) | The IQ Power Edge Level attribute is relative to the value of the RFMXBT_ATTR_REFERENCE_LEVEL attribute. |
| RFMXBT_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE (1) | The IQ Power Edge Level attribute specifies the absolute power. |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_txp_averaging_count.html language=enus -->
## TOPIC 00114: RFMXBT_ATTR_TXP_AVERAGING_COUNT

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_txp_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_txp_averaging_count.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_TXP_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXBT_ATTR_TXP_AVERAGING_ENABLED attribute to RFMXBT_VAL_TXP_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxBT_TXPGetAveragingCount Set Function: RFmxBT_TXPSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_txp_averaging_enabled.html language=enus -->
## TOPIC 00115: RFMXBT_ATTR_TXP_AVERAGING_ENABLED

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_txp_averaging_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_txp_averaging_enabled.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_TXP_AVERAGING_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies whether to enable averaging for the transmit power (TxP) measurements. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_TXP_AVERAGING_ENABLED_FALSE. Get Function: RFmxBT_TXPGetAveragingEnabled Set Function: RFmxBT_TXPSetAveragingEnabled |
| Values: | RFMXBT_VAL_TXP_AVERAGING_ENABLED_FALSE (0)The measurement is performed on a single acquisition. RFMXBT_VAL_TXP_AVERAGING_ENABLED_TRUE (1)The measurement uses the RFMXBT_ATTR_TXP_AVERAGING_COUNT attribute as the number of acquisitions over which the TXP measurement is averaged. |
| RFMXBT_VAL_TXP_AVERAGING_ENABLED_FALSE (0) | The measurement is performed on a single acquisition. |
| RFMXBT_VAL_TXP_AVERAGING_ENABLED_TRUE (1) | The measurement uses the RFMXBT_ATTR_TXP_AVERAGING_COUNT attribute as the number of acquisitions over which the TXP measurement is averaged. |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_txp_burst_synchronization_type.html language=enus -->
## TOPIC 00116: RFMXBT_ATTR_TXP_BURST_SYNCHRONIZATION_TYPE

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_txp_burst_synchronization_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_txp_burst_synchronization_type.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_TXP_BURST_SYNCHRONIZATION_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxBT_SetAttributeI32RFmxBT_GetAttributeI32 |
| Description: | Specifies the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXBT_VAL_TXP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE. Get Function: RFmxBT_TXPGetBurstSynchronizationType Set Function: RFmxBT_TXPSetBurstSynchronizationType |
| Values: | RFMXBT_VAL_TXP_BURST_SYNCHRONIZATION_TYPE_NONE (0)Specifies that the measurement does not perform synchronization to detect the start of the packet. RFMXBT_VAL_TXP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE (1)Specifies that the measurement uses the preamble field to detect the start of the packet. RFMXBT_VAL_TXP_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD (2)Specifies that the measurement uses sync word for the BR/EDR packets and access address for LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the RFMXBT_ATTR_BD_ADDRESS_LAP attribute. |
| RFMXBT_VAL_TXP_BURST_SYNCHRONIZATION_TYPE_NONE (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| RFMXBT_VAL_TXP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE (1) | Specifies that the measurement uses the preamble field to detect the start of the packet. |
| RFMXBT_VAL_TXP_BURST_SYNCHRONIZATION_TYPE_SYNC_WORD (2) | Specifies that the measurement uses sync word for the BR/EDR packets and access address for LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the RFMXBT_ATTR_BD_ADDRESS_LAP attribute. |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_txp_results_average_power_mean.html language=enus -->
## TOPIC 00117: RFMXBT_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_txp_results_average_power_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_txp_results_average_power_mean.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeF64 |
| Description: | Returns the average power computed over the measurement interval. When you set the RFMXBT_ATTR_DIRECTION_FINDING_MODE attribute to RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE for LE packets, it will exclude guard period and all the switching slots for the average power computation. This value is expressed in dBm. When you set the RFMXBT_ATTR_TXP_AVERAGING_ENABLED attribute to RFMXBT_VAL_TXP_AVERAGING_ENABLED_TRUE, it returns the mean of the average power results computed for each averaging count. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxBT_TXPGetResultsAveragePowerMean |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_txp_results_average_power_minimum.html language=enus -->
## TOPIC 00118: RFMXBT_ATTR_TXP_RESULTS_AVERAGE_POWER_MINIMUM

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_txp_results_average_power_minimum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_txp_results_average_power_minimum.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_TXP_RESULTS_AVERAGE_POWER_MINIMUM

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeF64 |
| Description: | Returns the average power computed over the measurement interval. When you set the RFMXBT_ATTR_DIRECTION_FINDING_MODE attribute to RFMXBT_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the RFMXBT_ATTR_TXP_AVERAGING_ENABLED attribute to RFMXBT_VAL_TXP_AVERAGING_ENABLED_TRUE, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxBT_TXPGetResultsAveragePowerMinimum |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_txp_results_edr_dpsk_average_power_mean.html language=enus -->
## TOPIC 00119: RFMXBT_ATTR_TXP_RESULTS_EDR_DPSK_AVERAGE_POWER_MEAN

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_txp_results_edr_dpsk_average_power_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_txp_results_edr_dpsk_average_power_mean.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_TXP_RESULTS_EDR_DPSK_AVERAGE_POWER_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeF64 |
| Description: | Returns the average power of the DPSK portion of the EDR packet. When you set the RFMXBT_ATTR_TXP_AVERAGING_ENABLED attribute to RFMXBT_VAL_TXP_AVERAGING_ENABLED_TRUE, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxBT_TXPGetResultsEDRDPSKAveragePowerMean |

<!--NI_TOPIC bundle=rfmx-bt-cvi path=rfmxbt_attr_txp_results_edr_dpsk_gfsk_average_power_ratio_mean.html language=enus -->
## TOPIC 00120: RFMXBT_ATTR_TXP_RESULTS_EDR_DPSK_GFSK_AVERAGE_POWER_RATIO_MEAN

- bundle_id: `rfmx-bt-cvi`
- source_path: `rfmxbt_attr_txp_results_edr_dpsk_gfsk_average_power_ratio_mean.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-bt-cvi/raw/resource/enus/rfmxbt_attr_txp_results_edr_dpsk_gfsk_average_power_ratio_mean.html
- document_id: `rfmx-bt-cvi`
- page_type: `leaf`
- content_type: ``

RFMXBT_ATTR_TXP_RESULTS_EDR_DPSK_GFSK_AVERAGE_POWER_RATIO_MEAN

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxBT_GetAttributeF64 |
| Description: | Returns the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the RFMXBT_ATTR_TXP_AVERAGING_ENABLED attribute to RFMXBT_VAL_TXP_AVERAGING_ENABLED_TRUE, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxBT_TXPGetResultsEDR_DPSK_GFSKAveragePowerRatioMean |
