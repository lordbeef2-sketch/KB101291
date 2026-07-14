# NI DOCUMENT BUNDLE: ni-scope-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-scope-c-api-ref start=1 end=167 -->
<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_abort.html language=enus -->
## TOPIC 00001: niScope_Abort

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_abort.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_Abort

#### C Function Prototype

ViStatus niScope_Abort (ViSession vi);

#### Purpose

Aborts an acquisition and returns the digitizer to the Idle state. Call this function if the digitizer times out waiting for a trigger.

#### Related topics:

- NI-SCOPE Programming Flow
- Acquisition Functions

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_acquisitionstatus.html language=enus -->
## TOPIC 00002: niScope_AcquisitionStatus

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_acquisitionstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_acquisitionstatus.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_AcquisitionStatus

#### C Function Prototype

ViStatus niScope_AcquisitionStatus (ViSession vi, ViInt32* status);

#### Purpose

Returns status information about the acquisition to the **status** output parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| Output |  |  |
| Name | Type | Description |
| status | ViInt32* | Returns whether the acquisition is complete, in progress, or unknown. Defined Values NISCOPE_VAL_ACQ_COMPLETE NISCOPE_VAL_ACQ_IN_PROGRESS NISCOPE_VAL_ACQ_STATUS_UNKNOWN |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_actualrecordlength.html language=enus -->
## TOPIC 00003: niScope_ActualRecordLength

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_actualrecordlength.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_actualrecordlength.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ActualRecordLength

#### C Function Prototype

ViStatus niScope_ActualRecordLength (ViSession vi, ViInt32* recordLength);

#### Purpose

Returns the actual number of points the digitizer acquires for each channel. After configuring the digitizer for an acquisition, call this function to determine the size of the waveforms that the digitizer acquires. The value is equal to or greater than the minimum number of points specified in any of the Configure Horizontal functions.

#### Related topics:

- Sample Rate
- Coercions of Horizontal Parameters

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| Output |  |  |
| Name | Type | Description |
| recordLength | ViInt32* | Returns the actual number of points the digitizer acquires for each channel; NI-SCOPE returns the value held in the NISCOPE_ATTR_HORZ_RECORD_LENGTH attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_acquisition_type.html language=enus -->
## TOPIC 00004: NISCOPE_ATTR_ACQUISITION_TYPE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_acquisition_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_acquisition_type.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_ACQUISITION_TYPE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niScope_ConfigureAcquisition |

#### Description

Specifies how the oscilloscope acquires data and fills the waveform record.

##### Defined Values

| NISCOPE_VAL_NORMAL (0) | Sets the oscilloscope to normal resolution mode. The oscilloscope can use real-time sampling or equivalent-time sampling. |
| --- | --- |
| NISCOPE_VAL_FLEXRES (1001) | Sets legacy oscilloscopes to flexible resolution mode, if supported. |
| NISCOPE_VAL_DDC (1002) | Sets legacy oscilloscopes to DDC mode, if supported. To use DDC mode for the PXI/PCI-5142 or PXIe-5622, set this attribute to NISCOPE_VAL_NORMAL and set the NISCOPE_ATTR_DDC_ENABLED attribute to VI_TRUE. |

#### Related topics:

- Acquisition Functions

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_advance_trigger_terminal_name.html language=enus -->
## TOPIC 00005: NISCOPE_ATTR_ADVANCE_TRIGGER_TERMINAL_NAME

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_advance_trigger_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_advance_trigger_terminal_name.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_ADVANCE_TRIGGER_TERMINAL_NAME

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R | N/A | None | N/A |

#### Description

Returns the fully qualified name for the Advance Trigger terminal.

You can use this terminal as the source for a trigger.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_bandwidth.html language=enus -->
## TOPIC 00006: NISCOPE_ATTR_BANDWIDTH

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_bandwidth.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_BANDWIDTH

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | None |

#### Description

Specifies the bandwidth of the channel. Express this value as the frequency (in hertz) 
at which the input circuitry attenuates the input signal by 3 dB.

|  | Note This attribute is obsolete. Use NISCOPE_ATTR_MAX_INPUT_FREQUENCY for future programs. |
| --- | --- |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_binary_sample_width.html language=enus -->
## TOPIC 00007: NISCOPE_ATTR_BINARY_SAMPLE_WIDTH

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_binary_sample_width.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_binary_sample_width.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_BINARY_SAMPLE_WIDTH

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Indicates the bit width of the binary data in the acquired waveform, which is useful for 
determining which Binary Fetch function to use. Compare to [NISCOPE_ATTR_RESOLUTION](cviniscope_attr_resolution.html).

To configure the device to store samples with a lower resolution than the native resolution, 
set this attribute to the desired binary width. This process can be useful for streaming at faster speeds 
at the cost of resolution. The least significant bits are lost with this configuration.

##### Defined Values

8, 16, 32

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_exported_sample_clock_output_terminal.html language=enus -->
## TOPIC 00008: NISCOPE_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_exported_sample_clock_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_exported_sample_clock_output_terminal.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niScope_ExportSignal |

#### Description

Exports the sample clock to the specified terminal.

##### Defined Values

| NISCOPE_VAL_NO_SOURCE | ("VAL_NO_SOURCE") |
| --- | --- |
| NISCOPE_VAL_RTSI_0 | ("VAL_RTSI_0") |
| NISCOPE_VAL_RTSI_1 | ("VAL_RTSI_1") |
| NISCOPE_VAL_RTSI_2 | ("VAL_RTSI_2") |
| NISCOPE_VAL_RTSI_3 | ("VAL_RTSI_3") |
| NISCOPE_VAL_RTSI_4 | ("VAL_RTSI_4") |
| NISCOPE_VAL_RTSI_5 | ("VAL_RTSI_5") |
| NISCOPE_VAL_RTSI_6 | ("VAL_RTSI_6") |
| NISCOPE_VAL_PXI_STAR | ("VAL_PXI_STAR") |
| NISCOPE_VAL_PFI_0 | ("VAL_PFI_0") |
| NISCOPE_VAL_PFI_1 | ("VAL_PFI_1") |
| NISCOPE_VAL_CLK_OUT | ("VAL_CLK_OUT") |

#### Related topics:

- Sample Clock
- NI-TClk Overview
- Reference Clock/Phase-Lock Loop

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_fetch_interleaved_data.html language=enus -->
## TOPIC 00009: NISCOPE_ATTR_FETCH_INTERLEAVED_DATA

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_fetch_interleaved_data.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_fetch_interleaved_data.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_FETCH_INTERLEAVED_DATA

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether to interleave I and Q data retrieved from the IF digitizer in a single array or to retrieve two separate arrays, one for I data and another for Q data.

Default value: VI_FALSE

| VI_TRUE | Retrieves a single array of alternating I and Q values. The resulting array is twice the size of the actual record length. |
| --- | --- |
| VI_FALSE | Retrieves two arrays, one for I values and another for Q values. |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_fetch_num_records.html language=enus -->
## TOPIC 00010: NISCOPE_ATTR_FETCH_NUM_RECORDS

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_fetch_num_records.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_fetch_num_records.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_FETCH_NUM_RECORDS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Number of records to fetch. Use –1 to fetch all configured records.

Default Value: –1

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_flex_fir_antialias_filter_type.html language=enus -->
## TOPIC 00011: NISCOPE_ATTR_FLEX_FIR_ANTIALIAS_FILTER_TYPE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_flex_fir_antialias_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_flex_fir_antialias_filter_type.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_FLEX_FIR_ANTIALIAS_FILTER_TYPE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | Channel | None | None |

#### Description

The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter. 
Use this attribute to select from several types of filters to achieve desired filtering characteristics. For most applications, the default value of this property is recommended. The other available filters are useful for optimizing settling time measurements of step responses.

Default Value: NISCOPE_VAL_48_TAP_STANDARD

##### Defined Values

|  | Note Settling time values refer to the FIR filter only and do not take into account settling time caused by the analog front end. Refer to the NI PXI-5922 Specifications for combined digital and analog settling times. |
| --- | --- |

| NISCOPE_VAL_48_TAP_STANDARD (0) | This filter is optimized for alias protection and frequency-domain flatness. Alias protection: ranges from 80 dB to 100 dB depending on sample rate Settling time: within 14 samples from a 50% vertical trigger point Cutoff frequency: 0.43 × sample rate Flatness: Ripple ranges from 0.005 dB to 0.120 dB depending of selected sample rate (refer to the NI PXI-5922 Specifications for more information) Rise time: Approximately 0.75/(sample rate) |
| --- | --- |
| NISCOPE_VAL_48_TAP_HANNING (1) | This filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the signal-to-noise ratio (SNR). Settling time: within 14 samples from a 50% vertical trigger point Cutoff frequency: 0.030 × sample rate Flatness: 0 to –3 dB within cutoff frequency Rise time: 11.6/(sample rate) |
| NISCOPE_VAL_16_TAP_HANNING (2) | This filter is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR. Settling time: 6 samples from a 50% vertical trigger point Cutoff frequency: 0.08 × sample rate Flatness: 0 to –3 dB within cutoff frequency Rise time: 7.7/(sample rate) |
| NISCOPE_VAL_8_TAP_HANNING (3) | This filter is optimized for the lowest possible bandwidth for an 8 tap filter and maximizes the SNR. Settling time: 4 samples from a 50% vertical trigger point Cutoff frequency: 0.15 × sample rate Flatness: 0 to –3 dB within cutoff frequency Rise time: 3.9/(sample rate) |

#### Related topics:

- Aliasing
- FIR Filters

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_fractional_resample_enabled.html language=enus -->
## TOPIC 00012: NISCOPE_ATTR_FRACTIONAL_RESAMPLE_ENABLED

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_fractional_resample_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_fractional_resample_enabled.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_FRACTIONAL_RESAMPLE_ENABLED

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Enables the onboard signal processing block that resamples the input waveform to the desired sample rate.

| Default Value: | VI_FALSE |
| --- | --- |
| Valid Values: | VI_TRUE or VI_FALSE |

#### Related topics:

- Frequency Domain Fundamentals

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_glitch_polarity.html language=enus -->
## TOPIC 00013: NISCOPE_ATTR_GLITCH_POLARITY

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_glitch_polarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_glitch_polarity.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_GLITCH_POLARITY

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niScope_ConfigureTriggerGlitch |

#### Description

Specifies the polarity of pulses that trigger the oscilloscope for glitch triggering.

Default Value: NISCOPE_VAL_GLITCH_POSITIVE

##### Defined Values

| NISCOPE_VAL_GLITCH_POSITIVE | (1) | The oscilloscope triggers on pulses of positive polarity relative to the trigger threshold. |
| --- | --- | --- |
| NISCOPE_VAL_GLITCH_NEGATIVE | (2) | The oscilloscope triggers on pulses of negative polarity relative to the trigger threshold. |
| NISCOPE_VAL_GLITCH_EITHER | (3) | The oscilloscope triggers on pulses of either positive or negative polarity. |

#### Related topics:

- Glitch Triggers

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_glitch_width.html language=enus -->
## TOPIC 00014: NISCOPE_ATTR_GLITCH_WIDTH

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_glitch_width.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_glitch_width.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_GLITCH_WIDTH

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | niScope_ConfigureTriggerGlitch |

#### Description

Specifies the glitch duration, in seconds.

The oscilloscope triggers when it detects a pulse of duration either less than or greater than this value depending on the value of the [NISCOPE_ATTR_GLITCH_CONDITION](cviniscope_attr_glitch_condition.html) attribute.

Default Value: 0.0

#### Related topics:

- Glitch Triggers

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_horz_min_num_pts.html language=enus -->
## TOPIC 00015: NISCOPE_ATTR_HORZ_MIN_NUM_PTS

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_horz_min_num_pts.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_horz_min_num_pts.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_HORZ_MIN_NUM_PTS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the minimum number of points you require in the waveform record for each channel. NI-SCOPE uses the value you 
specify to configure the record length that the digitizer uses for waveform acquisition.
 [NISCOPE_ATTR_HORZ_RECORD_LENGTH](cviniscope_attr_horz_record_length.html) returns the 
 actual record length.

Valid Values: 1 – available onboard memory

#### Related topics:

- Coercions of Horizontal Parameters

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_horz_num_records.html language=enus -->
## TOPIC 00016: NISCOPE_ATTR_HORZ_NUM_RECORDS

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_horz_num_records.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_horz_num_records.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_HORZ_NUM_RECORDS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the number of records to acquire. Can be used for multirecord acquisitions and single record 
acquisitions. Setting this attribute to 1 indicates a single record 
acquisition.

#### Related topics:

- Making Multiple-Record Acquisitions

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_horz_record_length.html language=enus -->
## TOPIC 00017: NISCOPE_ATTR_HORZ_RECORD_LENGTH

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_horz_record_length.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_horz_record_length.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_HORZ_RECORD_LENGTH

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | niScope_ActualRecordLength |

#### Description

Returns the actual number of points the digitizer acquires for each channel.
 The value is equal to or greater than the minimum number of points you specify with 
 [NISCOPE_ATTR_HORZ_MIN_NUM_PTS](cviniscope_attr_horz_min_num_pts.html).

Allocate a ViReal64 array of this size or greater to pass as the WaveformArray parameter of the Read and 
 Fetch functions. This attribute is only valid after a call to the one of the Configure Horizontal 
 functions. The value is equal to or greater than the minimum number of points you specify in [niScope_ConfigureHorizontalTiming](cviniscope_configurehorizontaltiming.html) functions.

#### Related topics:

- Coercions of Horizontal Parameters

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_horz_sample_rate.html language=enus -->
## TOPIC 00018: NISCOPE_ATTR_HORZ_SAMPLE_RATE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_horz_sample_rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_horz_sample_rate.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_HORZ_SAMPLE_RATE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | RO | N/A | None | niScope_SampleRate |

#### Description

Returns the effective sample rate using the current configuration. This attribute is only valid after a call to the one of the Configure Horizontal functions.

Units: hertz (Samples / Second)

#### Related topics:

- Sample Clock

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_horz_time_per_record.html language=enus -->
## TOPIC 00019: NISCOPE_ATTR_HORZ_TIME_PER_RECORD

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_horz_time_per_record.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_horz_time_per_record.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_HORZ_TIME_PER_RECORD

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies the length of time (in seconds) that corresponds to the record length. This attribute is invalid when the device is configured to use an external sample clock timebase. This attribute is also invalid when a DDC is enabled. When both NISCOPE_ATTR_HORZ_TIME_PER_RECORD and NISCOPE_ATTR_MIN_SAMPLE_RATE are set, the attribute that was set first is ignored.

Units: Seconds

#### Related topics:

- Coercions of Horizontal Parameters

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_input_clock_source.html language=enus -->
## TOPIC 00020: NISCOPE_ATTR_INPUT_CLOCK_SOURCE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_input_clock_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_input_clock_source.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_INPUT_CLOCK_SOURCE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niScope_ConfigureClock |

#### Description

Specifies the input source for the PLL reference clock.

##### Defined Values

| NISCOPE_VAL_NO_SOURCE | ("VAL_NO_SOURCE") |
| --- | --- |
| NISCOPE_VAL_PFI_1 | ("VAL_PFI_1") |
| NISCOPE_VAL_PFI_2 | ("VAL_PFI_2") |
| NISCOPE_VAL_EXTERNAL | ("VAL_EXTERNAL") |
| NISCOPE_VAL_CLK_IN | ("VAL_CLK_IN") |
| NISCOPE_VAL_PXI_CLOCK | ("VAL_PXI_CLOCK") |
| NISCOPE_VAL_RTSI_CLOCK | ("VAL_RTSI_CLOCK") |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_input_impedance.html language=enus -->
## TOPIC 00021: NISCOPE_ATTR_INPUT_IMPEDANCE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_input_impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_input_impedance.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_INPUT_IMPEDANCE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | niScope_ConfigureChanCharacteristics |

#### Description

Specifies the input impedance for the channel in Ohms.

##### Defined Values

NISCOPE_VAL_50_OHMS (50)

NISCOPE_VAL_1_MEG_OHM (1000000)

#### Related topics:

- Impedance and Impedance Matching

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_instrument_firmware_revision.html language=enus -->
## TOPIC 00022: NISCOPE_ATTR_INSTRUMENT_FIRMWARE_REVISION

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_instrument_firmware_revision.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_instrument_firmware_revision.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_INSTRUMENT_FIRMWARE_REVISION

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

A string that contains the firmware revision information for the instrument.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_instrument_manufacturer.html language=enus -->
## TOPIC 00023: NISCOPE_ATTR_INSTRUMENT_MANUFACTURER

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_instrument_manufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_instrument_manufacturer.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_INSTRUMENT_MANUFACTURER

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

A string that contains the name of the instrument manufacturer.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_instrument_model.html language=enus -->
## TOPIC 00024: NISCOPE_ATTR_INSTRUMENT_MODEL

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_instrument_model.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_instrument_model.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_INSTRUMENT_MODEL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

A string that contains the model number of the current instrument.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_interchange_check.html language=enus -->
## TOPIC 00025: NISCOPE_ATTR_INTERCHANGE_CHECK

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_interchange_check.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_interchange_check.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_INTERCHANGE_CHECK

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

NI-SCOPE does not generate interchange warnings and therefore ignores this attribute.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_interleaving_offset_correction_enabled.html language=enus -->
## TOPIC 00026: NISCOPE_ATTR_BANDPASS_FILTER_ENABLED

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_interleaving_offset_correction_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_interleaving_offset_correction_enabled.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_INTERLEAVING_OFFSET_CORRECTION_ENABLED

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | Channel | None | None |

#### Description

Enables the interleaving offset correction on the specified channel.

|  | Note If disabled, warranted specifications are not guaranteed. |
| --- | --- |

| Default Value: | VI_TRUE |
| --- | --- |
| Valid Values: | VI_TRUE or VI_FALSE |

#### Related topics:

- Timed Interleaved Sampling

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_logical_name.html language=enus -->
## TOPIC 00027: NISCOPE_ATTR_LOGICAL_NAME

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_logical_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_logical_name.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_LOGICAL_NAME

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

A string containing the logical name you specified when opening the current IVI session. You can pass a logical name to [niScope_Init](cviniscope_init.html) or [niScope_InitWithOptions](cviniscope_initwithoptions.html). The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_max_ris_rate.html language=enus -->
## TOPIC 00028: NISCOPE_ATTR_MAX_RIS_RATE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_max_ris_rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_max_ris_rate.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MAX_RIS_RATE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | RO | N/A | None | None |

#### Description

Returns the maximum sample rate in RIS mode in Hz.

#### Related topics:

- Sampling Methods
- Equivalent-Time Sampling and Random Interleaved Sampling

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_array_gain.html language=enus -->
## TOPIC 00029: NISCOPE_ATTR_MEAS_ARRAY_GAIN

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_array_gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_array_gain.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_ARRAY_GAIN

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | None |

#### Description

Every element of an array is multiplied by this scalar value during the Array Gain 
measurement.

Default Value: 1.0

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_filter_order.html language=enus -->
## TOPIC 00030: NISCOPE_ATTR_MEAS_FILTER_ORDER

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_filter_order.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_filter_order.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_FILTER_ORDER

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | Channel | None | None |

#### Description

Specifies the order of an IIR filter. All positive integers are valid.

Default Value: 2

#### Related topics:

- Reference Levels
- Measuring Reference-Level Crossings

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_filter_ripple.html language=enus -->
## TOPIC 00031: NISCOPE_ATTR_MEAS_FILTER_RIPPLE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_filter_ripple.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_filter_ripple.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_FILTER_RIPPLE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | None |

#### Description

Specifies the amount of passband ripple in decibels (positive values) 

for Chebyshev filters.

Default Value: 0.1 dB

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_filter_type.html language=enus -->
## TOPIC 00032: NISCOPE_ATTR_MEAS_FILTER_TYPE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_filter_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_filter_type.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_FILTER_TYPE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | Channel | None | None |

#### Description

Specifies the type of filter, for both IIR and FIR filters.

Default Value: Lowpass

##### Defined Values

NISCOPE_VAL_MEAS_LOWPASS (0)

NISCOPE_VAL_MEAS_HIGHPASS (1)

NISCOPE_VAL_MEAS_BANDPASS (2)

NISCOPE_VAL_MEAS_BANDSTOP (3)

#### Related topics:

- Reference Levels
- Measuring Reference-Level Crossings

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_filter_width.html language=enus -->
## TOPIC 00033: NISCOPE_ATTR_MEAS_FILTER_WIDTH

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_filter_width.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_filter_width.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_FILTER_WIDTH

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | None |

#### Description

Specifies the width of bandpass and bandstop type filters in hertz. 
The cutoff frequencies occur at [NISCOPE_ATTR_MEAS_FILTER_CENTER_FREQ](cviniscope_attr_meas_filter_center_freq.html) ±one-half width.

Default Value: 1.0e3 Hz

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_other_channel.html language=enus -->
## TOPIC 00034: NISCOPE_ATTR_MEAS_OTHER_CHANNEL

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_other_channel.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_other_channel.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_OTHER_CHANNEL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | Channel | None | None |

#### Description

Specifies the second channel for two-channel measurements. If processing steps are 
registered with this channel, the processing is done before the waveform is used in a two-channel 
measurement.

Default Value: 0

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_percentage_method.html language=enus -->
## TOPIC 00035: NISCOPE_ATTR_MEAS_PERCENTAGE_METHOD

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_percentage_method.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_percentage_method.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_PERCENTAGE_METHOD

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | Channel | None | None |

#### Description

