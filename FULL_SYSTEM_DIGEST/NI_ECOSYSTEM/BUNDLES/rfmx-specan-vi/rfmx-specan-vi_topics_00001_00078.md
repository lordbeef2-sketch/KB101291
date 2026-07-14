# NI DOCUMENT BUNDLE: rfmx-specan-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-specan-vi start=1 end=78 -->
<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/markers_pal.html language=enus -->
## TOPIC 00001: rfmxspecanvi/markers_pal.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/markers_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/markers_pal.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

Marker

Marker

Owning Palette:

RFmx SpecAn VIs

Use the VIs on this palette to configure marker measurements.

| Palette Object | Description |
| --- | --- |
| RFmxSpecAn Marker Configure Number of Markers | Configures the number of markers. |
| RFmxSpecAn Marker Configure Type | Configures the marker type. Use "marker<n>" as the selector string to configure this VI. |
| RFmxSpecAn Marker Configure Reference Marker | Configures the reference marker to a delta marker. Use "marker<n>" as the selector string to configure this VI. |
| RFmxSpecAn Marker Configure X Location | Configures the X location of the marker. You must configure the reference marker X location or perform peak search on the reference marker before configuring the X location for the Delta marker. Use "marker<n>" as the selector string to configure this VI. |
| RFmxSpecAn Marker Configure Y Location | Configures the Y location of the marker. You must configure the reference marker Y location or perform peak search on the reference marker before configuring the X location for the Delta marker. Use "marker<n>" as the selector string to configure this VI. |
| RFmxSpecAn Marker Configure Threshold | Configures the threshold to use for peak search. |
| RFmxSpecAn Marker Configure Trace | Configures the measurement trace to be used by the marker. Use "marker<n>" as the selector string to configure this VI. |
| RFmxSpecAn Marker Peak Search | Moves the marker to the highest peak that satisfies peak threshold and peak excursion criteria. Use "marker<n>" as the selector string to read results from this VI. |
| RFmxSpecAn Marker Next Peak | Moves the marker to the next highest or next left or next right peak above the threshold on the configured trace. Use "marker<n>" as the selector string to read results from this VI. |
| RFmxSpecAn Marker Configure Peak Excursion | Configures the peak excursion. |
| RFmxSpecAn Marker Fetch XY | Returns the X and Y locations of the marker. |
| RFmxSpecAn Build Marker String2 | Creates selector string for use with marker configuration or fetch properties and VIs. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/nf_pal.html language=enus -->
## TOPIC 00002: rfmxspecanvi/nf_pal.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/nf_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/nf_pal.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

NF

NF

Owning Palette:

Configuration

Use the VIs on this palette to configure NF measurements. You can also use the RFmxSpecAn Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxSpecAn NF Configure Frequency List | Configures the list of frequencies at which to perform the noise figure (NF) measurement. |
| RFmxSpecAn NF Configure Measurement Bandwidth | Configures the effective noise-bandwidth in which power measurements are performed in the noise figure (NF) measurement. |
| RFmxSpecAn NF Configure Measurement Interval | Configures the duration for which the signals are acquired at each frequency to perform the noise figure (NF) measurement. |
| RFmxSpecAn NF Configure Measurement Method | Configures the noise figure (NF) measurement to use either the Y-factor or the cold source method. |
| RFmxSpecAn NF Configure Y-Factor Mode | Configures the Y-Factor based noise figure (NF) measurement to perform the calibration step or the measurement step. |
| RFmxSpecAn NF Configure Y-Factor Noise Source ENR | Configures excess noise ratio (ENR) and temperature of the noise source used by the Y-factor method. |
| RFmxSpecAn NF Configure Y-Factor Noise Source Settling Time | Configures the time required for the acquisition to wait till the noise source used in the Y-Factor method settles to hot or cold state when the noise source is powered on or off. |
| RFmxSpecAn NF Configure Y-Factor Noise Source Loss | Configures the ohmic loss inherent to the noise source used in the Y-Factor method that is common to the calibration and the measurement steps. |
| RFmxSpecAn NF Configure Cold Source Mode | Configures the cold source based noise figure (NF) measurement to perform the calibration step or the measurement step. |
| RFmxSpecAn NF Configure Cold Source Input Termination | Configures the characteristics of the microwave termination used as a noise source in the cold source method. |
| RFmxSpecAn NF Configure Cold Source DUT S-Parameters | Configures the scattering parameters of the DUT as a function of the frequency, for use in the cold source measurement method. |
| RFmxSpecAn Configure Loss | Configures the loss. |
| RFmxSpecAn NF Configure Averaging | Configures averaging for the noise figure (NF) measurement. |
| RFmxSpecAn NF Clear Calibration Database | Clear the noise figure calibration data for Cold Source and Y-Factor method. Calibration data associated with the selected VSA is cleared for the Cold Source method while calibration data associated with the noise source name and the VSA is cleared for the Y-Factor method. |
| RFmxSpecAn NF Recommend Reference Level | Computes and sets an appropriate reference level based on the expected maximum DUT gain, maximum DUT noise figure, and other measurement and analyzer properties. You must not set Mixer Level, Mixer Level Offset, IF Output Power Level Offset, and IF Filter Bandwidth properties in order to obtain an appropriate recommended reference level. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_acp_configure_offset_power_reference.html language=enus -->
## TOPIC 00003: rfmxspecanvi/rfmxspecan_acp_configure_offset_power_reference.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_acp_configure_offset_power_reference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_acp_configure_offset_power_reference.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn ACP Configure Offset Power Reference (VI)

RFmxSpecAn ACP Configure Offset Power Reference (VI)

Owning Palette:

ACP

Configures the power reference to use for measuring the relative power of the offset channel.

Use "offset<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxSpecAn ACP Configure Offset Power Reference' src='rfmxspecan_acp_configure_offset_power_reference.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset Power Reference Carrier specifies the carrier to be used as power reference to measure offset channel relative power. The offset channel power is measured only if you set the ACP Carrier Mode property of the reference carrier to Active. The default value is Closest. Closest (0) The measurement uses the power measured in the carrier closest to the offset channel center frequency, as the power reference. Highest (1) The measurement uses the highest power measured among all the active carriers as the power reference. Composite (2) The measurement uses the sum of powers measured in all the active carriers as the power reference. Specific (3) The measurement uses the power measured in the carrier that has an index specified by the ACP Offset Pwr Ref Specific property, as the power reference. |
| Closest (0) | The measurement uses the power measured in the carrier closest to the offset channel center frequency, as the power reference. |
| Highest (1) | The measurement uses the highest power measured among all the active carriers as the power reference. |
| Composite (2) | The measurement uses the sum of powers measured in all the active carriers as the power reference. |
| Specific (3) | The measurement uses the power measured in the carrier that has an index specified by the ACP Offset Pwr Ref Specific property, as the power reference. |
|  | Offset Power Reference Specific specifies the index of the carrier to be used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power, when you set the Offset Power Reference Carrier parameter to Specific. The default value is 0. |
|  | Selector String specifies the selector string comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "offset0". Example: "offset0" "signal::sig1/offset0" You can use the RFmxSpecAn Build Offset String2 VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_acp_configure_offset_power_reference_(array).html language=enus -->
## TOPIC 00004: rfmxspecanvi/rfmxspecan_acp_configure_offset_power_reference_(array).html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_acp_configure_offset_power_reference_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_acp_configure_offset_power_reference_(array).html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn ACP Configure Offset Power Reference (Array) (VI)

RFmxSpecAn ACP Configure Offset Power Reference (Array) (VI)

Owning Palette:

Array VIs

Configures the power reference to use for measuring the relative power of the offset channel.

