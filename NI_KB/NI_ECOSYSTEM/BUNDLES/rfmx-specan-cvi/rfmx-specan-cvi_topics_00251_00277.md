# NI DOCUMENT BUNDLE: rfmx-specan-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-specan-cvi start=251 end=277 -->
<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_frequency_resolution.html language=enus -->
## TOPIC 00251: RFMXSPECAN_ATTR_SEM_RESULTS_FREQUENCY_RESOLUTION

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_frequency_resolution.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_frequency_resolution.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_FREQUENCY_RESOLUTION

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the frequency bin spacing of the spectrum acquired by the measurement. This value is expressed in Hz. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_SEMGetResultsFrequencyResolution |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_lower_offset_margin_frequency.html language=enus -->
## TOPIC 00252: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_lower_offset_margin_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_lower_offset_margin_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsLowerOffsetMarginFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_lower_offset_margin_relative_power.html language=enus -->
## TOPIC 00253: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_lower_offset_margin_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_lower_offset_margin_relative_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the power at which the margin occurred in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. This value is expressed in dB. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsLowerOffsetMarginRelativePower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_lower_offset_measurement_status.html language=enus -->
## TOPIC 00254: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_lower_offset_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_lower_offset_measurement_status.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeI32 |
| Description: | Indicates the lower offset segment measurement status based on measurement limits and the fail criteria that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsLowerOffsetMeasurementStatus |
| Values: | RFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL (0)Indicates that the measurement has failed. RFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS (1)Indicates that the measurement has passed. |
| RFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL (0) | Indicates that the measurement has failed. |
| RFMXSPECAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS (1) | Indicates that the measurement has passed. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_lower_offset_peak_frequency.html language=enus -->
## TOPIC 00255: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_lower_offset_peak_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_lower_offset_peak_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsLowerOffsetPeakFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_lower_offset_peak_relative_power.html language=enus -->
## TOPIC 00256: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_RELATIVE_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_lower_offset_peak_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_lower_offset_peak_relative_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the peak power measured in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_INTEGRATION, the reference carrier power is the total power in the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_PEAK, the reference carrier power is the peak power in the reference carrier. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsLowerOffsetPeakRelativePower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_lower_offset_power_reference_carrier.html language=enus -->
## TOPIC 00257: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_POWER_REFERENCE_CARRIER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_lower_offset_power_reference_carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_lower_offset_power_reference_carrier.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_POWER_REFERENCE_CARRIER

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeI32 |
| Description: | Returns the index of the carrier that was used as the power reference to define the lower (negative) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsLowerOffsetPowerReferenceCarrier |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_lower_offset_start_frequency.html language=enus -->
## TOPIC 00258: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_START_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_lower_offset_start_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_lower_offset_start_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_START_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the start frequency of the lower (negative) offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsLowerOffsetStartFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_lower_offset_stop_frequency.html language=enus -->
## TOPIC 00259: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_STOP_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_lower_offset_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_lower_offset_stop_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_STOP_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the stop frequency of the lower (negative) offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsLowerOffsetStopFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_lower_offset_total_absolute_power.html language=enus -->
## TOPIC 00260: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_TOTAL_ABSOLUTE_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_lower_offset_total_absolute_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_lower_offset_total_absolute_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_TOTAL_ABSOLUTE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the power measured in the lower (negative) offset segment. The power is reported in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM, and in dBm/Hz when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsLowerOffsetTotalAbsolutePower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_total_carrier_power.html language=enus -->
## TOPIC 00261: RFMXSPECAN_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_total_carrier_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_total_carrier_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the total integrated power, in dBm, of all the enabled carriers measured when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM. Returns the power spectral density, in dBm/Hz, when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Get Function: RFmxSpecAn_SEMGetResultsTotalCarrierPower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_upper_offset_peak_frequency.html language=enus -->
## TOPIC 00262: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_upper_offset_peak_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_upper_offset_peak_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsUpperOffsetPeakFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_upper_offset_power_reference_carrier.html language=enus -->
## TOPIC 00263: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_upper_offset_power_reference_carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_upper_offset_power_reference_carrier.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER

| Data Type: | int32 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeI32 |
| Description: | Returns the index of the carrier that was used as the power reference to define the upper (positive) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsUpperOffsetPowerReferenceCarrier |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_upper_offset_stop_frequency.html language=enus -->
## TOPIC 00264: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_STOP_FREQUENCY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_upper_offset_stop_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_upper_offset_stop_frequency.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_STOP_FREQUENCY

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the stop frequency of the upper (positive) offset segment. This value is expressed in Hz. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsUpperOffsetStopFrequency |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_results_upper_offset_total_relative_power.html language=enus -->
## TOPIC 00265: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_RELATIVE_POWER

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_results_upper_offset_total_relative_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_results_upper_offset_total_relative_power.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_RELATIVE_POWER

| Data Type: | float64 |
| --- | --- |
| Access: | read only |
| Functions: | RFmxSpecAn_GetAttributeF64 |
| Description: | Returns the power measured in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_INTEGRATION, the reference carrier power is the total power in the reference carrier. When you set the RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE attribute to RFMXSPECAN_VAL_SEM_REFERENCE_TYPE_PEAK, the reference carrier power is the peak power in the reference. Use 'offset(n)' as the selector string to read this result. Get Function: RFmxSpecAn_SEMGetResultsUpperOffsetTotalRelativePower |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_sem_sweep_time_interval.html language=enus -->
## TOPIC 00266: RFMXSPECAN_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_sem_sweep_time_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_sem_sweep_time_interval.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SEM_SWEEP_TIME_INTERVAL

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the sweep time when you set the RFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTO attribute to RFMXSPECAN_VAL_SEM_SWEEP_TIME_AUTO_FALSE. This value is expressed in seconds. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0.001. Get Function: RFmxSpecAn_SEMGetSweepTimeInterval Set Function: RFmxSpecAn_SEMSetSweepTimeInterval |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_spur_range_rbw_filter_bandwidth_definition.html language=enus -->
## TOPIC 00267: RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_spur_range_rbw_filter_bandwidth_definition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_spur_range_rbw_filter_bandwidth_definition.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the bandwidth definition which you use to specify the value of the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH attribute. Use 'range(n)' as the selector string to configure or read this attribute. The default value is RFMXSPECAN_VAL_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION_3DB. Get Function: RFmxSpecAn_SpurGetRangeRBWFilterBandwidthDefinition Set Function: RFmxSpecAn_SpurSetRangeRBWFilterBandwidthDefinition |
| Values: | RFMXSPECAN_VAL_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION_3DB (0)Defines the RBW in terms of the 3dB bandwidth of the RBW filter. When you set the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_TYPE attribute to RFMXSPECAN_VAL_SPUR_RBW_FILTER_TYPE_FFT_BASED, RBW is the 3dB bandwidth of the window specified by the RFMXSPECAN_ATTR_SPUR_FFT_WINDOW attribute. RFMXSPECAN_VAL_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION_BIN_WIDTH (2)Defines the RBW in terms of the spectrum bin width computed using FFT when you set the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_TYPE attribute to FFT Based. RFMXSPECAN_VAL_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION_ENBW (3)Defines the RBW in terms of the ENBW bandwidth of the RBW filter. When you set the Spur RBW Filter Type attribute to FFT Based, RBW is the ENBW bandwidth of the window specified by the RFMXSPECAN_ATTR_SPUR_FFT_WINDOW attribute. |
| RFMXSPECAN_VAL_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION_3DB (0) | Defines the RBW in terms of the 3dB bandwidth of the RBW filter. When you set the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_TYPE attribute to RFMXSPECAN_VAL_SPUR_RBW_FILTER_TYPE_FFT_BASED, RBW is the 3dB bandwidth of the window specified by the RFMXSPECAN_ATTR_SPUR_FFT_WINDOW attribute. |
| RFMXSPECAN_VAL_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION_BIN_WIDTH (2) | Defines the RBW in terms of the spectrum bin width computed using FFT when you set the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_TYPE attribute to FFT Based. |
| RFMXSPECAN_VAL_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION_ENBW (3) | Defines the RBW in terms of the ENBW bandwidth of the RBW filter. When you set the Spur RBW Filter Type attribute to FFT Based, RBW is the ENBW bandwidth of the window specified by the RFMXSPECAN_ATTR_SPUR_FFT_WINDOW attribute. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_spur_trace_range_index.html language=enus -->
## TOPIC 00268: RFMXSPECAN_ATTR_SPUR_TRACE_RANGE_INDEX

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_spur_trace_range_index.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_spur_trace_range_index.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_SPUR_TRACE_RANGE_INDEX

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the index of the range used to store and retrieve spurious emission (Spur) traces. This attribute is not used if you set the Spur All Traces Enabled Attribute to FALSE. When you set this attribute to -1, the measurement stores and retrieves traces for all enabled ranges. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is -1. Supported devices: PXIe-5665/5668 Get Function: RFmxSpecAn_SpurGetTraceRangeIndex Set Function: RFmxSpecAn_SpurSetTraceRangeIndex |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_trigger_delay.html language=enus -->
## TOPIC 00269: RFMXSPECAN_ATTR_TRIGGER_DELAY

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_trigger_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_trigger_delay.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_TRIGGER_DELAY

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre-trigger samples. If the delay is positive, the measurement acquires post-trigger samples. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Get Function: RFmxSpecAn_GetTriggerDelay Set Function: RFmxSpecAn_SetTriggerDelay |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_trigger_minimum_quiet_time_duration.html language=enus -->
## TOPIC 00270: RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_trigger_minimum_quiet_time_duration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_trigger_minimum_quiet_time_duration.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to RFMXSPECAN_VAL_IQ_POWER_EDGE_RISING_SLOPE, the signal is quiet below the trigger level. If you set the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to RFMXSPECAN_VAL_IQ_POWER_EDGE_FALLING_SLOPE, the signal is quiet above the trigger level. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default of this attribute is hardware dependent. Get Function: RFmxSpecAn_GetTriggerMinimumQuietTimeDuration Set Function: RFmxSpecAn_SetTriggerMinimumQuietTimeDuration |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_trigger_minimum_quiet_time_mode.html language=enus -->
## TOPIC 00271: RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_trigger_minimum_quiet_time_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_trigger_minimum_quiet_time_mode.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether the measurement computes the minimum quiet time used for triggering. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL. Get Function: RFmxSpecAn_GetTriggerMinimumQuietTimeMode Set Function: RFmxSpecAn_SetTriggerMinimumQuietTimeMode |
| Values: | RFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL (0)The minimum quiet time for triggering is the value of the RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. RFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO (1)The measurement computes the minimum quiet time used for triggering. |
| RFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL (0) | The minimum quiet time for triggering is the value of the RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |
| RFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO (1) | The measurement computes the minimum quiet time used for triggering. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_trigger_type.html language=enus -->
## TOPIC 00272: RFMXSPECAN_ATTR_TRIGGER_TYPE

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_trigger_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_trigger_type.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_TRIGGER_TYPE

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the trigger type. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is None. Get Function: RFmxSpecAn_GetTriggerType Set Function: RFmxSpecAn_SetTriggerType |
| Values: | RFMXSPECAN_VAL_TRIGGER_TYPE_NONE (0)No Reference Trigger is configured. RFMXSPECAN_VAL_TRIGGER_TYPE_DIGITAL_EDGE (1)The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXSPECAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. RFMXSPECAN_VAL_TRIGGER_TYPE_IQ_POWER_EDGE (2)The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. RFMXSPECAN_VAL_TRIGGER_TYPE_SOFTWARE (3)The Reference Trigger is not asserted until a software trigger occurs. |
| RFMXSPECAN_VAL_TRIGGER_TYPE_NONE (0) | No Reference Trigger is configured. |
| RFMXSPECAN_VAL_TRIGGER_TYPE_DIGITAL_EDGE (1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXSPECAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. |
| RFMXSPECAN_VAL_TRIGGER_TYPE_IQ_POWER_EDGE (2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. |
| RFMXSPECAN_VAL_TRIGGER_TYPE_SOFTWARE (3) | The Reference Trigger is not asserted until a software trigger occurs. |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_txp_averaging_count.html language=enus -->
## TOPIC 00273: RFMXSPECAN_ATTR_TXP_AVERAGING_COUNT

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_txp_averaging_count.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_txp_averaging_count.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_TXP_AVERAGING_COUNT

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED attribute to RFMXSPECAN_VAL_TXP_AVERAGING_ENABLED_TRUE. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 10. Get Function: RFmxSpecAn_TXPGetAveragingCount Set Function: RFmxSpecAn_TXPSetAveragingCount |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_txp_measurement_enabled.html language=enus -->
## TOPIC 00274: RFMXSPECAN_ATTR_TXP_MEASUREMENT_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_txp_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_txp_measurement_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_TXP_MEASUREMENT_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable the TXP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_FALSE. Get Function: RFmxSpecAn_TXPGetMeasurementEnabled Set Function: RFmxSpecAn_TXPSetMeasurementEnabled |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_txp_number_of_analysis_threads.html language=enus -->
## TOPIC 00275: RFMXSPECAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_txp_number_of_analysis_threads.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_txp_number_of_analysis_threads.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies the maximum number of threads used for parallelism for TXP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1. Get Function: RFmxSpecAn_TXPGetNumberOfAnalysisThreads Set Function: RFmxSpecAn_TXPSetNumberOfAnalysisThreads |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_txp_rbw_filter_bandwidth.html language=enus -->
## TOPIC 00276: RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_txp_rbw_filter_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_txp_rbw_filter_bandwidth.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTH

| Data Type: | float64 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeF64RFmxSpecAn_GetAttributeF64 |
| Description: | Specifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the signal. This value is expressed in Hz. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 100 kHz. Get Function: RFmxSpecAn_TXPGetRBWFilterBandwidth Set Function: RFmxSpecAn_TXPSetRBWFilterBandwidth |

<!--NI_TOPIC bundle=rfmx-specan-cvi path=rfmxspecan_attr_txp_threshold_enabled.html language=enus -->
## TOPIC 00277: RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED

- bundle_id: `rfmx-specan-cvi`
- source_path: `rfmxspecan_attr_txp_threshold_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-cvi/raw/resource/enus/rfmxspecan_attr_txp_threshold_enabled.html
- document_id: `rfmx-specan-cvi`
- page_type: `leaf`
- content_type: ``

RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED

| Data Type: | int32 |
| --- | --- |
| Access: | read/write |
| Functions: | RFmxSpecAn_SetAttributeI32RFmxSpecAn_GetAttributeI32 |
| Description: | Specifies whether to enable thresholding of the acquired samples to be used for the TXP measurement. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_FALSE. Get Function: RFmxSpecAn_TXPGetThresholdEnabled Set Function: RFmxSpecAn_TXPSetThresholdEnabled |
| Values: | RFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_FALSE (0)All the acquired samples are considered for the TXP measurement. RFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_TRUE (1)The samples above the threshold level specified in the RFMXSPECAN_ATTR_TXP_THRESHOLD_LEVEL attribute are considered for the TXP measurement. |
| RFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_FALSE (0) | All the acquired samples are considered for the TXP measurement. |
| RFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_TRUE (1) | The samples above the threshold level specified in the RFMXSPECAN_ATTR_TXP_THRESHOLD_LEVEL attribute are considered for the TXP measurement. |