Specifies the method used to map percentage reference units to voltages for the reference.

Default Value: NISCOPE_VAL_MEAS_BASE_TOP

##### Defined Values

NISCOPE_VAL_MEAS_LOW_HIGH

NISCOPE_VAL_MEAS_MIN_MAX

NISCOPE_VAL_MEAS_BASE_TOP

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_time_histogram_high_time.html language=enus -->
## TOPIC 00036: NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_TIME

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_time_histogram_high_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_time_histogram_high_time.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_TIME

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | None |

#### Description

Specifies the highest time value included in the multiple acquisition time histogram. The units are always seconds.

Default Value: 5.0e-4 seconds

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_time_histogram_high_volts.html language=enus -->
## TOPIC 00037: NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_VOLTS

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_time_histogram_high_volts.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_time_histogram_high_volts.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_VOLTS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | None |

#### Description

Specifies the highest voltage value included in the multiple-acquisition time histogram.

Default Value: 10.0 V

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_time_histogram_low_time.html language=enus -->
## TOPIC 00038: NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_TIME

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_time_histogram_low_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_time_histogram_low_time.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_TIME

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | None |

#### Description

Specifies the lowest time value n seconds) included in the multiple-acquisition time histogram.

Default Value: –5.0e-4 seconds

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_time_histogram_low_volts.html language=enus -->
## TOPIC 00039: NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_VOLTS

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_time_histogram_low_volts.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_time_histogram_low_volts.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_VOLTS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | None |

#### Description

Specifies the lowest voltage value included in the multiple acquisition time histogram.

Default Value: –10.0 V

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_time_histogram_size.html language=enus -->
## TOPIC 00040: NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_SIZE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_time_histogram_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_time_histogram_size.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_SIZE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | Channel | None | None |

#### Description

Determines the multiple acquisition voltage histogram size. The size is set during the first call to a time histogram measurement after clearing the measurement history with [niScope_ClearWaveformMeasurementStats](cviniscope_clearwaveformmeasurementstats.html).

Default Value: 256

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_meas_voltage_histogram_high_volts.html language=enus -->
## TOPIC 00041: NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_meas_voltage_histogram_high_volts.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_meas_voltage_histogram_high_volts.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | None |

#### Description

Specifies the highest voltage value included in the multiple acquisition voltage histogram.

Default Value: 10.0 V

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_onboard_memory_size.html language=enus -->
## TOPIC 00042: NISCOPE_ATTR_ONBOARD_MEMORY_SIZE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_onboard_memory_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_onboard_memory_size.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_ONBOARD_MEMORY_SIZE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the total combined amount of onboard memory (that is, memory size) for all channels in bytes.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_oscillator_phase_dac_value.html language=enus -->
## TOPIC 00043: NISCOPE_ATTR_OSCILLATOR_PHASE_DAC_VALUE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_oscillator_phase_dac_value.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_oscillator_phase_dac_value.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_OSCILLATOR_PHASE_DAC_VALUE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Gets or sets the binary phase DAC value that controls the delay added to the phase-locked loop (PLL) of the sample clock.

**Valid Values**: [0, 65535]

**Default Value**: " "

Use this attribute when performing manual adjustment to correct for skew and jitter between oscilloscopes synchronized with NI-TClk.

1. Apply time offset with the niScope_AdjustSampleClockRelativeDelay function.
2. Use this attribute to convert the time offset into a value that can apply the manual adjustment across sessions and improve synchronization repeatability.

For details on performing manual adjustment, refer to [Improving NI-TClk Synchronization of Oscilloscopes with Manual Adjustment](/csh?topicname=digitizers/ni-tclk-manual-adjustment-oscilloscopes.html).

|  | Note If this value is set, sample clock adjust and TClk cannot do any sub-sample adjustment of the timebase sample clock. |
| --- | --- |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_output_clock_source.html language=enus -->
## TOPIC 00044: NISCOPE_ATTR_OUTPUT_CLOCK_SOURCE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_output_clock_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_output_clock_source.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_OUTPUT_CLOCK_SOURCE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niScope_ConfigureClock |

#### Description

Exports the reference clock to the specified output terminal.

##### Defined Values

NISCOPE_VAL_NO_SOURCE

NISCOPE_VAL_RTSI_CLOCK

NISCOPE_VAL_PFI_0

NISCOPE_VAL_PFI_1

NISCOPE_VAL_PFI_2

NISCOPE_VAL_CLK_OUT

#### Related topics:

- Sample Clock
- NI-TClk Overview

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_overflow_error_reporting.html language=enus -->
## TOPIC 00045: NISCOPE_ATTR_OVERFLOW_ERROR_REPORTING

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_overflow_error_reporting.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_overflow_error_reporting.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_OVERFLOW_ERROR_REPORTING

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Configures error reporting when the onboard signal processing block detects an overflow in any of its stages. 
Overflows lead to clipping of the waveform.

|  | Note This attribute can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this attribute with a device that does not support OSP. |
| --- | --- |

Default Value: Warning

##### Valid Values

NISCOPE_VAL_ERROR_REPORTING_ERROR (0)—NI-SCOPE returns an error when an overflow has occurred in the OSP block.

NISCOPE_VAL_ERROR_REPORTING_WARNING (1)—NI-SCOPE returns a warning when an overflow has occurred in the OSP block.

NISCOPE_VAL_ERROR_REPORTING_DISABLED (2)—NI-SCOPE does not return an error when an overflow has occurred in the OSP block.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_p2p_data_trans_permission_addr_type.html language=enus -->
## TOPIC 00046: NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR_TYPE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_p2p_data_trans_permission_addr_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_p2p_data_trans_permission_addr_type.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR_TYPE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | Endpoint | None | None |

#### Description

Specifies the type of address returned from the 
[NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR](../scopefunc/cviniscope_attr_p2p_data_trans_permission_addr.html)
 attribute.

|  | Note This attribute can be used only with high-speed digitizers that support peer-to-peer streaming. |
| --- | --- |

Default Value: NISCOPE_VAL_ADDR_VIRTUAL

##### Defined Values

NISCOPE_VAL_ADDR_PHYSICAL (0)

NISCOPE_VAL_ADDR_VIRTUAL (1)

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_p2p_destination_window_addr.html language=enus -->
## TOPIC 00047: NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_p2p_destination_window_addr.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_p2p_destination_window_addr.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt64 | R/W | Endpoint | None | None |

#### Description

Specifies the destination for data written by the peer-to-peer endpoint. The type
 of this address is specified by the 
 [NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR_TYPE](../scopefunc/cviniscope_attr_p2p_destination_window_addr_type.html) attribute.

|  | Note This attribute can be used only with high-speed digitizers that support peer-to-peer streaming. |
| --- | --- |

##### Valid Values

A valid, non-NULL physical or virtual address.

#### Related topics:

- Peer-to-Peer Streaming

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_p2p_endpoint_size.html language=enus -->
## TOPIC 00048: NISCOPE_ATTR_P2P_ENDPOINT_SIZE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_p2p_endpoint_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_p2p_endpoint_size.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_P2P_ENDPOINT_SIZE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | Endpoint | None | None |

#### Description

Returns the size in samples of the peer-to-peer endpoint.

|  | Note This attribute can be used only with high-speed digitizers that support peer-to-peer streaming. |
| --- | --- |

#### Related topics:

- Peer-to-Peer Streaming

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_p2p_fifo_endpoint_count.html language=enus -->
## TOPIC 00049: NISCOPE_ATTR_P2P_FIFO_ENDPOINT_COUNT

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_p2p_fifo_endpoint_count.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_p2p_fifo_endpoint_count.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_P2P_FIFO_ENDPOINT_COUNT

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the number of FIFO-based peer-to-peer endpoints this device supports.

|  | Note This attribute can be used only with high-speed digitizers that support peer-to-peer streaming. |
| --- | --- |

#### Related topics:

- Peer-to-Peer Streaming

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_p2p_manual_configuration_enabled.html language=enus -->
## TOPIC 00050: NISCOPE_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_p2p_manual_configuration_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_p2p_manual_configuration_enabled.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| Boolean | R/W | Endpoint | None | None |

#### Description

Enables/disables the advanced attributes for a peer-to-peer endpoint. These attributes cannot 
be used if an endpoint is being configured by NI-P2P, or a resource
 reservation error will occur.

|  | Note This attribute can be used only with high-speed digitizers that support peer-to-peer streaming. |
| --- | --- |

#### Related topics:

- Peer-to-Peer Streaming

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_p2p_most_samples_avail_in_endpoint.html language=enus -->
## TOPIC 00051: NISCOPE_ATTR_P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_p2p_most_samples_avail_in_endpoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_p2p_most_samples_avail_in_endpoint.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | Endpoint | None | None |

#### Description

Returns the most number of samples available to stream from a peer-to-peer endpoint since the last time this attribute was read.

|  | Note This attribute can be used only with high-speed digitizers that support peer-to-peer streaming. |
| --- | --- |

#### Related topics:

- Peer-to-Peer Streaming

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_p2p_notify_message_push_addr.html language=enus -->
## TOPIC 00052: NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_p2p_notify_message_push_addr.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_p2p_notify_message_push_addr.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt64 | R/W | Endpoint | None | None |

#### Description

Specifies the address to Push Message push Value to on the event specified by the
[NISCOPE_ATTR_P2P_NOTIFY_PUSH_MESSAGE_ON](../scopefunc/cviniscope_attr_p2p_notify_push_message_on.html) attribute.

|  | Note This attribute can be used only with high-speed digitizers that support peer-to-peer streaming. |
| --- | --- |

#### Related topics:

- Peer-to-Peer Streaming

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_p2p_samples_transferred.html language=enus -->
## TOPIC 00053: NISCOPE_ATTR_P2P_SAMPLES_TRANSFERRED

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_p2p_samples_transferred.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_p2p_samples_transferred.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_P2P_SAMPLES_TRANSFERRED

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt64 | RO | Endpoint | None | None |

#### Description

Returns the number of samples transferred through the peer-to-peer endpoint since it was last reset.

|  | Note This attribute can be used only with high-speed digitizers that support peer-to-peer streaming. |
| --- | --- |

#### Related topics:

- Peer-to-Peer Streaming

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_p2p_samples_transferred_per_record.html language=enus -->
## TOPIC 00054: NISCOPE_ATTR_P2P_SAMPLES_TRANSFERRED_PER_RECORD

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_p2p_samples_transferred_per_record.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_p2p_samples_transferred_per_record.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_P2P_SAMPLES_TRANSFERRED_PER_RECORD

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | Endpoint | None | None |

#### Description

Returns the number of samples transferred per record when you set the [NISCOPE_ATTR_P2P_STREAM_RELATIVE_TO](cviniscope_attr_p2p_stream_relative_to.html) attribute to **NISCOPE_VAL_STREAM_RELATIVE_TO_REFERENCE_TRIGGER** or **NISCOPE_VAL_STREAM_RELATIVE_TO_SYNC_TRIGGER**.

|  | Note This attribute is only supported on NI 5160/5162 digitizers. |
| --- | --- |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_p2p_stream_relative_to.html language=enus -->
## TOPIC 00055: NISCOPE_ATTR_P2P_STREAM_RELATIVE_TO

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_p2p_stream_relative_to.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_p2p_stream_relative_to.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_P2P_STREAM_RELATIVE_TO

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RW | Endpoint | None | None |

#### Description

Determines which trigger peer-to-peer data is streamed relative to.

|  | Note On the NI 5122/5622, only NISCOPE_VAL_STREAM_RELATIVE_TO_START_TRIGGER is valid for this attribute. |
| --- | --- |

Default Value: NISCOPE_VAL_STREAM_RELATIVE_TO_START_TRIGGER (0)

##### Defined Values

NISCOPE_VAL_STREAM_RELATIVE_TO_START_TRIGGER (0)

NISCOPE_VAL_STREAM_RELATIVE_TO_REFERENCE_TRIGGER (1)

NISCOPE_VAL_STREAM_RELATIVE_TO_SYNC_TRIGGER (2)

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_poll_interval.html language=enus -->
## TOPIC 00056: NISCOPE_ATTR_POLL_INTERVAL

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_poll_interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_poll_interval.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_POLL_INTERVAL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the poll interval in milliseconds to use during RIS acquisitions to check whether the acquisition is complete.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_probe_attenuation.html language=enus -->
## TOPIC 00057: NISCOPE_ATTR_PROBE_ATTENUATION

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_probe_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_probe_attenuation.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_PROBE_ATTENUATION

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | niScope_ConfigureVertical |

#### Description

Specifies the probe attenuation for the input channel. For example, for a 10:1 probe, set this attribute to 10.0.

Valid Values: Any positive real number. Typical values are 1, 10, and 100.

#### Related topics:

- Probes and Their Effects

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_query_instrument_status.html language=enus -->
## TOPIC 00058: NISCOPE_ATTR_QUERY_INSTRUMENT_STATUS

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_query_instrument_status.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_query_instrument_status.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_QUERY_INSTRUMENT_STATUS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether the instrument driver queries the instrument status after each 
operation. Querying the instrument status is very useful for debugging. After you validate your 
program, you can set this attribute to VI_FALSE to disable status checking and maximize 
performance.

The instrument driver can choose to ignore status checking for particular
 attributes regardless of the setting of this attribute.
 The default value is VI_TRUE. Use [niScope_InitWithOptions](cviniscope_initwithoptions.html) 
 to override the default.

##### Defined Values

VI_TRUE

VI_FALSE

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_range_check.html language=enus -->
## TOPIC 00059: NISCOPE_ATTR_RANGE_CHECK

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_range_check.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_range_check.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_RANGE_CHECK

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether to validate attribute values and function parameters. If enabled, 
the instrument driver validates the parameters values that you pass to driver functions. Range 
checking parameters is very useful for debugging. After you validate your program, you can set this 
attribute to VI_FALSE to disable range checking and maximize performance. 
 The default value is
 VI_TRUE. Use [niScope_InitWithOptions](cviniscope_initwithoptions.html) to override the default.

##### Defined Values

VI_TRUE

VI_FALSE

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_ready_for_advance_event_output_terminal.html language=enus -->
## TOPIC 00060: NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_ready_for_advance_event_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_ready_for_advance_event_output_terminal.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niScope_ExportSignal |

#### Description

Specifies the destination for the Ready for Advance Event. When this event is asserted, the digitizer is ready to receive an advance trigger.

Refer to the device-specific documentation in the *NI High-Speed Digitizers Help*
for a list of valid destinations for your device.

##### Defined Values

| NISCOPE_VAL_RTSI_0 | ("VAL_RTSI_0") |
| --- | --- |
| NISCOPE_VAL_RTSI_1 | ("VAL_RTSI_1") |
| NISCOPE_VAL_RTSI_2 | ("VAL_RTSI_2") |
| NISCOPE_VAL_RTSI_3 | ("VAL_RTSI_3") |
| NISCOPE_VAL_RTSI_4 | ("VAL_RTSI_4") |
| NISCOPE_VAL_RTSI_5 | ("VAL_RTSI_5") |
| NISCOPE_VAL_RTSI_6 | ("VAL_RTSI_6") |
| NISCOPE_VAL_PFI_0 | ("VAL_PFI_0") |
| NISCOPE_VAL_PFI_1 | ("VAL_PFI_1") |
| NISCOPE_VAL_PFI_2 | ("VAL_PFI_2") |
| NISCOPE_VAL_PXI_STAR | ("VAL_PXI_STAR") |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_ready_for_advance_event_terminal_name.html language=enus -->
## TOPIC 00061: NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_ready_for_advance_event_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_ready_for_advance_event_terminal_name.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R | N/A | None | N/A |

#### Description

Returns the fully qualified name for the Ready for Advance Event terminal.

You can use this terminal as the source for a trigger.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_ready_for_ref_event_output_terminal.html language=enus -->
## TOPIC 00062: NISCOPE_ATTR_READY_FOR_REF_EVENT_OUTPUT_TERMINAL

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_ready_for_ref_event_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_ready_for_ref_event_output_terminal.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_READY_FOR_REF_EVENT_OUTPUT_TERMINAL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niScope_ExportSignal |

#### Description

Specifies the destination for the Ready for Reference Event.
 When this event is asserted, the digitizer is ready to receive a reference trigger.

##### Defined Values

| NISCOPE_VAL_RTSI_0 | ("VAL_RTSI_0") |
| --- | --- |
| NISCOPE_VAL_RTSI_1 | ("VAL_RTSI_1") |
| NISCOPE_VAL_RTSI_2 | ("VAL_RTSI_2") |
| NISCOPE_VAL_RTSI_3 | ("VAL_RTSI_3") |
| NISCOPE_VAL_RTSI_4 | ("VAL_RTSI_4") |
| NISCOPE_VAL_RTSI_5 | ("VAL_RTSI_5") |
| NISCOPE_VAL_RTSI_6 | ("VAL_RTSI_6") |
| NISCOPE_VAL_PFI_0 | ("VAL_PFI_0") |
| NISCOPE_VAL_PFI_1 | ("VAL_PFI_1") |
| NISCOPE_VAL_PFI_2 | ("VAL_PFI_2") |
| NISCOPE_VAL_PXI_STAR | ("VAL_PXI_STAR") |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_ready_for_start_event_terminal_name.html language=enus -->
## TOPIC 00063: NISCOPE_ATTR_READY_FOR_START_EVENT_TERMINAL_NAME

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_ready_for_start_event_terminal_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_ready_for_start_event_terminal_name.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_READY_FOR_START_EVENT_TERMINAL_NAME

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R | N/A | None | N/A |

#### Description

Returns the fully qualified name for the Ready for Start Event terminal.

You can use this terminal as the source for a trigger.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_ref_clk_rate.html language=enus -->
## TOPIC 00064: NISCOPE_ATTR_REF_CLK_RATE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_ref_clk_rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_ref_clk_rate.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_REF_CLK_RATE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

If [NISCOPE_ATTR_INPUT_CLOCK_SOURCE](cviniscope_attr_input_clock_source.html) is an external source, this attribute specifies the frequency of the input, or reference clock, to which the internal sample clock timebase is synchronized. The frequency is in hertz.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_ref_trigger_detector_location.html language=enus -->
## TOPIC 00065: NISCOPE_ATTR_REF_TRIGGER_DETECTOR_LOCATION

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_ref_trigger_detector_location.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_ref_trigger_detector_location.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_REF_TRIGGER_DETECTOR_LOCATION

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Indicates which reference trigger detection circuitry to use on the device.

|  | Note This attribute can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this attribute with a device that does not support OSP. |
| --- | --- |

Default Value: NISCOPE_VAL_ANALOG_DETECTION_CIRCUIT

##### Valid Values

NISCOPE_VAL_DDC_OUTPUT—Use the onboard signal processing logic to implement the 
reference trigger. This option detects trigger conditions by analyzing the processed digital signal.

NISCOPE_VAL_ANALOG_DETECTION_CIRCUIT—Use the hardware analog circuitry to implement 
the reference trigger. This option detects trigger conditions by analyzing the unprocessed analog signal.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_trigger_hysteresis.html language=enus -->
## TOPIC 00066: NISCOPE_ATTR_TRIGGER_HYSTERESIS

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_trigger_hysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_trigger_hysteresis.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TRIGGER_HYSTERESIS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies, in volts, the size of the hysteresis window on either side of the trigger level. The digitizer triggers when the trigger signal passes through the threshold you specify with the **level** control, has the slope you specify with the **slope** control, and passes through the hysteresis window that you specify with this attribute.

Valid Values

| Positive trigger slope | 0 ≤ Hysteresis ≤ Trigger Level + (Vertical Range / 2) - Vertical Offset |
| --- | --- |
| Negative trigger slope | 0 ≤ Hysteresis ≤ (Vertical Range / 2) + Vertical Offset - Trigger Level |

#### Related topics:

- Hysteresis Triggers

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_trigger_impedance.html language=enus -->
## TOPIC 00067: NISCOPE_ATTR_TRIGGER_IMPEDANCE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_trigger_impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_trigger_impedance.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TRIGGER_IMPEDANCE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies the input impedance for the external analog trigger channel in Ohms.

##### Defined Values

NISCOPE_VAL_50_OHMS (50)

NISCOPE_VAL_1_MEG_OHM (1000000)

##### Supported Devices

- PXIe‑5160
- PXIe‑5162

#### Related topics:

- Impedance and Impedance Matching

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_trigger_level.html language=enus -->
## TOPIC 00068: NISCOPE_ATTR_TRIGGER_LEVEL

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_trigger_level.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_trigger_level.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TRIGGER_LEVEL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | niScope_ConfigureTriggerEdge niScope_ConfigureTriggerGlitch niScope_ConfigureTriggerHysteresis niScope_ConfigureTriggerWidth |

#### Description

Specifies the voltage threshold for the trigger subsystem in volts. This attribute 
affects instrument behavior only when the [NISCOPE_ATTR_TRIGGER_TYPE](cviniscope_attr_trigger_type.html) is 
set to NISCOPE_VAL_EDGE, 
NISCOPE_VAL_HYSTERESIS, or 
 NISCOPE_VAL_WINDOW.

Valid Values: 
The values of 
the range and offset
 parameters in [niScope_ConfigureVertical](cviniscope_configurevertical.html) determine the 
 valid range for the trigger level on the channel you use as the Trigger Source. The value you pass for
 this parameter must meet the following conditions:

*Trigger Level* <= (*Vertical Range*/2) + *Vertical Offset*

*Vertical Range* >= (*–Vertical Range*/2) + *Vertical Offset*

#### Related topics:

- Edge Triggers
- Window Triggers

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_trigger_modifier.html language=enus -->
## TOPIC 00069: NISCOPE_ATTR_TRIGGER_MODIFIER

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_trigger_modifier.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_trigger_modifier.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TRIGGER_MODIFIER

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Configures whether the device automatically completes an acquisition if a trigger is not received after a period of time.

|  | Note When NISCOPE_VAL_AUTO is selected, you may need to modify the timeout on calls to fetch data to ensure that the acquisition does not time out before the auto trigger time elapses. |
| --- | --- |

##### Defined Values

NISCOPE_VAL_NO_TRIGGER_MOD (1)

NISCOPE_VAL_AUTO (2)

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_trigger_slope.html language=enus -->
## TOPIC 00070: NISCOPE_ATTR_TRIGGER_SLOPE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_trigger_slope.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_trigger_slope.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TRIGGER_SLOPE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niScope_ConfigureTriggerDigitalniScope_ConfigureTriggerEdge niScope_ConfigureTriggerHysteresis |

#### Description

Specifies whether rising or a falling edge triggers the digitizer. 
This attribute affects instrument operation only when 
[NISCOPE_ATTR_TRIGGER_TYPE](cviniscope_attr_trigger_type.html) is set to NISCOPE_VAL_EDGE_TRIGGER, 
NISCOPE_VAL_HYSTERESIS_TRIGGER, or NISCOPE_VAL_DIGITAL_TRIGGER.

##### Defined Values

NISCOPE_VAL_POSITIVE

NISCOPE_VAL_NEGATIVE

#### Related topics:

- Edge Triggers
- Window Triggers

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_trigger_source.html language=enus -->
## TOPIC 00071: NISCOPE_ATTR_TRIGGER_SOURCE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_trigger_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_trigger_source.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TRIGGER_SOURCE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niScope_ConfigureTriggerDigital niScope_ConfigureTriggerEdge niScope_ConfigureTriggerGlitch niScope_ConfigureTriggerHysteresis niScope_ConfigureTriggerRunt niScope_ConfigureTriggerVideo niScope_ConfigureTriggerWidth niScope_ConfigureTriggerWindow |

#### Description

Specifies the source the digitizer monitors for the trigger event. Trigger sources vary for each digitizer model.

##### Defined Values

"0"

"1"

"2"

"3"

"4"

"5"

"6"

"7"

NISCOPE_VAL_IMMEDIATE ("VAL_IMMEDIATE")

NISCOPE_VAL_EXTERNAL ("VAL_EXTERNAL")

NISCOPE_VAL_SW_TRIG_FUNC ("VAL_SW_TRIG_FUNC")

NISCOPE_VAL_RTSI_0 ("VAL_RTSI_0")

NISCOPE_VAL_RTSI_1 ("VAL_RTSI_1")

NISCOPE_VAL_RTSI_2 ("VAL_RTSI_2")

NISCOPE_VAL_RTSI_3 ("VAL_RTSI_3")

NISCOPE_VAL_RTSI_4 ("VAL_RTSI_4")

NISCOPE_VAL_RTSI_5 ("VAL_RTSI_5")

NISCOPE_VAL_RTSI_6 ("VAL_RTSI_6")

NISCOPE_VAL_PFI_0 ("VAL_PFI_0")

NISCOPE_VAL_PFI_1 ("VAL_PFI_1")

NISCOPE_VAL_PFI_2 ("VAL_PFI_2")

NISCOPE_VAL_PFI_3 ("VAL_PFI_3")

NISCOPE_VAL_PFI_4 ("VAL_PFI_4")

NISCOPE_VAL_PFI_5 ("VAL_PFI_5")

NISCOPE_VAL_PFI_6 ("VAL_PFI_6")

NISCOPE_VAL_PFI_7 ("VAL_PFI_7")

NISCOPE_VAL_PXI_STAR ("VAL_PXI_STAR")

#### Related topics:

- Trigger Types

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_trigger_type.html language=enus -->
## TOPIC 00072: NISCOPE_ATTR_TRIGGER_TYPE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_trigger_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_trigger_type.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TRIGGER_TYPE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the type of trigger to use.

##### Defined Values

NISCOPE_VAL_DIGITAL_TRIGGER

NISCOPE_VAL_EDGE_TRIGGER

NISCOPE_VAL_GLITCH_TRIGGER

NISCOPE_VAL_HYSTERESIS_TRIGGER

NISCOPE_VAL_IMMEDIATE_TRIGGER

NISCOPE_VAL_RUNT_TRIGGER

NISCOPE_VAL_SOFTWARE_TRIGGER

NISCOPE_VAL_TV_TRIGGER

NISCOPE_VAL_WIDTH_TRIGGER

NISCOPE_VAL_WINDOW_TRIGGER

#### Related topics:

- Trigger Types

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_trigger_window_low_level.html language=enus -->
## TOPIC 00073: NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_trigger_window_low_level.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_trigger_window_low_level.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | niScope_ConfigureTriggerWindow |

#### Description

The lower voltage threshold you want the digitizer to use for window triggering.

The digitizer triggers when the trigger signal enters or leaves the window you 
specify with this attribute and
 [NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL](cviniscope_attr_trigger_window_high_level.html).

Valid Values:
 The value you pass for this attribute must meet the following conditions:

*Low Trigger Level* <= *Vertical Range*/2 + *Vertical Offset*

*Low Trigger Level* >= (*–Vertical Range*/2) + *Vertical Offset*

*Low Trigger Level* < *High Trigger Level*

#### Related topics:

- Window Triggers

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_tv_trigger_event.html language=enus -->
## TOPIC 00074: NISCOPE_ATTR_TV_TRIGGER_EVENT

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_tv_trigger_event.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_tv_trigger_event.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TV_TRIGGER_EVENT

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niScope_ConfigureTriggerVideo |

#### Description

Specifies the condition in the video signal that causes the digitizer to trigger.

##### Defined Values

NISCOPE_VAL_TV_EVENT_FIELD1 (1)

NISCOPE_VAL_TV_EVENT_FIELD2 (2)

NISCOPE_VAL_TV_EVENT_ANY_FIELD (3)

NISCOPE_VAL_TV_EVENT_ANY_LINE (4)

NISCOPE_VAL_TV_EVENT_LINE_NUMBER (5)

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_tv_trigger_line_number.html language=enus -->
## TOPIC 00075: NISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_tv_trigger_line_number.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_tv_trigger_line_number.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niScope_ConfigureTriggerVideo |

#### Description

Specifies the line on which to trigger, if [NISCOPE_ATTR_TV_TRIGGER_EVENT](cviniscope_attr_tv_trigger_event.html) is set to NISCOPE_VAL_TV_EVENT_LINE_NUMBER. 
The valid range of the attribute depends on the signal format selected.

| Signal Format | Line Numbers |
| --- | --- |
| M-NTSC, 480i, 480p | 1 to 525 |
| BG/PAL, SECAM, 576i, 576p | 1 to 625 |
| 720p | 1 to 750 |
| 1080i,1080p | 1 to 1,125 |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_tv_trigger_polarity.html language=enus -->
## TOPIC 00076: NISCOPE_ATTR_TV_TRIGGER_POLARITY

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_tv_trigger_polarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_tv_trigger_polarity.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_TV_TRIGGER_POLARITY

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niScope_ConfigureTriggerVideo |

#### Description

Specifies whether the video signal sync is positive or negative.

##### Defined Values

NISCOPE_VAL_TV_POSITIVE (1)

NISCOPE_VAL_TV_NEGATIVE (2)

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_vertical_coupling.html language=enus -->
## TOPIC 00077: NISCOPE_ATTR_VERTICAL_COUPLING

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_vertical_coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_vertical_coupling.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_VERTICAL_COUPLING

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | Channel | None | niScope_ConfigureVertical |

#### Description

Specifies how the digitizer couples the input signal for the channel. 
When input coupling changes, the input stage takes a finite amount of time to settle.

##### Defined Values

NISCOPE_VAL_AC (0)

NISCOPE_VAL_DC (1)

NISCOPE_VAL_GND (2)

#### Related topics:

- Input Coupling

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_vertical_offset.html language=enus -->
## TOPIC 00078: NISCOPE_ATTR_VERTICAL_OFFSET

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_vertical_offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_vertical_offset.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_VERTICAL_OFFSET

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | niScope_ConfigureVertical |

#### Description

Specifies the location of the center of the range with respect to ground in volts. 
For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this attribute to 5.0 V.

|  | Note This attribute is not supported by all digitizers. Refer to the Features Supported by Device for a list of vertical offsets supported for each device. |
| --- | --- |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_vertical_range.html language=enus -->
## TOPIC 00079: NISCOPE_ATTR_VERTICAL_RANGE

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_vertical_range.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_vertical_range.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_VERTICAL_RANGE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | Yes | niScope_ConfigureVertical |

#### Description

Specifies the absolute value of the input range for a channel in volts. 
For example, to acquire a sine wave that spans between –5 and +5 V, set this attribute to 
10.0 V.

Refer to the *NI High-Speed Digitizers Help* for a list of supported vertical ranges for each device. 
If the specified range is not supported by a device, the value is coerced up to the next valid range.

#### Related topics:

- Coercions of Vertical Parameters

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_attr_width_polarity.html language=enus -->
## TOPIC 00080: NISCOPE_ATTR_WIDTH_POLARITY

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_attr_width_polarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_attr_width_polarity.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISCOPE_ATTR_WIDTH_POLARITY

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niScope_ConfigureTriggerWidth |

#### Description

Specifies the polarity of pulses that trigger the oscilloscope for width triggering.

Default Value: NISCOPE_VAL_POSITIVE

##### Defined Values

| NISCOPE_VAL_WIDTH_POSITIVE | (1) | The oscilloscope triggers on pulses of positive polarity relative to the trigger threshold. |
| --- | --- | --- |
| NISCOPE_VAL_WIDTH_NEGATIVE | (2) | The oscilloscope triggers on pulses of negative polarity relative to the trigger threshold. |
| NISCOPE_VAL_WIDTH_EITHER | (3) | The oscilloscope triggers on pulses of either positive or negative polarity. |

#### Related topics:

- Width Triggers

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_cablesensesignalstart.html language=enus -->
## TOPIC 00081: niScope_CableSenseSignalStart

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_cablesensesignalstart.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_cablesensesignalstart.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CableSenseSignalStart

#### C Function Prototype

ViStatus niScope_CableSenseSignalStart
 (ViSession Instrument_Handle);

#### Purpose

Generates the CableSense signal on all channels of an oscilloscope for which the signal is enabled, as configured by the [NISCOPE_ATTR_CABLE_SENSE_MODE](/csh?topicname=scopefunc/cviniscope_attr_cable_sense_mode.html) attribute.

|  | Note The input impedance of the channel(s) to convey the CableSense signal must be set to 50 Ω. |
| --- | --- |

You can call this function only during an acquisition. If you call this function while your oscilloscope is not acquiring, NI‑SCOPE generates an error.

##### Supported Devices

- PXIe-5110
- PXIe-5111
- PXIe-5113
- PXIe-5160
- PXIe-5162

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_cablesensesignalstop.html language=enus -->
## TOPIC 00082: niScope_CableSenseSignalStop

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_cablesensesignalstop.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_cablesensesignalstop.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CableSenseSignalStop

#### C Function Prototype

ViStatus niScope_CableSenseSignalStop
 (ViSession Instrument_Handle);

#### Purpose

Disables the CableSense signal on all channels of an oscilloscope for which the signal is enabled.

##### Supported Devices

- PXIe-5110
- PXIe-5111
- PXIe-5113
- PXIe-5160
- PXIe-5162

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_caladjustdcm.html language=enus -->
## TOPIC 00083: niScope_CalAdjustDCM

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_caladjustdcm.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_caladjustdcm.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CalAdjustDCM

#### C Function Prototype

ViStatus niScope_CalAdjustDCM (ViSession sessionHandle,
 ViConstString channelName,
 ViReal64 stimulusFreq);

#### Purpose

For the NI 5104/5105 digitizer, calibrates the external clock digital 
clock managers (DCMs). DCM calibration ensures that data can be sampled at the correct time in the clock period.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sessionHandle | ViSession | The session handle you obtain from niScope_CalStart. |
| channelName | ViConstString | This parameter is ignored. |
| stimulusFreq | ViReal64 | The external stimulus applied to the digitizer. Default value: 0 |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_calend.html language=enus -->
## TOPIC 00084: niScope_CalEnd

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_calend.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_calend.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CalEnd

#### C Function Prototype

ViStatus _VI_FUNC niScope_CalEnd 
(
ViSession sessionHandle,
ViInt32 action
);

#### Purpose

Closes an external calibration session. If **action** is set to 
NISCOPE_VAL_ACTION_ABORT, the session is closed and the new calibration constants 
are lost. 

Some devices may write to the EEPROM during calibration, in which case the Abort Calibration 
action restores the EEPROM to its original state. 

It is, therefore, very important to call
 niScope_CalEnd each time [niScope_CalStart](/csh?topicname=scopefunc/cviniscope_calstart.html) is called, 
 even if an error occurs during 
 calibration.

If **action** is set to NISCOPE_VAL_ACTION_STORE, the 
new calibration constants are 
stored in the EEPROM. For most digitizers, the current system date and the incremented calibration 
count are also stored; for SMC-based digitizers, the current 
 system date and onboard temperature are stored.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sessionHandle | ViSession | The session handle returned by niScope_CalStart. |
| action | ViInt32 | NISCOPE_VAL_CAL_ACTION_STORE or NISCOPE_VAL_CAL_ACTION_ABORT |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_calfetchcount.html language=enus -->
## TOPIC 00085: niScope_CalFetchCount

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_calfetchcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_calfetchcount.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CalFetchCount

#### C Function Prototype

ViStatus _VI_FUNC niScope_CalFetchCount
(
 ViSession sessionHandle, 
 ViInt32 whichOne, 
 ViInt32* calibrationCount 
);

#### Purpose

Returns the calibration count, which is the number of times the device has been calibrated.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sessionHandle | ViSession | The session handle you obtain from niScope_CalStart or niScope_init. |
| whichOne | ViInt32 | Which type of calibration count to store: self-calibration or external calibration count. |
| Output |  |  |
| Name | Type | Description |
| calibrationCount | ViInt32* | The number of calibrations performed on this device. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_calfetchmiscinfo.html language=enus -->
## TOPIC 00086: niScope_CalFetchMiscInfo

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_calfetchmiscinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_calfetchmiscinfo.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CalFetchMiscInfo

#### C Function Prototype

ViStatus _VI_FUNC niScope_CalFetchMiscInfo
(
 ViSession sessionHandle, 
 ViChar* miscInfo 
);

#### Purpose

Returns the miscellaneous information stored in the EEPROM using [niScope_CalStoreMiscInfo](/csh?topicname=scopefunc/cviniscope_calstoremiscinfo.html).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sessionHandle | ViSession | The session handle you obtain from niScope_CalStart or niScope_init. |
| Output |  |  |
| Name | Type | Description |
| miscInfo | ViChar* | 4 characters stored in the EEPROM. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_calfetchtemperature.html language=enus -->
## TOPIC 00087: niScope_CalFetchTemperature

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_calfetchtemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_calfetchtemperature.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CalFetchTemperature

#### C Function Prototype

ViStatus _VI_FUNC niScope_CalFetchTemperature
(ViSession sessionHandle,
 ViInt32 whichOne, 
 ViReal64* temperature);

#### Purpose

For SMC-based digitizers, returns the onboard temperature of the digitizer at the time of the last 
self-calibration or external calibration, in degrees Celsius. The temperature returned by this function is an onboard 
temperature read from a sensor on the surface of the digitizer. This temperature should not be confused with the 
environmental temperature of the digitizer's surroundings. During operation, the onboard temperature is normally higher 
than the environmental temperature.

Temperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature
 is usually the more important one to read.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sessionHandle | ViSession | The session handle you obtain from niScope_CalStart. |
| whichOne | ViInt32 | Defined Values NISCOPE_VAL_CAL_SELF NISCOPE_VAL_CAL_EXTERNAL |
| Output |  |  |
| Name | Type | Description |
| temperature | ViReal64* | The returned temperature of last calibration, in °C. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_calmeasurerisdistribution.html language=enus -->
## TOPIC 00088: niScope_CalMeasureRISDistribution

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_calmeasurerisdistribution.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_calmeasurerisdistribution.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CalMeasureRISDistribution

#### C Function Prototype

ViStatus _VI_FUNC niScope_CalMeasureRISDistribution
(ViSession sessionHandle, 
 ViConstString channelName, 
 ViInt32 maxTime, 
 ViReal64* minBinPercent, 
 ViInt32 distributionSize, 
 ViInt32* distribution);

#### Purpose

Calls [niScope_Read](/csh?topicname=scopefunc/cviniscope_read.html) 2,000 times to take an 
acquisition from the specified channel and retrieve the initial X value, which includes 
the time-to-digital (TDC) conversion. The TDC should be a uniform distribution between two
 sample points because triggers should occur randomly. To test this distribution, the distribution of initial X values is created. 
 The percentage of triggers in the smallest bin of this distribution is returned for comparison to a 
 specification to determine if RIS is operating correctly.



The **distribution** parameter must be declared as an array of **distributionSize** to return 
the distribution. Optionally, setting **distribution** to VI_NULL specifies that 
the distribution is not returned.

#### Related topics:

- Equivalent-Time Sampling and Random Interleaved Sampling

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sessionHandle | ViSession | The session handle you obtain from niScope_CalStart or niScope_init. |
| channelName | ViConstString | The name of the channel to calibrate. For more information, refer to Channel String Syntax. |
| maxTime | ViInt32 | The maximum time in ms for each acquisition. |
| minBinPercent | ViReal64* | The percentage (0–1) of triggers in the least full bin. |
| Output |  |  |
| Name | Type | Description |
| distributionSize | ViInt32 | The number of bins for distribution. |
| distribution | ViInt32* | The array for distribution; use VI_NULL for do not return. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_calsetaccessorysource.html language=enus -->
## TOPIC 00089: niScope_CalSetAccessorySource

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_calsetaccessorysource.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_calsetaccessorysource.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CalSetAccessorySource

#### C Function Prototype

ViStatus _VI_FUNC niScope_CalSetAccessorySource ( ViSession sessionHandle, ViConstString channelName, ViInt32 calSource );

#### Purpose

For the NI 5900, this function sets the calibration source for the device.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sessionHandle | ViSession | The session handle returned by niScope_CalStart. |
| channelName | ViConstString | The string name of the channel to calibrate. For more information, refer to Channel String Syntax. |
| calSource | ViInt32 | The calibration signal souce. Defined Values NISCOPE_VAL_CAL_SOURCE_GROUND NISCOPE_VAL_CAL_SOURCE_POSITIVEFS NISCOPE_VAL_CAL_SOURCE_NEGATIVEFS |
| Defined Values |  |  |
| NISCOPE_VAL_CAL_SOURCE_GROUND |  |  |
| NISCOPE_VAL_CAL_SOURCE_POSITIVEFS |  |  |
| NISCOPE_VAL_CAL_SOURCE_NEGATIVEFS |  |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_calstart.html language=enus -->
## TOPIC 00090: niScope_CalStart

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_calstart.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_calstart.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CalStart

#### C Function Prototype

ViStatus _VI_FUNC niScope_CalStart(ViRsrc resourceName, ViConstString password, ViSession* sessionHandle);

#### Purpose

Opens an external calibration session and produces a calibration session handle that is 
required by 
the external calibration functions. 
 All other calibration functions, such as verification and fetch VIs, work with both a calibration 
 session and a session handle obtained from [niScope_init](/csh?topicname=scopefunc/cviniscope_init.html). 
 Acceptable session handles are documented for each function in the calibration procedure documents.

By default, the calibration password for the SMC-based digitizers is "NI". The password is stored in the EEPROM as an array of four characters.
 Nonprintable characters are allowed, but the array is padded with NULLs after the first NULL is found. This padding 
 allows strings of less than four characters to be valid passwords. The password is verified against the password stored 
 in the EEPROM. You can change the password from the default by calling [niScope_CalChangePassword](/csh?topicname=scopefunc/cviniscope_calchangepassword.html).

Only one session handle can be obtained at a time, and every session started with niScope_CalStart must be 
closed by calling [niScope_CalEnd](/csh?topicname=scopefunc/cviniscope_calend.html). If you fail to close the session, you must unload the niScope_32.dll by closing your application or 
application development environment (ADE) before you can open another session.

If an error occurs during calibration, call [niScope_errorHandler](/csh?topicname=scopefunc/cviniscope_errorhandler.html) to get the 
error message text. You can call [niScope_CalEnd](/csh?topicname=scopefunc/cviniscope_calend.html) with **action** set to 

NISCOPE_VAL_CAL_ACTION_ABORT to end the session without updating the EEPROM. For SMC-based digitizers, the EEPROM is also not 
updated if an error occurs.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| resourceName | ViRsrc | The device number assigned by Measurement & Automation Explorer (MAX). |
| password | ViConstString | The password you use, which is verified against the password stored in the EEPROM. |
| Output |  |  |
| Name | Type | Description |
| sessionHandle | ViSession* | The returned session handle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_calstoremiscinfo.html language=enus -->
## TOPIC 00091: niScope_CalStoreMiscInfo

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_calstoremiscinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_calstoremiscinfo.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CalStoreMiscInfo

#### C Function Prototype

ViStatus _VI_FUNC niScope_CalStoreMiscInfo (ViSession 
sessionHandle, ViConstString miscInfo);

#### Purpose

Stores miscellaneous information in the 
EEPROM. For example, you can store an operator ID for the person or company 
performing a calibration.

Four characters are stored in the EEPROM, and nonprintable 
characters are valid. However, NULL is treated as an end-of-string marker, and 
all characters following the first NULL are also set to NULL.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sessionHandle | ViSession | The session handle you obtain from niScope_CalStart or niScope_init. |
| miscInfo | ViConstString | Pointer to 4 characters stored in the EEPROM; can be less than four if NULL terminated. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_checkattributeviboolean.html language=enus -->
## TOPIC 00092: niScope_CheckAttributeViBoolean

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_checkattributeviboolean.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_checkattributeviboolean.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CheckAttributeViBoolean

#### C Function Prototype

ViStatus niScope_CheckAttributeViBoolean (ViSession vi, ViConstString channelList, ViAttr attributeID, ViBoolean value);

#### Purpose

Verifies the validity of a value you specify for a ViBoolean attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute |
| value | ViBoolean | The value that you want to verify for the attribute. Some values might not be valid depending on the current settings of the instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_checkattributeviint32.html language=enus -->
## TOPIC 00093: niScope_CheckAttributeViInt32

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_checkattributeviint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_checkattributeviint32.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CheckAttributeViInt32

#### C Function Prototype

ViStatus niScope_CheckAttributeViInt32 (ViSession vi, ViConstString channelList, ViAttr attributeID, ViInt32 value);

#### Purpose

Verifies the validity of a value you specify for a ViInt32 attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| value | ViInt32 | The value that you want to verify for the attribute. Some values might not be valid depending on the current settings of the instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_checkattributeviint64.html language=enus -->
## TOPIC 00094: niScope_CheckAttributeViInt64

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_checkattributeviint64.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_checkattributeviint64.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CheckAttributeViInt64

#### C Function Prototype

ViStatus niScope_CheckAttributeViInt64 (ViSession vi, ViConstString channelList, ViAttr attributeID, ViInt64 value);

#### Purpose

Verifies the validity of a value you specify for a ViInt64 attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| value | ViInt64 | The value that you want to verify for the attribute. Some values might not be valid depending on the current settings of the instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_checkattributevireal64.html language=enus -->
## TOPIC 00095: niScope_CheckAttributeViReal64

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_checkattributevireal64.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_checkattributevireal64.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CheckAttributeViReal64

#### C Function Prototype

ViStatus niScope_CheckAttributeViReal64 (ViSession vi, ViConstString channelList, ViAttr attributeID, ViReal64 value);

#### Purpose

Verifies the validity of a value you specify for a ViReal64 attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| value | ViReal64 | The value that you want to verify for the attribute. Some values might not be valid depending on the current settings of the instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_checkattributevisession.html language=enus -->
## TOPIC 00096: niScope_CheckAttributeViSession

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_checkattributevisession.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_checkattributevisession.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CheckAttributeViSession

#### C Function Prototype

ViStatus niScope_CheckAttributeViSession (ViSession vi, ViConstString channelList, ViAttr attributeID, ViSession value);

#### Purpose

Verifies the validity of a value you specify for a ViSession attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| value | ViSession | The value that you want to verify for the attribute. Some values might not be valid depending on the current settings of the instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_checkattributevistring.html language=enus -->
## TOPIC 00097: niScope_CheckAttributeViString

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_checkattributevistring.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_checkattributevistring.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_CheckAttributeViString

#### C Function Prototype

ViStatus niScope_CheckAttributeViString (ViSession vi, ViConstString channelList, ViAttr attributeID, ViConstString value);

#### Purpose

Verifies the validity of a value you specify for a ViString attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| value | ViConstString | The value that you want to verify for the attribute. Some values might not be valid depending on the current settings of the instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_clearerror.html language=enus -->
## TOPIC 00098: niScope_ClearError

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_clearerror.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_clearerror.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ClearError

#### C Function Prototype

ViStatus niScope_ClearError (ViSession vi);

#### Purpose

|  | Note This function is included for compliance with the IviScope Class Specification. |
| --- | --- |

Clears the error information for the current execution thread and the IVI session you specify. If you pass VI_NULL for the Instrument Handle parameter, this function clears the error information only for the current execution thread.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_clearinterchangewarnings.html language=enus -->
## TOPIC 00099: niScope_ClearInterchangeWarnings

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_clearinterchangewarnings.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_clearinterchangewarnings.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ClearInterchangeWarnings

#### C Function Prototype

ViStatus niScope_ClearInterchangeWarnings (ViSession vi);

#### Purpose

|  | Note This function is included for compliance with the IviScope Class Specification. |
| --- | --- |

Clears the list of current interchange warnings.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_clearwaveformmeasurementstats.html language=enus -->
## TOPIC 00100: niScope_ClearWaveformMeasurementStats

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_clearwaveformmeasurementstats.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_clearwaveformmeasurementstats.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ClearWaveformMeasurementStats

#### C Function Prototype

ViStatus niScope_ClearWaveformMeasurementStats (ViSession vi, ViConstString channelList, ViInt32 clearableMeasurementFunction);

#### Purpose

Clears the waveform stats on the channel and measurement you specify. If you want 
to clear all of the measurements, use NISCOPE_VAL_ALL_MEASUREMENTS in the 
**clearableMeasurementFunction** parameter.

Every time a measurement is called, the statistics information is updated, including the min, max, mean, standard deviation, and number of updates. This information is fetched with [niScope_FetchMeasurementStats](/csh?topicname=scopefunc/cviniscope_fetchmeasurementstats.html). The multi-acquisition array measurements are also cleared with this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| clearableMeasurementFunction | ViInt32 | The scalar measurement or array measurement to clear the stats for. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_clearwaveformprocessing.html language=enus -->
## TOPIC 00101: niScope_ClearWaveformProcessing

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_clearwaveformprocessing.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_clearwaveformprocessing.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ClearWaveformProcessing

#### C Function Prototype

ViStatus niScope_ClearWaveformProcessing (ViSession vi, ViConstString channelList);

#### Purpose

Clears the list of processing steps assigned to the given channel. The processing is added using the [niScope_AddWaveformProcessing](/csh?topicname=scopefunc/cviniscope_addwaveformprocessing.html) function, where the processing steps are completed in the same order in which they are registered. The processing measurements are streamed, so the result of the first processing step is used as the input for the next step. The processing is also done before any other measurements.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_close.html language=enus -->
## TOPIC 00102: niScope_close

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_close.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_close.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_close

#### C Function Prototype

ViStatus niScope_close (ViSession vi);

#### Purpose

When you are finished using an instrument driver session, you must call this function to perform the following actions:

- Closes the instrument I/O session.
- Destroys the IVI session and all of its attributes.
- Deallocates any memory resources used by the IVI session.

#### Related topics:

- NI-SCOPE Programming Flow

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_commit.html language=enus -->
## TOPIC 00103: niScope_Commit

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_commit.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_commit.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_Commit

#### C Function Prototype

ViStatus niScope_Commit (ViSession vi);

#### Purpose

Commits to hardware all the parameter settings associated with the task.
Use this function if you want a parameter change to be immediately reflected in 
the hardware.

#### Related topics:

- SMC-Based Digitizers Acquisition Engine State Diagram
- NI-SCOPE Programming Flow

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configureacquisition.html language=enus -->
## TOPIC 00104: niScope_ConfigureAcquisition

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configureacquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configureacquisition.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureAcquisition

#### C Function Prototype

ViStatus niScope_ConfigureAcquisition(ViSession vi, ViInt32 acquisitionType);

#### Purpose

Configures how the oscilloscope acquires data and fills the waveform record.

#### Related topics:

- Acquisition Functions

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| acquisitionType | ViInt32 | Specifies the manner in which the digitizer acquires data and fills the waveform record; NI-SCOPE sets NISCOPE_ATTR_ACQUISITION_TYPE to this value. Defined Values NISCOPE_VAL_NORMAL (0) Sets the oscilloscope to normal resolution mode. The oscilloscope can use real-time sampling or equivalent-time sampling. NISCOPE_VAL_FLEXRES (1001) Sets legacy oscilloscopes to flexible resolution mode, if supported. NISCOPE_VAL_DDC (1002) Sets legacy oscilloscopes to DDC mode, if supported. To use DDC mode for the PXI/PCI-5142 or PXIe-5622, set this control to NISCOPE_VAL_NORMAL and set the NISCOPE_ATTR_DDC_ENABLED attribute to VI_TRUE. |
| NISCOPE_VAL_NORMAL (0) | Sets the oscilloscope to normal resolution mode. The oscilloscope can use real-time sampling or equivalent-time sampling. |  |
| NISCOPE_VAL_FLEXRES (1001) | Sets legacy oscilloscopes to flexible resolution mode, if supported. |  |
| NISCOPE_VAL_DDC (1002) | Sets legacy oscilloscopes to DDC mode, if supported. To use DDC mode for the PXI/PCI-5142 or PXIe-5622, set this control to NISCOPE_VAL_NORMAL and set the NISCOPE_ATTR_DDC_ENABLED attribute to VI_TRUE. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configureacquisitionrecord.html language=enus -->
## TOPIC 00105: niScope_ConfigureAcquisitionRecord

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configureacquisitionrecord.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configureacquisitionrecord.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureAcquisitionRecord

#### C Function Prototype

ViStatus niScope_ConfigureAcquisitionRecord (ViSession vi, ViReal64 timeperRecord, ViInt32 minNumPoints, ViReal64 acquisitionStartTime);

#### Purpose

This function is included for compliance with the IviScope Class Specification.

Configures the most commonly configured attributes of the instrument acquisition subsystem.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| timeperRecord | ViReal64 | Specifies the time per record.Units: Seconds. |
| minNumPoints | ViInt32 | Pass the minimum number of points you require in the record for each channel. Call niScope_ActualRecordLength to obtain the actual record length used. Valid Values: 1 – available onboard memory |
| acquisitionStartTime | ViReal64 | Specifies the position of the first point in the waveform record relative to the trigger event. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configurechancharacteristics.html language=enus -->
## TOPIC 00106: niScope_ConfigureChanCharacteristics

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configurechancharacteristics.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configurechancharacteristics.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureChanCharacteristics

#### C Function Prototype

ViStatus niScope_ConfigureChanCharacteristics (ViSession vi, ViConstString channelList, ViReal64 inputImpedance, ViReal64 maxInputFrequency);

#### Purpose

Configures the attributes that control the electrical characteristics of the channel—the input impedance and the bandwidth.

#### Related topics:

- Using Configure Chan Characteristics
- Impedance and Impedance Matching

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| inputImpedance | ViReal64 | The input impedance for the channel; NI-SCOPE sets NISCOPE_ATTR_INPUT_IMPEDANCE to this value. |
| maxInputFrequency | ViReal64 | The bandwidth for the channel; NI-SCOPE sets NISCOPE_ATTR_MAX_INPUT_FREQUENCY to this value. Pass 0 for this value to use the hardware default bandwidth. Pass –1 for this value to achieve full bandwidth. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configurechannel.html language=enus -->
## TOPIC 00107: niScope_ConfigureChannel

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configurechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configurechannel.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureChannel

#### C Function Prototype

ViStatus niScope_ConfigureChannel (ViSession vi, ViConstString channel, ViReal64 range, ViReal64 offset, ViInt32 coupling, ViReal64 probeAttenuation, ViBoolean enabled);

#### Purpose

This function is included for compliance with the IviScope Class Specification.

Configures the most commonly configured attributes of the instrument's channel subsystem.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channel | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. Default Value: "0" |
| range | ViReal64 | Specifies the voltage range for the specified channel(s). |
| offset | ViReal64 | Selects the DC offset added to the specified channel(s).Default Value: 0 |
| coupling | ViInt32 | Specify how you want the digitizer to couple the input signal for the channel. Defined Values NISCOPE_VAL_AC (0) NISCOPE_VAL_DC (1) NISCOPE_VAL_GND (2) A certain amount of delay is required for the coupling capacitor to charge after changing vertical coupling from DC to AC. This delay is typically: Low Impedance Source—150 ms 10X Probe—1.5 s 100X Probe—15 s |
| probeAttenuation | ViReal64 | Specifies the probe attenuation for the specified channel(s).Default Value: 1.00Valid Range: 1.00 – 100 If you have a probe with yX attenuation, set this parameter to y. For example, enter a value of 10 for a 10X probe. |
| enabled | ViBoolean | Specify whether to enable the digitizer to acquire data for the channel when you call niScope_InitiateAcquisition or niScope_ReadWaveform. Default Value:NISCOPE_VAL_TRUE (1) Defined Values NISCOPE_VAL_TRUE (1)—Acquire data on this channelNISCOPE_VAL_FALSE (0)—Do not acquire data on this channel |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configureclock.html language=enus -->
## TOPIC 00108: niScope_ConfigureClock

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configureclock.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configureclock.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureClock

#### C Function Prototype

ViStatus niScope_ConfigureClock (ViSession vi, ViConstString inputClockSource, ViConstString outputClockSource, ViConstString clockSyncPulseSource, ViBoolean masterEnabled);

#### Purpose

Configures the attributes for synchronizing the digitizer to a reference or sending the digitizer's reference clock output to be used as a synchronizing clock for other digitizers.

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Related topics:

- Sample Clock
- Sample Rate
- Coercions of Horizontal Parameters

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| inputClockSource | ViConstString | Specifies the input source for the PLL reference clock (such as the 1-20 MHz clock on SMC-based devices) to which the digitizer is phase-locked for all digitizers. Refer to NISCOPE_ATTR_INPUT_CLOCK_SOURCE for more information. |
| outputClockSource | ViConstString | Specifies the output source for the reference clock to which the sample clock of another oscilloscope can be phase-locked. Refer to NISCOPE_ATTR_OUTPUT_CLOCK_SOURCE for more information |
| clockSyncPulseSource | ViConstString | Specifies the line on which the sample clock or the one-time sync pulse is sent or received. This line should be the same for all devices to be synchronized. Refer to NISCOPE_ATTR_CLOCK_SYNC_PULSE_SOURCE for more information. |
| masterEnabled | ViBoolean | Specifies whether the device is a master or a slave. The master device is typically the originator of the trigger signal and the clock sync pulse. For a standalone device, set this control to VI_FALSE. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configureedgetriggersource.html language=enus -->
## TOPIC 00109: niScope_ConfigureEdgeTriggerSource

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configureedgetriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configureedgetriggersource.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureEdgeTriggerSource

#### C Function Prototype

ViStatus niScope_ConfigureEdgeTriggerSource (ViSession vi, ViConstString source, ViReal64 level, ViInt32 slope);

#### Purpose

|  | Note This function is included for compliance with the IviScope Class Specification. |
| --- | --- |

Sets the edge triggering attributes. An edge trigger occurs when the trigger signal specified with the source parameter passes through the voltage threshold specified with the 
level parameter and has the slope specified with the slope parameter.

This function affects instrument behavior only if the triggerType is NISCOPE_VAL_EDGE. Set the trigger type and trigger coupling before calling this function.

If the trigger source is one of the analog input channels, you must configure the vertical range, vertical offset, vertical coupling, probe attenuation, and the maximum input frequency before calling this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| level | ViReal64 | The voltage threshold for the trigger. Refer to NISCOPE_ATTR_TRIGGER_LEVEL for more information. |
| level | ViReal64 | The voltage threshold for the trigger. Refer to NISCOPE_ATTR_TRIGGER_LEVEL for more information. |
| slope | ViInt32 | Specifies whether you want a rising edge or a falling edge to trigger the digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configureequalizationfiltercoefficients.html language=enus -->
## TOPIC 00110: niScope_ConfigureEqualizationFilterCoefficients

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configureequalizationfiltercoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configureequalizationfiltercoefficients.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureEqualizationFilterCoefficients

#### C Function Prototype

ViStatus _VI_FUNC niScope_ConfigureEqualizationFilterCoefficients (ViSession vi,
 ViConstString channel,
 ViInt32 numberOfCoefficients,
 ViReal64* coefficients);

#### Purpose

Configures the custom coefficients for the equalization FIR filter on the device. 
This filter is designed to compensate the input signal for artifacts introduced to the signal outside
 of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. 
 Coefficient values should be between +1 and –1.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| numberOfCoefficients | ViInt32 | The number of coefficients being passed in the coefficients array. |
| coefficients | ViReal64* | The custom coefficients for the equalization FIR filter on the device. These coefficients should be between +1 and –1. You can obtain the number of coefficients from the NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS attribute. The NISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED attribute must be set to TRUE to enable the filter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configurehorizontaltiming.html language=enus -->
## TOPIC 00111: niScope_ConfigureHorizontalTiming

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configurehorizontaltiming.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configurehorizontaltiming.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureHorizontalTiming

#### C Function Prototype

ViStatus niScope_ConfigureHorizontalTiming (ViSession vi, ViReal64 minSampleRate, ViInt32 minNumPts, ViReal64 refPosition, ViInt32 numRecords, ViBoolean enforceRealtime);

#### Purpose

Configures the common properties of the horizontal subsystem for a multirecord acquisition in terms of minimum sample rate.

#### Related topics:

- Configuring the Horizontal Settings
- NI-TClk Overview
- Coercions of Horizontal Parameters

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| minSampleRate | ViReal64 | The sampling rate for the acquisition. Refer to NISCOPE_ATTR_MIN_SAMPLE_RATE for more information. |
| minNumPts | ViInt32 | The minimum number of points you need in the record for each channel; call niScope_ActualRecordLength to obtain the actual record length used. Valid Values: Greater than 1; limited by available memory |
| refPosition | ViReal64 | The position of the Reference Event in the waveform record specified as a percentage. |
| numRecords | ViInt32 | The number of records to acquire |
| enforceRealtime | ViBoolean | Indicates whether the digitizer enforces real-time measurements or allows equivalent-time (RIS) measurements; not all digitizers support RIS—refer to Features Supported by Device for more information. Default value: VI_TRUE Defined Values VI_TRUE—Allow real-time acquisitions only VI_FALSE—Allow real-time and equivalent-time acquisitions |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configurereflevels.html language=enus -->
## TOPIC 00112: niScope_ConfigureRefLevels

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configurereflevels.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configurereflevels.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureRefLevels

#### C Function Prototype

ViStatus niScope_ConfigureRefLevels (ViSession vi, ViReal64 low, ViReal64 mid, ViReal64 high);

#### Purpose

This function is included for compliance with the IviScope Class Specification.

Configures the reference levels for all channels of the digitizer. The levels may be set on a per channel basis by setting [NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL](/csh?topicname=scopefunc/cviniscope_attr_meas_chan_high_ref_level.html), 
[NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL](/csh?topicname=scopefunc/cviniscope_attr_meas_chan_low_ref_level.html), and [NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL.](/csh?topicname=scopefunc/cviniscope_attr_meas_chan_mid_ref_level.html)

This function configures the reference levels for waveform measurements. 
Call this function before calling [niScope_FetchMeasurement](/csh?topicname=scopefunc/cviniscope_fetchmeasurement.html) to take a rise time, fall time, width negative, width positive, duty cycle negative, or duty cycle positive measurement.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| low | ViReal64 | Pass the low reference you want the digitizer to use for waveform measurements.Units: Either a percentage or voltage based on NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with the voltage low and voltage high measurements representing 0% and 100%, respectively.Default Value: 10.0 |
| mid | ViReal64 | Pass the mid reference you want the digitizer to use for waveform measurements.Units: Either a percentage or voltage based on NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with the voltage low and voltage high measurements representing 0% and 100%, respectively.Default Value: 50.0 |
| high | ViReal64 | Pass the high reference you want the digitizer to use for waveform measurements.Units: Either a percentage or voltage based on NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with the voltage low and voltage high measurements representing 0% and 100%, respectively. Default Value: 90.0 |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretrigger.html language=enus -->
## TOPIC 00113: niScope_ConfigureTrigger

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretrigger.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTrigger

#### C Function Prototype

ViStatus niScope_ConfigureTrigger (ViSession vi, ViInt32 triggerType, ViReal64 holdoff);

#### Purpose

|  | Note This function is included for compliance with the IviScope Class Specification. |
| --- | --- |

Configures the common attributes of the trigger subsystem.

When you use [niScope_ReadWaveform](/csh?topicname=scopefunc/cviniscope_readwaveform.html), the instrument waits for a trigger. You specify the type of trigger for which the instrument waits with the Trigger Type parameter.

If the instrument requires multiple waveform acquisitions to build a complete waveform, it waits for the length of time you specify with the **holdoff** parameter to elapse since the previous trigger. The instrument then waits for the next trigger.

#### Related topics:

- Configuring Triggers
- Coercions of Trigger Parameters
- Triggering
- NI-SCOPE Programming Flow

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| triggerType | ViInt32 | Specifies the type of trigger for which the digitizer will wait. |
| holdoff | ViReal64 | The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to NISCOPE_ATTR_TRIGGER_HOLDOFF for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggercoupling.html language=enus -->
## TOPIC 00114: niScope_ConfigureTriggerCoupling

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggercoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggercoupling.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerCoupling

#### C Function Prototype

ViStatus niScope_ConfigureTriggerCoupling (ViSession vi, ViInt32 coupling);

#### Purpose

|  | Note This function is included for compliance with the IviScope Class Specification. |
| --- | --- |