[IMAGE alt='RFmxSpecAn ACP Configure Offset Power Reference (Array)' src='rfmxspecan_acp_configure_offset_power_reference_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset Reference Carrier specifies the array of carriers to be used as power reference to measure offset channel relative power. The offset channel power is measured only if you set the ACP Carrier Mode property of the reference carrier to Active. The default value is Closest. Closest (0) The measurement uses the power measured in the carrier closest to the offset channel center frequency, as the power reference. Highest (1) The measurement uses the highest power measured among all the active carriers as the power reference. Composite (2) The measurement uses the sum of powers measured in all the active carriers as the power reference. Specific (3) The measurement uses the power measured in the carrier that has an index specified by the ACP Offset Pwr Ref Specific property, as the power reference. |
| Closest (0) | The measurement uses the power measured in the carrier closest to the offset channel center frequency, as the power reference. |
| Highest (1) | The measurement uses the highest power measured among all the active carriers as the power reference. |
| Composite (2) | The measurement uses the sum of powers measured in all the active carriers as the power reference. |
| Specific (3) | The measurement uses the power measured in the carrier that has an index specified by the ACP Offset Pwr Ref Specific property, as the power reference. |
|  | Offset Reference Specific specifies the array of carrier indices to use as the reference carrier for each offset channel. The power measured in this carrier is used as the power reference for measuring the offset channel relative power, when you set the Offset Power Reference Carrier parameter to Specific. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_acp_configure_offset_relative_attenuation.html language=enus -->
## TOPIC 00005: rfmxspecanvi/rfmxspecan_acp_configure_offset_relative_attenuation.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_acp_configure_offset_relative_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_acp_configure_offset_relative_attenuation.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn ACP Configure Offset Relative Attenuation (VI)

RFmxSpecAn ACP Configure Offset Relative Attenuation (VI)

Owning Palette:

ACP

Configures the attenuation, in dB, relative to the external attenuation.

Use "offset<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxSpecAn ACP Configure Offset Relative Attenuation' src='rfmxspecan_acp_configure_offset_relative_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Relative Attenuation specifies the attenuation, in dB, relative to the external attenuation. Use this parameter to compensate for variations in external attenuation when the offset channels are spread wide in frequency. The default value is 0. |
|  | Selector String specifies the selector string comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "offset0". Example: "offset0" "signal::sig1/offset0" You can use the RFmxSpecAn Build Offset String2 VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_acp_configure_offset_relative_attenuation_(array).html language=enus -->
## TOPIC 00006: rfmxspecanvi/rfmxspecan_acp_configure_offset_relative_attenuation_(array).html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_acp_configure_offset_relative_attenuation_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_acp_configure_offset_relative_attenuation_(array).html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn ACP Configure Offset Relative Attenuation (Array) (VI)

RFmxSpecAn ACP Configure Offset Relative Attenuation (Array) (VI)

Owning Palette:

Array VIs

Configures the attenuation, in dB, relative to the external attenuation.

[IMAGE alt='RFmxSpecAn ACP Configure Offset Relative Attenuation (Array)' src='rfmxspecan_acp_configure_offset_relative_attenuation_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Relative Attenuation specifies an array of attenuation values, in dB, relative to the external attenuation. Use this parameter to compensate for the variations in external attenuation when offset channels are spread wide in frequency. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_acp_configure_offset_rrc_filter_(array).html language=enus -->
## TOPIC 00007: rfmxspecanvi/rfmxspecan_acp_configure_offset_rrc_filter_(array).html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_acp_configure_offset_rrc_filter_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_acp_configure_offset_rrc_filter_(array).html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn ACP Configure Offset RRC Filter (Array) (VI)

RFmxSpecAn ACP Configure Offset RRC Filter (Array) (VI)

Owning Palette:

Array VIs

Configures the root raised cosine (RRC) channel filter to be applied on the offset channel before measuring channel power.

[IMAGE alt='RFmxSpecAn ACP Configure Offset RRC Filter (Array)' src='rfmxspecan_acp_configure_offset_rrc_filter_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RRC Filter Enabled specifies whether to apply the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power. The default value is False. False (0) The channel power of the acquired offset channel is measured directly. True (1) The measurement applies the RRC filter on the acquired offset channel before measuring the offset channel power. |
| False (0) | The channel power of the acquired offset channel is measured directly. |
| True (1) | The measurement applies the RRC filter on the acquired offset channel before measuring the offset channel power. |
|  | RRC Alpha specifies an array of roll-off factors of the root-raised-cosine (RRC) filter to apply on the acquired offset channel before measuring the offset channel power. The default value is 0.1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_ampm_configure_reference_power_type.html language=enus -->
## TOPIC 00008: rfmxspecanvi/rfmxspecan_ampm_configure_reference_power_type.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_ampm_configure_reference_power_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_ampm_configure_reference_power_type.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn AMPM Configure Reference Power Type (VI)

RFmxSpecAn AMPM Configure Reference Power Type (VI)

Configures the reference power to be used for AM to AM and AM to PM traces.

[IMAGE alt='RFmxSpecAn AMPM Configure Reference Power Type' src='rfmxspecan_ampm_configure_reference_power_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Power Type specifies the reference power used for AM to AM and AM to PM traces. The default value is Input. Input (0) The instantaneous powers at the input port of the device under test (DUT) forms the x-axis of AM to AM and AM to PM traces. Output (1) The instantaneous powers at the output port of the DUT forms the x-axis of AM to AM and AM to PM traces. |
| Input (0) | The instantaneous powers at the input port of the device under test (DUT) forms the x-axis of AM to AM and AM to PM traces. |
| Output (1) | The instantaneous powers at the output port of the DUT forms the x-axis of AM to AM and AM to PM traces. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_ampm_configure_synchronization_method.html language=enus -->
## TOPIC 00009: rfmxspecanvi/rfmxspecan_ampm_configure_synchronization_method.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_ampm_configure_synchronization_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_ampm_configure_synchronization_method.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn AMPM Configure Synchronization Method (VI)

RFmxSpecAn AMPM Configure Synchronization Method (VI)

Owning Palette:

AMPM

Configures the synchronization method used to synchronize the reference waveform and acquired waveform.

[IMAGE alt='RFmxSpecAn AMPM Configure Synchronization Method' src='rfmxspecan_ampm_configure_synchronization_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Method specifies the method used for time-synchronization of acquired waveform with reference waveform. Direct (1) Synchronizes the acquired and reference waveforms assuming that sample rate is sufficient to prevent aliasing in intermediate operations. This method is recommended when the measurement sampling rate is high. Alias Protected (2) Synchronizes the acquired and reference waveforms while ascertaining that intermediate operations are not impacted by aliasing. This method is recommended for non-contiguous carriers separated by a large gap, and/or when the measurement sampling rate is low. Refer to AMPM concept help for more information. |
| Direct (1) | Synchronizes the acquired and reference waveforms assuming that sample rate is sufficient to prevent aliasing in intermediate operations. This method is recommended when the measurement sampling rate is high. |
| Alias Protected (2) | Synchronizes the acquired and reference waveforms while ascertaining that intermediate operations are not impacted by aliasing. This method is recommended for non-contiguous carriers separated by a large gap, and/or when the measurement sampling rate is low. Refer to AMPM concept help for more information. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_ampm_fetch.html language=enus -->
## TOPIC 00010: rfmxspecanvi/rfmxspecan_ampm_fetch.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_ampm_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_ampm_fetch.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn AMPM Fetch (VI)

RFmxSpecAn AMPM Fetch (VI)

Owning Palette:

Fetch

Fetches AMPM measurement results.

#### RFmxSpecAn AMPM Fetch DUT Characteristics

Fetches the mean linear gain, 1 dB compression point, and mean RMS EVM of the DUT.

[IMAGE alt='RFmxSpecAn AMPM Fetch DUT Characteristics' src='rfmxspecan_ampm_fetch_dut_characteristics.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Mean Linear Gain returns the average linear gain, in dB, of the device under test, computed by rejecting signal samples suffering gain compression. |
|  | 1 dB Compression Point returns the theoretical output power, in dBm, at which gain of the device under test drops by 1 dB from its mean linear gain. This parameter returns NaN when the AM-to-AM characteristics of the device under test are flat. |
|  | Mean RMS EVM returns the ratio, as a percentage, of l2 norm of difference between the normalized reference and acquired waveforms, to the l2 norm of the normalized reference waveform. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn AMPM Fetch Error

Fetches the maximum gain error range, phase error range, and mean phase error for the DUT.

[IMAGE alt='RFmxSpecAn AMPM Fetch Error' src='rfmxspecan_ampm_fetch_error.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Gain Error Range returns the peak-to-peak deviation, in dB, in the gain of the device under test. |
|  | Phase Error Range returns the peak-to-peak deviation, in degrees, in the phase distortion of the acquired signal relative to the reference waveform caused by the device under test. |
|  | Mean Phase Error returns the mean phase error, in degrees, of the acquired signal relative to the reference waveform caused by the device under test. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn AMPM Fetch Curve Fit Coefficients

Fetches the coefficients of the polynomials that approximate the AM-to-AM and AM-to-PM responses of the device under test.

[IMAGE alt='RFmxSpecAn AMPM Fetch Curve Fit Coefficients' src='rfmxspecan_ampm_fetch_curve_fit_coefficients.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | AM to AM Coefficients returns the coefficients of the polynomial that approximates the AM-to-AM characteristic of the device under test. |
|  | AM to PM Coefficients returns the coefficients of the polynomial that approximates the AM-to-PM characteristic of the device under test. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn AMPM Fetch Curve Fit Residual

Fetches the polynomial approximation residuals for AM-to-AM and AM-to-PM response of the device under test.

[IMAGE alt='RFmxSpecAn AMPM Fetch Curve Fit Residual' src='rfmxspecan_ampm_fetch_curve_fit_residual.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | AM to AM Residual returns the approximation error, in dB, in the polynomial approximation of the AM-to-AM characteristic of the device under test. |
|  | AM to PM Residual returns the approximation error, in degrees, in the polynomial approximation of the AM-to-PM characteristic of the device under test. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn AMPM Fetch AM to AM Trace

Fetches the AM to AM trace, where the **Reference Powers** array forms the x-axis of the trace; and the **Measured AM to AM** and **Curve Fit AM to AM** arrays form the y-axis of the trace.

[IMAGE alt='RFmxSpecAn AMPM Fetch AM to AM Trace' src='rfmxspecan_ampm_fetch_am_to_am_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Reference Powers returns the array of reference powers. This value is expressed in dBm. Reference Powers are the instantaneous powers at the input port of the DUT when you set the AMPM Ref Pwr Type property to Input, and Reference Powers are the instantaneous powers at the output port of the DUT when you set the AMPM Ref Pwr Type property to Output. |
|  | Measured AM to AM returns the gain values corresponding to the reference powers. This value is expressed in dB. |
|  | Curve Fit AM to AM returns the polynomial fit gain values corresponding to the reference powers. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn AMPM Fetch AM to PM Trace

Fetches the AM to PM trace, where the **Reference Powers** array forms the x-axis of the trace; and the **Measured AM to PM** and **Curve Fit AM to PM** arrays form the y-axis of the trace.

[IMAGE alt='RFmxSpecAn AMPM Fetch AM to PM Trace' src='rfmxspecan_ampm_fetch_am_to_pm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Reference Powers returns the array of reference powers. This value is expressed in dBm. Reference Powers are the instantaneous powers at the input port of the DUT when you set the AMPM Ref Pwr Type property to Input, and Reference Powers are the instantaneous powers at the output port of the DUT when you set the AMPM Ref Pwr Type property to Output. |
|  | Measured AM to PM returns the polynomial fit phase distortion values corresponding to the reference powers. This value is expressed in degrees. |
|  | Curve Fit AM to PM returns the phase distortion values corresponding to the reference powers. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn AMPM Fetch Processed Reference Waveform

Fetches the segment of the reference waveform used to perform the AMPM measurement.

[IMAGE alt='RFmxSpecAn AMPM Fetch Processed Reference Waveform' src='rfmxspecan_ampm_fetch_processed_reference_waveform.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Processed Reference Waveform returns the segment of the reference waveform used to perform the measurement. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the complex baseband samples, in volts. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the complex baseband samples, in volts. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn AMPM Fetch Processed Mean Acquired Waveform

Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the AMPM measurement.

[IMAGE alt='RFmxSpecAn AMPM Fetch Processed Mean Acquired Waveform' src='rfmxspecan_ampm_fetch_processed_mean_acquired_waveform.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Processed Mean Acquired Waveform returns the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the measurement. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the complex baseband samples, in volts. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the complex baseband samples, in volts. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn AMPM Fetch Relative Power Trace

Fetches the power of the processed mean acquired waveform relative to the processed reference waveform.

[IMAGE alt='RFmxSpecAn AMPM Fetch Relative Power Trace' src='rfmxspecan_ampm_fetch_relative_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Relative Power returns the relative power trace values. This value is expressed in dB. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the instantaneous relative power, in dB. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the instantaneous relative power, in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn AMPM Fetch Relative Phase Trace

Fetches the phase of the processed mean acquired waveform relative to the processed reference waveform.

[IMAGE alt='RFmxSpecAn AMPM Fetch Relative Phase Trace' src='rfmxspecan_ampm_fetch_relative_phase_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Relative Phase returns the relative phase trace values. This value is expressed in degree. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the instantaneous relative phase. This value is expressed in degree. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the instantaneous relative phase. This value is expressed in degree. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn AMPM Fetch Compression Points

Fetches the compression points.

[IMAGE alt='RFmxSpecAn AMPM Fetch Compression Points' src='rfmxspecan_ampm_fetch_compression_points.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Input Compression Point returns the theoretical input power at which the device gain drops by the compression level, specified by the AMPM Compression Point Level parameter, from its mean linear gain. This value is expressed in dBm. |
|  | Output Compression Point returns the theoretical output power at which device gain drops by the compression level, specified by the AMPM Compression Point Level parameter, from its mean linear gain. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_analyze2.html language=enus -->
## TOPIC 00011: rfmxspecanvi/rfmxspecan_analyze2.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_analyze2.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Analyze2 (VI)

RFmxSpecAn Analyze2 (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance.

#### RFmxSpecAn Analyze (IQ, 1 Wfm)

Performs the enabled measurements on the I/Q complex waveform that you specify in the **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.

Use this VI only if the Recommended Acquisition Type property value is either **IQ** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmxSpecAn Commit VI. |
| --- | --- |

[IMAGE alt='RFmxSpecAn Analyze (IQ 1 Wfm)' src='rfmxspecan_analyze_(iq_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with the option string as "AnalysisOnly=1". |
| --- | --- |
|  | IQ specifies the data for a complex I/Q waveform including the start, delta, and actual values. x0 specifies the start time of the input y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn Analyze (Spectrum, 1 Wfm)

Performs the enabled measurements on the spectrum that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.

Use this VI only if the Recommended Acquisition Type property value is either **Spectral** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmxSpecAn Commit VI. |
| --- | --- |

[IMAGE alt='RFmxSpecAn Analyze (Spectrum 1 Wfm)' src='rfmxspecan_analyze_(spectrum_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with the option string as "AnalysisOnly=1". |
| --- | --- |
|  | Spectrum specifies the data for a Spectrum waveform including the start, delta, and actual values. x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx specifies the frequency interval between data points in the spectrum. y specifies the real-value power spectrum. |
|  | x0 specifies the start frequency of the spectrum. This value is expressed in Hz. |
|  | dx specifies the frequency interval between data points in the spectrum. |
|  | y specifies the real-value power spectrum. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_auto_level.html language=enus -->
## TOPIC 00012: rfmxspecanvi/rfmxspecan_auto_level.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_auto_level.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Auto Level (VI)

RFmxSpecAn Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxSpecAn Auto Level VI does the following:

1. Resets the mixer level, mixer level offset and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

You can also specify the starting reference level using the Auto Level Initial Reference Level property.

When using PXIe-5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmx SpecAn Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this VI, thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxSpecAn Auto Level' src='rfmxspecan_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Bandwidth specifies the bandwidth, in Hz, of the signal to be analyzed. The default value is 200 kHz. |
|  | Measurement Interval specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and as Vpk-pk for baseband devices. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_build_segment_string.html language=enus -->
## TOPIC 00013: rfmxspecanvi/rfmxspecan_build_segment_string.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_build_segment_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_build_segment_string.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Build Segment String (VI)

RFmxSpecAn Build Segment String (VI)

Owning Palette:

Build String

Creates a selector string for use with the PAVT configuration or fetch properties and VIs.

[IMAGE alt='RFmxSpecAn Build Segment String' src='rfmxspecan_build_segment_string.gif']

|  | Segment Number specifies the segment number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_build_signal_string.html language=enus -->
## TOPIC 00014: rfmxspecanvi/rfmxspecan_build_signal_string.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_build_signal_string.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Build Signal String (VI)

RFmxSpecAn Build Signal String (VI)

Owning Palette:

Build String

Creates selector string for use with configuration or fetch properties and VIs.

[IMAGE alt='RFmxSpecAn Build Signal String' src='rfmxspecan_build_signal_string.gif']

|  | Result Name specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Example: "" "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "" "signal::sig1" "sig1" |
|  | Selector String returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_build_spur_string2.html language=enus -->
## TOPIC 00015: rfmxspecanvi/rfmxspecan_build_spur_string2.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_build_spur_string2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_build_spur_string2.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Build Spur String2 (VI)

RFmxSpecAn Build Spur String2 (VI)

Owning Palette:

Spur

Creates the selector string for use with spurious emissions (Spur) measurement results or fetch VIs.

[IMAGE alt='RFmxSpecAn Build Spur String2' src='rfmxspecan_build_spur_string2.gif']

|  | Spur Number specifies the Spur number. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, and range number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. You can also pass the Selector String Out parameter from RFmxSpecAn Build Range String2 VI as an input to this VI. The default value is "range0". Example: "range0" "signal::sig1/range0" "result::r1/range0" "signal::sig1/result::r1/range0" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_ccdf_configure_measurement_interval.html language=enus -->
## TOPIC 00016: rfmxspecanvi/rfmxspecan_ccdf_configure_measurement_interval.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_ccdf_configure_measurement_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_ccdf_configure_measurement_interval.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn CCDF Configure Measurement Interval (VI)

RFmxSpecAn CCDF Configure Measurement Interval (VI)

Owning Palette:

CCDF

Configures the acquisition time, in seconds, for the complementary cumulative distribution function (CCDF) measurement.

[IMAGE alt='RFmxSpecAn CCDF Configure Measurement Interval' src='rfmxspecan_ccdf_configure_measurement_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Interval specifies the acquisition time, in seconds, for the measurement. The default value is 1 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_chp_configure_integration_bandwidth.html language=enus -->
## TOPIC 00017: rfmxspecanvi/rfmxspecan_chp_configure_integration_bandwidth.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_chp_configure_integration_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_chp_configure_integration_bandwidth.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn CHP Configure Integration Bandwidth (VI)

RFmxSpecAn CHP Configure Integration Bandwidth (VI)

Owning Palette:

CHP

Configures the frequency range, in Hz, over which the measurement integrates the power.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxSpecAn CHP Configure Integration Bandwidth' src='rfmxspecan_chp_configure_integration_bandwidth.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Integration Bandwidth specifies the frequency range, in Hz, over which the measurement integrates the carrier channel power. The default value is 1 MHz. |
|  | Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxSpecAn Build Carrier String2 VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_chp_configure_number_of_carriers.html language=enus -->
## TOPIC 00018: rfmxspecanvi/rfmxspecan_chp_configure_number_of_carriers.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_chp_configure_number_of_carriers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_chp_configure_number_of_carriers.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn CHP Configure Number Of Carriers (VI)

RFmxSpecAn CHP Configure Number Of Carriers (VI)

Owning Palette:

CHP

Configures the number of carriers for a channel power (CHP) measurement.

[IMAGE alt='RFmxSpecAn CHP Configure Number Of Carriers' src='rfmxspecan_chp_configure_number_of_carriers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Carriers specifies the number of carriers. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_chp_configure_rbw_filter.html language=enus -->
## TOPIC 00019: rfmxspecanvi/rfmxspecan_chp_configure_rbw_filter.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_chp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_chp_configure_rbw_filter.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn CHP Configure RBW Filter (VI)

RFmxSpecAn CHP Configure RBW Filter (VI)

Owning Palette:

CHP

Configures the resolution bandwidth (RBW) filter.

[IMAGE alt='RFmxSpecAn CHP Configure RBW Filter' src='rfmxspecan_chp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the CHP topic for more details on RBW and sweep time. The default value is True. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 10 kHz. |
|  | RBW Filter Type specifies the response of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_chp_configure_rrc_filter.html language=enus -->
## TOPIC 00020: rfmxspecanvi/rfmxspecan_chp_configure_rrc_filter.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_chp_configure_rrc_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_chp_configure_rrc_filter.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn CHP Configure RRC Filter (VI)

RFmxSpecAn CHP Configure RRC Filter (VI)

Owning Palette:

CHP

Configures the root raised cosine (RRC) filter to apply on the channel before measuring the channel power.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxSpecAn CHP Configure RRC Filter' src='rfmxspecan_chp_configure_rrc_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RRC Filter Enabled specifies whether to apply the RRC filter on the acquired channel before measuring the channel power. The default value is False. False (0) The measurement measures the channel power directly on the acquired channel. True (1) The measurement applies the RRC filter on the acquired channel before measuring the channel power. |
| False (0) | The measurement measures the channel power directly on the acquired channel. |
| True (1) | The measurement applies the RRC filter on the acquired channel before measuring the channel power. |
|  | RRC Alpha specifies the roll-off factor for the root-raised-cosine (RRC) filter. The default value is 0.1. |
|  | Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxSpecAn Build Carrier String2 VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_chp_configure_span.html language=enus -->
## TOPIC 00021: rfmxspecanvi/rfmxspecan_chp_configure_span.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_chp_configure_span.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_chp_configure_span.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn CHP Configure Span (VI)

RFmxSpecAn CHP Configure Span (VI)

Owning Palette:

CHP

Configures the frequency range, in Hz, around the center frequency, to acquire for the channel power (CHP) measurement.

[IMAGE alt='RFmxSpecAn CHP Configure Span' src='rfmxspecan_chp_configure_span.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Span specifies the frequency range, in Hz, around the center frequency, to acquire for the measurement. The default value is 1 MHz. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_clear_noise_calibration_database.html language=enus -->
## TOPIC 00022: rfmxspecanvi/rfmxspecan_clear_noise_calibration_database.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_clear_noise_calibration_database.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_clear_noise_calibration_database.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Clear Noise Calibration Database (VI)

RFmxSpecAn Clear Noise Calibration Database (VI)

Owning Palette:

Advanced

Clears the noise calibration database used for noise compensation.

[IMAGE alt='RFmxSpecAn Clear Noise Calibration Database' src='rfmxspecan_clear_noise_calibration_database.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_clone_signal_configuration.html language=enus -->
## TOPIC 00023: rfmxspecanvi/rfmxspecan_clone_signal_configuration.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_clone_signal_configuration.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Clone Signal Configuration (VI)

RFmxSpecAn Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxSpecAn Clone Signal Configuration' src='rfmxspecan_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_commit.html language=enus -->
## TOPIC 00024: rfmxspecanvi/rfmxspecan_commit.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_commit.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Commit (VI)

RFmxSpecAn Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxSpecAn commits settings to the hardware when you call the [RFmxSpecAn Initiate](rfmxspecan_initiate.html) VI or any of the measurement Read VIs.

[IMAGE alt='RFmxSpecAn Commit' src='rfmxspecan_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_configure_external_attenuation.html language=enus -->
## TOPIC 00025: rfmxspecanvi/rfmxspecan_configure_external_attenuation.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_configure_external_attenuation.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Configure External Attenuation (VI)

RFmxSpecAn Configure External Attenuation (VI)

Owning Palette:

Configuration

Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer.

[IMAGE alt='RFmxSpecAn Configure External Attenuation' src='rfmxspecan_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | External Attenuation specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_configure_frequency.html language=enus -->
## TOPIC 00026: rfmxspecanvi/rfmxspecan_configure_frequency.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_configure_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_configure_frequency.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Configure Frequency (VI)

RFmxSpecAn Configure Frequency (VI)

Owning Palette:

Configuration

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='RFmxSpecAn Configure Frequency' src='rfmxspecan_configure_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_configure_reference_level.html language=enus -->
## TOPIC 00027: rfmxspecanvi/rfmxspecan_configure_reference_level.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_configure_reference_level.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Configure Reference Level (VI)

RFmxSpecAn Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level, which represents the maximum expected power of an RF input signal.

[IMAGE alt='RFmxSpecAn Configure Reference Level' src='rfmxspecan_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Level specifies the reference level which represents the maximum expected power of an RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default of this property is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_configure_rf.html language=enus -->
## TOPIC 00028: rfmxspecanvi/rfmxspecan_configure_rf.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_configure_rf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_configure_rf.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Configure RF (VI)

RFmxSpecAn Configure RF (VI)

Owning Palette:

Configuration

Configures the RF properties of the signal specified by the selector string.

[IMAGE alt='RFmxSpecAn Configure RF' src='rfmxspecan_configure_rf.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. |
|  | Reference Level specifies the reference level which represents the maximum expected power of an RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default of this property is hardware dependent. |
|  | External Attenuation specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_apply_digital_predistortion.html language=enus -->
## TOPIC 00029: rfmxspecanvi/rfmxspecan_dpd_apply_digital_predistortion.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_apply_digital_predistortion.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_apply_digital_predistortion.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Apply Digital Predistortion (VI)

RFmxSpecAn DPD Apply Digital Predistortion (VI)

Owning Palette:

Apply DPD

Scales the input waveform to DUT average input power and then predistorts using the DPD polynomial or the lookup table. To scale the waveform correctly, specify if the idle duration is present in the waveform.

[IMAGE alt='RFmxSpecAn DPD Apply Digital Predistortion' src='rfmxspecan_dpd_apply_digital_predistortion.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Waveform In specifies the complex baseband equivalent of the RF signal on which to apply digital predistortion. x0 specifies the start time, in seconds. dx specifies the sample duration, in seconds. y specifies the complex baseband samples, in volts. |
|  | x0 specifies the start time, in seconds. |
|  | dx specifies the sample duration, in seconds. |
|  | y specifies the complex baseband samples, in volts. |
|  | Idle Duration Present specifies whether the waveform contains an idle duration. The default value is False. False (0) The reference waveform does not contain idle duration. True (1) The reference waveform contains idle duration. |
| False (0) | The reference waveform does not contain idle duration. |
| True (1) | The reference waveform contains idle duration. |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | Waveform Out returns the complex baseband equivalent of the RF signal obtained after applying digital predistortion on the input waveform. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the complex baseband samples, in volts. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the complex baseband samples, in volts. |
|  | PAPR returns the peak-to-average power ratio of the waveform obtained after applying digital predistortion. This value is expressed in dB. |
|  | Power Offset returns the change in the average power in the waveform due to applying digital predistortion. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_apply_pre-dpd_signal_conditioning.html language=enus -->
## TOPIC 00030: rfmxspecanvi/rfmxspecan_dpd_apply_pre-dpd_signal_conditioning.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_apply_pre-dpd_signal_conditioning.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_apply_pre-dpd_signal_conditioning.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Apply Pre-DPD Signal Conditioning (VI)

RFmxSpecAn DPD Apply Pre-DPD Signal Conditioning (VI)

Applies signal conditioning on the input waveform in the form of crest factor reduction before using the output waveform as the reference waveform for DPD measurement.

[IMAGE alt='RFmxSpecAn DPD Apply Pre-DPD Signal Conditioning' src='rfmxspecan_dpd_apply_pre-dpd_signal_conditioning.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Waveform In specifies the complex baseband equivalent of the RF signal on which the pre-DPD signal conditioning is applied. x0 specifies the start time, in seconds. dx specifies the sample duration, in seconds. y specifies the complex baseband samples, in volts. |
|  | x0 specifies the start time, in seconds. |
|  | dx specifies the sample duration, in seconds. |
|  | y specifies the complex baseband samples, in volts. |
|  | Idle Duration Present specifies whether the waveform contains an idle duration. The default value is False. False (0) The input waveform does not contain idle duration. True (1) The input waveform contains idle duration. |
| False (0) | The input waveform does not contain idle duration. |
| True (1) | The input waveform contains idle duration. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Waveform Out returns the complex baseband equivalent of the RF signal after applying signal conditioning on the input waveform. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the complex baseband samples, in volts. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the complex baseband samples, in volts. |
|  | PAPR returns the peak-to-average power ratio of the waveform obtained after applying pre-DPD signal conditioning on the input waveform. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_lookup_table_correction_type.html language=enus -->
## TOPIC 00031: rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_lookup_table_correction_type.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_lookup_table_correction_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_lookup_table_correction_type.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure Apply DPD Lookup Table Correction Type (VI)

RFmxSpecAn DPD Configure Apply DPD Lookup Table Correction Type (VI)

Owning Palette:

Apply DPD

Configures the predistortion type when you set the DPD Model property to **Lookup Table**.

[IMAGE alt='RFmxSpecAn DPD Configure Apply DPD Lookup Table Correction Type' src='rfmxspecan_dpd_configure_apply_dpd_lookup_table_correction_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | LUT Correction Type specifies the predistortion type when you set the DPD Model property to Lookup Table. The default value is Magnitude and Phase. Magnitude and Phase (0) The measurement predistorts the magnitude and phase of the input waveform. Magnitude Only (1) The measurement predistorts only the magnitude of the input waveform. Phase Only (2) The measurement predistorts only the phase of the input waveform. |
| Magnitude and Phase (0) | The measurement predistorts the magnitude and phase of the input waveform. |
| Magnitude Only (1) | The measurement predistorts only the magnitude of the input waveform. |
| Phase Only (2) | The measurement predistorts only the phase of the input waveform. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_memory_models_correction_type.html language=enus -->
## TOPIC 00032: rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_memory_models_correction_type.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_memory_models_correction_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_memory_models_correction_type.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure Apply DPD Memory Models Correction Type (VI)

RFmxSpecAn DPD Configure Apply DPD Memory Models Correction Type (VI)

Owning Palette:

Apply DPD

Configures the predistortion type when you set the DPD Model property to **Memory Polynomial** or **Generalized Memory Polynomial**.

[IMAGE alt='RFmxSpecAn DPD Configure Apply DPD Memory Models Correction Type' src='rfmxspecan_dpd_configure_apply_dpd_memory_models_correction_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Mem Models Correction Type specifies the predistortion type when you set the DPD Model property to Memory Polynomial or Generalized Memory Polynomial. The default value is Magnitude and Phase. Magnitude and Phase (0) The measurement predistorts the magnitude and phase of the input waveform. Magnitude Only (1) The measurement predistorts only the magnitude of the input waveform. Phase Only (2) The measurement predistorts only the phase of the input waveform. |
| Magnitude and Phase (0) | The measurement predistorts the magnitude and phase of the input waveform. |
| Magnitude Only (1) | The measurement predistorts only the magnitude of the input waveform. |
| Phase Only (2) | The measurement predistorts only the phase of the input waveform. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_user_dpd_polynomial.html language=enus -->
## TOPIC 00033: rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_user_dpd_polynomial.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_user_dpd_polynomial.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_user_dpd_polynomial.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure Apply DPD User DPD Polynomial (VI)

RFmxSpecAn DPD Configure Apply DPD User DPD Polynomial (VI)

Owning Palette:

User DPD

Configures the array of memory polynomial or generalized memory polynomial coefficients when you set the DPD Model property to **Memory Polynomial** or **Generalized Memory Polynomial**.

[IMAGE alt='RFmxSpecAn DPD Configure Apply DPD User DPD Polynomial' src='rfmxspecan_dpd_configure_apply_dpd_user_dpd_polynomial.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | DPD Polynomial specifies the array of memory polynomial or generalized memory polynomial coefficients when you set the DPD Model property to Memory Polynomial or Generalized Memory Polynomial. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_user_lookup_table.html language=enus -->
## TOPIC 00034: rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_user_lookup_table.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_user_lookup_table.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_apply_dpd_user_lookup_table.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure Apply DPD User Lookup Table (VI)

RFmxSpecAn DPD Configure Apply DPD User Lookup Table (VI)

Owning Palette:

User DPD

Configures the predistortion lookup table when you set the DPD Model property to **Lookup Table**.

[IMAGE alt='RFmxSpecAn DPD Configure Apply DPD User Lookup Table' src='rfmxspecan_dpd_configure_apply_dpd_user_lookup_table.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | LUT Input Powers specifies the array of lookup table power levels, in dBm. |
|  | LUT Complex Gains specifies the array of lookup table complex gain values for magnitude and phase predistortion. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_averaging.html language=enus -->
## TOPIC 00035: rfmxspecanvi/rfmxspecan_dpd_configure_averaging.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_averaging.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure Averaging (VI)

RFmxSpecAn DPD Configure Averaging (VI)

Owning Palette:

DPD

Configures averaging for the DPD measurement.

[IMAGE alt='RFmxSpecAn DPD Configure Averaging' src='rfmxspecan_dpd_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_dpd_model.html language=enus -->
## TOPIC 00036: rfmxspecanvi/rfmxspecan_dpd_configure_dpd_model.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_dpd_model.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_dpd_model.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure DPD Model (VI)

RFmxSpecAn DPD Configure DPD Model (VI)

Owning Palette:

DPD

Specifies the DPD model used by the DPD measurement.

[IMAGE alt='RFmxSpecAn DPD Configure DPD Model' src='rfmxspecan_dpd_configure_dpd_model.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | DPD Model specifies the DPD model used by the DPD measurement. The default value is Lookup Table. Lookup Table (0) This model computes the complex gain coefficients applied when performing digital predistortion to linearize systems with negligible memory effects. Memory Polynomial (1) This model computes the memory polynomial predistortion coefficients used to linearize systems with moderate memory effects. Generalized Memory Polynomial (2) This model computes the generalized memory polynomial predistortion coefficients used to linearize systems with significant memory effects. |
| Lookup Table (0) | This model computes the complex gain coefficients applied when performing digital predistortion to linearize systems with negligible memory effects. |
| Memory Polynomial (1) | This model computes the memory polynomial predistortion coefficients used to linearize systems with moderate memory effects. |
| Generalized Memory Polynomial (2) | This model computes the generalized memory polynomial predistortion coefficients used to linearize systems with significant memory effects. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_dut_average_input_power.html language=enus -->
## TOPIC 00037: rfmxspecanvi/rfmxspecan_dpd_configure_dut_average_input_power.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_dut_average_input_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_dut_average_input_power.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure DUT Average Input Power (VI)

RFmxSpecAn DPD Configure DUT Average Input Power (VI)

Owning Palette:

DPD

Configures the average power, in dBm, of the signal at the input port of the device under test (DUT).

[IMAGE alt='RFmxSpecAn DPD Configure DUT Average Input Power' src='rfmxspecan_dpd_configure_dut_average_input_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | DUT Average Input Power specifies the average power of the signal at the input port of the DUT. The default value is -20 dBm. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_generalized_memory_polynomial_cross_terms.html language=enus -->
## TOPIC 00038: rfmxspecanvi/rfmxspecan_dpd_configure_generalized_memory_polynomial_cross_terms.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_generalized_memory_polynomial_cross_terms.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_generalized_memory_polynomial_cross_terms.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure Generalized Memory Polynomial Cross Terms (VI)

RFmxSpecAn DPD Configure Generalized Memory Polynomial Cross Terms (VI)

Owning Palette:

DPD

Configures the cross terms of the generalized memory polynomial when you set the DPD Model property to **Generalized Memory Polynomial**. Use the [RFmxSpecAn DPD Configure Memory Polynomial](rfmxspecan_dpd_configure_memory_polynomial.html) VI to configure the normal terms in the DPD polynomial, along with configuring the cross terms when you set the DPD Model property to **Generalized Memory Polynomial**.

[IMAGE alt='RFmxSpecAn DPD Configure Generalized Memory Polynomial Cross Terms' src='rfmxspecan_dpd_configure_generalized_memory_polynomial_cross_terms.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Memory Polynomial Lead Order specifies the lead order cross term of the DPD polynomial when you set the DPD Model property to Generalized Memory Polynomial. This value corresponds to Kc in the equation for the generalized memory polynomial. The default value is 0. |
|  | Memory Polynomial Lag Order specifies the lag order cross term of the DPD polynomial when you set the DPD Model property to Generalized Memory Polynomial. This value corresponds to Kb in the equation for the generalized memory polynomial. The default value is 0. |
|  | Memory Polynomial Lag Memory Depth specifies the lag memory depth cross term of the DPD polynomial when you set the DPD Model property to Generalized Memory Polynomial. This value corresponds to Qb in the equation for the generalized memory polynomial. The default value is 0. |
|  | Memory Polynomial Lead Memory Depth specifies the lead memory depth cross term of the DPD polynomial when you set the DPD Model property to Generalized Memory Polynomial. This value corresponds to Qc in the equation for the generalized memory polynomial. The value of this parameter must be greater than or equal to the value of the Memory Polynomial Max Lead parameter. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | Memory Polynomial Max Lead specifies the maximum lead stagger cross term of the DPD polynomial when you set the DPD Model property to Generalized Memory Polynomial. This value corresponds to Mc in the equation for the generalized memory polynomial. The default value is 0. |
|  | Memory Polynomial Max Lag specifies the maximum lag stagger cross term of the DPD polynomial when you set the DPD Model property to Generalized Memory Polynomial. This value corresponds to Mb in the equation for the generalized memory polynomial. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_lookup_table_am_to_am_curve_fit.html language=enus -->
## TOPIC 00039: rfmxspecanvi/rfmxspecan_dpd_configure_lookup_table_am_to_am_curve_fit.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_lookup_table_am_to_am_curve_fit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_lookup_table_am_to_am_curve_fit.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure Lookup Table AM to AM Curve Fit (VI)

RFmxSpecAn DPD Configure Lookup Table AM to AM Curve Fit (VI)

Owning Palette:

DPD

Configures the degree of the polynomial and the approximation method used for polynomial approximation of the AM-to-AM response of the device under test (DUT) when you set the DPD Model property to **Lookup Table**.

[IMAGE alt='RFmxSpecAn DPD Configure Lookup Table AM to AM Curve Fit' src='rfmxspecan_dpd_configure_lookup_table_am_to_am_curve_fit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | AM to AM Curve Fit Order specifies the degree of the polynomial used to approximate the AM-to-AM characteristic of the DUT when you set the DPD Model property to Lookup Table. The default value is 7. |
|  | AM to AM Curve Fit Type specifies the polynomial approximation cost-function of the DUT AM-to-AM characteristic when you set the DPD Model property to Lookup Table. The default value is Least Absolute Residual. Least Square (0) Minimizes the energy of the polynomial approximation error. Least Absolute Residual (1) Minimizes the magnitude of the polynomial approximation error. Bisquare (2) Excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |
| Least Square (0) | Minimizes the energy of the polynomial approximation error. |
| Least Absolute Residual (1) | Minimizes the magnitude of the polynomial approximation error. |
| Bisquare (2) | Excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_reference_waveform.html language=enus -->
## TOPIC 00040: rfmxspecanvi/rfmxspecan_dpd_configure_reference_waveform.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_reference_waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_reference_waveform.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure Reference Waveform (VI)

RFmxSpecAn DPD Configure Reference Waveform (VI)

Owning Palette:

DPD

Configures the complex baseband equivalent of the RF signal applied at the input port of the DUT when performing the DPD measurement.

[IMAGE alt='RFmxSpecAn DPD Configure Reference Waveform' src='rfmxspecan_dpd_configure_reference_waveform.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Waveform specifies the complex baseband equivalent of the RF signal applied at the input port of the DUT when performing the measurement. x0 specifies the start time, in seconds. dx specifies the sample duration, in seconds. y specifies the complex baseband samples, in volts. |
|  | x0 specifies the start time, in seconds. |
|  | dx specifies the sample duration, in seconds. |
|  | y specifies the complex baseband samples, in volts. |
|  | Idle Duration Present specifies whether the reference waveform contains an idle duration. The default value is False. False (0) The reference waveform does not contain an idle duration. True (1) The reference waveform contains an idle duration. |
| False (0) | The reference waveform does not contain an idle duration. |
| True (1) | The reference waveform contains an idle duration. |
|  | Signal Type specifies whether the reference waveform is a modulated signal or tones. The default value is Modulated. Modulated (0) The reference waveform is a cellular or connectivity standard signal. Tones (1) The reference waveform is continuous signals comprising of one or more tones. |
| Modulated (0) | The reference waveform is a cellular or connectivity standard signal. |
| Tones (1) | The reference waveform is continuous signals comprising of one or more tones. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_configure_synchronization_method.html language=enus -->
## TOPIC 00041: rfmxspecanvi/rfmxspecan_dpd_configure_synchronization_method.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_configure_synchronization_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_configure_synchronization_method.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Configure Synchronization Method (VI)

RFmxSpecAn DPD Configure Synchronization Method (VI)

Owning Palette:

DPD

Configures the synchronization method used to synchronize the reference waveform and acquired waveform.

[IMAGE alt='RFmxSpecAn DPD Configure Synchronization Method' src='rfmxspecan_dpd_configure_synchronization_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Method specifies the method used for time-synchronization of acquired waveform with reference waveform. Direct (1) Synchronizes the acquired and reference waveforms assuming that sample rate is sufficient to prevent aliasing in intermediate operations. This method is recommended when the measurement sampling rate is high. Alias Protected (2) Synchronizes the acquired and reference waveforms while ascertaining that intermediate operations are not impacted by aliasing. This method is recommended for non-contiguous carriers separated by a large gap, and/or when the measurement sampling rate is low. Refer to DPD concept help for more information. |
| Direct (1) | Synchronizes the acquired and reference waveforms assuming that sample rate is sufficient to prevent aliasing in intermediate operations. This method is recommended when the measurement sampling rate is high. |
| Alias Protected (2) | Synchronizes the acquired and reference waveforms while ascertaining that intermediate operations are not impacted by aliasing. This method is recommended for non-contiguous carriers separated by a large gap, and/or when the measurement sampling rate is low. Refer to DPD concept help for more information. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_dpd_fetch.html language=enus -->
## TOPIC 00042: rfmxspecanvi/rfmxspecan_dpd_fetch.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_dpd_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_dpd_fetch.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn DPD Fetch (VI)

RFmxSpecAn DPD Fetch (VI)

Owning Palette:

Fetch

Fetches DPD measurement results.

#### RFmxSpecAn DPD Fetch Average Gain

Fetches the average gain, in dB, of the device under test (DUT) for the DPD measurement.

[IMAGE alt='RFmxSpecAn DPD Fetch Average Gain' src='rfmxspecan_dpd_fetch_average_gain.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Average Gain returns the average gain, in dB, of the DUT. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn DPD Fetch Lookup Table

Fetches the predistortion lookup table when DPD Model property to **Lookup Table**.

[IMAGE alt='RFmxSpecAn DPD Fetch Lookup Table' src='rfmxspecan_dpd_fetch_lookup_table.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Input Powers returns the lookup table power levels, in dBm. |
|  | Complex Gains returns the lookup table complex gain values, in dB, for magnitude and phase predistortion. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn DPD Fetch DPD Polynomial

Fetches the memory polynomial or generalized memory polynomial coefficients when you set the DPD Model property to **Memory Polynomial** or **Generalized Memory Polynomial**.

[IMAGE alt='RFmxSpecAn DPD Fetch DPD Polynomial' src='rfmxspecan_dpd_fetch_dpd_polynomial.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | DPD Polynomial returns the memory polynomial or generalized memory polynomial coefficients when you set the DPD Model property to Memory Polynomial or Generalized Memory Polynomial. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn DPD Fetch Processed Reference Waveform

Fetches the segment of the reference waveform used to perform the DPD measurement.

[IMAGE alt='RFmxSpecAn DPD Fetch Processed Reference Waveform' src='rfmxspecan_dpd_fetch_processed_reference_waveform.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Processed Reference Waveform returns the segment of the reference waveform used to perform the measurement. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the complex baseband samples, in volts. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the complex baseband samples, in volts. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn DPD Fetch Processed Mean Acquired Waveform

Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the DPD measurement.

[IMAGE alt='RFmxSpecAn DPD Fetch Processed Mean Acquired Waveform' src='rfmxspecan_dpd_fetch_processed_mean_acquired_waveform.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Processed Mean Acquired Waveform returns the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the measurement. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the complex baseband samples, in volts. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the complex baseband samples, in volts. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn DPD Fetch NMSE

Fetches the normalized mean-squared DPD modeling error.

[IMAGE alt='RFmxSpecAn DPD Fetch NMSE' src='rfmxspecan_dpd_fetch_nmse.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | NMSE returns the normalized mean-squared DPD modeling error when you set the DPD NMSE Enabled property to True. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn DPD Fetch Apply DPD Pre-CFR PAPR

Fetches the PAPR of the pre-distorted waveform before CFR is applied to it.

[IMAGE alt='RFmxSpecAn DPD Fetch Apply DPD Pre-CFR PAPR' src='rfmxspecan_dpd_fetch_apply_dpd_pre-cfr_papr.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. Result name is not supported. Any specified result name is ignored and the Pre-CFR PAPR returned corresponds to the latest execution of apply DPD for the specified signal name. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Pre-CFR PAPR returns the PAPR of the pre-distorted waveform before CFR is applied when you set the DPD Apply DPD CFR Enabled property to True. This value is expressed in dB. When you set the DPD Apply DPD CFR Enabled property to False and the DPD Model property to Lookup Table, the PAPR of the pre-distorted waveform is returned. When you set the DPD Apply DPD CFR Enabled property to False and the DPD Model property to Memory Polynomial or Generalized Memory Polynomial, the PAPR of the clipped pre-distorted waveform is returned. The pre-distorted waveform is clipped such that its peak amplitude does not exceed the peak of the input waveform, scaled to DUT average input power, by 6 dB. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_fcnt_fetch.html language=enus -->
## TOPIC 00043: rfmxspecanvi/rfmxspecan_fcnt_fetch.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_fcnt_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_fcnt_fetch.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn FCnt Fetch (VI)

RFmxSpecAn FCnt Fetch (VI)

Owning Palette:

Fetch

Fetches frequency count (FCnt) measurement results.

#### RFmxSpecAn FCnt Fetch Measurement

Returns the frequency and phase measured using the FCnt measurement.

[IMAGE alt='RFmxSpecAn FCnt Fetch Measurement' src='rfmxspecan_fcnt_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Average Absolute Frequency returns the RF signal frequency. Only samples above the threshold are used when you set the FCnt Threshold Enabled property to True. |
|  | Average Relative Frequency returns the signal frequency relative to the RF center frequency. Only samples above the threshold are used when you set the FCnt Threshold Enabled property to True. |
|  | Mean Phase returns the net phase of the vector sum of the I/Q samples used for frequency measurement. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn FCnt Fetch Frequency Trace

Fetches the frequency trace for FCnt measurement.

[IMAGE alt='RFmxSpecAn FCnt Fetch Frequency Trace' src='rfmxspecan_fcnt_fetch_frequency_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Frequency Trace returns the frequency versus time trace. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the frequency, in Hz, measured at each time instance. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the frequency, in Hz, measured at each time instance. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn FCnt Fetch Phase Trace

Fetches the phase trace for FCnt measurement.

[IMAGE alt='RFmxSpecAn FCnt Fetch Phase Trace' src='rfmxspecan_fcnt_fetch_phase_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Phase Trace returns the phase versus time trace. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the averaged phase, in degrees, measured at each time instance. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the averaged phase, in degrees, measured at each time instance. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn FCnt Fetch Power Trace

Fetches the power trace for FCnt measurement.

[IMAGE alt='RFmxSpecAn FCnt Fetch Power Trace' src='rfmxspecan_fcnt_fetch_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Power Trace returns the power versus time trace. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the measured average power, in dBm, at each time instance. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the measured average power, in dBm, at each time instance. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn FCnt Fetch Allan Deviation

Fetches the two-sample deviation of the measured frequency.

[IMAGE alt='RFmxSpecAn FCnt Fetch Allan Deviation' src='rfmxspecan_fcnt_fetch_allan_deviation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Allan Deviation returns the two-sample deviation of the measured frequency. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_harm_configure_auto_harmonics.html language=enus -->
## TOPIC 00044: rfmxspecanvi/rfmxspecan_harm_configure_auto_harmonics.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_harm_configure_auto_harmonics.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_harm_configure_auto_harmonics.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Harm Configure Auto Harmonics (VI)

RFmxSpecAn Harm Configure Auto Harmonics (VI)

Owning Palette:

Harmonics

Configures auto configuration of successive harmonics.

**Supported devices:** PXIe-5665, PXIe-5668

[IMAGE alt='RFmxSpecAn Harm Configure Auto Harmonics' src='rfmxspecan_harm_configure_auto_harmonics.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Auto Harmonics Setup Enabled specifies whether to enable auto configuration of successive harmonics. The default value is True. False (0) The measurement uses manual configuration for the harmonic order, harmonic bandwidth, and harmonic measurement interval. True (1) The measurement uses the Harm Num Harmonics property and configuration of the fundamental to configure successive harmonics. Bandwidth of Nth order harmonic = N * (Bandwidth of fundamental). Measurement interval of Nth order harmonics = (Measurement interval of fundamental)/N |
| False (0) | The measurement uses manual configuration for the harmonic order, harmonic bandwidth, and harmonic measurement interval. |
| True (1) | The measurement uses the Harm Num Harmonics property and configuration of the fundamental to configure successive harmonics. Bandwidth of Nth order harmonic = N * (Bandwidth of fundamental). Measurement interval of Nth order harmonics = (Measurement interval of fundamental)/N |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_harm_configure_averaging.html language=enus -->
## TOPIC 00045: rfmxspecanvi/rfmxspecan_harm_configure_averaging.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_harm_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_harm_configure_averaging.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Harm Configure Averaging (VI)

RFmxSpecAn Harm Configure Averaging (VI)

Owning Palette:

Harmonics

Configures averaging for the harmonics measurement.

**Supported devices:** PXIe-5665, PXIe-5668

[IMAGE alt='RFmxSpecAn Harm Configure Averaging' src='rfmxspecan_harm_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging the power over multiple acquisitions. The averaged power trace is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS. RMS (0) The power trace is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power trace is averaged in a logarithmic scale. Scalar (2) The square root of the power trace is averaged. Max (3) The peak power in the power trace at each sample instance is retained from one acquisition to the next. Min (4) The least power in the power trace at each sample instance is retained from one acquisition to the next. |
| RMS (0) | The power trace is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power trace is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power trace is averaged. |
| Max (3) | The peak power in the power trace at each sample instance is retained from one acquisition to the next. |
| Min (4) | The least power in the power trace at each sample instance is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_harm_configure_fundamental_rbw.html language=enus -->
## TOPIC 00046: rfmxspecanvi/rfmxspecan_harm_configure_fundamental_rbw.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_harm_configure_fundamental_rbw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_harm_configure_fundamental_rbw.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Harm Configure Fundamental RBW (VI)

RFmxSpecAn Harm Configure Fundamental RBW (VI)

Owning Palette:

Harmonics

Configures the resolution bandwidth (RBW) filter to be applied on the acquired signal. The bandwidth of the filter specified is applicable for fundamental signal.

**Supported devices:** PXIe-5665, PXIe-5668

[IMAGE alt='RFmxSpecAn Harm Configure Fundamental RBW' src='rfmxspecan_harm_configure_fundamental_rbw.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW specifies the bandwidth, in Hz, of the resolution bandwidth (RBW) filter used to acquire the fundamental signal. The default value is 100 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. None (1) The measurement does not use any RBW filtering. Gaussian (2) An RBW filter with a Gaussian response is applied. Flat (3) An RBW filter with a flat response is applied. RRC (4) The measurement uses RRC FIR coefficients for filtering. |
| None (1) | The measurement does not use any RBW filtering. |
| Gaussian (2) | An RBW filter with a Gaussian response is applied. |
| Flat (3) | An RBW filter with a flat response is applied. |
| RRC (4) | The measurement uses RRC FIR coefficients for filtering. |
|  | RRC Alpha specifies the roll-off factor for the root-raised-cosine (RRC) filter. The default value is 0.1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_im_configure_auto_intermods_setup.html language=enus -->
## TOPIC 00047: rfmxspecanvi/rfmxspecan_im_configure_auto_intermods_setup.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_im_configure_auto_intermods_setup.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_im_configure_auto_intermods_setup.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn IM Configure Auto Intermods Setup (VI)

RFmxSpecAn IM Configure Auto Intermods Setup (VI)

Owning Palette:

IM

Configures whether the measurement computes the intermod frequencies or uses manually specified frequencies.

[IMAGE alt='RFmxSpecAn IM Configure Auto Intermods Setup' src='rfmxspecan_im_configure_auto_intermods_setup.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Auto Intermods Setup Enabled specifies whether the measurement computes the intermod frequencies or uses manually specified frequencies. The default value is True. False (0) The measurement uses the values that you specify for the IM Lower Intermod Freq and IM Upper Intermod Freq properties. True (1) The measurement computes intermod frequencies. The number of intermods to measure is based on the value of the Maximum Intermod Order parameter. |
| False (0) | The measurement uses the values that you specify for the IM Lower Intermod Freq and IM Upper Intermod Freq properties. |
| True (1) | The measurement computes intermod frequencies. The number of intermods to measure is based on the value of the Maximum Intermod Order parameter. |
|  | Maximum Intermod Order specifies the order up to which the RFmx driver measures odd order intermodulation products when you set the Auto Intermods Setup Enabled parameter to True. The lower and upper intermodulation products are measured for each order. The default value is 3. 3 (3) The RFmx driver measures third order intermodulation products. 5 (5) The RFmx driver measures third and fifth order intermodulation products. 7 (7) The RFmx driver measures third, fifth, and seventh order intermodulation products. 9 (9) The RFmx driver measures third, fifth, seventh, and ninth order intermodulation products. |
| 3 (3) | The RFmx driver measures third order intermodulation products. |
| 5 (5) | The RFmx driver measures third and fifth order intermodulation products. |
| 7 (7) | The RFmx driver measures third, fifth, and seventh order intermodulation products. |
| 9 (9) | The RFmx driver measures third, fifth, seventh, and ninth order intermodulation products. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_im_configure_averaging.html language=enus -->
## TOPIC 00048: rfmxspecanvi/rfmxspecan_im_configure_averaging.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_im_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_im_configure_averaging.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn IM Configure Averaging (VI)

RFmxSpecAn IM Configure Averaging (VI)

Owning Palette:

IM

Configures averaging for the IM measurement.

[IMAGE alt='RFmxSpecAn IM Configure Averaging' src='rfmxspecan_im_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging the power over multiple acquisitions. The averaged power trace is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS. RMS (0) The power trace is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power trace is averaged in a logarithmic scale. Scalar (2) The square root of the power trace is averaged. Max (3) The peak power in the power trace at each sample instance is retained from one acquisition to the next. Min (4) The least power in the power trace at each sample instance is retained from one acquisition to the next. |
| RMS (0) | The power trace is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power trace is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power trace is averaged. |
| Max (3) | The peak power in the power trace at each sample instance is retained from one acquisition to the next. |
| Min (4) | The least power in the power trace at each sample instance is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_im_configure_measurement_method.html language=enus -->
## TOPIC 00049: rfmxspecanvi/rfmxspecan_im_configure_measurement_method.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_im_configure_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_im_configure_measurement_method.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn IM Configure Measurement Method (VI)

RFmxSpecAn IM Configure Measurement Method (VI)

Owning Palette:

IM

Configures the method for performing the IM measurement.

[IMAGE alt='RFmxSpecAn IM Configure Measurement Method' src='rfmxspecan_im_configure_measurement_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Method specifies the method for performing the IM measurement. The default value is Normal. Normal (0) The IM measurement acquires the spectrum using the same signal analyzer settings across frequency bands. Use this method when the fundamental tone separation is not large. Supported devices: PXIe-5644/5645/5646/5840/5841/5842/5830/5831/5832, PXIe-5663/5665/5668. Dynamic Range (1) The IM measurement acquires a segmented spectrum using the signal analyzer specific optimizations for different frequency bands. The spectrum is acquired in segments, one per tone or intermod frequency to be measured. The span of each acquired spectral segment is equal to the frequency separation between the two input tones, or 1 MHz, whichever is smaller. Use this method to configure the IM measurement and the signal analyzer for maximum dynamic range instead of measurement speed. Supported devices: PXIe-5665/5668 Segmented (2) Similar to the Dynamic Range method, this method also acquires a segmented spectrum, except that signal analyzer is not explicitly configured to provide maximum dynamic range. Use this method when the frequency separation of the two input tones is large and the measurement accuracy can be traded off for measurement speed. Supported devices: PXIe-5644/5645/5646/5840/5841/5842/5830/5831/5832, PXIe-5663/5665/5668 |
| Normal (0) | The IM measurement acquires the spectrum using the same signal analyzer settings across frequency bands. Use this method when the fundamental tone separation is not large. Supported devices: PXIe-5644/5645/5646/5840/5841/5842/5830/5831/5832, PXIe-5663/5665/5668. |
| Dynamic Range (1) | The IM measurement acquires a segmented spectrum using the signal analyzer specific optimizations for different frequency bands. The spectrum is acquired in segments, one per tone or intermod frequency to be measured. The span of each acquired spectral segment is equal to the frequency separation between the two input tones, or 1 MHz, whichever is smaller. Use this method to configure the IM measurement and the signal analyzer for maximum dynamic range instead of measurement speed. Supported devices: PXIe-5665/5668 |
| Segmented (2) | Similar to the Dynamic Range method, this method also acquires a segmented spectrum, except that signal analyzer is not explicitly configured to provide maximum dynamic range. Use this method when the frequency separation of the two input tones is large and the measurement accuracy can be traded off for measurement speed. Supported devices: PXIe-5644/5645/5646/5840/5841/5842/5830/5831/5832, PXIe-5663/5665/5668 |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_im_configure_number_of_intermods.html language=enus -->
## TOPIC 00050: rfmxspecanvi/rfmxspecan_im_configure_number_of_intermods.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_im_configure_number_of_intermods.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_im_configure_number_of_intermods.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn IM Configure Number of Intermods (VI)

RFmxSpecAn IM Configure Number of Intermods (VI)

Owning Palette:

IM

Configures the number of intermods to measure when you set the IM Auto Intermods Setup Enabled property to **False**.

[IMAGE alt='RFmxSpecAn IM Configure Number of Intermods' src='rfmxspecan_im_configure_number_of_intermods.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Intermods specifies the number of intermods to measure when you set the IM Auto Intermods Setup Enabled property to False. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_im_configure_rbw_filter.html language=enus -->
## TOPIC 00051: rfmxspecanvi/rfmxspecan_im_configure_rbw_filter.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_im_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_im_configure_rbw_filter.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn IM Configure RBW Filter (VI)

RFmxSpecAn IM Configure RBW Filter (VI)

Owning Palette:

IM

Configures the RBW filter.

[IMAGE alt='RFmxSpecAn IM Configure RBW Filter' src='rfmxspecan_im_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the Spectral Measurements topic for more details on RBW and sweep time. The default value is True. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 10 kHz. |
|  | RBW Filter Type specifies the response of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_im_configure_sweep_time.html language=enus -->
## TOPIC 00052: rfmxspecanvi/rfmxspecan_im_configure_sweep_time.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_im_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_im_configure_sweep_time.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn IM Configure Sweep Time (VI)

RFmxSpecAn IM Configure Sweep Time (VI)

Owning Palette:

IM

Configures the sweep time.

[IMAGE alt='RFmxSpecAn IM Configure Sweep Time' src='rfmxspecan_im_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement computes the sweep time based on the value of the IM RBW property. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement computes the sweep time based on the value of the IM RBW property. |
|  | Sweep Time Interval specifies the sweep time, in seconds, when you set the Sweep Time Auto parameter to False. The default value is 1 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_im_fetch.html language=enus -->
## TOPIC 00053: rfmxspecanvi/rfmxspecan_im_fetch.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_im_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_im_fetch.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn IM Fetch (VI)

RFmxSpecAn IM Fetch (VI)

Owning Palette:

Fetch

Fetches the IM measurement results.

#### RFmxSpecAn IM Fetch Intermod Measurement (Array)

Fetches an array of peak powers of the lower and upper intermods.

[IMAGE alt='RFmxSpecAn IM Fetch Intermod Measurement (Array)' src='rfmxspecan_im_fetch_intermod_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Intermod Order returns an array of the orders of the intermods. |
|  | Lower Intermod Absolute Power returns an array of the peak power values measured around the lower intermod frequency when you set the IM Local Peak Search Enabled property to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled property to False, the measurement returns the power at the lower intermod frequency. |
|  | Upper Intermod Absolute Power returns an array of the peak power values measured around the upper intermod frequency when you set the IM Local Peak Search Enabled property to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled property to False, the measurement returns the power at the upper intermod frequency. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn IM Fetch Spectrum

Fetches the array of spectrums used for the IM measurement. The **Spectrums** parameter contains one spectrum element when you set the IM Meas Method property to **Normal**.

When you set the IM Meas Method property to **Dynamic Range** or **Segmented**, each tone and intermod has a separate spectrum element in the **Spectrums** parameter.

This array is populated in the following order:

- Lower tone spectrum
- Upper tone spectrum
- Lower intermod< n > spectrum
- Upper intermod< n > spectrum

[IMAGE alt='RFmxSpecAn IM Fetch Spectrum' src='rfmxspecan_im_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Spectrums returns the data for the spectrum. This value is expressed in dBm. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the array of averaged powers measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the array of averaged powers measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn IM Fetch Intermod Measurement

Fetches the peak powers of the lower and upper intermods.

Use "intermod<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxSpecAn IM Fetch Intermod Measurement' src='rfmxspecan_im_fetch_intermod_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and intermod number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "intermod0" "signal::sig1/intermod0" "result::r1/intermod0" "signal::sig1/result::r1/intermod0" You can use the RFmxSpecAn Build Intermod String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Intermod Order returns the order of the intermod. |
|  | Lower Intermod Absolute Power returns the peak power measured around the lower intermod frequency when you set the IM Local Peak Search Enabled property to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled property to False, the measurement returns the power at the lower intermod frequency. |
|  | Upper Intermod Absolute Power returns the peak power measured around the upper intermod frequency when you set the IM Local Peak Search Enabled property to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled property to False, the measurement returns the power at the upper intermod frequency. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn IM Fetch Intercept Power (Array)

Fetches the output intercept powers for the intermod.

[IMAGE alt='RFmxSpecAn IM Fetch Intercept Power (Array)' src='rfmxspecan_im_fetch_intercept_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Intermod Order returns an array of the orders of the intermods. |
|  | Worst Case Output Intercept Power returns an array of the worst case output intercept powers which are equal to the minimum of the values of the IM Results Upper Output Intercept Power and IM Results Lower Output Intercept Power results. This value is expressed in dBm. |
|  | Upper Output Intercept Power returns an array of the upper output intercept power values. This value is expressed in dBm. |
|  | Lower Output Intercept Power returns an array of the lower output intercept power values. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn IM Fetch Intercept Power

Fetches the output intercept powers for the intermod.

Use "intermod<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxSpecAn IM Fetch Intercept Power' src='rfmxspecan_im_fetch_intercept_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and intermod number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "intermod0" "signal::sig1/intermod0" "result::r1/intermod0" "signal::sig1/result::r1/intermod0" You can use the RFmxSpecAn Build Intermod String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Intermod Order returns the order of the intermod. |
|  | Worst Case Output Intercept Power returns the worst case output intercept power which is equal to the minimum of the values of the IM Results Upper Output Intercept Power and IM Results Lower Output Intercept Power results. This value is expressed in dBm. |
|  | Upper Output Intercept Power returns the upper output intercept power. This value is expressed in dBm. |
|  | Lower Output Intercept Power returns the lower output intercept power. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn IM Fetch Fundamental Measurement

Fetches the peak powers of the two fundamental tones.

[IMAGE alt='RFmxSpecAn IM Fetch Fundamental Measurement' src='rfmxspecan_im_fetch_fundamental_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Lower Tone Power returns the peak power measured around the lower tone frequency when you set the IM Local Peak Search Enabled property to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled property to False, the measurement returns the power at the lower tone frequency. |
|  | Upper Tone Power returns the peak power measured around the upper tone frequency when you set the IM Local Peak Search Enabled property to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled property to False, the measurement returns the power at the upper tone frequency. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_initiate.html language=enus -->
## TOPIC 00054: rfmxspecanvi/rfmxspecan_initiate.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_initiate.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Initiate (VI)

RFmxSpecAn Initiate (VI)

Owning Palette:

RFmx SpecAn VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [RFmxSpecAn Wait for Measurement Complete](rfmxspecan_wait_for_measurement_complete.html) VI or [RFmxSpecAn Check Measurement Status](rfmxspecan_check_measurement_status.html) VI.

[IMAGE alt='RFmxSpecAn Initiate' src='rfmxspecan_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_iq_configure_acquisition.html language=enus -->
## TOPIC 00055: rfmxspecanvi/rfmxspecan_iq_configure_acquisition.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_iq_configure_acquisition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_iq_configure_acquisition.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn IQ Configure Acquisition (VI)

RFmxSpecAn IQ Configure Acquisition (VI)

Owning Palette:

IQ

Configures the acquisition settings for the I/Q measurement.

[IMAGE alt='RFmxSpecAn IQ Configure Acquisition' src='rfmxspecan_iq_configure_acquisition.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sample Rate specifies the acquisition sample rate, in samples per second (S/s). The default value is 50 MS/s. |
|  | Acquisition Time specifies the acquisition time, in seconds, for the I/Q measurement. The default value is 0.001. |
|  | Number of Records specifies the number of records to acquire. The default value is 1. |
|  | Pretrigger Time specifies the pretrigger time, in seconds, for the I/Q measurement. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_iq_configure_bandwidth.html language=enus -->
## TOPIC 00056: rfmxspecanvi/rfmxspecan_iq_configure_bandwidth.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_iq_configure_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_iq_configure_bandwidth.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn IQ Configure Bandwidth (VI)

RFmxSpecAn IQ Configure Bandwidth (VI)

Owning Palette:

IQ

Configures the bandwidth for the I/Q measurement.

[IMAGE alt='RFmxSpecAn IQ Configure Bandwidth' src='rfmxspecan_iq_configure_bandwidth.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Bandwidth Auto specifies whether the measurement computes the minimum acquisition bandwidth. The default value is True. False (0) The measurement uses the value of the Bandwidth parameter as the minimum acquisition bandwidth. True (1) The measurement uses 0.8 * sample rate as the minimum signal bandwidth. |
| False (0) | The measurement uses the value of the Bandwidth parameter as the minimum acquisition bandwidth. |
| True (1) | The measurement uses 0.8 * sample rate as the minimum signal bandwidth. |
|  | Bandwidth specifies the minimum acquisition bandwidth, in Hz, when you set the Bandwidth Auto parameter to False. The default value is 1 MHz. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_marker_configure_trace.html language=enus -->
## TOPIC 00057: rfmxspecanvi/rfmxspecan_marker_configure_trace.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_marker_configure_trace.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_marker_configure_trace.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Marker Configure Trace (VI)

RFmxSpecAn Marker Configure Trace (VI)

Owning Palette:

Marker

Configures the measurement trace to be used by the marker.

Use "marker<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxSpecAn Marker Configure Trace' src='rfmxspecan_marker_configure_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Trace specifies the trace. The default value is Spectrum. ACP Spectrum (0) The marker uses the ACP spectrum trace. CCDF Gaussian Probabilities Trace (1) The marker uses the CCDF Gaussian probabilities trace. CCDF Probabilities Trace (2) The marker uses the CCDF probabilities trace. CHP Spectrum (3) The marker uses the CHP spectrum trace. FCnt Power Trace (4) The marker uses the FCnt power trace. OBW Spectrum (5) The marker uses the OBW spectrum trace. SEM Spectrum (6) The marker uses the SEM spectrum trace. Spectrum (7) The marker uses the Spectrum trace. TXP Power Trace (8) The marker uses the TXP power trace. |
| ACP Spectrum (0) | The marker uses the ACP spectrum trace. |
| CCDF Gaussian Probabilities Trace (1) | The marker uses the CCDF Gaussian probabilities trace. |
| CCDF Probabilities Trace (2) | The marker uses the CCDF probabilities trace. |
| CHP Spectrum (3) | The marker uses the CHP spectrum trace. |
| FCnt Power Trace (4) | The marker uses the FCnt power trace. |
| OBW Spectrum (5) | The marker uses the OBW spectrum trace. |
| SEM Spectrum (6) | The marker uses the SEM spectrum trace. |
| Spectrum (7) | The marker uses the Spectrum trace. |
| TXP Power Trace (8) | The marker uses the TXP power trace. |
|  | Selector String specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" You can use the RFmxSpecAn Build Marker String2 VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_obw_configure_sweep_time.html language=enus -->
## TOPIC 00058: rfmxspecanvi/rfmxspecan_obw_configure_sweep_time.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_obw_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_obw_configure_sweep_time.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn OBW Configure Sweep Time (VI)

RFmxSpecAn OBW Configure Sweep Time (VI)

Owning Palette:

OBW

Configures the sweep time.

[IMAGE alt='RFmxSpecAn OBW Configure Sweep Time' src='rfmxspecan_obw_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement calculates the sweep time based on the value of the OBW RBW property. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement calculates the sweep time based on the value of the OBW RBW property. |
|  | Sweep Time Interval specifies the sweep time, in seconds, when you set the Sweep Time Auto parameter to False. The default value is 1 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_pavt_configure_measurement_interval.html language=enus -->
## TOPIC 00059: rfmxspecanvi/rfmxspecan_pavt_configure_measurement_interval.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_pavt_configure_measurement_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_pavt_configure_measurement_interval.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn PAVT Configure Measurement Interval (VI)

RFmxSpecAn PAVT Configure Measurement Interval (VI)

Owning Palette:

PAVT

Configures the measurement offset and measurement length for the segments.

[IMAGE alt='RFmxSpecAn PAVT Configure Measurement Interval' src='rfmxspecan_pavt_configure_measurement_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Offset specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid only when you set the PAVT Meas Interval Mode property to Uniform. The default value is 0. |
|  | Measurement Length specifies the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid when you set the PAVT Meas Interval Mode property to Uniform. The default value is 1 millisecond. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_pavt_configure_measurement_interval_mode.html language=enus -->
## TOPIC 00060: rfmxspecanvi/rfmxspecan_pavt_configure_measurement_interval_mode.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_pavt_configure_measurement_interval_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_pavt_configure_measurement_interval_mode.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn PAVT Configure Measurement Interval Mode (VI)

RFmxSpecAn PAVT Configure Measurement Interval Mode (VI)

Configures the measurement interval mode.

[IMAGE alt='RFmxSpecAn PAVT Configure Measurement Interval Mode' src='rfmxspecan_pavt_configure_measurement_interval_mode.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Interval Mode specifies the mode of configuring the measurement interval. The default value is Uniform. Uniform (0) The time offset from the start of segment and the duration over which the measurement is performed is uniform for all segments and is given by the PAVT Meas Offset property and the PAVT Meas Length property respectively. Variable (1) The time offset from the start of segment and the duration over which the measurement is performed is configured separately for each segment and is given by the PAVT Segment Meas Offset property and the PAVT Segment Meas Length property respectively. |
| Uniform (0) | The time offset from the start of segment and the duration over which the measurement is performed is uniform for all segments and is given by the PAVT Meas Offset property and the PAVT Meas Length property respectively. |
| Variable (1) | The time offset from the start of segment and the duration over which the measurement is performed is configured separately for each segment and is given by the PAVT Segment Meas Offset property and the PAVT Segment Meas Length property respectively. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_pavt_configure_measurement_location_type.html language=enus -->
## TOPIC 00061: rfmxspecanvi/rfmxspecan_pavt_configure_measurement_location_type.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_pavt_configure_measurement_location_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_pavt_configure_measurement_location_type.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn PAVT Configure Measurement Location Type (VI)

RFmxSpecAn PAVT Configure Measurement Location Type (VI)

Owning Palette:

PAVT

Configures the measurement location type for the segments.

[IMAGE alt='RFmxSpecAn PAVT Configure Measurement Location Type' src='rfmxspecan_pavt_configure_measurement_location_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Location Type specifies whether the location at which the segment is measured is indicated by time or trigger. The default value is Time. Time (0) The measurement is performed over a single record across multiple segments separated in time. The measurement locations of the segments are specified by the PAVT Segment Start Time property. The number of segments is equal to the number of segment start times. Trigger (1) The measurement is performed across segments obtained in multiple records, where each record is obtained when a trigger is received. The number of segments is equal to the number of triggers (records). |
| Time (0) | The measurement is performed over a single record across multiple segments separated in time. The measurement locations of the segments are specified by the PAVT Segment Start Time property. The number of segments is equal to the number of segment start times. |
| Trigger (1) | The measurement is performed across segments obtained in multiple records, where each record is obtained when a trigger is received. The number of segments is equal to the number of triggers (records). |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_pavt_configure_number_of_segments.html language=enus -->
## TOPIC 00062: rfmxspecanvi/rfmxspecan_pavt_configure_number_of_segments.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_pavt_configure_number_of_segments.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_pavt_configure_number_of_segments.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn PAVT Configure Number of Segments (VI)

RFmxSpecAn PAVT Configure Number of Segments (VI)

Owning Palette:

PAVT

Configures the number of segments.

[IMAGE alt='RFmxSpecAn PAVT Configure Number of Segments' src='rfmxspecan_pavt_configure_number_of_segments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Segments specifies the number of segments to be measured. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_pavt_configure_segment_type_(array).html language=enus -->
## TOPIC 00063: rfmxspecanvi/rfmxspecan_pavt_configure_segment_type_(array).html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_pavt_configure_segment_type_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_pavt_configure_segment_type_(array).html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn PAVT Configure Segment Type (Array) (VI)

RFmxSpecAn PAVT Configure Segment Type (Array) (VI)

Configures an array of segment types.

[IMAGE alt='RFmxSpecAn PAVT Configure Segment Type (Array)' src='rfmxspecan_pavt_configure_segment_type_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Segment Type specifies the type of segment. The default value is Phase and Amplitude. Phase and Amplitude (0) Phase and amplitude is measured in this segment. Amplitude (1) Amplitude is measured in this segment. Frequency Error Measurement (2) Frequency error is measured in this segment. |
| Phase and Amplitude (0) | Phase and amplitude is measured in this segment. |
| Amplitude (1) | Amplitude is measured in this segment. |
| Frequency Error Measurement (2) | Frequency error is measured in this segment. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_phasenoise_configure_number_of_ranges.html language=enus -->
## TOPIC 00064: rfmxspecanvi/rfmxspecan_phasenoise_configure_number_of_ranges.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_phasenoise_configure_number_of_ranges.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_phasenoise_configure_number_of_ranges.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn PhaseNoise Configure Number of Ranges (VI)

RFmxSpecAn PhaseNoise Configure Number of Ranges (VI)

Owning Palette:

PhaseNoise

Configures the number of offset ranges when you set the PhaseNoise Range Definition property to **Manual**.

[IMAGE alt='RFmxSpecAn PhaseNoise Configure Number of Ranges' src='rfmxspecan_phasenoise_configure_number_of_ranges.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Ranges specifies the number of manual ranges. The default value is 1. None (0) Integrated noise measurement is not computed. Measurement (1) The complete log plot frequency range, considered as a single range, is used for computing integrated measurements. Custom (2) The measurement range(s) specified by PhaseNoise Integrated Noise Start Freq property and the PhaseNoise Integrated Noise Stop Freq property is used for computing integrated measurements. |
| None (0) | Integrated noise measurement is not computed. |
| Measurement (1) | The complete log plot frequency range, considered as a single range, is used for computing integrated measurements. |
| Custom (2) | The measurement range(s) specified by PhaseNoise Integrated Noise Start Freq property and the PhaseNoise Integrated Noise Stop Freq property is used for computing integrated measurements. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_phasenoise_configure_range_definition.html language=enus -->
## TOPIC 00065: rfmxspecanvi/rfmxspecan_phasenoise_configure_range_definition.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_phasenoise_configure_range_definition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_phasenoise_configure_range_definition.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn PhaseNoise Configure Range Definition (VI)

RFmxSpecAn PhaseNoise Configure Range Definition (VI)

Owning Palette:

PhaseNoise

Specifies how the measurement computes offset subranges.

[IMAGE alt='RFmxSpecAn PhaseNoise Configure Range Definition' src='rfmxspecan_phasenoise_configure_range_definition.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Range Definition specifies how the measurement computes offset subranges. Manual (0) Specify the offset sub-ranges used for the measurement. Use the PhaseNoise Range Start Freq property and the PhaseNoise Range Stop Freq property to configure single or multiple range start and range stop frequencies. Auto (1) Measurement computes offset sub-ranges by dividing the user configured offset range into multiple decade sub-ranges. The range is specified by the PhaseNoise Start Freq and the PhaseNoise Stop Freq properties. |
| Manual (0) | Specify the offset sub-ranges used for the measurement. Use the PhaseNoise Range Start Freq property and the PhaseNoise Range Stop Freq property to configure single or multiple range start and range stop frequencies. |
| Auto (1) | Measurement computes offset sub-ranges by dividing the user configured offset range into multiple decade sub-ranges. The range is specified by the PhaseNoise Start Freq and the PhaseNoise Stop Freq properties. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_phasenoise_configure_smoothing.html language=enus -->
## TOPIC 00066: rfmxspecanvi/rfmxspecan_phasenoise_configure_smoothing.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_phasenoise_configure_smoothing.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_phasenoise_configure_smoothing.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn PhaseNoise Configure Smoothing (VI)

RFmxSpecAn PhaseNoise Configure Smoothing (VI)

Owning Palette:

PhaseNoise

Configures the smoothing type and smoothing percentage used to smoothen the measured log plot trace.

[IMAGE alt='RFmxSpecAn PhaseNoise Configure Smoothing' src='rfmxspecan_phasenoise_configure_smoothing.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Smoothing Type specifies the smoothing type used to smoothen the measured log plot trace. The default value is Logarithmic. None (0) Smoothing is disabled. Linear (1) Performs linear moving average filtering on the measured phase noise log plot trace. Logarithmic (2) Performs logarithmic moving average filtering on the measured phase noise log plot trace. Median (3) Performs moving median filtering on the measured phase noise log plot trace. |
| None (0) | Smoothing is disabled. |
| Linear (1) | Performs linear moving average filtering on the measured phase noise log plot trace. |
| Logarithmic (2) | Performs logarithmic moving average filtering on the measured phase noise log plot trace. |
| Median (3) | Performs moving median filtering on the measured phase noise log plot trace. |
|  | Smoothing Percentage specifies the number of points to use in the moving average filter as a percentage of total number of points in the log plot trace. This value is expressed as a percentage. The default value is 2. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_reset_to_default.html language=enus -->
## TOPIC 00067: rfmxspecanvi/rfmxspecan_reset_to_default.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_reset_to_default.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Reset to Default (VI)

RFmxSpecAn Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxSpecAn Reset to Default' src='rfmxspecan_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_select_measurement.html language=enus -->
## TOPIC 00068: rfmxspecanvi/rfmxspecan_select_measurement.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_select_measurement.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Select Measurement (VI)

RFmxSpecAn Select Measurement (VI)

Owning Palette:

RFmx SpecAn VIs

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

#### RFmxSpecAn Select Measurement (Single)

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxSpecAn Select Measurement (Single)' src='rfmxspecan_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. You can specify one of the following measurements. The default value is ACP. ACP (0) Enables ACP measurement. CCDF (1) Enables CCDF measurement. CHP (2) Enables CHP measurement. FCnt (3) Enables FCnt measurement. Harmonics (4) Enables harmonics measurement. OBW (5) Enables OBW measurement. SEM (6) Enables SEM measurement. Spectrum (7) Enables spectrum measurement. Spur (8) Enables spurious emissions (Spur) measurement. TXP (9) Enables TXP measurement. AMPM (10) Enables AMPM measurement. DPD (11) Enables DPD measurement. IQ (12) Enables I/Q measurement. IM (13) Enables IM measurement. NF (14) Enables NF measurement. PhaseNoise (15) Enables phase noise measurement. PAVT (16) Enables PAVT measurement. |
| ACP (0) | Enables ACP measurement. |
| CCDF (1) | Enables CCDF measurement. |
| CHP (2) | Enables CHP measurement. |
| FCnt (3) | Enables FCnt measurement. |
| Harmonics (4) | Enables harmonics measurement. |
| OBW (5) | Enables OBW measurement. |
| SEM (6) | Enables SEM measurement. |
| Spectrum (7) | Enables spectrum measurement. |
| Spur (8) | Enables spurious emissions (Spur) measurement. |
| TXP (9) | Enables TXP measurement. |
| AMPM (10) | Enables AMPM measurement. |
| DPD (11) | Enables DPD measurement. |
| IQ (12) | Enables I/Q measurement. |
| IM (13) | Enables IM measurement. |
| NF (14) | Enables NF measurement. |
| PhaseNoise (15) | Enables phase noise measurement. |
| PAVT (16) | Enables PAVT measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxSpecAn Select Measurement (Multiple)

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='RFmxSpecAn Select Measurement (Multiple)' src='rfmxspecan_select_measurement_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurements specifies the measurement to perform. You can specify one or more of the following measurements. The default is an empty array. ACP (0) Enables ACP measurement. CCDF (1) Enables CCDF measurement. CHP (2) Enables CHP measurement. FCnt (3) Enables FCnt measurement. Harmonics (4) Enables harmonics measurement. OBW (5) Enables OBW measurement. SEM (6) Enables SEM measurement. Spectrum (7) Enables spectrum measurement. Spur (8) Enables spurious emissions (Spur) measurement. TXP (9) Enables TXP measurement. AMPM (10) Enables AMPM measurement. DPD (11) Enables DPD measurement. IQ (12) Enables I/Q measurement. IM (13) Enables IM measurement. NF (14) Enables NF measurement. PhaseNoise (15) Enables phase noise measurement. PAVT (16) Enables PAVT measurement. |
| ACP (0) | Enables ACP measurement. |
| CCDF (1) | Enables CCDF measurement. |
| CHP (2) | Enables CHP measurement. |
| FCnt (3) | Enables FCnt measurement. |
| Harmonics (4) | Enables harmonics measurement. |
| OBW (5) | Enables OBW measurement. |
| SEM (6) | Enables SEM measurement. |
| Spectrum (7) | Enables spectrum measurement. |
| Spur (8) | Enables spurious emissions (Spur) measurement. |
| TXP (9) | Enables TXP measurement. |
| AMPM (10) | Enables AMPM measurement. |
| DPD (11) | Enables DPD measurement. |
| IQ (12) | Enables I/Q measurement. |
| IM (13) | Enables IM measurement. |
| NF (14) | Enables NF measurement. |
| PhaseNoise (15) | Enables phase noise measurement. |
| PAVT (16) | Enables PAVT measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_sem_configure_averaging.html language=enus -->
## TOPIC 00069: rfmxspecanvi/rfmxspecan_sem_configure_averaging.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_sem_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_sem_configure_averaging.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn SEM Configure Averaging (VI)

RFmxSpecAn SEM Configure Averaging (VI)

Owning Palette:

SEM

Configures averaging for the spectral emission mask (SEM) measurement.

[IMAGE alt='RFmxSpecAn SEM Configure Averaging' src='rfmxspecan_sem_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectral Measurements topic for more information about averaging types. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_sem_configure_carrier_offset.html language=enus -->
## TOPIC 00070: rfmxspecanvi/rfmxspecan_sem_configure_carrier_offset.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_sem_configure_carrier_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_sem_configure_carrier_offset.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn SEM Configure Carrier Offset (VI)

RFmxSpecAn SEM Configure Carrier Offset (VI)

Owning Palette:

SEM

Configures the center frequency, in Hz, of the carrier, relative to the RF center frequency.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxSpecAn SEM Configure Carrier Offset' src='rfmxspecan_sem_configure_carrier_offset.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Carrier Frequency specifies the center frequency, in Hz, of the carrier, relative to the RF center frequency. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxSpecAn Build Carrier String2 VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_sem_configure_number_of_offsets.html language=enus -->
## TOPIC 00071: rfmxspecanvi/rfmxspecan_sem_configure_number_of_offsets.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_sem_configure_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_sem_configure_number_of_offsets.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn SEM Configure Number of Offsets (VI)

RFmxSpecAn SEM Configure Number of Offsets (VI)

Owning Palette:

SEM

Configures the number of offset segments for the spectral emission mask (SEM) measurement.

[IMAGE alt='RFmxSpecAn SEM Configure Number of Offsets' src='rfmxspecan_sem_configure_number_of_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Offsets specifies the number of offset segments. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_attenuation.html language=enus -->
## TOPIC 00072: rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_attenuation.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_attenuation.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn SEM Configure Offset Relative Attenuation (VI)

RFmxSpecAn SEM Configure Offset Relative Attenuation (VI)

Owning Palette:

SEM

Configures the attenuation, in dB, relative to the external attenuation.

Use "offset<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxSpecAn SEM Configure Offset Relative Attenuation' src='rfmxspecan_sem_configure_offset_relative_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Relative Attenuation specifies the attenuation, in dB, relative to the external attenuation. Use this parameter to compensate for variations in external attenuation when the offset channels are spread wide in frequency. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used. Example: "offset0" "signal::sig1/offset0" You can use the RFmxSpecAn Build Offset String2 VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_limit.html language=enus -->
## TOPIC 00073: rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_limit.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_limit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_limit.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn SEM Configure Offset Relative Limit (VI)

RFmxSpecAn SEM Configure Offset Relative Limit (VI)

Owning Palette:

SEM

Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment.

Use "offset<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxSpecAn SEM Configure Offset Relative Limit' src='rfmxspecan_sem_configure_offset_relative_limit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Relative Limit Mode specifies whether the relative limit mask is a flat line or a line with a slope. The default value is Manual. Manual (0) The line specified by the SEM Offset Rel Limit Start and SEM Offset Rel Limit Stop property values as the two ends is considered as the mask. Couple (1) The two ends of the line are coupled to the value of the SEM Offset Rel Limit Start property. |
| Manual (0) | The line specified by the SEM Offset Rel Limit Start and SEM Offset Rel Limit Stop property values as the two ends is considered as the mask. |
| Couple (1) | The two ends of the line are coupled to the value of the SEM Offset Rel Limit Start property. |
|  | Relative Limit Start specifies the relative power limit, in dB, corresponding to the beginning of the offset segment. The value of this parameter is also set as the stop limit for the offset segment when you set the Relative Limit Mode parameter to Couple. The default value is -20. |
|  | Relative Limit Stop specifies the relative power limit, in dB, corresponding to the end of the offset segment. This parameter is ignored if you set the Relative Limit Mode parameter to Couple. The default value is -30. |
|  | Selector String specifies a selector string comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used. Example: "offset0" "signal::sig1/offset0" You can use the RFmxSpecAn Build Offset String2 VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_limit_(array).html language=enus -->
## TOPIC 00074: rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_limit_(array).html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_limit_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_sem_configure_offset_relative_limit_(array).html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn SEM Configure Offset Relative Limit (Array) (VI)

RFmxSpecAn SEM Configure Offset Relative Limit (Array) (VI)

Owning Palette:

Array VIs

Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment.

[IMAGE alt='RFmxSpecAn SEM Configure Offset Relative Limit (Array)' src='rfmxspecan_sem_configure_offset_relative_limit_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Relative Limit Mode specifies whether the relative limit mask is a flat line or a line with a slope. The default value is Manual. Manual (0) The line specified by the SEM Offset Rel Limit Start and SEM Offset Rel Limit Stop property values as the two ends is considered as the mask. Couple (1) The two ends of the line are coupled to the value of the SEM Offset Rel Limit Start property. |
| Manual (0) | The line specified by the SEM Offset Rel Limit Start and SEM Offset Rel Limit Stop property values as the two ends is considered as the mask. |
| Couple (1) | The two ends of the line are coupled to the value of the SEM Offset Rel Limit Start property. |
|  | Relative Limit Start specifies the array of relative power limits, in dB, corresponding to the beginning of the offset segment. The value of this parameter is also set as the stop limit for the offset segment when you set the Relative Limit Mode parameter to Couple. The default value is -20. |
|  | Relative Limit Stop specifies the array of relative power limits, in dB, corresponding to the end of the offset segment. This parameter is ignored if you set the Relative Limit Mode parameter to Couple. The default value is -30. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_spectrum_configure_averaging.html language=enus -->
## TOPIC 00075: rfmxspecanvi/rfmxspecan_spectrum_configure_averaging.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_spectrum_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_spectrum_configure_averaging.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Spectrum Configure Averaging (VI)

RFmxSpecAn Spectrum Configure Averaging (VI)

Owning Palette:

Spectrum

Configures averaging for the spectrum measurement.

[IMAGE alt='RFmxSpecAn Spectrum Configure Averaging' src='rfmxspecan_spectrum_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectral Measurements topic for more information about averaging types. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_spectrum_configure_fft.html language=enus -->
## TOPIC 00076: rfmxspecanvi/rfmxspecan_spectrum_configure_fft.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_spectrum_configure_fft.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_spectrum_configure_fft.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Spectrum Configure FFT (VI)

RFmxSpecAn Spectrum Configure FFT (VI)

Owning Palette:

Spectrum

Configures window and FFT to obtain a spectrum for the spectrum measurement.

[IMAGE alt='RFmxSpecAn Spectrum Configure FFT' src='rfmxspecan_spectrum_configure_fft.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | FFT Window specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectral Measurements topic for more information about FFT window types. The default value is Flat Top. None (0) Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. Flat Top (1) Measures single-tone amplitudes accurately. Hanning (2) Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. Hamming (3) Analyzes closely-spaced sine waves. Gaussian (4) Provides a balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis. Blackman (5) Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. Blackman-Harris (6) Useful as a general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. Kaiser-Bessel (7) Separates two tones with frequencies close to each other but with widely-differing amplitudes. |
| None (0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |
| Flat Top (1) | Measures single-tone amplitudes accurately. |
| Hanning (2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |
| Hamming (3) | Analyzes closely-spaced sine waves. |
| Gaussian (4) | Provides a balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis. |
| Blackman (5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |
| Blackman-Harris (6) | Useful as a general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |
| Kaiser-Bessel (7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |
|  | FFT Padding specifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding. This parameter is used only when the acquisition span is less than the device instantaneous bandwidth. The default value is -1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_spectrum_configure_frequency_start_stop.html language=enus -->
## TOPIC 00077: rfmxspecanvi/rfmxspecan_spectrum_configure_frequency_start_stop.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_spectrum_configure_frequency_start_stop.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_spectrum_configure_frequency_start_stop.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Spectrum Configure Frequency Start Stop (VI)

RFmxSpecAn Spectrum Configure Frequency Start Stop (VI)

Owning Palette:

Spectrum

Configures the start frequency and stop frequency for the spectrum measurement.

[IMAGE alt='RFmxSpecAn Spectrum Configure Frequency Start Stop' src='rfmxspecan_spectrum_configure_frequency_start_stop.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Start Frequency specifies the start frequency, in Hz, for the spectrum measurement. The default value is 995 MHz. |
|  | Stop Frequency specifies the stop frequency, in Hz, for the spectrum measurement. The default value is 1.005 GHz. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-specan-vi path=rfmxspecanvi/rfmxspecan_spectrum_configure_noise_compensation_enabled.html language=enus -->
## TOPIC 00078: rfmxspecanvi/rfmxspecan_spectrum_configure_noise_compensation_enabled.html

- bundle_id: `rfmx-specan-vi`
- source_path: `rfmxspecanvi/rfmxspecan_spectrum_configure_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-vi/raw/resource/enus/rfmxspecanvi/rfmxspecan_spectrum_configure_noise_compensation_enabled.html
- document_id: `rfmx-specan-vi`
- page_type: `leaf`
- content_type: ``

RFmxSpecAn Spectrum Configure Noise Compensation Enabled (VI)

RFmxSpecAn Spectrum Configure Noise Compensation Enabled (VI)

Owning Palette:

Spectrum

Configures compensation of the spectrum for the inherent noise floor of the signal analyzer.

[IMAGE alt='RFmxSpecAn Spectrum Configure Noise Compensation Enabled' src='rfmxspecan_spectrum_configure_noise_compensation_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Spectrum Noise Comp Enabled specifies whether to enable compensation of the spectrum for the inherent noise floor of the signal analyzer. The default value is False. False (0) Disables compensation of the spectrum for the noise floor of the signal analyzer. True (1) Enables compensation of the spectrum for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the Spectrum measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. Supported Devices: PXIe-5663/5665/5668, PXIe-5830/5831/5832 |
| False (0) | Disables compensation of the spectrum for the noise floor of the signal analyzer. |
| True (1) | Enables compensation of the spectrum for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the Spectrum measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. Supported Devices: PXIe-5663/5665/5668, PXIe-5830/5831/5832 |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |
