# NI DOCUMENT BUNDLE: rfmx-tdscdma-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-tdscdma-cvi start=1 end=7 -->
<!--NI_TOPIC bundle=rfmx-tdscdma-cvi path=bp_help_file_title.html language=enus -->
## TOPIC 00001: RFmx TD-SCDMA C Reference

- bundle_id: `rfmx-tdscdma-cvi`
- source_path: `bp_help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-cvi/raw/resource/enus/bp_help_file_title.html
- document_id: `rfmx-tdscdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmx TD-SCDMA C Reference

This help file contains information about the RFmxTDSCDMA functions, attributes, and values that you can use when programming your application.

<!--NI_TOPIC bundle=rfmx-tdscdma-cvi path=cvirfmxtdscdma_abortmeasurements.html language=enus -->
## TOPIC 00002: RFmxTDSCDMA_AbortMeasurements

- bundle_id: `rfmx-tdscdma-cvi`
- source_path: `cvirfmxtdscdma_abortmeasurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-cvi/raw/resource/enus/cvirfmxtdscdma_abortmeasurements.html
- document_id: `rfmx-tdscdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA_AbortMeasurements

int32 __stdcall RFmxTDSCDMA_AbortMeasurements (niRFmxInstrHandle instrumentHandle,
 char selectorString[]);

#### Purpose

Stops the acquisition and measurements associated with the signal instance that you specify in the **selectorString** parameter. The acquisition and measurements were previously initiated by the [RFmxTDSCDMA_Initiate](/csh?topicname=rfmxtdscdmacvi/cvirfmxtdscdma_initiate.html) function or measurement read functions. 
Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxTDSCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-tdscdma-cvi path=cvirfmxtdscdma_modaccfetchdataevm.html language=enus -->
## TOPIC 00003: RFmxTDSCDMA_ModAccFetchDataEVM

- bundle_id: `rfmx-tdscdma-cvi`
- source_path: `cvirfmxtdscdma_modaccfetchdataevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-cvi/raw/resource/enus/cvirfmxtdscdma_modaccfetchdataevm.html
- document_id: `rfmx-tdscdma-cvi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA_ModAccFetchDataEVM

int32 __stdcall RFmxTDSCDMA_ModAccFetchDataEVM (niRFmxInstrHandle instrumentHandle,
 char selectorString[],
 float64 timeout,
 float64* RMSDataEVM,
 float64* peakDataEVM,
 float64* dataRho,
 float64* RMSDataMagnitudeError,
 float64* RMSDataPhaseError);

#### Purpose

Returns the EVM measurement of the data channel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| instrumentHandle | niRFmxInstrHandle | Specifies the instrument session. The RFmx driver obtains this parameter from the RFmxTDSCDMA_Initialize function. |
| selectorString | char[] | Specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxTDSCDMA_BuildSignalString function to build the selector string. |
| timeout | float64 | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |
| Output |  |  |
| Name | Type | Description |
| RMSDataEVM | float64* | Returns the RMS of the data EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |
| peakDataEVM | float64* | Returns the peak data EVM among all active time slots and averaging iterations. This value is expressed as a percentage. |
| dataRho | float64* | Returns the data rho value, averaged over all active time slots and all averaging iterations. |
| RMSDataMagnitudeError | float64* | Returns the RMS of the data magnitude error, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |
| RMSDataPhaseError | float64* | Returns the RMS of the data phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the RFmxTDSCDMA_GetError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-tdscdma-cvi path=rfmxtdscdma_attr_modacc_results_data_field_2_power.html language=enus -->
## TOPIC 00004: RFMXTDSCDMA_ATTR_MODACC_RESULTS_DATA_FIELD_2_POWER

- bundle_id: `rfmx-tdscdma-cvi`
- source_path: `rfmxtdscdma_attr_modacc_results_data_field_2_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-cvi/raw/resource/enus/rfmxtdscdma_attr_modacc_results_data_field_2_power.html
- document_id: `rfmx-tdscdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXTDSCDMA_ATTR_MODACC_RESULTS_DATA_FIELD_2_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxTDSCDMA_GetAttributeF64 |
| Description: | Returns the data field 2 power, averaged over all measured active time slots. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxTDSCDMA_ModAccGetResultsDataField2Power |

<!--NI_TOPIC bundle=rfmx-tdscdma-cvi path=rfmxtdscdma_attr_modacc_results_data_rho.html language=enus -->
## TOPIC 00005: RFMXTDSCDMA_ATTR_MODACC_RESULTS_DATA_RHO

- bundle_id: `rfmx-tdscdma-cvi`
- source_path: `rfmxtdscdma_attr_modacc_results_data_rho.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-cvi/raw/resource/enus/rfmxtdscdma_attr_modacc_results_data_rho.html
- document_id: `rfmx-tdscdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXTDSCDMA_ATTR_MODACC_RESULTS_DATA_RHO

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxTDSCDMA_GetAttributeF64 |
| Description: | Returns the data rho value, averaged over all active time slots and all averaging iterations. You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Get Function: RFmxTDSCDMA_ModAccGetResultsDataRho |

<!--NI_TOPIC bundle=rfmx-tdscdma-cvi path=rfmxtdscdma_attr_modacc_results_detected_channelization_code.html language=enus -->
## TOPIC 00006: RFMXTDSCDMA_ATTR_MODACC_RESULTS_DETECTED_CHANNELIZATION_CODE

- bundle_id: `rfmx-tdscdma-cvi`
- source_path: `rfmxtdscdma_attr_modacc_results_detected_channelization_code.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-cvi/raw/resource/enus/rfmxtdscdma_attr_modacc_results_detected_channelization_code.html
- document_id: `rfmx-tdscdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXTDSCDMA_ATTR_MODACC_RESULTS_DETECTED_CHANNELIZATION_CODE

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxTDSCDMA_GetAttributeI32 |
| Description: | Returns the channelization code of the selected channel within the set of active channels. If the averaging is enabled, this attribute refers to the last averaging iteration. Use 'channel(n)' as the selector string to read this result. Get Function: RFmxTDSCDMA_ModAccGetResultsDetectedChannelizationCode |

<!--NI_TOPIC bundle=rfmx-tdscdma-cvi path=rfmxtdscdma_attr_sem_results_lower_offset_absolute_peak_power.html language=enus -->
## TOPIC 00007: RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmx-tdscdma-cvi`
- source_path: `rfmxtdscdma_attr_sem_results_lower_offset_absolute_peak_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-cvi/raw/resource/enus/rfmxtdscdma_attr_sem_results_lower_offset_absolute_peak_power.html
- document_id: `rfmx-tdscdma-cvi`
- page_type: `leaf`
- content_type: ``

RFMXTDSCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxTDSCDMA_GetAttributeF64 |
| Description: | Returns the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxTDSCDMA_SEMGetResultsLowerOffsetAbsolutePeakPower |