Sets the trigger coupling attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| coupling | ViInt32 | Specify how you want the instrument to couple the trigger signal. Defined Values NISCOPE_VAL_AC (0) NISCOPE_VAL_DC (1) NISCOPE_VAL_HF_REJECT (2) NISCOPE_VAL_LF_REJECT (3) NISCOPE_VAL_AC_PLUS_HF_REJECT (1001) |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggerdigital.html language=enus -->
## TOPIC 00115: niScope_ConfigureTriggerDigital

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggerdigital.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggerdigital.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerDigital

#### C Function Prototype

ViStatus niScope_ConfigureTriggerDigital (ViSession vi, ViConstString triggerSource, ViInt32 slope, ViReal64 holdoff, ViReal64 delay);

#### Purpose

Configures the common properties of a digital trigger.

When you initiate an acquisition, the digitizer waits for the start trigger, which is configured through the [NISCOPE_ATTR_ACQ_ARM_SOURCE](/csh?topicname=scopefunc/cviniscope_attr_acq_arm_source.html) (Start Trigger Source) attribute. The default is immediate. Upon receiving the start trigger the digitizer begins sampling pretrigger points. After the digitizer finishes sampling pretrigger points, the digitizer waits for a reference (stop) trigger that you specify with a function such as this one. Upon receiving the reference trigger the digitizer finishes the acquisition after completing posttrigger sampling. With each Configure Trigger function, you specify configuration parameters such as the trigger source and the amount of trigger delay.

|  | Notes For multirecord acquisitions, all records after the first record are started by using the Advance Trigger Source. The default is immediate. You can adjust the amount of pre-trigger and post-trigger samples using the reference position parameter on the niScope_ConfigureHorizontalTiming function. The default is half of the record length. Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. Digital triggering is not supported in RIS mode. |
| --- | --- |

#### Related topics:

- Digital Triggers
- Equivalent-Time Sampling and Random Interleaved Sampling

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| triggerSource | ViConstString | Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE for defined values. |
| slope | ViInt32 | Specifies whether you want a rising edge or a falling edge to trigger the digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more information. |
| holdoff | ViReal64 | The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to NISCOPE_ATTR_TRIGGER_HOLDOFF for more information. |
| delay | ViReal64 | How long the digitizer waits after receiving the trigger to start acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggeredge.html language=enus -->
## TOPIC 00116: niScope_ConfigureTriggerEdge

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggeredge.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerEdge

#### C Function Prototype

ViStatus niScope_ConfigureTriggerEdge (ViSession vi, ViConstString triggerSource, ViReal64 level, ViInt32 slope, ViInt32 triggerCoupling, ViReal64 holdoff, ViReal64 delay);

#### Purpose

Configures common properties for analog edge triggering.

When you initiate an acquisition, the digitizer waits for the start trigger, which is configured through the [NISCOPE_ATTR_ACQ_ARM_SOURCE](/csh?topicname=scopefunc/cviniscope_attr_acq_arm_source.html) (Start Trigger Source) attribute. The default is immediate. Upon receiving the start trigger the digitizer begins sampling pretrigger points. After the digitizer finishes sampling pretrigger points, the digitizer waits for a reference (stop) trigger that you specify with a function such as this one. Upon receiving the reference trigger the digitizer finishes the acquisition after completing posttrigger sampling. With each Configure Trigger function, you specify configuration parameters such as the trigger source and the amount of trigger delay.

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Related topics:

- Edge Triggers

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| triggerSource | ViConstString | Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE for defined values. |
| level | ViReal64 | The voltage threshold for the trigger. Refer to NISCOPE_ATTR_TRIGGER_LEVEL for more information. |
| slope | ViInt32 | Specifies whether you want a rising edge or a falling edge to trigger the digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more information. |
| triggerCoupling | ViInt32 | Applies coupling and filtering options to the trigger signal. Refer to NISCOPE_ATTR_TRIGGER_COUPLING for more information. |
| holdoff | ViReal64 | The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to NISCOPE_ATTR_TRIGGER_HOLDOFF for more information. |
| delay | ViReal64 | How long the digitizer waits after receiving the trigger to start acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggerglitch.html language=enus -->
## TOPIC 00117: niScope_ConfigureTriggerGlitch

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggerglitch.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggerglitch.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerGlitch

ViStatus niScope_ConfigureTriggerGlitch
 (ViSession Instrument_Handle,
 ViChar _VI_FAR Trigger_Source[], ViReal64 Level,
 ViReal64 Width, ViInt32 Polarity,
 ViInt32 Condition, ViInt32 Trigger_Coupling,
 ViReal64 Holdoff, ViReal64 Delay);

#### Purpose

Configures common properties for glitch triggering.

A glitch trigger occurs when a pulse that crosses a vertical threshold you specify and with a polarity you specify also has a width that is either greater than or less than a duration you specify.

##### Trigger System Operation

When you initiate an acquisition, the trigger system operates in the following manner.

- The digitizer waits for the start trigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE attribute. The default is NISCOPE_VAL_IMMEDIATE .
- Upon receiving the start trigger, the digitizer begins sampling pretrigger points.
- After the digitizer finishes sampling pretrigger points, the digitizer waits for a reference (stop) trigger that you specify with a trigger function such as this one.
- Upon receiving the reference trigger, the digitizer finishes the acquisition after completing posttrigger sampling.

With each Configure Trigger function, you specify configuration parameters such as the trigger source and the amount of trigger delay. Additionally, you can adjust the amount of pretrigger and posttrigger samples using the **refPosition** input of the [niScope_ConfigureHorizontalTiming](/csh?topicname=scopefunc/cviniscope_configurehorizontaltiming.html) function. The default is half the record length.

For multirecord acquisitions, all records after the first record are started based on the setting of the [NISCOPE_ATTR_ADV_TRIG_SRC](/csh?topicname=scopefunc/cviniscope_attr_adv_trig_src.html) attribute. The default value is NISCOPE_VAL_IMMEDIATE.

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Related topics:

- Glitch Triggers

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| triggerSource | ViConstString | Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE for defined values. |
| level | ViReal64 | The voltage threshold for the trigger. Refer to NISCOPE_ATTR_TRIGGER_LEVEL for more information. |
| Width | ViReal64 | Specifies, in seconds, the glitch duration to be used in combination with the glitch condition that triggers the oscilloscope. The oscilloscope triggers when it detects a pulse of duration either less than or greater than this value depending on the value of the NISCOPE_ATTR_GLITCH_CONDITION attribute. Refer to the NISCOPE_ATTR_GLITCH_WIDTH attribute for more information. |
| Polarity | ViInt32 | Specifies the polarity of the pulses that trigger the oscilloscope for glitch triggering. Refer to the NISCOPE_ATTR_GLITCH_POLARITY attribute for defined values. |
| Glitch Condition | ViInt32 | Specifies whether the oscilloscope triggers on pulses of duration less than or greater than the specified NISCOPE_ATTR_GLITCH_WIDTH. Refer to the NISCOPE_ATTR_GLITCH_CONDITION attribute for defined values. |
| triggerCoupling | ViInt32 | Applies coupling and filtering options to the trigger signal. Refer to NISCOPE_ATTR_TRIGGER_COUPLING for more information. |
| holdoff | ViReal64 | The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to NISCOPE_ATTR_TRIGGER_HOLDOFF for more information. |
| delay | ViReal64 | How long the digitizer waits after receiving the trigger to start acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggerhysteresis.html language=enus -->
## TOPIC 00118: niScope_ConfigureTriggerHysteresis

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggerhysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggerhysteresis.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerHysteresis

#### C Function Prototype

ViStatus niScope_ConfigureTriggerHysteresis (ViSession vi, ViConstString triggerSource, ViReal64 level, ViReal64 hysteresis, ViInt32 slope, ViInt32 triggerCoupling, ViReal64 holdoff, ViReal64 delay);

#### Purpose

Configures common properties for analog hysteresis triggering. This kind of trigger specifies an additional value, specified in the **hysteresis** parameter, that a signal must pass through before a trigger can occur. This additional value acts as a kind of buffer zone that keeps noise from triggering an acquisition.

When you initiate an acquisition, the digitizer waits for the start trigger, which is configured through the [NISCOPE_ATTR_ACQ_ARM_SOURCE (Start Trigger Source)](/csh?topicname=scopefunc/cviniscope_attr_acq_arm_source.html). The default is immediate. Upon receiving the start trigger the digitizer begins sampling pretrigger points. After the digitizer finishes sampling pretrigger points, the digitizer waits for a reference (stop) trigger that you specify with a function such as this one. Upon receiving the reference trigger the digitizer finishes the acquisition after completing posttrigger sampling. With each Configure Trigger function, you specify configuration parameters such as the trigger source and the amount of trigger delay.

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Related topics:

- Hysteresis Triggers

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| triggerSource | ViConstString | Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE for defined values. |
| level | ViReal64 | The voltage threshold for the trigger. Refer to NISCOPE_ATTR_TRIGGER_LEVEL for more information. |
| hysteresis | ViReal64 | The size of the hysteresis window on either side of the level in volts; the digitizer triggers when the trigger signal passes through the hysteresis value you specify with this parameter, has the slope you specify with slope, and passes through the level. Refer to NISCOPE_ATTR_TRIGGER_HYSTERESIS for defined values. |
| slope | ViInt32 | Specifies whether you want a rising edge or a falling edge to trigger the digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more information. |
| triggerCoupling | ViInt32 | Applies coupling and filtering options to the trigger signal. Refer to NISCOPE_ATTR_TRIGGER_COUPLING for more information. |
| holdoff | ViReal64 | The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to NISCOPE_ATTR_TRIGGER_HOLDOFF for more information. |
| delay | ViReal64 | How long the digitizer waits after receiving the trigger to start acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggerimmediate.html language=enus -->
## TOPIC 00119: niScope_ConfigureTriggerImmediate

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggerimmediate.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggerimmediate.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerImmediate

#### C Function Prototype

ViStatus niScope_ConfigureTriggerImmediate (ViSession vi);

#### Purpose

Configures common properties for immediate triggering. Immediate triggering means the digitizer triggers itself.

When you initiate an acquisition, the digitizer waits for a trigger. You specify the type of trigger that the digitizer waits for with a Configure Trigger function, such as niScope_ConfigureTriggerImmediate.

#### Related topics:

- Immediate Triggers

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggeroutput.html language=enus -->
## TOPIC 00120: niScope_ConfigureTriggerOutput

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggeroutput.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggeroutput.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerOutput

#### C Function Prototype

ViStatus niScope_ConfigureTriggerOutput (ViSession vi, ViInt32 triggerEvent, ViConstString triggerOutput);

#### Purpose

|  | Note This function is obsolete. Consider using niScope_ExportSignal instead. |
| --- | --- |

Configures the digitizer to generate a signal pulse that other digitizers can detect when configured for digital triggering.

For NI-DAQmx devices, closing the session clears the route. However, if you want to clear the routes before closing the session, call this function again and route the NISCOPE_VAL_STOP_TRIGGER_EVENT to NISCOPE_VAL_NONE.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| triggerEvent | ViInt32 | Specifies the condition in which this device generates a digital pulse. |
| triggerOutput | ViConstString | Specifies the hardware signal line on which the digital pulse is generated. Valid Values NISCOPE_VAL_NO_EVENT NISCOPE_VAL_STOP_TRIGGER_EVENT NISCOPE_VAL_START_TRIGGER_EVENT NISCOPE_VAL_END_OF_ACQUISITION_EVENT NISCOPE_VAL_END_OF_RECORD_EVENT |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggerrunt.html language=enus -->
## TOPIC 00121: niScope_ConfigureTriggerRunt

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggerrunt.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggerrunt.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerRunt

ViStatus niScope_ConfigureTriggerRunt
 (ViSession Instrument_Handle,
 ViChar _VI_FAR Trigger_Source[],
 ViReal64 Low_Threshold, ViReal64 High_Threshold,
 ViInt32 Polarity, ViInt32 Trigger_Coupling,
 ViReal64 Holdoff, ViReal64 Delay);

#### Purpose

Configures common properties for runt triggering.

A runt trigger occurs when both the leading edge and trailing edge of a pulse cross only one of two trigger thresholds you specify and with a polarity you specify, where the polarity is relative to the threshold crossed.

##### Trigger System Operation

When you initiate an acquisition, the trigger system operates in the following manner.

- The digitizer waits for the start trigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE attribute. The default is NISCOPE_VAL_IMMEDIATE .
- Upon receiving the start trigger, the digitizer begins sampling pretrigger points.
- After the digitizer finishes sampling pretrigger points, the digitizer waits for a reference (stop) trigger that you specify with a trigger function such as this one.
- Upon receiving the reference trigger, the digitizer finishes the acquisition after completing posttrigger sampling.

With each Configure Trigger function, you specify configuration parameters such as the trigger source and the amount of trigger delay. Additionally, you can adjust the amount of pretrigger and posttrigger samples using the **refPosition** input of the [niScope_ConfigureHorizontalTiming](/csh?topicname=scopefunc/cviniscope_configurehorizontaltiming.html) function. The default is half the record length.

For multirecord acquisitions, all records after the first record are started based on the setting of the [NISCOPE_ATTR_ADV_TRIG_SRC](/csh?topicname=scopefunc/cviniscope_attr_adv_trig_src.html) attribute. The default value is NISCOPE_VAL_IMMEDIATE.

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Related topics:

- Runt Triggers

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| triggerSource | ViConstString | Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE for defined values. |
| Low Threshold | ViReal64 | Specifies, in volts, the lower of two thresholds that bound the vertical range to examine for runt pulses. Refer to the NISCOPE_ATTR_RUNT_LOW_THRESHOLD attribute for more information. |
| High Threshold | ViReal64 | Specifies, in volts, the higher of two thresholds that bound the vertical range to examine for runt pulses. Refer to the NISCOPE_ATTR_RUNT_HIGH_THRESHOLD attribute for more information. |
| Polarity | ViInt32 | Specifies the polarity of the runt pulses, relative to the runt threshold the pulses cross, that trigger the oscilloscope for runt triggering. Refer to the NISCOPE_ATTR_RUNT_POLARITY attribute for defined values. |
| triggerCoupling | ViInt32 | Applies coupling and filtering options to the trigger signal. Refer to NISCOPE_ATTR_TRIGGER_COUPLING for more information. |
| holdoff | ViReal64 | The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to NISCOPE_ATTR_TRIGGER_HOLDOFF for more information. |
| delay | ViReal64 | How long the digitizer waits after receiving the trigger to start acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggersoftware.html language=enus -->
## TOPIC 00122: niScope_ConfigureTriggerSoftware

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggersoftware.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggersoftware.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerSoftware

#### C Function Prototype

ViStatus niScope_ConfigureTriggerSoftware (ViSession vi, ViReal64 holdoff, ViReal64 delay);

#### Purpose

Configures common properties for software triggering.

When you initiate an acquisition, the digitizer waits for the start trigger, which is configured through the 
[NISCOPE_ATTR_ACQ_ARM_SOURCE](/csh?topicname=scopefunc/cviniscope_attr_acq_arm_source.html) 
(Start Trigger Source) attribute. The default is immediate. Upon receiving the start trigger 
the digitizer begins sampling pretrigger points. After the digitizer finishes sampling 
pretrigger points, the digitizer waits for a reference (stop) trigger that you specify with a 
function such as this one. Upon receiving the reference trigger the digitizer finishes the 
acquisition after completing posttrigger sampling. With each Configure Trigger function, you 
specify configuration parameters such as the trigger source and the amount of trigger delay.

To trigger the acquisition, use [niScope_SendSoftwareTriggerEdge](/csh?topicname=scopefunc/cviniscope_sendsoftwaretriggeredge.html).

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Related topics:

- Software Triggers

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| holdoff | ViReal64 | The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to NISCOPE_ATTR_TRIGGER_HOLDOFF for more information. |
| delay | ViReal64 | How long the digitizer waits after receiving the trigger to start acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggervideo.html language=enus -->
## TOPIC 00123: niScope_ConfigureTriggerVideo

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggervideo.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggervideo.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerVideo

#### C Function Prototype

ViStatus niScope_ConfigureTriggerVideo (ViSession vi, ViConstString triggerSource,
 ViBoolean enableDCRestore,
 ViInt32 signalFormat,
 ViInt32 event,
 ViInt32 lineNumber, 
 ViInt32 polarity,
 ViInt32 triggerCoupling,
 ViReal64 holdoff,
 ViReal64 delay);

#### Purpose

Configures the common properties for video triggering, including the signal format, TV event, line number, polarity, and enable DC restore. A video trigger occurs when the digitizer finds a valid video signal sync.

When you initiate an acquisition, the digitizer waits for the start trigger, which is configured through the [NISCOPE_ATTR_ACQ_ARM_SOURCE](/csh?topicname=scopefunc/cviniscope_attr_acq_arm_source.html) (Start Trigger Source) attribute. The default is immediate. Upon receiving the start trigger the digitizer begins sampling pretrigger points. After the digitizer finishes sampling pretrigger points, the digitizer waits for a reference (stop) trigger that you specify with a function such as this one. Upon receiving the reference trigger the digitizer finishes the acquisition after completing posttrigger sampling. With each Configure Trigger function, you specify configuration parameters such as the trigger source and the amount of trigger delay.

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| triggerSource | ViConstString | Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE for defined values. |
| enableDCRestore | ViBoolean | Offsets each video line so the clamping level (the portion of the video line between the end of the color burst and the beginning of the active image) is moved to zero volt. Refer to NISCOPE_ATTR_ENABLE_DC_RESTORE for defined values. |
| signalFormat | ViInt32 | Specifies the type of video signal sync the digitizer should look for. Refer to NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT for more information. |
| event | ViInt32 | Specifies the TV event you want to trigger on. You can trigger on a specific or on the next coming line or field of the signal. |
| lineNumber | ViInt32 | Selects the line number to trigger on. The line number range covers an entire frame and is referenced as shown on Vertical Blanking and Synchronization Signal. Refer to NISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER for more information. Default value: 1 |
| polarity | ViInt32 | Specifies the polarity of the video signal sync. |
| triggerCoupling | ViInt32 | Applies coupling and filtering options to the trigger signal. Refer to NISCOPE_ATTR_TRIGGER_COUPLING for more information. |
| holdoff | ViReal64 | The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to NISCOPE_ATTR_TRIGGER_HOLDOFF for more information. |
| delay | ViReal64 | How long the digitizer waits after receiving the trigger to start acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggerwidth.html language=enus -->
## TOPIC 00124: niScope_ConfigureTriggerWidth

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggerwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggerwidth.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerWidth

ViStatus niScope_ConfigureTriggerWidth
 (ViSession Instrument_Handle,
 ViChar _VI_FAR Trigger_Source[], ViReal64 Level,
 ViReal64 Low_Threshold, ViReal64 High_Threshold,
 ViInt32 Polarity, ViInt32 Condition,
 ViInt32 Trigger_Coupling, ViReal64 Holdoff,
 ViReal64 Delay);

#### Purpose

Configures common properties for width triggering.

A width trigger occurs when a pulse that crosses a vertical threshold you specify and with a polarity you specify also has a duration that is either within or outside a duration range you specify.

##### Trigger System Operation

When you initiate an acquisition, the trigger system operates in the following manner.

- The digitizer waits for the start trigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE attribute. The default is NISCOPE_VAL_IMMEDIATE .
- Upon receiving the start trigger, the digitizer begins sampling pretrigger points.
- After the digitizer finishes sampling pretrigger points, the digitizer waits for a reference (stop) trigger that you specify with a trigger function such as this one.
- Upon receiving the reference trigger, the digitizer finishes the acquisition after completing posttrigger sampling.

With each Configure Trigger function, you specify configuration parameters such as the trigger source and the amount of trigger delay. Additionally, you can adjust the amount of pretrigger and posttrigger samples using the **refPosition** input of the [niScope_ConfigureHorizontalTiming](/csh?topicname=scopefunc/cviniscope_configurehorizontaltiming.html) function. The default is half the record length.

For multirecord acquisitions, all records after the first record are started based on the setting of the [NISCOPE_ATTR_ADV_TRIG_SRC](/csh?topicname=scopefunc/cviniscope_attr_adv_trig_src.html) attribute. The default value is NISCOPE_VAL_IMMEDIATE.

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Related topics:

- Width Triggers

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| triggerSource | ViConstString | Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE for defined values. |
| level | ViReal64 | The voltage threshold for the trigger. Refer to NISCOPE_ATTR_TRIGGER_LEVEL for more information. |
| Low Threshold | ViReal64 | Specifies, in seconds, the lower bound on the range of pulse durations that triggers the oscilloscope. Refer to the NISCOPE_ATTR_WIDTH_LOW_THRESHOLD attribute for defined values. |
| High Threshold | ViReal64 | Specifies, in seconds, the upper bound on the range of pulse durations that triggers the oscilloscope. Refer to the NISCOPE_ATTR_WIDTH_HIGH_THRESHOLD attribute for defined values. |
| Polarity | ViInt32 | Specifies the polarity of the pulses that trigger the oscilloscope for width triggering. Refer to the NISCOPE_ATTR_WIDTH_POLARITY attribute for defined values. |
| Condition | ViInt32 | Specifies whether the oscilloscope triggers on pulses of duration within or outside the range of pulse durations bounded by Low Threshold and High Threshold. Refer to the NISCOPE_ATTR_WIDTH_CONDITION attribute for defined values. |
| triggerCoupling | ViInt32 | Applies coupling and filtering options to the trigger signal. Refer to NISCOPE_ATTR_TRIGGER_COUPLING for more information. |
| holdoff | ViReal64 | The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to NISCOPE_ATTR_TRIGGER_HOLDOFF for more information. |
| delay | ViReal64 | How long the digitizer waits after receiving the trigger to start acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretriggerwindow.html language=enus -->
## TOPIC 00125: niScope_ConfigureTriggerWindow

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretriggerwindow.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretriggerwindow.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTriggerWindow

#### C Function Prototype

ViStatus niScope_ConfigureTriggerWindow (ViSession vi, ViConstString triggerSource, ViReal64 lowLevel, ViReal64 highLevel, ViInt32 windowMode, ViInt32 triggerCoupling, ViReal64 holdoff, ViReal64 delay);

#### Purpose

Configures common properties for analog window triggering. A window trigger occurs when a signal enters or leaves a window you specify with the **high level** or **low level** parameters.

When you initiate an acquisition, the digitizer waits for the start trigger, which is configured through the 
[NISCOPE_ATTR_ACQ_ARM_SOURCE](/csh?topicname=scopefunc/cviniscope_attr_acq_arm_source.html) 
(Start Trigger Source) attribute. The default is immediate. Upon receiving the start trigger 
the digitizer begins sampling pretrigger points. After the digitizer finishes sampling 
pretrigger points, the digitizer waits for a reference (stop) trigger that you specify with a 
function such as this one. Upon receiving the reference trigger the digitizer finishes the 
acquisition after completing posttrigger sampling. With each Configure Trigger function, you 
specify configuration parameters such as the trigger source and the amount of trigger delay.

To trigger the acquisition, use [niScope_SendSoftwareTriggerEdge](/csh?topicname=scopefunc/cviniscope_sendsoftwaretriggeredge.html).

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Related topics:

- Window Triggers

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| triggerSource | ViConstString | Specifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE for defined values. |
| lowLevel | ViReal64 | Passes the voltage threshold you want the digitizer to use for low triggering. |
| highLevel | ViReal64 | Passes the voltage threshold you want the digitizer to use for high triggering. |
| windowMode | ViInt32 | Specifies whether you want the trigger to occur when the signal enters or leaves a window. |
| triggerCoupling | ViInt32 | Applies coupling and filtering options to the trigger signal. Refer to NISCOPE_ATTR_TRIGGER_COUPLING for more information. |
| holdoff | ViReal64 | The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to NISCOPE_ATTR_TRIGGER_HOLDOFF for more information. |
| delay | ViReal64 | How long the digitizer waits after receiving the trigger to start acquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretvtriggerlinenumber.html language=enus -->
## TOPIC 00126: niScope_ConfigureTVTriggerLineNumber

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretvtriggerlinenumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretvtriggerlinenumber.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTVTriggerLineNumber

#### C Function Prototype

ViStatus niScope_ConfigureTVTriggerLineNumber (ViSession vi, ViInt32 lineNumber);

#### Purpose

This function is included for compliance with the IviScope Class Specification.

Configures the TV line upon which the instrument triggers. The line number is absolute and not relative to the field of the TV signal.

This function affects instrument behavior only if the trigger type is set to NISCOPE_VAL_TV_TRIGGER and the TV trigger event is set to NISCOPE_VAL_TV_EVENT_LINE_NUMBER. Call [niScope_ConfigureTVTriggerSource](/csh?topicname=scopefunc/cviniscope_configuretvtriggersource.html) to set the TV trigger event before calling this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| lineNumber | ViInt32 | Specify the line number of the signal you want to trigger off of. The valid ranges of the attribute depend on the signal format configured. Default Value: 1 Signal FormatLine Numbers M-NTSC, 480i, 480p 1 to 525 BG/PAL, SECAM, 576i, 576p 1 to 625 720p 1 to 750 1080i,1080p 1 to 1,125 |
| Signal Format | Line Numbers |  |
| M-NTSC, 480i, 480p | 1 to 525 |  |
| BG/PAL, SECAM, 576i, 576p | 1 to 625 |  |
| 720p | 1 to 750 |  |
| 1080i,1080p | 1 to 1,125 |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configuretvtriggersource.html language=enus -->
## TOPIC 00127: niScope_ConfigureTVTriggerSource

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configuretvtriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configuretvtriggersource.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureTVTriggerSource

#### C Function Prototype

ViStatus niScope_ConfigureTVTriggerSource (ViSession vi, ViConstString source, ViInt32 signalFormat, ViInt32 event, ViInt32 polarity);

#### Purpose

|  | Note This function is included for compliance with the IviScope Class Specification. |
| --- | --- |

Configures the instrument for TV triggering. It configures the TV signal format, the event, and the signal polarity.

This function affects instrument behavior 
only if the trigger type is NISCOPE_VAL_TV_TRIGGER. Set the trigger type 
and trigger coupling before calling this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| source | ViConstString | Pass the source you want the digitizer to monitor for a trigger. Defined Values "0"—Channel 0"1"—Channel 1 NISCOPE_VAL_EXTERNAL—Analog External Trigger Input |
| signalFormat | ViInt32 | Specifies the Video/TV signal format. Defined Values NISCOPE_VAL_NTSC (1) NISCOPE_VAL_PAL (2) NISCOPE_VAL_SECAM (3) |
| event | ViInt32 | Video/TV event to trigger off of. Defined Values NISCOPE_VAL_TV_EVENT_FIELD1 (1)—trigger on field 1 of the signal NISCOPE_VAL_TV_EVENT_FIELD2 (2)—trigger on field 2 of the signal NISCOPE_VAL_TV_EVENT_ANY_FIELD (3)—trigger on the first field acquired NISCOPE_VAL_TV_EVENT_ANY_LINE (4)—trigger on the first line acquired NISCOPE_VAL_TV_EVENT_LINE_NUMBER (5)—trigger on a specific line of a video signal. Valid values vary depending on the signal format configured. |
| polarity | ViInt32 | Specifies the polarity of the video signal to trigger off of. Defined Values NISCOPE_VAL_TV_POSITIVE (1)NISCOPE_VAL_TV_NEGATIVE (2) |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_configurevertical.html language=enus -->
## TOPIC 00128: niScope_ConfigureVertical

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_configurevertical.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_configurevertical.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ConfigureVertical

#### C Function Prototype

ViStatus niScope_ConfigureVertical (ViSession vi, ViConstString channelList, ViReal64 range, ViReal64 offset, ViInt32 coupling, ViReal64 probeAttenuation, ViBoolean enabled);

#### Purpose

Configures the most commonly configured attributes of the digitizer vertical subsystem, such as the range, offset, coupling, probe attenuation, and the channel.

#### Related topics:

- Configuring the Vertical Settings
- NI-SCOPE Programming Flow
- Coercions of Vertical Parameters

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| range | ViReal64 | Specifies the vertical range Refer to NISCOPE_ATTR_VERTICAL_RANGE for more information. |
| offset | ViReal64 | Specifies the vertical offset. Refer to NISCOPE_ATTR_VERTICAL_OFFSET for more information. |
| coupling | ViInt32 | Specifies how to couple the input signal. Refer to NISCOPE_ATTR_VERTICAL_COUPLING for more information. |
| probeAttenuation | ViReal64 | Specifies the probe attenuation. Refer to NISCOPE_ATTR_PROBE_ATTENUATION for valid values. |
| enabled | ViBoolean | Specifies whether the channel is enabled for acquisition. Refer to NISCOPE_ATTR_CHANNEL_ENABLED for more information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_disable.html language=enus -->
## TOPIC 00129: niScope_Disable

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_disable.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_Disable

#### C Function Prototype

ViStatus niScope_Disable (ViSession vi);

#### Purpose

Aborts any current operation, opens data channel relays, and releases RTSI and PFI lines.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_error_message.html language=enus -->
## TOPIC 00130: niScope_error_message

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_error_message.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_error_message.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_error_message

#### C Function Prototype

ViStatus niScope_error_message (ViSession vi,
 ViStatus errorCode,
 ViChar errorMessage[IVI_MAX_MESSAGE_BUF_SIZE]);

#### Purpose

Takes the error code returned by NI-SCOPE functions and returns the interpretation as a user-readable
 string. You can pass VI_NULL as the instrument handle, which is useful to interpret errors after [niScope_init](cviniscope_init.html) has failed.

|  | Note This function is obsolete. Consider using niScope_GetErrorMessage instead. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| errorCode | ViStatus | The error code that is returned from any of the instrument driver functions. |
| Output |  |  |
| Name | Type | Description |
| errorMessage[] | ViChar | Returns the interpreted error code as a user-readable string; you must pass a ViChar array at least IVI_MAX_MESSAGE_BUF_SIZE bytes in length. |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_error_query.html language=enus -->
## TOPIC 00131: niScope_error_query

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_error_query.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_error_query.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_error_query

#### C Function Prototype

ViStatus niScope_error_query (ViSession vi, ViInt32* errCode, ViChar[] errMessage);

#### Purpose

|  | Note This function is included for compliance with the IviScope Class Specification. |
| --- | --- |

Reads an error code and message from the error queue. National Instruments digitizers do not contain an error queue. Errors are reported as they occur. Therefore, this function does not detect errors.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| Output |  |  |
| Name | Type | Description |
| errCode | ViInt32* | Returns the error code for the session or execution thread. If you pass 0 for the Buffer Size, you can pass VI_NULL for this parameter. |
| errMessage | ViChar[] | Formats the error code into a user-readable message string. The array must contain at least 256 elements (ViChar[256]). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_errorhandler.html language=enus -->
## TOPIC 00132: niScope_errorHandler

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_errorhandler.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_errorhandler.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_errorHandler

#### C Function Prototype

ViStatus niScope_errorHandler (ViSession vi,
 ViInt32 errorCode,
 ViChar errorSource[MAX_FUNCTION_NAME_SIZE],
 ViChar errorDescription[MAX_ERROR_DESCRIPTION]);

#### Purpose

Takes the error code returned by NI-SCOPE functions and returns the interpretation as a user-readable string.

|  | Note You can pass VI_NULL as the instrument handle, which is useful to interpret errors after niScope_init has failed. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| errorCode | ViStatus | The error code that is returned from any of the instrument driver functions. |
| errorSource[] | ViChar | Specifies the function in which the error occurred. You can pass in a string no longer than MAX_FUNCTION_NAME_SIZE. If you pass in a valid string, this source is included in the errorDescription string. For example: "Error <errorCode> at <errorSource>" If you pass in NULL or an empty string, this parameter is ignored. |
| Output |  |  |
| Name | Type | Description |
| errorDescription[] | ViChar | Returns the interpreted error code as a user readable message string; you must pass a ViChar array at least MAX_ERROR_DESCRIPTION bytes in length. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_exportattributeconfigurationbuffer.html language=enus -->
## TOPIC 00133: niScope_ExportAttributeConfigurationBuffer

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_exportattributeconfigurationbuffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_exportattributeconfigurationbuffer.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ExportAttributeConfigurationBuffer

ViStatus niScope_ExportAttributeConfigurationBuffer
 (ViSession vi,
 ViInt32 size, ViAddr configuration);

#### Purpose

Exports the attribute configuration of the session to a buffer.

You can export and import session attribute configurations only between NI‑SCOPE devices with identical bus types, model numbers, channel counts, and onboard memory sizes and between NI-SCOPE sessions with the same number of initialized channels.

This function verifies that the attributes you have configured for the session are valid. If the configuration is invalid, NI-SCOPE returns an error.

**Device Mapping Behavior**

When exporting and importing configurations between NI‑SCOPE sessions that were both initialized with multiple instruments, the configurations of the exporting instruments are mapped to the importing instruments in the order you specify in the **resourceName** input to the [niScope_InitWithOptions](/csh?topicname=scopefunc/cviniscope_initwithoptions.html) or [niScope_init](/csh?topicname=scopefunc/cviniscope_init.html) functions.

For example, if your entry for **resourceName** is PXI1Slot1,PXI1Slot2 for the exporting session and PXI2Slot2,PXI2Slot3 for the importing session:

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

|  | Note NI-SCOPE will return an error if the total number of channels initialized for the exporting session is not equal to the total number of channels initialized for the importing session. |
| --- | --- |

**Related Topics:**

[Attributes and Attribute Functions](/csh?topicname=digitizers/attributes_and_attribute_functions.html)

[Setting Attributes Before Reading Attributes](/csh?topicname=digitizers/setting_before_reading_attributes.html)

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| size | ViInt32 | Specifies the size, in bytes, of the byte array to export. If you enter 0, this function returns the needed size. |
| configuration | ViAddr | Specifies the byte array that contains the exported configuration. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_exportattributeconfigurationfile.html language=enus -->
## TOPIC 00134: niScope_ExportAttributeConfigurationFile

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_exportattributeconfigurationfile.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_exportattributeconfigurationfile.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ExportAttributeConfigurationFile

ViStatus niScope_ExportAttributeConfigurationFile
 (ViSession vi,
 ViConstString filePath);

#### Purpose

Exports the attribute configuration of the session to the specified file.

You can export and import session attribute configurations only between NI‑SCOPE devices with identical bus types, model numbers, channel counts, and onboard memory sizes and between NI-SCOPE sessions with the same number of initialized channels.

This function verifies that the attributes you have configured for the session are valid. If the configuration is invalid, NI-SCOPE returns an error.

**Device Mapping Behavior**

When exporting and importing configurations between NI‑SCOPE sessions that were both initialized with multiple instruments, the configurations of the exporting instruments are mapped to the importing instruments in the order you specify in the **resourceName** input to the [niScope_InitWithOptions](/csh?topicname=scopefunc/cviniscope_initwithoptions.html) or [niScope_init](/csh?topicname=scopefunc/cviniscope_init.html) functions.

For example, if your entry for **resourceName** is PXI1Slot1,PXI1Slot2 for the exporting session and PXI2Slot2,PXI2Slot3 for the importing session:

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

|  | Note NI-SCOPE will return an error if the total number of channels initialized for the exporting session is not equal to the total number of channels initialized for the importing session. |
| --- | --- |

**Related Topics:**

[Attributes and Attribute Functions](/csh?topicname=digitizers/attributes_and_attribute_functions.html)

[Setting Attributes Before Reading Attributes](/csh?topicname=digitizers/setting_before_reading_attributes.html)

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| filePath | ViConstString | The absolute path to a placeholder file you must create to contain the attribute configuration you want to export. If you specify an empty or relative path, this function returns an error.Default file extension: .niscopeconfig |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_exportsignal.html language=enus -->
## TOPIC 00135: niScope_ExportSignal

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_exportsignal.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_exportsignal.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ExportSignal

#### C Function Prototype

ViStatus niScope_ExportSignal (ViSession vi,
 ViInt32 signal,
 ViConstString signalIdentifier,
 ViConstString outputTerminal);

#### Purpose

|  | Note This function replaces niScope_ConfigureTriggerOutput. |
| --- | --- |

Configures the digitizer to generate a signal that other devices can detect 
when configured for digital triggering or sharing clocks. The **signal** parameter 
specifies what condition causes the digitizer to generate the signal. 
The **outputTerminal** parameter specifies where to send the signal on the hardware 
(such as a PFI connector or RTSI line).

In cases where multiple instances of a particular signal exist, use the **signalIdentifier** input to specify 
 which instance to control. For normal signals, only one instance exists and you should leave 
 this parameter set to the empty string. You can call this function multiple times and set each available line 
 to a different signal.

To unprogram a specific line on device, call this function with 
the signal you no longer want to export and 
set **outputTerminal** to NISCOPE_VAL_NONE.

#### Related topics:

- Triggering
- SMC-Based Digitizers Acquisition Engine State Diagram
- PXI Trigger Lines

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| signal | ViInt32 | Signal (clock, trigger, or event) to export. Defined Values NISCOPE_VAL_REF_TRIGGER(1)Generate a pulse when detecting the Stop/Reference trigger. NISCOPE_VAL_START_TRIGGER (2)Generate a pulse when detecting a Start trigger. NISCOPE_VAL_END_OF_ACQUISITION_EVENT(3)Generate a pulse when the acquisition finishes. NISCOPE_VAL_END_OF_RECORD_EVENT (4)Generate a pulse at the end of the record. NISCOPE_VAL_ADVANCE_TRIGGER (5)Generate a pulse when detecting an Advance trigger. NISCOPE_VAL_READY_FOR_ADVANCE_EVENT (6)Asserts when the digitizer is ready to advance to the next record. NISCOPE_VAL_READY_FOR_START_EVENT (7)Asserts when the digitizer is initiated and ready to accept a Start trigger and begin sampling. NISCOPE_VAL_READY_FOR_REF_EVENT (10)Asserts when the digitizer is ready to accept a Reference trigger. NISCOPE_VAL_REF_CLOCK (100) Export the Reference clock for the digitizer to the specified terminal. NISCOPE_VAL_SAMPLE_CLOCK (101)Export the Sample clock for the digitizer to the specified terminal. NISCOPE_VAL_5V_OUT (13)Exports a 5 V power supply. |
| NISCOPE_VAL_REF_TRIGGER | (1) | Generate a pulse when detecting the Stop/Reference trigger. |
| NISCOPE_VAL_START_TRIGGER | (2) | Generate a pulse when detecting a Start trigger. |
| NISCOPE_VAL_END_OF_ACQUISITION_EVENT | (3) | Generate a pulse when the acquisition finishes. |
| NISCOPE_VAL_END_OF_RECORD_EVENT | (4) | Generate a pulse at the end of the record. |
| NISCOPE_VAL_ADVANCE_TRIGGER | (5) | Generate a pulse when detecting an Advance trigger. |
| NISCOPE_VAL_READY_FOR_ADVANCE_EVENT | (6) | Asserts when the digitizer is ready to advance to the next record. |
| NISCOPE_VAL_READY_FOR_START_EVENT | (7) | Asserts when the digitizer is initiated and ready to accept a Start trigger and begin sampling. |
| NISCOPE_VAL_READY_FOR_REF_EVENT | (10) | Asserts when the digitizer is ready to accept a Reference trigger. |
| NISCOPE_VAL_REF_CLOCK | (100) | Export the Reference clock for the digitizer to the specified terminal. |
| NISCOPE_VAL_SAMPLE_CLOCK | (101) | Export the Sample clock for the digitizer to the specified terminal. |
| NISCOPE_VAL_5V_OUT | (13) | Exports a 5 V power supply. |
| signalIdentifier | ViConstString | Describes the signal being exported. |
| outputTerminal | ViConstString | Identifies the hardware signal line on which the digital pulse is generated. Defined Values NISCOPE_VAL_RTSI_0 ("VAL_RTSI_0") NISCOPE_VAL_RTSI_1("VAL_RTSI_1") NISCOPE_VAL_RTSI_2("VAL_RTSI_2") NISCOPE_VAL_RTSI_3 ("VAL_RTSI_3") NISCOPE_VAL_RTSI_4("VAL_RTSI_4") NISCOPE_VAL_RTSI_5 ("VAL_RTSI_5") NISCOPE_VAL_RTSI_6("VAL_RTSI_6") NISCOPE_VAL_RTSI_7("VAL_RTSI_7") NISCOPE_VAL_PXI_STAR("VAL_PXI_STAR") NISCOPE_VAL_PFI_0("VAL_PFI_0") NISCOPE_VAL_PFI_1("VAL_PFI_1") NISCOPE_VAL_PFI_2("VAL_PFI_2") NISCOPE_VAL_CLK_OUT("VAL_CLK_OUT") |
| NISCOPE_VAL_RTSI_0 | ("VAL_RTSI_0") |  |
| NISCOPE_VAL_RTSI_1 | ("VAL_RTSI_1") |  |
| NISCOPE_VAL_RTSI_2 | ("VAL_RTSI_2") |  |
| NISCOPE_VAL_RTSI_3 | ("VAL_RTSI_3") |  |
| NISCOPE_VAL_RTSI_4 | ("VAL_RTSI_4") |  |
| NISCOPE_VAL_RTSI_5 | ("VAL_RTSI_5") |  |
| NISCOPE_VAL_RTSI_6 | ("VAL_RTSI_6") |  |
| NISCOPE_VAL_RTSI_7 | ("VAL_RTSI_7") |  |
| NISCOPE_VAL_PXI_STAR | ("VAL_PXI_STAR") |  |
| NISCOPE_VAL_PFI_0 | ("VAL_PFI_0") |  |
| NISCOPE_VAL_PFI_1 | ("VAL_PFI_1") |  |
| NISCOPE_VAL_PFI_2 | ("VAL_PFI_2") |  |
| NISCOPE_VAL_CLK_OUT | ("VAL_CLK_OUT") |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetch.html language=enus -->
## TOPIC 00136: niScope_Fetch

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetch.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetch.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_Fetch

#### C Function Prototype

ViStatus niScope_Fetch (ViSession vi, ViConstString channelList, ViReal64 timeout, ViInt32 numSamples, ViReal64* wfm, struct niScope_wfmInfo* wfmInfo);

#### Purpose

Returns the waveform from a previously initiated acquisition that the digitizer acquires for the specified channel. This function returns scaled voltage waveforms.

This function may return multiple waveforms depending on the number of channels, the acquisition type, and the number of records you specify.

|  | Notes You can use niScope_Read instead of this function. niScope_Read starts an acquisition on all enabled channels, waits for the acquisition to complete, and returns the waveform for the specified channel. Some functionality, such as time stamping, is not supported in all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Related topics:

- Fetching Data
- Acquiring Data Continuously

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| timeout | ViReal64 | The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. |
| numSamples | ViInt32 | The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function returns an error. |
| Output |  |  |
| Name | Type | Description |
| wfm | ViReal64* | Returns an array whose length is the numSamples times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms. NI-SCOPE returns this data sequentially, so all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values: index 0 = record 0, channel 0 index x = record 0, channel 1 index 2x = record 1, channel 0 index 3x = record 1, channel 1 Where x = the record length |
| wfmInfo | struct niScope_ wfmInfo* | Returns an array of structures with the following timing and scaling information about each waveform: relativeInitialX—the time (in seconds) from the trigger to the first sample in the fetched waveform absoluteInitialX—timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. xIncrement—the time between points in the acquired waveform in seconds actualSamples—the actual number of samples fetched and placed in the waveform array gain—the gain factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset offset—the offset factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset Call niScope_ActualNumWfms to determine the size of this array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetcharraymeasurement.html language=enus -->
## TOPIC 00137: niScope_FetchArrayMeasurement

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetcharraymeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetcharraymeasurement.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_FetchArrayMeasurement

#### C Function Prototype

ViStatus niScope_FetchArrayMeasurement (ViSession vi, ViConstString channelList, ViReal64 timeout, ViInt32 arrayMeasFunction, ViInt32 measWfmSize, ViReal64* measWfm, struct niScope_wfmInfo* wfmInfo);

#### Purpose

Obtains a waveform from the digitizer and returns the specified measurement array. This function may return multiple waveforms depending on the number of channels, the acquisition type, and the number of records you specify.

|  | Note Some functionality, such as time stamping, is not supported in all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| timeout | ViReal64 | The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. |
| arrayMeasFunction | ViInt32 | The array measurement to perform. |
| measWfmSize | ViInt32 | The maximum number of samples returned in the measurement waveform array for each waveform measurement. Use niScope_ActualMeasWfmSize to determine the number of available samples. Note Use the attribute NISCOPE_ATTR_FETCH_MEAS_NUM_SAMPLES to set the number of samples to fetch when performing a measurement. For more information about when to use this attribute, refer to the NI KnowledgeBase. |
|  | Note Use the attribute NISCOPE_ATTR_FETCH_MEAS_NUM_SAMPLES to set the number of samples to fetch when performing a measurement. For more information about when to use this attribute, refer to the NI KnowledgeBase. |  |
| Output |  |  |
| Name | Type | Description |
| measWfm | ViReal64* | Returns an array whose length is the number of waveforms times measWfmSize; call niScope_ActualNumWfms to determine the number of waveforms; call niScope_ActualMeasWfmSize to determine the size of each waveform. NI-SCOPE returns this data sequentially, so all record 0 waveforms are first. For example, with channel list of 0, 1, you would have the following index values: index 0 = record 0, channel 0 index x = record 0, channel 1 index 2x = record 1, channel 0 index 3x = record 1, channel 1 Where x = the record length |
| wfmInfo | struct niScope_ wfmInfo* | Returns an array of structures with the following timing and scaling information about each waveform: relativeInitialX—the time (in seconds) from the trigger to the first sample in the fetched waveform absoluteInitialX—timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. xIncrement—the time between points in the acquired waveform in seconds actualSamples—the actual number of samples fetched and placed in the waveform array gain—the gain factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset offset—the offset factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset Call niScope_ActualNumWfms to determine the size of this array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetchbinary16.html language=enus -->
## TOPIC 00138: niScope_FetchBinary16

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetchbinary16.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetchbinary16.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_FetchBinary16

#### C Function Prototype

ViStatus niScope_FetchBinary16 (ViSession vi, ViConstString channelList, ViReal64 timeout, ViInt32 numSamples, ViInt16* wfm, struct niScope_wfmInfo* wfmInfo);

#### Purpose

Retrieves data from a previously initiated acquisition and returns binary 16-bit waveforms. 
This function may return multiple waveforms depending on the number of channels, the acquisition type, 
and the number of records you specify.

Refer to [Using Fetch Functions](/csh?topicname=digitizers/using_fetch_functions.html) for more information on using this function.

|  | Note Some functionality, such as time stamping, is not supported in all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| timeout | ViReal64 | The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. |
| numSamples | ViInt32 | The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function returns an error. |
| Output |  |  |
| Name | Type | Description |
| wfm | ViInt16* | Returns an array whose length is the numSamples times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms. NI-SCOPE returns this data sequentially, so all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values: index 0 = record 0, channel 0 index x = record 0, channel 1 index 2x = record 1, channel 0 index 3x = record 1, channel 1 Where x = the record length |
| wfmInfo | struct niScope_ wfmInfo* | Returns an array of structures with the following timing and scaling information about each waveform: relativeInitialX—the time (in seconds) from the trigger to the first sample in the fetched waveform absoluteInitialX—timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. xIncrement—the time between points in the acquired waveform in seconds actualSamples—the actual number of samples fetched and placed in the waveform array gain—the gain factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset offset—the offset factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset Call niScope_ActualNumWfms to determine the size of this array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetchbinary32.html language=enus -->
## TOPIC 00139: niScope_FetchBinary32

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetchbinary32.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetchbinary32.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_FetchBinary32

#### C Function Prototype

ViStatus niScope_FetchBinary32 (ViSession vi, ViConstString channelList, ViReal64 timeout, ViInt32 numSamples, ViInt32* wfm, struct niScope_wfmInfo* wfmInfo);

#### Purpose

Retrieves data from a previously initiated acquisition and returns binary 32-bit waveforms. This function may return multiple waveforms depending on the number of channels, the acquisition type, and the number of records you specify.

Refer to [Using Fetch Functions](/csh?topicname=digitizers/using_fetch_functions.html) for more information on using this function.

|  | Note Some functionality, such as time stamping, is not supported in all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| timeout | ViReal64 | The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. |
| numSamples | ViInt32 | The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function returns an error. |
| Output |  |  |
| Name | Type | Description |
| wfm | ViInt32* | Returns an array whose length is the numSamples times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms. NI-SCOPE returns this data sequentially, so all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values: index 0 = record 0, channel 0 index x = record 0, channel 1 index 2x = record 1, channel 0 index 3x = record 1, channel 1 Where x = the record length |
| wfmInfo | struct niScope_ wfmInfo* | Returns an array of structures with the following timing and scaling information about each waveform: relativeInitialX—the time (in seconds) from the trigger to the first sample in the fetched waveform absoluteInitialX—timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. xIncrement—the time between points in the acquired waveform in seconds actualSamples—the actual number of samples fetched and placed in the waveform array gain—the gain factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset offset—the offset factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset Call niScope_ActualNumWfms to determine the size of this array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetchbinary8.html language=enus -->
## TOPIC 00140: niScope_FetchBinary8

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetchbinary8.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetchbinary8.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_FetchBinary8

#### C Function Prototype

ViStatus niScope_FetchBinary8 (ViSession vi, ViConstString channelList, ViReal64 timeout, ViInt32 numSamples, ViInt8* wfm, struct niScope_wfmInfo* wfmInfo);

#### Purpose

Retrieves data from a previously initiated acquisition and returns binary 8-bit waveforms. This function may return multiple waveforms depending on the number of channels, the acquisition type, and the number of records you specify.

Refer to [Using Fetch Functions](/csh?topicname=digitizers/using_fetch_functions.html) for more information on using this function.

|  | Note Some functionality, such as time stamping, is not supported in all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| timeout | ViReal64 | The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. |
| numSamples | ViInt32 | The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function returns an error. |
| Output |  |  |
| Name | Type | Description |
| wfm | ViInt8* | Returns an array whose length is the numSamples times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms. NI-SCOPE returns this data sequentially, so all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values: index 0 = record 0, channel 0 index x = record 0, channel 1 index 2x = record 1, channel 0 index 3x = record 1, channel 1 Where x = the record length |
| wfmInfo | struct niScope_ wfmInfo* | Returns an array of structures with the following timing and scaling information about each waveform: relativeInitialX—the time (in seconds) from the trigger to the first sample in the fetched waveform absoluteInitialX—timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. xIncrement—the time between points in the acquired waveform in seconds actualSamples—the actual number of samples fetched and placed in the waveform array gain—the gain factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset offset—the offset factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset Call niScope_ActualNumWfms to determine the size of this array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetchcomplex.html language=enus -->
## TOPIC 00141: niScope_FetchComplex

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetchcomplex.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetchcomplex.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_FetchComplex

#### C Function Prototype

niScope_FetchComplex (
ViSession vi,
ViConstString channelList,
ViReal64 timeout,
ViInt32 numSamples,
NIComplexNumber* wfm,
struct niScope_wfmInfo* wfmInfo);

#### Purpose

Retrieves data that the digitizer has acquired from a previously initiated acquisition and returns a one-dimensional array of complex, scaled waveforms.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| timeout | ViReal64 | The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. |
| numSamples | ViInt32 | The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function returns an error. |
| Output |  |  |
| Name | Type | Description |
| wfm | NIComplexNumber* | Returns an array whose length is the numSamples times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms. |
| wfmInfo | struct niScope_ wfmInfo* | Returns an array of structures with the following timing and scaling information about each waveform: relativeInitialX—the time (in seconds) from the trigger to the first sample in the fetched waveform absoluteInitialX—timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. xIncrement—the time between points in the acquired waveform in seconds actualSamples—the actual number of samples fetched and placed in the waveform array gain—the gain factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset offset—the offset factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset Call niScope_ActualNumWfms to determine the size of this array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetchcomplexbinary16.html language=enus -->
## TOPIC 00142: niScope_FetchComplexBinary16

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetchcomplexbinary16.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetchcomplexbinary16.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_FetchComplexBinary16

#### C Function Prototype

niScope_FetchComplexBinary16 (
ViSession vi,
ViConstString channelList,
ViReal64 timeout,
ViInt32 numSamples,
NIComplexI16* wfm,
Struct niScope_wfmInfo* wfmInfo);

#### Purpose

Retrieves data from single channels and records. Returns a one-dimensional array of complex binary 16-bit waveforms.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| timeout | ViReal64 | The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. |
| numSamples | ViInt32 | The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function returns an error. |
| Output |  |  |
| Name | Type | Description |
| wfm | NIComplexI16* | Returns an array whose length is the numSamples times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms. |
| wfmInfo | struct niScope_ wfmInfo* | Returns an array of structures with the following timing and scaling information about each waveform: relativeInitialX—the time (in seconds) from the trigger to the first sample in the fetched waveform absoluteInitialX—timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. xIncrement—the time between points in the acquired waveform in seconds actualSamples—the actual number of samples fetched and placed in the waveform array gain—the gain factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset offset—the offset factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset Call niScope_ActualNumWfms to determine the size of this array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetchmeasurement.html language=enus -->
## TOPIC 00143: niScope_FetchMeasurement

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetchmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetchmeasurement.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_FetchMeasurement

#### C Function Prototype

ViStatus niScope_FetchMeasurement (ViSession vi, ViConstString channelList, ViReal64 timeout, ViInt32 scalarMeasFunction, ViReal64* result);

#### Purpose

Fetches a waveform from the digitizer and performs the specified waveform measurement. 

Refer to [Using Fetch Functions](/csh?topicname=digitizers/using_fetch_functions.html) for more information.

Many of the measurements use the low, mid, and high reference levels. You configure the low, mid, and high references by using [NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL](/csh?topicname=scopefunc/cviniscope_attr_meas_chan_low_ref_level.html), [NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL](/csh?topicname=scopefunc/cviniscope_attr_meas_chan_mid_ref_level.html), and [NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL](/csh?topicname=scopefunc/cviniscope_attr_meas_chan_high_ref_level.html) to set each channel differently.

#### Related topics:

- Making Waveform Measurements

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| timeout | ViReal64 | The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. |
| scalarMeasFunction | ViInt32 | The scalar measurement to be performed. |
| Output |  |  |
| Name | Type | Description |
| result | ViReal64* | Contains an array of all measurements acquired; call niScope_ActualNumWfms to determine the array length. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetchmeasurementstats.html language=enus -->
## TOPIC 00144: niScope_FetchMeasurementStats

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetchmeasurementstats.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetchmeasurementstats.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_FetchMeasurementStats

#### C Function Prototype

ViStatus niScope_FetchMeasurementStats (ViSession vi, ViConstString channelList, ViReal64 timeout, ViInt32 scalarMeasFunction, ViReal64* result, ViReal64* mean, ViReal64* stdev, ViReal64* min, ViReal64* max, ViInt32*numInStats);

#### Purpose

Obtains a waveform measurement and returns the measurement value. This function may return multiple statistical results depending on the number of channels, the acquisition type, and the number of records you specify.

You specify a particular measurement type, such as rise time, frequency, or voltage peak-to-peak. The waveform on which the digitizer calculates the waveform measurement is from an acquisition that you previously initiated. The statistics for the specified measurement function are returned, where the statistics are updated once every acquisition when the specified measurement is fetched by any of the Fetch Measurement functions. If a Fetch Measurement function has not been called, this function fetches the data on which to perform the measurement. The statistics are cleared by calling [niScope_ClearWaveformMeasurementStats](/csh?topicname=scopefunc/cviniscope_clearwaveformmeasurementstats.html). Refer to [Using Fetch Functions](/csh?topicname=digitizers/using_fetch_functions.html) for more information on incorporating fetch functions in your application.

Many of the measurements use the low, mid, and high reference levels. You configure the low, mid, and high references with [NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL](/csh?topicname=scopefunc/cviniscope_attr_meas_chan_low_ref_level.html), [NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL](/csh?topicname=scopefunc/cviniscope_attr_meas_chan_mid_ref_level.html), and [NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL](/csh?topicname=scopefunc/cviniscope_attr_meas_chan_high_ref_level.html) to set each channel differently.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| timeout | ViReal64 | The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. |
| scalarMeasFunction | ViInt32 | The scalar measurement to be performed on each fetched waveform. |
| Output |  |  |
| Name | Type | Description |
| result | ViReal64* | Returns the resulting measurement |
| mean | ViReal64* | Returns the mean scalar value, which is obtained by averaging each niScope_FetchMeasurementStats call. |
| stdev | ViReal64* | Returns the standard deviation of the most recent numInStats measurements. |
| min | ViReal64* | Returns the smallest scalar value acquired (the minimum of the numInStats measurements). |
| max | ViReal64* | Returns the largest scalar value acquired (the maximum of the numInStats measurements). |
| numInStats | ViInt32* | Returns the number of times niScope_FetchMeasurementStats has been called. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetchwaveform.html language=enus -->
## TOPIC 00145: niScope_FetchWaveform

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetchwaveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetchwaveform.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_FetchWaveform

#### C Function Prototype

ViStatus niScope_FetchWaveform (ViSession vi, ViConstString channel, ViInt32 waveformSize, ViReal64[] waveform, ViInt32* actualPoints, ViReal64* initialX, ViReal64* xIncrement);

#### Purpose

|  | Note This function is included for compliance with the IviScope Class Specification. |
| --- | --- |

Returns the waveform from a previously initiated acquisition that the digitizer acquires for the channel you specify.

[niScope_InitiateAcquisition](/csh?topicname=scopefunc/cviniscope_initiateacquisition.html) starts an acquisition on the channels that you enable with [niScope_ConfigureVertical](/csh?topicname=scopefunc/cviniscope_configurevertical.html). The digitizer acquires waveforms for the enabled channels concurrently. You use [niScope_AcquisitionStatus](/csh?topicname=scopefunc/cviniscope_acquisitionstatus.html) to determine when the acquisition is complete. You must call this function separately for each enabled channel to obtain the waveforms.

You can call [niScope_ReadWaveform](/csh?topicname=scopefunc/cviniscope_readwaveform.html) instead of [niScope_InitiateAcquisition](/csh?topicname=scopefunc/cviniscope_initiateacquisition.html). [niScope_ReadWaveform](/csh?topicname=scopefunc/cviniscope_readwaveform.html) starts an acquisition on all enabled channels, waits for the acquisition to complete, and returns the waveform for the channel you specify. Call this function to obtain the waveforms for each of the remaining channels.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channel | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. Default Value: "0" |
| waveformSize | ViInt32 | The number of elements to insert into the waveform array. |
| Output |  |  |
| Name | Type | Description |
| waveform | ViReal64[] | Returns the waveform that the digitizer acquires. Units: voltsNotes:If the digitizer cannot sample a point in the waveform, this function returns an error. |
| actualPoints | ViInt32* | Indicates the actual number of points the function placed in the waveform array. |
| initialX | ViReal64* | Indicates the time of the first point in the waveform array relative to the Reference Position. Units: seconds For example, if the digitizer acquires the first point in the waveform array 1 second before the trigger, this parameter returns the value –1.0. If the acquisition of the first point occurs at the same time as the trigger, this parameter returns the value 0.0. |
| xIncrement | ViReal64* | Indicates the length of time between points in the waveform array. Units: seconds |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_fetchwaveformmeasurement.html language=enus -->
## TOPIC 00146: niScope_FetchWaveformMeasurement

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_fetchwaveformmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_fetchwaveformmeasurement.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_FetchWaveformMeasurement

#### C Function Prototype

ViStatus niScope_FetchWaveformMeasurement (ViSession vi, ViConstString channel, ViInt32 measFunction, ViReal64* measurement);

#### Purpose

|  | Notes This function is included for compliance with the IviScope Class Specification. You can use niScope_ReadWaveformMeasurement instead of this function. niScope_ReadWaveformMeasurement starts an acquisition on all enabled channels, waits for the acquisition to complete, obtains a waveform measurement on the specified channel, and returns the waveform for the specified channel. Call this function separately to obtain any other waveform measurements on a specific channel. |
| --- | --- |

Configure the appropriate reference 
levels before calling this function. You can configure the low, mid, and high references by setting the 
following attributes:

[NISCOPE_ATTR_MEAS_HIGH_REF](/csh?topicname=scopefunc/cviniscope_attr_meas_high_ref.html) 
[NISCOPE_ATTR_MEAS_LOW_REF](/csh?topicname=scopefunc/cviniscope_attr_meas_low_ref.html) 
[NISCOPE_ATTR_MEAS_MID_REF](/csh?topicname=scopefunc/cviniscope_attr_meas_mid_ref.html)

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channel | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. Default Value: "0" |
| measFunction | ViInt32 | Characteristic of the acquired waveform to be measured. |
| Output |  |  |
| Name | Type | Description |
| measurement | ViReal64* | The measured value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_getattributeviboolean.html language=enus -->
## TOPIC 00147: niScope_GetAttributeViBoolean

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_getattributeviboolean.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_getattributeviboolean.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_GetAttributeViBoolean

#### C Function Prototype

ViStatus niScope_GetAttributeViBoolean (ViSession vi, ViConstString channelList, ViAttr attributeID, ViBoolean* value);

#### Purpose

Queries the value of a ViBoolean attribute. You can use this function to get the values of instrument-specific attributes and inherent IVI attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| value | ViBoolean* | Returns the current value of the attribute; pass the address of a ViBoolean variable. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_getattributeviint32.html language=enus -->
## TOPIC 00148: niScope_GetAttributeViInt32

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_getattributeviint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_getattributeviint32.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_GetAttributeViInt32

#### C Function Prototype

ViStatus niScope_GetAttributeViInt32 (ViSession vi, ViConstString channelList, ViAttr attributeID, ViInt32* value);

#### Purpose

Queries the value of a ViInt32 attribute. You can use this function to
 get the values of instrument-specific attributes and inherent IVI attributes. If the attribute represents an 
 instrument state, this function performs instrument I/O in the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| value | ViInt32* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_getattributeviint64.html language=enus -->
## TOPIC 00149: niScope_GetAttributeViInt64

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_getattributeviint64.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_getattributeviint64.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_GetAttributeViInt64

#### C Function Prototype

ViStatus niScope_GetAttributeViInt64 (ViSession vi, ViConstString channelList, ViAttr attributeID, ViInt64* value);

#### Purpose

Queries the value of a ViInt64 attribute. You can use this function to
 get the values of instrument-specific attributes and inherent IVI attributes. If the attribute represents an 
 instrument state, this function performs instrument I/O in the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| Output |  |  |
| Name | Type | Description |
| value | ViInt64* | Returns the current value of the attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_getnextinterchangewarning.html language=enus -->
## TOPIC 00150: niScope_GetNextInterchangeWarning

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_getnextinterchangewarning.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_getnextinterchangewarning.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_GetNextInterchangeWarning

#### C Function Prototype

ViStatus niScope_GetNextInterchangeWarning (ViSession vi, ViInt32 bufferSize, ViChar[] interchangeWarning);

#### Purpose

|  | Note This function is included for compliance with the IviScope Class Specification. |
| --- | --- |

Returns the interchangeability warnings associated with the IVI session. It retrieves and clears the oldest instance in which the class driver recorded an interchangeability warning. Interchangeability warnings indicate that using your 
application with a different instrument might cause different behavior.

Use this function to retrieve interchangeability warnings. The driver performs interchangeability checking 
when [NISCOPE_ATTR_INTERCHANGE_CHECK](/csh?topicname=scopefunc/cviniscope_attr_interchange_check.html) is set to 

VI_TRUE. The function returns an empty string in the **interchangeWarning** parameter if no 
interchangeability warnings remain for the session.

In general, the instrument driver generates interchangeability warnings when an attribute that affects the behavior of the instrument is in a state that you did not specify.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| bufferSize | ViInt32 | Passes the number of bytes in the ViChar array you specify for the Description parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies bufferSize; – 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the Buffer Size is 4, the function places "123" into the buffer and returns 7. If you pass a negative number, the function copies the value to the buffer regardless of the number of bytes in the value.If you pass 0, you can pass VI_NULL for the Description buffer parameter. |
| Output |  |  |
| Name | Type | Description |
| interchangeWarning | ViChar[] | Returns the next interchange warning for the IVI session. If there are no interchange warnings, the function returns an empty string. The buffer must contain at least as many elements as the value you specify with the bufferSize parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_getnormalizationcoefficients.html language=enus -->
## TOPIC 00151: niScope_GetNormalizationCoefficients

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_getnormalizationcoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_getnormalizationcoefficients.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_GetNormalizationCoefficients

ViStatus _VI_FUNC niScope_GetNormalizationCoefficients (ViSession vi,
 ViConstString channelList,
 ViInt32 bufferSize,
 struct niScope_coefficientInfo coefficientInfo[],
 ViInt32* numberOfCoefficientSets);

#### Purpose

Returns coefficients that can be used to convert binary data to normalized and calibrated data.

Refer to 
[Scaling and Normalization of Binary Data](/csh?topicname=digitizers/scaling_and_norm_binary_data.html) for more information about how to use this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channel List | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| bufferSize | ViInt32 | The array size for the coefficentInfo parameter. To determine the size of the buffer to allocate for coefficientInfo, pass a value of 0 to the buffersize parameter and a value of NULL to the coefficientInfo parameter. In this case, the return value of the numberOfCoefficientSets parameter is the size of the array necessary to hold the coefficient structures. Allocate an array of niScope_coefficientInfo structures of this size, then call this function again (with the correct bufferSize parameter) to retrieve the actual values. |
| coefficientInfo | struct niScope_coefficientInfo | An array of structures containing gain and offset coefficients for a given channel. |
| Output |  |  |
| Name | Type | Description |
| numberOfCoefficientSets | ViInt32* | Returns the number of coefficient sets returned in the coefficientInfo array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_getscalingcoefficients.html language=enus -->
## TOPIC 00152: niScope_GetScalingCoefficients

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_getscalingcoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_getscalingcoefficients.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_GetScalingCoefficients

ViStatus _VI_FUNC niScope_GetScalingCoefficients (ViSession vi, 
 ViConstString channelList,
 ViInt32 bufferSize,
 struct niScope_coefficientInfo coefficientInfo[],
 ViInt32* numberOfCoefficientSets);

#### Purpose

Returns coefficients that can be used to scale binary data to volts.

Refer to 
[Scaling and Normalization of Binary Data](/csh?topicname=digitizers/scaling_and_norm_binary_data.html) for more information about how to use this function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| bufferSize | ViInt32 | The array size for the coefficentInfo parameter. To determine the size of the buffer to allocate for coefficientInfo, pass a value of 0 to the buffersize parameter and a value of NULL to the coefficientInfo parameter. In this case, the return value of the numberOfCoefficientSets parameter is the size of the array necessary to hold the coefficient structures. Allocate an array of niScope_coefficientInfo structures of this size, then call this function again (with the correct bufferSize parameter) to retrieve the actual values. |
| coefficientInfo | struct niScope_coefficientInfo | An array of structures containing gain and offset coefficients for a given channel. |
| Output |  |  |
| Name | Type | Description |
| numberOfCoefficientSets | ViInt32 | Returns the number of coefficient sets returned in the coefficientInfo array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_getstreamendpointhandle.html language=enus -->
## TOPIC 00153: niScope_GetStreamEndpointHandle

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_getstreamendpointhandle.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_getstreamendpointhandle.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_GetStreamEndpointHandle

ViStatus niScope_GetStreamEndpointHandle (ViSession vi, 
 ViConstString Stream_Name,
 ViUInt32 *Writer_Handle);

#### Purpose

Returns a writer endpoint that can be used with NI-P2P to configure a peer-to-peer stream with a digitizer endpoint.

#### Related topics:

- Peer-to-Peer Streaming

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| Stream_Name | ViConstString | The stream endpoint FIFO to configure. Refer to the device-specific documentation for peer-to-peer streaming in the High-Speed Digitizers Help for more information. |
| Output |  |  |
| Name | Type | Description |
| Writer_Handle | ViUInt32 | Returns a reference to a peer-to-peer writer FIFO that can be used to create a peer-to-peer streaming session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_importattributeconfigurationfile.html language=enus -->
## TOPIC 00154: niScope_ImportAttributeConfigurationFile

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_importattributeconfigurationfile.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_importattributeconfigurationfile.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ImportAttributeConfigurationFile

ViStatus niScope_ImportAttributeConfigurationFile (ViSession vi, ViConstString filePath);

#### Purpose

Imports an attribute configuration to the session from the specified file.

You can export and import session attribute configurations only between NI‑SCOPE devices with identical bus types, model numbers, channel counts, and onboard memory sizes and between NI-SCOPE sessions with the same number of initialized channels..

|  | Note You cannot call this function while the session is in a running state, such as while acquiring a signal. |
| --- | --- |

**Device Mapping Behavior**

When exporting and importing configurations between NI‑SCOPE sessions that were both initialized with multiple instruments, the configurations of the exporting instruments are mapped to the importing instruments in the order you specify in the **resourceName** input to the [niScope_InitWithOptions](/csh?topicname=scopefunc/cviniscope_initwithoptions.html) or [niScope_init](/csh?topicname=scopefunc/cviniscope_init.html) functions.

For example, if your entry for **resourceName** is PXI1Slot1,PXI1Slot2 for the exporting session and PXI2Slot2,PXI2Slot3 for the importing session:

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

|  | Note NI-SCOPE will return an error if the total number of channels initialized for the exporting session is not equal to the total number of channels initialized for the importing session. |
| --- | --- |

**Related Topics:**

[Attributes and Attribute Functions](/csh?topicname=digitizers/attributes_and_attribute_functions.html)

[Setting Attributes Before Reading Attributes](/csh?topicname=digitizers/setting_before_reading_attributes.html)

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| filePath | ViConstString | The absolute path to the file that contains the attribute configuration to import. If you specify an empty or relative path, this function returns an error.Default File Extension: .niscopeconfig |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_initwithoptions.html language=enus -->
## TOPIC 00155: niScope_InitWithOptions

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_initwithoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_initwithoptions.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_InitWithOptions

#### C Function Prototype

ViStatus niScope_InitWithOptions (ViRsrc 
resourceName, ViBoolean IDQuery, ViBoolean resetDevice, ViString optionString, 
ViSession* newVi);

#### Purpose

Performs the following initialization actions:

- Creates a new IVI instrument driver session and optionally sets the initial state 
 of the following session properties: Range Check, Cache, Simulate, Record 
 Value Coercions
- Opens a session to the device(s) specified using the interface and address 
 you use for the resourceName
- Queries each instrument ID and verifies that it is valid for this 
 instrument driver
- Resets the digitizer(s) to a known state if resetDevice is set 
 to VI_TRUE
- Returns an instrument handle that you use to identify the instrument(s) in 
 all subsequent instrument driver function calls

#### Related topics:

- NI-SCOPE Programming Flow

#### Parameters

| Input |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Description |  |
| resourceName | ViRsrc | Specifies the device name assigned by Measurement & Automation Explorer (MAX) to an NI-SCOPE instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot3,PXI1Slot4, where PXI1Slot3 is one instrument resource name and PXI1Slot4 is another. Note You can only specify multiple instruments of identical model numbers, bus types, channel counts, and onboard memory sizes. The instruments must be in the same chassis. resourceName Examples Example # Device Type Syntax Variable 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1, you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Note NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must make sure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. |  |
|  | Note You can only specify multiple instruments of identical model numbers, bus types, channel counts, and onboard memory sizes. The instruments must be in the same chassis. |  |  |
| Example # | Device Type | Syntax | Variable |
| 1 | NI-DAQmx device | myDAQmxDevice | (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice | (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 | (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName | (myLogicalName = name) |
|  | Note NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must make sure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. |  |  |
| idQuery | ViBoolean | Specify whether to perform an ID query. When you set this parameter to VI_TRUE, NI-SCOPE verifies that the device you initialize is a type that it supports. When you set this parameter to VI_FALSE, the function initializes the device without performing an ID query. Defined Values VI_TRUE—Perform ID query VI_FALSE—Skip ID query Default Value: VI_TRUE |  |
| resetDevice | ViBoolean | Specify whether to reset the device during the initialization process. Default Value: VI_TRUE Defined Values VI_TRUE (1)—Reset device VI_FALSE (0)—Do not reset device |  |
| optionString |  | Specifies initialization commands. The following table lists the attributes and the name you use in the optionString to identify the attribute. Attribute Name Attribute Values RangeCheck - NISCOPE_ATTR_RANGE_CHECK VI_TRUE, VI_FALSE QueryInstrStatus - NISCOPE_QUERY_INSTRUMENT_STATUS VI_TRUE, VI_FALSE Cache - NISCOPE_ATTR_CACHE VI_TRUE, VI_FALSE Simulate - NISCOPE_ATTR_SIMULATE VI_TRUE, VI_FALSE Default Values: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1" You can use the option string to simulate a device. The DriverSetup flag specifies the model that is to be simulated and the type of the model. One example to simulate a PXI-5105 would be as follows: Option String: Simulate = 1, DriverSetup = Model:5105; BoardType:PXI Refer to the example niScope EX Simulated Acquisition for more information on simulation. You can also use the option string to attach an accessory such as the PXI-5900 to your digitizer session to allow the seamless use of the accessory: Option String: DriverSetup = Accessory:Dev1 Refer to the example niScope EX External Amplifier for more information. |  |
| Attribute Name | Attribute Values |  |  |
| RangeCheck - NISCOPE_ATTR_RANGE_CHECK | VI_TRUE, VI_FALSE |  |  |
| QueryInstrStatus - NISCOPE_QUERY_INSTRUMENT_STATUS | VI_TRUE, VI_FALSE |  |  |
| Cache - NISCOPE_ATTR_CACHE | VI_TRUE, VI_FALSE |  |  |
| Simulate - NISCOPE_ATTR_SIMULATE | VI_TRUE, VI_FALSE |  |  |
| Output |  |  |  |
| Name | Type | Description |  |
| vi | ViSession* | Returns a session handle that you can use to identify the device in all subsequent NI-SCOPE function calls. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_locksession.html language=enus -->
## TOPIC 00156: niScope_LockSession

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_locksession.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_locksession.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_LockSession

#### C Function Prototype

ViStatus niScope_LockSession (ViSession vi, ViBoolean* callerHasLock);

#### Purpose

Obtains a multithread lock on the instrument session. Before doing so, it waits until all other execution threads have released their locks on the instrument session. Other threads might have obtained a lock on this session in the following ways:

- Your application called niScope_LockSession
- A call to the instrument driver locked the session
- A call to the IVI engine locked the session

After your call to niScope_LockSession returns successfully, no other threads can access the instrument session until you call [niScope_UnlockSession](/csh?topicname=scopefunc/cviniscope_unlocksession.html). Use niScope_LockSession and niScope_UnlockSession around a sequence of calls to instrument driver functions if you require that the instrument retain its settings through the end of the sequence.

You can safely make nested calls to niScope_LockSession within the same thread. To completely unlock the session, you must balance each call to niScope_LockSession with a call to niScope_UnlockSession. If, however, you use the **callerHasLock** in all calls to niScope_LockSession and niScope_UnlockSession within a function, the IVI Library locks the session only once within the function regardless of the number of calls you make to niScope_LockSession. This allows you to call niScope_UnlockSession just once at the end of the function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| Output |  |  |
| Name | Type | Description |
| callerHasLock | ViBoolean* | This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL. Use this parameter in complex functions to keep track of whether you have obtained a lock and therefore need to unlock the session. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to niScope_LockSession or niScope_UnlockSession in the same function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_probecompensationsignalstop.html language=enus -->
## TOPIC 00157: niScope_ProbeCompensationSignalStop

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_probecompensationsignalstop.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_probecompensationsignalstop.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ProbeCompensationSignalStop

#### C Function Prototype

ViStatus niScope_ProbeCompensationSignalStop (ViSession vi);

#### Purpose

Disables the 1 kHz square wave signal for probe compensation.

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_read.html language=enus -->
## TOPIC 00158: niScope_Read

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_read.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_read.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_Read

#### C Function Prototype

ViStatus niScope_Read (ViSession vi, ViConstString channelList, ViReal64 timeout, ViInt32 numSamples, ViReal64* wfm, struct niScope_wfmInfo* wfmInfo);

#### Purpose

Initiates an acquisition, waits for it to complete, and retrieves the data. The process is similar to calling [niScope_InitiateAcquisition](/csh?topicname=scopefunc/cviniscope_initiateacquisition.html), 
[niScope_AcquisitionStatus](/csh?topicname=scopefunc/cviniscope_acquisitionstatus.html), and 
[niScope_Fetch](/csh?topicname=scopefunc/cviniscope_fetch.html). The only difference is that with niScope_Read, you enable all channels specified with **channelList** before the acquisition; in the other method, you enable the channels with [niScope_ConfigureVertical](/csh?topicname=scopefunc/cviniscope_configurevertical.html).

This function may return multiple waveforms depending on the number of channels, the acquisition type, and the number of records you specify.

|  | Note Some functionality is not supported in all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

#### Related topics:

- Acquisition Functions
- NI-SCOPE Programming Flow

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| timeout | ViReal64 | The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. |
| numSamples | ViInt32 | The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function returns an error. |
| Output |  |  |
| Name | Type | Description |
| wfm | ViReal64* | Returns an array whose length is the numSamples times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms. NI-SCOPE returns this data sequentially, so all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values: index 0 = record 0, channel 0 index x = record 0, channel 1 index 2x = record 1, channel 0 index 3x = record 1, channel 1 Where x = the record length |
| wfmInfo | struct niScope_ wfmInfo* | Returns an array of structures with the following timing and scaling information about each waveform: relativeInitialX—the time (in seconds) from the trigger to the first sample in the fetched waveform absoluteInitialX—timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. xIncrement—the time between points in the acquired waveform in seconds actualSamples—the actual number of samples fetched and placed in the waveform array gain—the gain factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset offset—the offset factor of the given channel; useful for scaling binary data with the following formula: voltage = binary data × gain factor + offset Call niScope_ActualNumWfms to determine the size of this array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_readwaveformmeasurement.html language=enus -->
## TOPIC 00159: niScope_ReadWaveformMeasurement

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_readwaveformmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_readwaveformmeasurement.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_ReadWaveformMeasurement

#### C Function Prototype

ViStatus niScope_ReadWaveformMeasurement (ViSession vi, ViConstString channel, ViInt32 measFunction, ViInt32 maxTime, ViReal64* measurement);

#### Purpose

|  | Note This function is included for compliance with the IviScope Class Specification. |
| --- | --- |

Initiates a new waveform acquisition and returns a specified waveform measurement from a specific channel.

This function initiates an acquisition on the channels that you enable with the [niScope_ConfigureVertical](/csh?topicname=scopefunc/cviniscope_configurevertical.html) function. It then waits for the acquisition to complete, obtains a waveform measurement on the channel you specify, and returns the measurement value. You specify a particular measurement type, such as rise time, frequency, or voltage peak-to-peak.

You can call the [niScope_FetchWaveformMeasurement](/csh?topicname=scopefunc/cviniscope_fetchwaveformmeasurement.html) function separately to obtain any other waveform measurement on a specific channel without initiating another acquisition.

You must configure the appropriate reference levels before calling this function. Configure the low, mid, and high references by calling [niScope_ConfigureRefLevels](/csh?topicname=scopefunc/cviniscope_configurereflevels.html) or by setting the following attributes:

[NISCOPE_ATTR_MEAS_HIGH_REF](/csh?topicname=scopefunc/cviniscope_attr_meas_high_ref.html) 
[NISCOPE_ATTR_MEAS_LOW_REF](/csh?topicname=scopefunc/cviniscope_attr_meas_low_ref.html) 
[NISCOPE_ATTR_MEAS_MID_REF](/csh?topicname=scopefunc/cviniscope_attr_meas_mid_ref.html)

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channel | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. Default Value: "0" |
| measFunction | ViInt32 | The scalar measurement to perform. |
| maxTime | ViInt32 | Pass the maximum length of time in which to allow the read waveform operation to complete. If the operation does not complete within this time interval, the function returns the NISCOPE_ERROR_MAX_TIME_EXCEEDED error code. When this occurs, you can call niScope_Abort to cancel the read waveform operation and return the digitizer to the idle state.Units: milliseconds |
| Output |  |  |
| Name | Type | Description |
| measurement | ViReal64* | The measured value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_setattributeviint32.html language=enus -->
## TOPIC 00160: niScope_SetAttributeViInt32

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_setattributeviint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_setattributeviint32.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_SetAttributeViInt32

#### C Function Prototype

ViStatus niScope_SetAttributeViInt32 (ViSession vi, ViConstString channelList, ViAttr attributeID, ViInt32 value);

#### Purpose

Sets the value of a ViInt32 attribute. This is a low-level function that you can use to set the values of instrument-specific attributes and inherent IVI attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid or is different than the value you specify.

|  | Note NI-SCOPE contains high-level functions that set most of the instrument attributes. Use the high-level functions as much as possible because they handle order dependencies and multithread locking for you. In addition, high-level functions perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the Set Attribute functions, the functions check the instrument status after each call. Also, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| value | ViInt32 | The value that you want to set the attribute. Some values might not be valid depending on the current settings of the instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_setattributevisession.html language=enus -->
## TOPIC 00161: niScope_SetAttributeViSession

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_setattributevisession.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_setattributevisession.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_SetAttributeViSession

#### C Function Prototype

ViStatus niScope_SetAttributeViSession (ViSession vi, ViConstString channelList, ViAttr attributeID, ViSession value);

#### Purpose

Sets the value of a ViSession attribute. This is a low-level function that you can use to set the values of instrument-specific attributes and inherent IVI attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid or is different than the value you specify.

|  | Note NI-SCOPE contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible because they handle order dependencies and multithread locking for you. In addition, the high-level functions perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the Set Attribute functions, the functions check the instrument status after each call. Also, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| value | ViSession | The value that you want to set the attribute to. Some values might not be valid depending on the current settings of the instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_setattributevistring.html language=enus -->
## TOPIC 00162: niScope_SetAttributeViString

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_setattributevistring.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_setattributevistring.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_SetAttributeViString

#### C Function Prototype

ViStatus niScope_SetAttributeViString (ViSession vi, ViConstString channelList, ViAttr attributeID, ViConstString value);

#### Purpose

Sets the value of a ViString attribute.

This is a low-level function that you can use to set the values of 
instrument-specific attributes and inherent IVI attributes. 
If the attribute represents an instrument state, this function performs instrument I/O in 
the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid or is different than the value you specify.

|  | Note NI-SCOPE contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible because they handle order dependencies and multithread locking for you. In addition, the high-level functions perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call. Also, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| channelList | ViConstString | The channel to configure. For more information, refer to Channel String Syntax. |
| attributeID | ViAttr | The ID of an attribute. |
| value | ViConstString | The value that you want to set the attribute to. Some values might not be valid depending on the current settings of the instrument session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/cviniscope_unlocksession.html language=enus -->
## TOPIC 00163: niScope_UnlockSession

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/cviniscope_unlocksession.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/cviniscope_unlocksession.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niScope_UnlockSession

#### C Function Prototype

ViStatus niScope_UnlockSession (ViSession vi, ViBoolean* callerHasLock);

#### Purpose

Releases a lock that you acquired on an instrument session using [niScope LockSession](/csh?topicname=scopefunc/cviniscope_locksession.html).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | The instrument handle you obtain from niScope_init that identifies a particular instrument session. |
| Output |  |  |
| Name | Type | Description |
| callerHasLock | ViBoolean* | This parameter serves as a convenience; if you do not want to use this parameter, pass VI_NULL. Use this parameter in complex functions to keep track of whether you have obtained a lock and therefore need to unlock the session; pass the address of a local ViBoolean variable; in the declaration of the local variable, initialize it to VI_FALSE; pass the address of the same local variable to any other calls you make to niScope_LockSession or niScope_UnlockSession in the same function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call niScope_GetErrorMessage. To obtain additional information concerning the error condition, use niScope_GetError and niScope_ClearError. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/ivi-obsolete.html language=enus -->
## TOPIC 00164: IVI Compliance and Obsolete Functions

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/ivi-obsolete.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/ivi-obsolete.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### IVI Compliance and Obsolete Functions

Expand this book to view the IVI compliance and obsolete functions in NI-SCOPE.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/ni_scope_function_reference_help.html language=enus -->
## TOPIC 00165: NI-SCOPE Function Reference Help

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/ni_scope_function_reference_help.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/ni_scope_function_reference_help.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-SCOPE Function Reference Help

May 2020

This help file provides C/C++/VB programming support for NI-SCOPE, the National Instruments driver that communicates with your high-speed digitizer. 
This help file describes the NI-SCOPE functions and attributes you can use to configure and operate NI high-speed digitizers.

© 2001–2020 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/niscope_attributes.html language=enus -->
## TOPIC 00166: NI-SCOPE Attributes

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/niscope_attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/niscope_attributes.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-SCOPE Attributes

Expand this book to view the NI-SCOPE attributes.

<!--NI_TOPIC bundle=ni-scope-c-api-ref path=scopefunc/niscope_functions.html language=enus -->
## TOPIC 00167: NI-SCOPE Function Tree

- bundle_id: `ni-scope-c-api-ref`
- source_path: `scopefunc/niscope_functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-c-api-ref/raw/resource/enus/scopefunc/niscope_functions.html
- document_id: `ni-scope-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-SCOPE Function Tree

Expand this book to view the NI-SCOPE functions.
